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

        scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
        scope.format = scope.formats[0];

        if (!scope.wrapper.start) {
            scope.wrapper.start = moment().subtract(1, 'days');
        }

        if (!scope.wrapper.end) {
            scope.wrapper.end = new Date();
        }

        scope.dateOptions = {
            formatYear: 'yy',
            startingDay: 1
        };

        scope.isOpen = { start: false, end: false };
        scope.open = function($event, picker) {
            $event.preventDefault();
            $event.stopPropagation();
            scope.isOpen[picker] = true;
        };

        scope.nodata = false;

        var load = function load() {
            scope.loading = true;
            var params = {params : {
                'resolution': scope.resolution
            }};

            var start = moment(scope.wrapper.start).utc().unix();
            var end = moment(scope.wrapper.end).utc().unix();
            var url = '/api/historical/points/' + start + '/' + end;

            http.get(url, params).then(function (result) {
                var data = result.data;
                if (!data || !data.length) {
                    debugger; 
                    scope.nodata = true;
                    return;
                }
                var points = _.map(data, function(d) {
                    d.time = new Date(d.time);
                    return d;
                });
                scope.graphdata = points;
                scope.dataUpdated = ++scope.dataUpdated || 0;
                scope.nodata = false;
                scope.loading = false;
                scope.bindDates();
            }, util.onError);
        };

        scope.setResolution = function(resolution) {
            scope.resolution = resolution;
            load();
        };

        scope.setResolution('30m');

        scope.bindDates = _.once(function bindDates() {
            scope.$watch('wrapper.start', function(newValue, oldValue) {
                if (newValue !== oldValue) {
                    load();
                }
            });
            scope.$watch('wrapper.end', function(newValue, oldValue) {
                if (newValue !== oldValue) {
                    load();
                }
            });
        });
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
