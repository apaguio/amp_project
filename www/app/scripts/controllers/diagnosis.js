'use strict';

(function() {

    function controller(scope, Session, location, http, util) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.wrappers = [];

        scope.addWrapper = function addWrapper() {
            scope.wrappers.push({
                start: moment().subtract(1, 'months'),
                end: moment()
            });
            update(scope.wrappers);
        };

        function onSuccess (result) {
            debugger; 
            scope.wrappers = result;
        }

        function onError(err) {
            console.log(err);
            console.log("Error, Connection issue.");
        }

        function load() {
            http.get('/api/historical', {}).success(onSuccess).error(onError);
        }

        function update(wrappers) {
            http.post('/api/historical', wrappers).success(onSuccess).error(onError);
        }

        load();
    }

    angular.module('insightApp')
    .controller('DiagnosisCtrl', ['$scope', 'Session', '$location', '$http', 'util', controller]);

}).call(null);
