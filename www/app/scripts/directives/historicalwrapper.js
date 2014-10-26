'use strict';

/**
 * @ngdoc directive
 * @name insightApp.directive:historicalwrapper
 * @description
 * # historicalwrapper
 * Wraps historical instance. Contains the graph and the date picking and 
 * makes calls to backend
 */
(function() {

    function controller(scope, Session, http, $q, util, historical, powerview) {

        scope.zoomEnabled = true;

        scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
        scope.format = scope.formats[0];

        scope.settings = false;
        scope.showSettings = function showSettings() {
            scope.settings = true;
        };
        scope.hideSettings = function hideSettings() {
            scope.settings = false;
        };

        if (!scope.wrapper.start) {
            scope.wrapper.start = moment().subtract(1, 'days').toDate();
        }

        if (!scope.wrapper.end) {
            scope.wrapper.end = new Date();
        }
        var update = _.throttle(function () {
            if (!scope.wrapper.id) {
                console.log("Wrapper has no ID");
                return;
            }
            scope.wrapper.start = moment(scope.wrapper.start).toDate();
            scope.wrapper.end = moment(scope.wrapper.end).toDate();
            scope.wrapper.zoom_start = moment(scope.wrapper.zoom_start).toDate();
            scope.wrapper.zoom_end = moment(scope.wrapper.zoom_end).toDate();
            historical.updateSingle(scope.wrapper).success(onUpdate).error(util.onError());
        }, 1000);

        scope.dateOptions = {
            formatYear: 'yy',
            startingDay: 1
        };

        scope.remove = function remove() {
            historical.remove(scope.wrapper.id);
        };

        scope.isOpen = { start: false, end: false };
        scope.open = function($event, picker) {
            $event.preventDefault();
            $event.stopPropagation();
            scope.isOpen[picker] = true;
        };

        scope.nodata = false;

        scope.graphConfig = {};
        function load() {
            scope.loading = true;
            $q.all([
                powerview.load(),
                powerview.maxDemand()
            ]).then(function(results) {
                var peak = scope.wrapper.maxDemandPeak || results[0].data.peak_period;
                scope.wrapper.maxDemandPeak = peak;
                scope.maxDemand = results[1][peak];
                scope.graphConfig = {
                    graphs: scope.wrapper.graphs || null,
                    maxDemand: scope.maxDemand.value,
                    maxDemandTitle: scope.maxDemand.title
                };
                scope.dataUpdated = ++scope.dataUpdated || 0;
            }, util.onError());

            var start = moment(scope.wrapper.start).utc().unix();
            var end = moment(scope.wrapper.end).utc().unix();

            historical.points(start, end, scope.wrapper.resolution).then(function (result) {
                var data = result.data;
                if (!data || !data.length) {
                    scope.nodata = true;
                    return;
                }
                var points = _.map(data, function(d) {
                    d.time = moment(d.time).toDate();
                    return d;
                });
                scope.graphdata = points;
                scope.dataUpdated = ++scope.dataUpdated || 0;
                scope.nodata = false;
                scope.loading = false;
                scope.bindDates();
            }, util.onError());
        }

        scope.toggleGraph = function(graph) {
            scope.wrapper.graphs[graph] = !scope.wrapper.graphs[graph];
            update();
        };

        function onUpdate (wrapper) {
            historical.fixServerWrapperObject(wrapper);
            load();
        }

        scope.selectMaxDemand = function(peak) {
            scope.wrapper.maxDemandPeak = peak;
            update();
        };

        scope.setResolution = function(resolution) {
            scope.wrapper.resolution = resolution;
            update();
        };

        if (!scope.wrapper.resolution) {
            scope.setResolution('30m');
        } else {
            load();
        }

        scope.bindDates = _.once(function bindDates() {
            scope.$watch('wrapper.start', function(newValue, oldValue) {
                if (+newValue !== +oldValue) {
                    update();
                }
            });
            scope.$watch('wrapper.end', function(newValue, oldValue) {
                if (+newValue !== +oldValue) {
                    update();
                }
            });
        });
    }

    angular.module('insightApp')
    .directive('historicalwrapper', function () {
        return {
            templateUrl: 'views/directives/historicalwrapper.html',
            restrict: 'E',
            replace: true,
            scope: {
                wrapper: '='
            },
            controller: ['$scope', 'Session', '$http', '$q', 'util', 'historical', 'powerview', controller]
        };
    });
}).call(null);
