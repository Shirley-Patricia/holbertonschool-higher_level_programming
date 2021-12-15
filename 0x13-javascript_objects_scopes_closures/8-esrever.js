#!/usr/bin/node

exports.esrever = function (list) {
  let i;
  const listrev = [];
  const a = list.length;

  for (i = a - 1; i >= 0; i--) {
    listrev.push(list[i]);
  }
  return listrev;
};
