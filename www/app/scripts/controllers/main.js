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

        var systemRoutes = ['/powerview', '/performance', '/diagnosis', '/settings', '/alerts'];
        scope.login = function(credentials) {
            Auth.login(credentials).then(function() {
                $rootScope.$broadcast(AuthEvents.loginSuccess);
                var lastPage = localStorage.getItem("lastPage");
                if (systemRoutes.indexOf(lastPage) < 0) {
                    location.path('/powerview');
                } else {
                    location.path(lastPage);
                }
            }, function (message) {
                console.log(message);
                scope.error = "Incorrect username or password.";
                $rootScope.$broadcast(AuthEvents.loginFailed);
            });
        };

    }

    var dependencies = ['$scope', 'Auth', '$location', '$rootScope', 'AuthEvents', controller];
    angular.module('insightApp').controller('MainCtrl', dependencies);

}).call(null);
