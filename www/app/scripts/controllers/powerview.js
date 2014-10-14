'use strict';

(function() {

    var fifteen = 15 * 60;

    function controller(scope, Session, http, timeout, $q, location, util) {
        scope.nodata = false;
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.lastTime = null;

        function onLoad(data) {

            scope.data = data;
            scope.data.billingPeriodStartDate  = util.toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = util.toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = util.toDate(data.season_enddate);
            scope.data.seasonStartDate = util.toDate(data.season_startdate);
            var today = new Date().toString().split(' ').slice(0, 4).join(' ') + ' ' ;
            var format = "hh:mm a";
            scope.data.peakStart = moment(today + data.peak_period_start).format(format);
            scope.data.peakEnd = moment(today + data.peak_period_end).format(format);

            var intervalTick = _.throttle(function(cont) {
                if (!cont) {
                    return;
                }
                scope.tickInterval = $q.defer();
                tick(scope.tickInterval);
                scope.tickInterval.promise.then(intervalTick, intervalTick);
            }, scope.reloadTime);
            intervalTick(true);
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

        function tick(deferred) {
            if (location.path() !== '/powerview') {
                return deferred.reject(false);
            }
            http.get('/api/powerview/max_demand').success(function (data) {
                if (!data.data.max_demand) {
                    return ;
                }
                scope.data.max_demand = data.data.max_demand;
                var maxDemandRange = util.toDateRange(data.data.time);
                scope.data.maxDemandStartDate = maxDemandRange[0];
                scope.data.maxDemandEndDate = maxDemandRange[1];
            });
            http.get('/api/powerview/current_demand').success(function (data) {
                scope.data.current_demand = data.data.current_demand;
                var currentDemandRange = util.toDateRange(data.data.time);
                scope.data.currentDemandStartDate = currentDemandRange[0];
                scope.data.currentDemandEndDate = currentDemandRange[1];
            });
            http.get('/api/powerview/points', {params : {'timeframe': scope.timeframe, 'resolution':scope.resolution}}).success(function (data) {
                var points = _.map(data.data, function(d) {
                    d.time = new Date(d.time);
                    return d;
                });
                var lastPoint = _.last(points);
                if (!lastPoint) {
                    scope.nodata = true;
                    return deferred.reject("Last point is undefined");
                }
                scope.lastTime = lastPoint.time;
                scope.data.power_factor = lastPoint.L1_PF;
                scope.data.voltage = lastPoint.L1_V;
                scope.graphdata = points;
                scope.dataUpdated = ++scope.dataUpdated || 0;
                scope.nodata = false;
                deferred.resolve(true);
                scope.loading = false;
            }).error(function(err) {
                console.log(err);
                console.log("Error, Connection issue.");
                deferred.reject(err);
            });
        }

        load(onLoad);

        /** 
         * @param timefram graph time frame in minutes
         */
        scope.setTimeFrame = function(timeframe) {
            scope.timeframe = timeframe;
            scope.loading = true;
            if (timeframe === '24h') {
                scope.setReloadTime(60000)
                return scope.setResolution('1m');
            }
            if (timeframe === '8h') {
                scope.setReloadTime(30000)
                return scope.setResolution('1m');
            }
            if (timeframe === '2h') {
                scope.setReloadTime(10000)
                return scope.setResolution('1m');
            }
            scope.setReloadTime(5000)
            return scope.setResolution('1s');
        };

        scope.setReloadTime = function(reloadTime) {
            scope.reloadTime = reloadTime;
        };

        scope.setResolution = function(resolution) {
            scope.resolution = resolution;
        };
        scope.setTimeFrame('30m');
        scope.setResolution('1s');
        scope.setReloadTime(5000);
    }

    angular.module('insightApp')
    .controller('PowerviewCtrl', ['$scope', 'Session', '$http', '$timeout', '$q', '$location', 'util', controller]);

}).call(null);
