#!/usr/bin/node
function secondBiggest (args) {
  if (args.length <= 2) {
    return 0;
  }

  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  return sortedArgs[1];
}

const args = process.argv.slice(2);

console.log(secondBiggest(args));
