'use strict';

(function() {

    function Auth(q, http, Session, $rootScope, AuthEvents) {

        function onSuccess(deferred) {
            return function(d) {
                Session.create(d);
                $rootScope.$broadcast(AuthEvents.loginSuccess);
                deferred.resolve(d);
            };
        }

        function onError(deferred) {
            return function(err) {
                console.log(err);
                if (err.status >= 500) {
                    return deferred.reject("Server Error");
                }
                deferred.reject("Login incorrect");
            };
        }

        this.logout = function() {
            http.post('/api/auth/logout').then(function() {
                $rootScope.$broadcast(AuthEvents.logoutSuccess);
            }, function(err) {
                console.log(err);
            });
        };

        this.login = function(credentials) {
            var deferred = q.defer();
            http.post('/api/auth/login', credentials)
                .then(onSuccess(deferred), onError(deferred));
            return deferred.promise;
        };

        this.isAuthorized = function(roles) {
            if (!angular.isArray(roles)) {
                roles = [roles];
            }
            return roles.indexOf(Session.user.role) !== -1;
        };

        this.loadUser = function() {
            var deferred = q.defer();
            if (!!Session.user)  {
                deferred.resolve(Session.user);
            } else {
                http.get('/api/auth/load').then(onSuccess(deferred), onError(deferred));
            }
            return deferred.promise;
        };

        this.isAuthenticated = function() {
            return !!Session.user;
        };

        return this;
    }

    var dependencies = ['$q', '$http', 'Session', '$rootScope', 'AuthEvents', Auth];
    angular.module('insightApp').service('Auth', dependencies);

}).call(null);
