'use strict';

describe('Controller: PowerviewCtrl', function () {

  // load the controller's module
  beforeEach(module('insightApp'));

  var PowerviewCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PowerviewCtrl = $controller('PowerviewCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
