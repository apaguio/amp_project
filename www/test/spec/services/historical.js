'use strict';

describe('Service: historical', function () {

  // load the service's module
  beforeEach(module('insightApp'));

  // instantiate service
  var historical;
  beforeEach(inject(function (_historical_) {
    historical = _historical_;
  }));

  it('should do something', function () {
    expect(!!historical).toBe(true);
  });

});
