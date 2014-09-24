'use strict';

(function() {

    function toDate(pyTimestamp) {
        var d = new Date();
        d.setTime(pyTimestamp * 1000);
        return d;
    }

    function controller(scope, Session, http) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = toDate(data.season_enddate);
            scope.data.seasonStartDate = toDate(data.season_startdate);
        }

        function load(onLoad) {
            http
                .get('/api/powerview', {})
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        console.log("Error : " + d.message);
                    } else {
                        onLoad(d.data);
                    }
                });
        }

        function tick() {
            http({method: 'get', url: '/api/powerview/max_demand'}).success(function (data) {
                if (!data.data.max_demand) {
                    return ;
                }
                scope.data.max_demand = data.data.max_demand;
                scope.data.maxDemandStartDate = new Date(data.data.time * 100);
                scope.data.maxDemandEndDate = new Date(data.data.time * 100);
            });
            http({method: 'get', url: '/api/powerview/current_demand'}).success(function (data) {
                scope.data.current_demand = data.data.current_demand;
                scope.data.currentDemandStartDate = new Date(data.data.time * 100);
                scope.data.currentDemandEndDate = new Date(data.data.time * 100);
            });
            http({method: 'get', url: '/api/powerview/points'}).success(function (data) {
                var c = data.data.consumption;
                var s = data.data.solar;
                var points = _.map(c.points, function(p, i) {
                    var consumedPoint = _.zipObject(c.columns, p);
                    var solarPoint = _.zipObject(s.columns, s.points[i]);
                    //  Add the solar saved power to the consumed point
                    consumedPoint.S = solarPoint.P;
                    consumedPoint.time *= 1000;
                    return consumedPoint;
                });
                var lastPoint = _.last(points);
                scope.data.power_factor = lastPoint.L1_PF;
                scope.graphdata = points;
            });
        }

        // Run tick every 5 seconds
        setInterval(tick, 5000);

        load(onLoad);
    }

    angular.module('insightApp')
    .controller('PowerviewCtrl', ['$scope', 'Session', '$http', controller]);

}).call(null);
