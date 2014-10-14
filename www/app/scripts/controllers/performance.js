'use strict';

(function() {

    function controller(scope, Session, http, util) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.dataUpdated = 0;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = util.toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = util.toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = util.toDate(data.season_enddate);
            scope.data.seasonStartDate = util.toDate(data.season_startdate);
        }

        function load(onLoad) {
            scope.loading = true;
            http.get('/api/performance')
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        alert(d.message);
                    } else {
                        onLoad(d.data);
                    }
                    http.get('/api/performance/graph')
                        .then(function (res) {
                            var d = res.data;
                            if (d.status === "error") {
                                alert(d.message);
                            } else {
                                scope.graphData = d.data;
                                scope.dataUpdated ++;
                                scope.loading = false;
                            }
                        });
                });
        }

        load(onLoad);
    }

    angular.module('insightApp')
    .controller('PerformanceCtrl', ['$scope', 'Session', '$http', 'util', controller]);

}).call(null);
