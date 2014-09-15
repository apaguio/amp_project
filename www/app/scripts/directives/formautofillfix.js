'use strict';

(function() {

    

    angular.module('insightApp')
    .directive('formAutofillFix', function ($timeout) {
        return {
            restrict: 'E',
            link: function postLink(scope, element, attrs) {
                element.prop('method', 'post');
                if (attrs.ngSubmit) {
                    $timeout(function () {
                        element
                        .unbind('submit')
                        .bind('submit', function (event) {
                            event.preventDefault();
                            element
                            .find('input, textarea, select')
                            .trigger('input')
                            .trigger('change')
                            .trigger('keydown');
                        scope.$apply(attrs.ngSubmit);
                        });
                    });
                }
            }
        };
    });

}).call(null);
