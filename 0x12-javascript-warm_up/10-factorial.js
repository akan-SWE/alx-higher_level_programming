#!/usr/bin/node

function factorial (base) {
  if (isNaN(base) || base < 1) {
    return 1;
  }
  return base * factorial(base - 1);
}
console.log(factorial(parseInt(process.argv[2])));
