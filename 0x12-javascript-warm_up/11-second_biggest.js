#!/usr/bin/node

// Second biggest!

let args = process.argv.slice(2);

if (args.length <= 1) {
  console.log('0');
} else {
  args = arrToInt(args);
  console.log(secondBiggest(args));
}

function arrToInt (array) {
  // convert the elements of an array to int if possible
  // and return the value
  const arr = array.map((x) => x); // copy array

  let i = 0;
  for (const num of arr) {
    if (!isNaN(num)) {
      arr[i] = parseInt(num);
    }
    i++;
  }
  return arr;
}

function secondBiggest (a) {
  // Return the second biggest value in a list
  const res1 = rmvBiggest(a);
  const res2 = rmvBiggest(res1.arr);

  return (res2.val);
}

function rmvBiggest (array) {
  // remove and return the biggest value in a list
  // as well as the list in a dictionary
  // res = {'arr': array, 'max': max};
  const list = array.map((x) => x); // copy array

  let max = list[0];
  let i = 0;
  let idx = 0;
  for (const num of list) {
    if ((!isNaN(num)) && num > max) {
      max = num;
      idx = i;
    }
    i++;
  }
  list.splice(idx, 1);
  const res = {
    arr: list,
    val: max
  };
  return (res);
}
