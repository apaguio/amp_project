'use strict';

(function() {

    function Session() {
        // AngularJS will instantiate a singleton by calling "new" on this function
        this.create = function (user) {
            this.user = user;
        };

        this.destroy = function () {
            this.user = null;
        };
    }

    angular.module('insightApp')
    .service('Session', Session);

}).call(null);
