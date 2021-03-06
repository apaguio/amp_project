'use strict';

describe('Directive: performance', function () {

  // load the directive's module
  beforeEach(module('insightApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<performance></performance>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the performance directive');
  }));
});
