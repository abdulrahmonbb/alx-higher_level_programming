#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) return '0';

    const digits = '0123456789abcdefghijklmnopqrstuvwxyz';
    let result = '';

    while (number > 0) {
      result = digits[number % base] + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
