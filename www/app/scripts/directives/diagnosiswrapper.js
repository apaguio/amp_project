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

    function controller(scope, http) {

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

        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;

        function onLoad(data) {
            scope.data = data;
            scope.data.billingPeriodStartDate  = util.toDate(data.billing_period_startdate);
            scope.data.billingPeriodEndDate = util.toDate(data.billing_period_enddate);
            scope.data.seasonEndDate = util.toDate(data.season_enddate);
            scope.data.seasonStartDate = util.toDate(data.season_startdate);
        }

        function load(onLoad) {

            scope.loading = true;

            if (location.path() !== '/diagnosis') {
                return deferred.reject(false);
            }

            var params = {'start': scope.start, 'end': scope.start};
            http.get('/api/historical', {params: params}).success(function (data) {
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

        scope.setGraph = function setGraph(graph) {
            scope.graph = graph;
            load(onLoad);
        };

    }

    angular.module('insightApp')
    .directive('diagnosiswrapper', function () {
        return {
            templateUrl: 'views/directives/diagnosiswrapper.html',
            restrict: 'E',
            scope: {
                start: '=',
                end: '='
            },
            link: ['scope', '$http', controller]
        };
    });
}).call(null);
