function manyChecks(a) {
  return (
    (a > 10
      ? "a is bigger than 10"
      : "a is less than or equal to 10 " +
        (a === 5 ? "an example of a special case" : "")) +
    (a === 15 ? "but a is not 15" : "") +
    (a > 5 ? "and a is greater than 5" : "and a is less than or equal to 5 ") +
    (a % 2 ? " and a is odd" : " and a is even ")
  );
}

let a = Math.floor(Math.random() * 20) + 1;
console.log("a =", a);

let ifElseResult = "";

if (a > 10) {
  ifElseResult += "a is bigger than 10";
} else {
  ifElseResult += "a is less than or equal to 10 ";

  if (a === 5) {
    ifElseResult += "an example of a special case";
  }
}

if (a === 15) {
  ifElseResult += "but a is not 15";
}

if (a > 5) {
  ifElseResult += "and a is greater than 5";
} else {
  ifElseResult += "and a is less than or equal to 5 ";
}

if (a % 2) {
  ifElseResult += " and a is odd";
} else {
  ifElseResult += " and a is even ";
}

console.log("if...else:", ifElseResult);

let switchResult = "";

switch (true) {
  case a > 10:
    switchResult += "a is bigger than 10";
    break;
  default:
    switchResult += "a is less than or equal to 10 ";

    switch (a) {
      case 5:
        switchResult += "an example of a special case";
        break;
    }
}

switch (a) {
  case 15:
    switchResult += "but a is not 15";
    break;
}

switch (true) {
  case a > 5:
    switchResult += "and a is greater than 5";
    break;
  default:
    switchResult += "and a is less than or equal to 5 ";
}

switch (a % 2) {
  case 0:
    switchResult += " and a is even ";
    break;
  default:
    switchResult += " and a is odd";
}

console.log("switch:", switchResult);
console.log("ternary:", manyChecks(a));
