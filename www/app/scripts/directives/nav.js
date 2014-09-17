'use strict';
(function() {

    function controller($rootScope, scope, Auth, AuthEvents, location) {

        scope.visible = Auth.isAuthenticated();

        scope.$on(AuthEvents.notAuthenticated, function() {
            scope.visible = false;
        });

        scope.logout = function() {
            Auth.logout();
            $rootScope.$broadcast(AuthEvents.logoutSuccess);
            location.path('/');
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
