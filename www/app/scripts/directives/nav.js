'use strict';
(function() {

    function ModalInstanceController($scope, $modalInstance) {

        $scope.ok = function () {
            $modalInstance.close();
        };

        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
    }

    function controller($rootScope, scope, Auth, AuthEvents, location, $modal) {

        scope.visible = Auth.isAuthenticated();

        scope.$on(AuthEvents.notAuthenticated, function() {
            scope.visible = false;
        });

        scope.$on(AuthEvents.loginSuccess, function() {
            scope.visible = true;
        });

        scope.logout = function() {

            var modalInstance = $modal.open({
                templateUrl: 'logoutModal.html',
                controller: 'ModalInstanceCtrl'
            });

            modalInstance.result.then(function() {
                Auth.logout();
            }, function() {
                $log.info('Modal dismissed at: ' + new Date());
            });

        };
    }

    angular.module('insightApp').controller('ModalInstanceCtrl', ModalInstanceController);
    angular.module('insightApp')
    .directive('nav', function () {
        var dependencies = ['$rootScope', '$scope', 'Auth', 'AuthEvents', '$location', '$modal', controller]
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
