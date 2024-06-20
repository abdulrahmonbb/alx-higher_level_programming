#!/usr/bin/node

const callMeMoby = require('./101-call_me_moby').CallMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
