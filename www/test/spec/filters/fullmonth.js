'use strict';

describe('Filter: fullmonth', function () {

  // load the filter's module
  beforeEach(module('insightApp'));

  // initialize a new instance of the filter before each test
  var fullmonth;
  beforeEach(inject(function ($filter) {
    fullmonth = $filter('fullmonth');
  }));

  it('should return the input prefixed with "fullmonth filter:"', function () {
    var text = 'angularjs';
    expect(fullmonth(text)).toBe('fullmonth filter: ' + text);
  });

});
