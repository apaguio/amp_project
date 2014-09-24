'use strict';

(function() {

    function toDate(pyTimestamp) {
        var d = new Date();
        d.setTime(pyTimestamp * 1000);
        return d;
    }

    var fifteen = 15 * 60;

    function toDateRange(pyTimestamp) {
        var d0 = new Date(),
            d1 = new Date();
        var start = Math.floor(pyTimestamp - (pyTimestamp % fifteen));
        var end = start + fifteen;
        d0.setTime(start * 1000);
        d1.setTime(end * 1000);
        return [d0, d1];
    }

    function controller(scope, Session, http) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = toDate(data.season_enddate);
            scope.data.seasonStartDate = toDate(data.season_startdate);
            var today = new Date().toString().split(' ').slice(0, 4).join(' ') + ' ' ;
            var format = "hh:mm a";
            scope.data.peakStart = moment(today + data.peak_period_start).format(format);
            scope.data.peakEnd = moment(today + data.peak_period_end).format(format);
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
                var maxDemandRange = toDateRange(data.data.time);
                scope.data.maxDemandStartDate = maxDemandRange[0];
                scope.data.maxDemandEndDate = maxDemandRange[1];
            });
            http({method: 'get', url: '/api/powerview/current_demand'}).success(function (data) {
                scope.data.current_demand = data.data.current_demand;
                var currentDemandRange = toDateRange(data.data.time);
                scope.data.currentDemandStartDate = currentDemandRange[0];
                scope.data.currentDemandEndDate = currentDemandRange[1];
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
                scope.data.voltage = lastPoint.L1_V;
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
