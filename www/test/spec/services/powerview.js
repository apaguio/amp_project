'use strict';

describe('Service: powerview', function () {

  // load the service's module
  beforeEach(module('insightApp'));

  // instantiate service
  var powerview;
  beforeEach(inject(function (_powerview_) {
    powerview = _powerview_;
  }));

  it('should do something', function () {
    expect(!!powerview).toBe(true);
  });

});
