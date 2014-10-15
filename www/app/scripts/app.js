'use strict';
(function() {

    var systemRoutes = ['/powerview', '/performance', '/historical', '/settings', '/alerts'];
    var app = angular
    .module('insightApp', [
        'ngCookies',
        'ngResource',
        'ngSanitize',
        'ngRoute',
        'ui.bootstrap'
    ]);

    app.constant('AuthEvents', {
        loginSuccess: 'auth-login-success',
        loginFailed: 'auth-login-failed',
        logoutSuccess: 'auth-logout-success',
        sessionTimeout: 'auth-session-timeout',
        notAuthenticated: 'auth-not-authenticated',
        notAuthorized: 'auth-not-authorized'
    });

    app.config(function ($routeProvider, $httpProvider) {
        $routeProvider
        .when('/', {
            templateUrl: 'views/main.html',
            controller: 'MainCtrl',
            access: 'anonymous'
        })
        .when('/powerview', {
            templateUrl: 'views/powerview.html',
            controller: 'PowerviewCtrl',
            access: 'user'
        })
        .when('/settings', {
            templateUrl: 'views/settings.html',
            controller: 'SettingsCtrl',
            access: 'user'
        })
        .when('/performance', {
            templateUrl: 'views/performance.html',
            controller: 'PerformanceCtrl',
            access: 'user'
        })
        .when('/historical', {
            templateUrl: 'views/historical.html',
            controller: 'HistoricalCtrl',
            access: 'user'
        })
        .when('/alerts', {
            templateUrl: 'views/alerts.html',
            controller: 'AlertsCtrl',
            access: 'user'
        })
        .otherwise({
            redirectTo: '/'
        });

        $httpProvider.interceptors.push([
            '$injector', function ($injector) {
                return $injector.get('AuthInterceptor');
            }
        ]);
    });

    app.run(['$rootScope', 'Auth', 'AuthEvents', '$location', 'Session',
    function($rootScope, Auth, AuthEvents, location, Session) {
        var next;
        function notAuth(event, err) {
            if (next.originalPath !== '/') {
                console.log(event.name);
                //if (event.name === "auth-not-authenticated") {
                //}
                Session.destroy();
                location.path('/');
            } else {
                console.log(err);
            }
        }

        function loginSuccess(event, err) {
            if (next.originalPath === '/') {
                var lastPage = localStorage.getItem("lastPage");
                if (systemRoutes.indexOf(lastPage) < 0) {
                    location.path('/powerview');
                } else {
                    location.path(lastPage);
                }
            }
        }

        $rootScope.$on('$routeChangeStart', function (event, pathNext) {
            next = pathNext;
            Auth.loadUser().then(function() {
                if (location.path() !== '/') {
                    localStorage.setItem("lastPage", location.path());
                }
            });
        });

        $rootScope.$on(AuthEvents.loginSuccess, loginSuccess);
        $rootScope.$on(AuthEvents.notAuthorized, notAuth);
        $rootScope.$on(AuthEvents.notAuthenticated, notAuth);
        $rootScope.$on(AuthEvents.sessionTimeout, notAuth);
        $rootScope.$on(AuthEvents.logoutSuccess, notAuth);
    }]);

}).call(null);
