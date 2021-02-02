#!/usr/bin/node
function add (i, j) {
  console.log(parseInt(i) + parseInt(j));
}
add(process.argv[2], process.argv[3]);
