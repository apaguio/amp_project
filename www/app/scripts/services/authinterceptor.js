'use strict';

(function() {

    function AuthInterceptor($rootScope, $q, AuthEvents) {

        function responseError (response) {
            $rootScope.$broadcast({
                401: AuthEvents.notAuthenticated,
                403: AuthEvents.notAuthorized,
                419: AuthEvents.sessionTimeout,
                440: AuthEvents.sessionTimeout
            }[response.status], response);
            return $q.reject(response);
        }

        return {
            responseError: responseError
        };
    }

    var deps = ['$rootScope', '$q', 'AuthEvents', AuthInterceptor];
    angular.module('insightApp').factory('AuthInterceptor', deps);

}).call(null);
