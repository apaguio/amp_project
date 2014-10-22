'use strict';

/**
 * @ngdoc service
 * @name insightApp.historical
 * @description
 * # historical
 * Service in the insightApp. Holds the callsto the historical backend.
 */
(function() {

    function historical(http) {

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
            wrapper.start = moment(wrapper.start.$date).toDate();
            wrapper.end = moment(wrapper.end.$date).toDate();
            var graphs = wrapper.graphs;
            wrapper.graphs = {
                powerfactor: graphs.indexOf('powerfactor') >= 0,
                voltage: graphs.indexOf('voltage') >= 0,
                consumption: graphs.indexOf('consumption') >= 0
            };
        };
    }

    angular.module('insightApp')
    .service('historical', ['$http', historical]);

}).call(null);
