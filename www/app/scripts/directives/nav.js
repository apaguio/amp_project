'use strict';
(function() {

    function controller($rootScope, scope, Auth, AuthEvents, location) {

        scope.visible = Auth.isAuthenticated();

        scope.$on(AuthEvents.notAuthenticated, function() {
            scope.visible = false;
        });

        scope.$on(AuthEvents.loginSuccess, function() {
            scope.visible = true;
        });

        scope.logout = function() {
            Auth.logout();
        };
    }

    angular.module('insightApp')
    .directive('nav', function () {
        var dependencies = ['$rootScope', '$scope', 'Auth', 'AuthEvents', '$location', controller]
        return {
            templateUrl: 'views/directives/nav.html',
            restrict: 'E',
            scope: {
                link: '@'
            },
            controller: dependencies
        };
    });
}).call(null);
