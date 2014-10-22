'use strict';

/**
 * @ngdoc directive
 * @name insightApp.controller:powerview
 * @description
 * # powerview
 * Contains the graph for power view and the peaks data and dates
 */
(function() {

    function controller(scope, Session, http, timeout, $q, location, util, dateFilter) {

        scope.titleTooltip = 'Summer rates apply May 1 to October 31. Winter rates apply November 1 to April 30.';
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
            http.get('/api/powerview').then(function (res) {
                onLoad(res.data);
            }, util.onError);
        }

        function tick(deferred) {
            if (location.path() !== '/powerview') {
                return deferred.reject(false);
            }

            var demandAPI = '/api/powerview/max_demand';
            var dateText = dateFilter(scope.data.maxDemandStartDate, 'fullDate') + " " + dateFilter(scope.data.maxDemandStartDate, 'h:mm') + " - " + dateFilter(scope.data.maxDemandEndDate, 'h:mm a');
            scope.maxDemandTitle = 'Max Peak Demand';
            scope.maxDemandDescription = 'This is your maximum kW demand during On Peak times in the current billing period. Your Max Demand this billing period, either on or off peak, is [' + scope.data.max_demand + ' kW], and occurred on [' + dateText + '].';
            if (scope.data.peak_period === 'offpeak') {
                scope.maxDemandDescription = 'This is your maximum kW demand during the current billing period, regardless of time. Your Max Peak Demand this billing period is [' + scope.data.max_demand + ' kW], and occurred on [' + dateText + '].';
                scope.maxDemandTitle = 'Max Demand';
                demandAPI =  '/api/powerview/max_demand_anytime';
            }
            http.get(demandAPI).then(function (result) {
                var data = result.data;
                if (!data.max_demand) {
                    return ;
                }
                scope.data.max_demand = data.max_demand;
                var maxDemandRange = util.toDateRange(data.time);
                scope.data.maxDemandStartDate = maxDemandRange[0];
                scope.data.maxDemandEndDate = maxDemandRange[1];
            }, util.onError);

            http.get('/api/powerview/current_demand').then(function (result) {
                var data = result.data;
                scope.data.current_demand = data.current_demand;
                var currentDemandRange = util.toDateRange(data.time);
                scope.data.currentDemandStartDate = currentDemandRange[0];
                scope.data.currentDemandEndDate = currentDemandRange[1];
            }, util.onError);

            var pointsParams = {params : {'timeframe': scope.timeframe, 'resolution':scope.resolution}};

            http.get('/api/powerview/points', pointsParams).then(function (result) {
                var data = result.data;
                var points = _.map(data, function(d) {
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

            }, function(err) {
                util.onError(err);
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
    }

    angular.module('insightApp')
    .controller('PowerviewCtrl', ['$scope', 'Session', '$http', '$timeout', '$q', '$location', 'util', 'dateFilter', controller]);

}).call(null);
