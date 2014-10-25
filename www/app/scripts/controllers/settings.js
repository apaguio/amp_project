'use strict';

(function() {

    function controller(scope, settings, util) {

        settings.load().then(function(result) {
            scope.settings = result.data;
            scope.originalSettings = _.clone(scope.settings);
        }, util.onError());

        scope.typing = function() {
            scope.error = null;
            scope.success = null;
        };

        scope.save = function save() {
            if (scope.settings.password !== scope.settings.cpassword) {
                scope.error = "Passwords do not match.";
            } else {
                settings.update(scope.settings.password, scope.settings.facility_name).then(function() {
                    scope.success = "Settings updated successfully.";
                }, function(err) {
                    console.log(err);
                    scope.error = err.message || "Server error.";
                });
            }
        };

        scope.cancel = function cancel() {
            scope.settings = _.clone(scope.originalSettings);
        };
    }

    angular.module('insightApp')
    .controller('SettingsCtrl', ['$scope', 'settings', 'util', controller]);

}).call(null);
