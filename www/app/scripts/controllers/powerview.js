'use strict';

/**
 * @ngdoc directive
 * @name insightApp.controller:powerview
 * @description
 * # powerview
 * Contains the graph for power view and the peaks data and dates
 */
(function() {

    function controller(scope, Session, http, timeout, $q, location, util, powerview) {

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

            scope.data.demandCharge = scope.data.demand_charge;
            if (scope.data.peak_period === 'onpeak') {
                scope.data.demandCharge = scope.data.peak_demand_charge;
            }

            scope.demandChargesTooltip = 'You pay $' + scope.data.demand_charge + ' / kW for your max demand, ';
            if (scope.data.season === 'Summer') {
                scope.demandChargesTooltip += 'regardless of when it occurred. You pay an additional $' + (scope.data.peak_demand_charge || 8.72)  + ' / kW for your max demand during peak times.';
            } else {
                scope.demandChargesTooltip += 'There is no additional charge for your max demand during partial peak times.';
            }

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
            powerview.load().then(function (res) {
                onLoad(res.data);
            }, util.onError());
        }

        scope.graphConfig = {};
        function tick(deferred) {
            if (location.path() !== '/powerview') {
                return deferred.reject(false);
            }

            powerview.maxDemand().then(function (result) {
                var resolved = result[scope.data.peak_period];
                scope.maxDemand = resolved;
                scope.graphConfig = {
                    graphs: null,
                    maxDemand: scope.maxDemand.value,
                    maxDemandTitle: scope.maxDemand.title
                };
                scope.dataUpdated = ++scope.dataUpdated || 0;
            }, util.onError());

            powerview.currentDemand().then(function (result) {
                scope.currentDemand = result;
            }, util.onError());

            powerview.points(scope.timeframe, scope.resolution).then(function (result) {
                var data = result.data;
                var points = _.map(data, function(d) {
                    d.time = moment(d.time).toDate();
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

            }, util.onError(deferred));
        }

        load(onLoad);

        /** 
         * @param timefram graph time frame in minutes
         */
        scope.setTimeFrame = function(timeframe) {
            scope.timeframe = timeframe;
            scope.loading = true;
            if (timeframe === '24h') {
                scope.setReloadTime(60000);
                return scope.setResolution('5m');
            }
            if (timeframe === '8h') {
                scope.setReloadTime(30000);
                return scope.setResolution('1m');
            }
            if (timeframe === '2h') {
                scope.setReloadTime(10000);
                return scope.setResolution('1m');
            }
            scope.setReloadTime(5000);
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
    .controller('PowerviewCtrl', ['$scope', 'Session', '$http', '$timeout', '$q', '$location', 'util', 'powerview', controller]);

}).call(null);
