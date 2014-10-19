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
    }

    angular.module('insightApp')
    .service('historical', ['$http', historical]);

}).call(null);
