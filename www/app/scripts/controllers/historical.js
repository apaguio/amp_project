'use strict';

(function() {

    function controller(scope, Session, location, http, util, historical) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.wrappers = [];

        scope.addWrapper = function addWrapper() {
            scope.wrappers.push({
                start: moment().subtract(1, 'days').toDate(),
                end: moment().toDate(),
                graphs: {
                    powerfactor: true,
                    voltage: true,
                    consumption: true
                }
            });
            update(scope.wrappers);
        };

        function onSuccess (result) {
            _.each(result, historical.fixServerWrapperObject);
            scope.wrappers = result;
        }

        function load() {
            historical.load().success(onSuccess).error(util.onError);
        }

        function update(wrappers) {
            historical.update(wrappers).success(onSuccess).error(util.onError);
        }

        load();

        scope.$on('historical_removed', function(event, data) {
            _.remove(scope.wrappers, {id: data.id});
        });
    }

    angular.module('insightApp')
    .controller('HistoricalCtrl', ['$scope', 'Session', '$location', '$http', 'util', 'historical', controller]);

}).call(null);
