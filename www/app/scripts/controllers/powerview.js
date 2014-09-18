'use strict';

(function() {

    function toDate(pyTimestamp) {
        var d = new Date();
        d.setTime(pyTimestamp * 1000);
        return d;
    }

    var api = '/api/powerview/points';

    function controller(scope, Session, http) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = toDate(data.season_enddate);
            scope.data.seasonStartDate = toDate(data.season_startdate);
            scope.data.currentDemandEndDate = toDate(data.current_demand_enddate);
            scope.data.currentDemandStartDate = toDate(data.current_demand_startdate);
            scope.data.maxDemandEndDate = toDate(data.max_demand_enddate);
            scope.data.maxDemandStartDate = toDate(data.max_demand_startdate);
        }

        function load(onLoad) {
            http
                .post('/api/powerview', {})
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        alert(d.message);
                    } else {
                        onLoad(d.data);
                    }
                });
        }

        load(onLoad);
        http({method: 'get', url: api}).success(function (data) {
            scope.graphdata = data;
        });
    }

    angular.module('insightApp')
    .controller('PowerviewCtrl', ['$scope', 'Session', '$http', controller]);

}).call(null);
