#!/usr/bin/node
exports.esrever = function (list) {
  const len = Math.floor(list.length / 2);
  for (let i = 0; i < len; i++) {
    const lid = list.length - i - 1;
    const holder = list[lid];
    list[lid] = list[i];
    list[i] = holder;
  }
  return (list);
};
