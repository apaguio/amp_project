'use strict';

/**
 * @ngdoc service
 * @name insightApp.powerview
 * @description
 * # powerview
 * Service in the insightApp. Holds the calls to the powerview backend
 */
(function() {

    function powerview(http, $q, $rootScope, dateFilter, util) {

        this.load = function load() {
            return http.get('/api/powerview', {});
        };

        this.maxDemand = function maxDemand() {
            var deferred = $q.defer();
            var peakDemandAPI = '/api/powerview/max_peak_demand',
                maxDemandAPI =  '/api/powerview/max_demand_anytime';
            $q.all([
                http.get(peakDemandAPI),
                http.get(maxDemandAPI)
            ]).then(function(results) {
                var peak = results[0].data;
                var alltime = results[1].data;
                var maxPeakDemandRange = util.toDateRange(peak.time);
                var maxDemandRange = util.toDateRange(alltime.time);
                var peakStart = maxPeakDemandRange[0];
                var peakEnd = maxPeakDemandRange[1];
                var start = maxDemandRange[0];
                var end = maxDemandRange[1];
                //var dateText = dateFilter(start, 'fullDate') + " " + dateFilter(start, 'h:mm') + " - " + dateFilter(end, 'h:mm a');
                var peakDateText = dateFilter(peakStart, 'fullDate') + " " + dateFilter(peakStart, 'h:mm') + " - " + dateFilter(peakEnd, 'h:mm a');
                var resolved = {
                    onpeak: {
                        title: 'Max Peak Demand',
                        tooltip: 'This is your maximum kW demand during On Peak times in the current billing period. Your Max Demand this billing period, either on or off peak, is [' + peak.max_demand + ' kW], and occurred on [' + peakDateText + '].',
                        value: peak.max_demand,
                        start: peakStart,
                        end: peakEnd
                    },
                    offpeak: {
                        title: 'Max Demand',
                        tooltip: 'This is your maximum kW demand during the current billing period, regardless of time. Your Max Peak Demand this billing period is [' + peak.max_demand + ' kW], and occurred on [' + peakDateText + '].',
                        value: alltime.max_demand,
                        start: start,
                        end: end
                    }
                };
                deferred.resolve(resolved);
            }, util.onError(deferred));
            return deferred.promise;
        };

        this.currentDemand = function currentDemand() {
            var deferred = $q.defer();
            http.get('/api/powerview/current_demand').then(function(result) {
                var data = result.data;
                var currentDemandRange = util.toDateRange(data.time);
                var resolved = {
                    value: data.current_demand,
                    start: currentDemandRange[0],
                    end: currentDemandRange[1]
                };
                deferred.resolve(resolved);
            }, util.onError(deferred));
            return deferred.promise;
        };

        this.points = function points(timeframe, resolution) {
            var url = '/api/powerview/points';
            var pointsParams = {params: {'timeframe': timeframe, 'resolution': resolution}};
            return http.get(url, pointsParams);
        };

        this.remove = function remove(id) {
            var deferred = $q.defer();
            http.delete('/api/historical/' + id).then(function() {
                $rootScope.$broadcast("historical_removed", {
                    id: id
                });
                deferred.resolve("id");
            });
            return deferred.promise;
        };
    }

    angular.module('insightApp')
    .service('powerview', ['$http', '$q', '$rootScope', 'dateFilter', 'util', powerview]);

}).call(null);
