'use strict';

(function() {

    function controller(scope, Session, location, http, util, historical) {
        http.defaults.headers.post['CSRF-TOKEN'] = Session.csrfToken;
        scope.wrappers = [];

        scope.onWrapperUpdate = function onWrapperUpdate(wrapper) {
            var i = _.findIndex(scope.wrappers, {id: wrapper.id});
            scope.wrappers[i] = wrapper;
        };

        scope.addWrapper = function addWrapper() {
            scope.wrappers.push({
                start: moment().subtract(1, 'days'),
                end: moment(),
                graphs: {
                    powerfactor: true,
                    voltage: true,
                    consumption: true
                }
            });
            update(scope.wrappers);
        };

        function onSuccess (result) {
            scope.wrappers = result;
        }

        function load() {
            historical.load().success(onSuccess).error(util.onError);
        }

        function update(wrappers) {
            historical.update(wrappers).success(onSuccess).error(util.onError);
        }

        load();
    }

    angular.module('insightApp')
    .controller('HistoricalCtrl', ['$scope', 'Session', '$location', '$http', 'util', 'historical', controller]);

}).call(null);
