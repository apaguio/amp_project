'use strict';

/**
 * @ngdoc service
 * @name insightApp.util
 * @description
 * # util
 * A collection of utilities used all over the system
 */
(function() {

    var fifteen = 15 * 60;

    function util() {

        this.toDate = function toDate(pyTimestamp) {
            return moment(pyTimestamp).toDate();
        };

        this.toDateRange = function toDateRange(timeformatted) {
            var d0 = new Date(),
                d1 = new Date();
            var pyTimestamp = moment(timeformatted).unix();
            var start = Math.floor(pyTimestamp - (pyTimestamp % fifteen));
            var end = start + fifteen;
            d0.setTime(start * 1000);
            d1.setTime(end * 1000);
            return [d0, d1];
        };

        this.onError = function onError(err) {
            console.log(err);
        };
    }

    angular.module('insightApp').service('util', util);

}).call(null);