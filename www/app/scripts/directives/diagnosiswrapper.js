'use strict';

/**
 * @ngdoc directive
 * @name insightApp.directive:diagnosiswrapper
 * @description
 * # diagnosiswrapper
 * Wraps diagnosis instance. Contains the graph and the date picking and 
 * makes calls to backend
 */
(function() {

    function controller(scope, Session, http, $q, util) {

        scope.today = function() {
            scope.dt = new Date();
        };
        scope.today();

        scope.clear = function () {
            scope.dt = null;
        };

        // Disable weekend selection
        scope.disabled = function(date, mode) {
            return ( mode === 'day' && ( date.getDay() === 0 || date.getDay() === 6 ) );
        };

        scope.toggleMin = function() {
            scope.minDate = scope.minDate ? null : new Date();
        };
        scope.toggleMin();

        scope.open = function($event) {
            $event.preventDefault();
            $event.stopPropagation();

            scope.opened = true;
        };

        scope.dateOptions = {
            formatYear: 'yy',
            startingDay: 1
        };

        scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
        scope.format = scope.formats[0];

        scope.setGraph = function setGraph(graph) {
            scope.graph = graph;
            load();
        };

        scope.nodata = false;

        function load() {

            var params = {params : {
                'timeframe': scope.timeframe,
                'resolution':scope.resolution
            }};

            http.get('/api/powerview/points', params).then(function (result) {
                var data = result.data;
                if (!result.data || !result.data.length) {
                    scope.nodata = true;
                    return;
                }
                var points = _.map(result.data, function(d) {
                    d.time = new Date(d.time);
                    return d;
                });
                scope.graphdata = points;
                scope.dataUpdated = ++scope.dataUpdated || 0;
                scope.nodata = false;
                scope.loading = false;
            }, util.onError);
        }

        load();

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
            return scope.setResolution('1s');
        };

        scope.setResolution = function(resolution) {
            scope.resolution = resolution;
        };

        scope.setTimeFrame('30m');
    }

    angular.module('insightApp')
    .directive('diagnosiswrapper', function () {
        return {
            templateUrl: 'views/directives/diagnosiswrapper.html',
            restrict: 'E',
            replace: true,
            scope: {
                wrapper: '='
            },
            controller: ['$scope', 'Session', '$http', '$q', 'util', controller]
        };
    });
}).call(null);
