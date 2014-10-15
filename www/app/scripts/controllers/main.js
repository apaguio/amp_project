'use strict';

(function() {

    function controller(scope, Auth, location, $rootScope, AuthEvents) {

        scope.credentials = {
            username: '',
            password: ''
        };

        if (Auth.isAuthenticated()) {
            location.path(localStorage.getItem("lastPage") || '/powerview');
        }

        scope.typing = function() {
            scope.error = null;
        };

        scope.login = function(credentials) {
            Auth.login(credentials).then(function() {
                // Everything is handled in loginSuccess in app.js
            }, function (message) {
                console.log(message);
                scope.error = message;
                $rootScope.$broadcast(AuthEvents.loginFailed);
            });
        };

    }

    var dependencies = ['$scope', 'Auth', '$location', '$rootScope', 'AuthEvents', controller];
    angular.module('insightApp').controller('MainCtrl', dependencies);

}).call(null);
