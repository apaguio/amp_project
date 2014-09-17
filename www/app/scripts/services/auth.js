'use strict';

(function() {

    function Auth(q, http, Session) {

        this.logout = function() {
            Session.destroy();
        };

        this.login = function(credentials) {
            var deferred = q.defer();
            http
                .post('/api/login', credentials)
                .then(function (res) {
                    var d = res.data;
                    if (d.status === "error") {
                        deferred.reject(d.data.message);
                    } else {
                        http.defaults.headers.post['CSRF-TOKEN'] = res.data.csrf_token;
                        Session.create(d.data.session_id, d.data.user_id,
                            d.data.user_role, d.data.csrf_token);
                        deferred.resolve(d.data);
                    }
                });
            return deferred.promise;
        };

        this.isAuthorized = function(roles) {
            if (!angular.isArray(roles)) {
                roles = [roles];
            }
            return (this.isAuthenticated() &&
                    roles.indexOf(Session.role) !== -1);
        };

        this.isAuthenticated = function() {
            return !!Session.userId;
        };

        return this;
    }

    var dependencies = ['$q', '$http', 'Session', Auth];
    angular.module('insightApp').service('Auth', dependencies);

}).call(null);
