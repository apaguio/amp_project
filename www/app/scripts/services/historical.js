'use strict';

/**
 * @ngdoc service
 * @name insightApp.historical
 * @description
 * # historical
 * Service in the insightApp. Holds the callsto the historical backend.
 */
(function() {

    function historical(http, $q, $rootScope) {

        this.load = function load() {
            return http.get('/api/historical', {});
        };

        this.update = function update(wrappers) {
            return http.post('/api/historical', wrappers);
        };

        this.updateSingle = function update(wrapper) {
            return http.post('/api/historical/' + wrapper.id, wrapper);
        };

        this.fixServerWrapperObject = function fixServerWrapperObject(wrapper) {
            var start = wrapper.start.$date || wrapper.start;
            var end = wrapper.end.$date || wrapper.end;
            wrapper.start = moment(start).toDate();
            wrapper.end = moment(end).toDate();
            var graphs = wrapper.graphs;
            wrapper.graphs = {
                powerfactor: graphs.indexOf('powerfactor') >= 0,
                voltage: graphs.indexOf('voltage') >= 0,
                consumption: graphs.indexOf('consumption') >= 0
            };
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

        this.points = function points(start, end, resolution) {
            var url = '/api/historical/points/' + start + '/' + end;
            var params = {params : {
                'resolution': resolution
            }};
            return http.get(url, params);
        };
    }

    angular.module('insightApp')
    .service('historical', ['$http', '$q', '$rootScope', historical]);

}).call(null);
