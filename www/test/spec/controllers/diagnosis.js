'use strict';

describe('Controller: DiagnosisCtrl', function () {

  // load the controller's module
  beforeEach(module('insightApp'));

  var DiagnosisCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    DiagnosisCtrl = $controller('DiagnosisCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
