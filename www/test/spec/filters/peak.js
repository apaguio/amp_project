'use strict';

describe('Filter: peak', function () {

  // load the filter's module
  beforeEach(module('insightApp'));

  // initialize a new instance of the filter before each test
  var peak;
  beforeEach(inject(function ($filter) {
    peak = $filter('peak');
  }));

  it('should return the input prefixed with "peak filter:"', function () {
    var text = 'angularjs';
    expect(peak(text)).toBe('peak filter: ' + text);
  });

});
