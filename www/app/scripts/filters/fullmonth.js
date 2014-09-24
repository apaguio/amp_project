'use strict';

angular.module('insightApp')
.filter('fullmonth', function () {
    var months = {
          'jan': 'January',
          'feb': 'February',
          'mar': 'March',
          'apr': 'April',
          'may': 'May',
          'jun': 'June',
          'jul': 'July',
          'aug': 'August',
          'sep': 'September',
          'oct': 'October',
          'nov': 'November',
          'dec': 'December'
    };
    return function (input) {
        if (input) {
            return months[input.toLowerCase()] || input;
        }
        return input;
    };
});
