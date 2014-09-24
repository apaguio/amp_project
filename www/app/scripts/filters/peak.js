'use strict';

angular.module('insightApp')
.filter('peak', function () {
    return function (input) {
        if (input === 'onpeak') {
            return 'On Peak';
        } else if (input === 'offpeak') {
            return 'Off Peak';
        } else if (input  === 'partpeak') {
            return 'Part Peak';
        }
        return input;
    };
});
