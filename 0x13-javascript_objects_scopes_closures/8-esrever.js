#!/usr/bin/node

exports.esrever = list => {
  for (let i = 0; i < list.length - 1; i++) {
    for (let j = 0; j < list.length - i - 1; j++) {
      // swap
      const temp = list[j];
      list[j] = list[j + 1];
      list[j + 1] = temp;
    }
  }
  return list;
};
