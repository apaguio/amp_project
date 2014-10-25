'use strict';

/**
 * @ngdoc service
 * @name insightApp.settings
 * @description
 * # settings
 * Service in the insightApp.
 */
(function() {

    function settings(http, $q) {

        this.update = function(password, facility_name) {
            return http.post('/api/settings', { facility_name: facility_name, password: password });
        };

        this.load = function() {
            return http.get('/api/settings');
        };
    }

    angular.module('insightApp')
    .service('settings', ['$http', '$q', settings]);

}).call(null);
