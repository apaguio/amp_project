'use strict';

(function() {

    function toDate(pyTimestamp) {
        return moment(pyTimestamp).toDate();
    }

    function controller(scope, Session, http) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.dataUpdated = 0;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = toDate(data.season_enddate);
            scope.data.seasonStartDate = toDate(data.season_startdate);
        }

        function load(onLoad) {
            http.get('/api/performance')
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        alert(d.message);
                    } else {
                        onLoad(d.data);
                    }
                });
            http.get('/api/performance/graph')
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        alert(d.message);
                    } else {
                        scope.graphData = d.data;
                        scope.dataUpdated ++;
                    }
                });
        }

        load(onLoad);
    }

    angular.module('insightApp')
    .controller('PerformanceCtrl', ['$scope', 'Session', '$http', controller]);

}).call(null);
