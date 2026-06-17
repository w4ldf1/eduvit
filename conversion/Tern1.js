let a = Math.floor(Math.random() * 100);
console.log("a =", a);

let ifElseResult;
let firstValue;

if (a > 10) {
  firstValue = a;
} else {
  firstValue = a * 2;
}

if (firstValue > 5) {
  ifElseResult = 2 * a + 1;
} else {
  let secondValue;

  if (a < 3) {
    secondValue = 1;
  } else {
    secondValue = 2 * (a - 2);
  }

  if (secondValue > 4) {
    ifElseResult = 5;
  } else if (a % 2 === 0) {
    ifElseResult = 6;
  } else {
    ifElseResult = 7;
  }
}

console.log("if...else:", ifElseResult);

let switchResult;
let switchFirstValue;

switch (true) {
  case a > 10:
    switchFirstValue = a;
    break;
  default:
    switchFirstValue = a * 2;
}

switch (true) {
  case switchFirstValue > 5:
    switchResult = 2 * a + 1;
    break;
  default: {
    let switchSecondValue;

    switch (true) {
      case a < 3:
        switchSecondValue = 1;
        break;
      default:
        switchSecondValue = 2 * (a - 2);
    }

    switch (true) {
      case switchSecondValue > 4:
        switchResult = 5;
        break;
      case a % 2 === 0:
        switchResult = 6;
        break;
      default:
        switchResult = 7;
    }
  }
}

console.log("switch:", switchResult);

let ternaryResult = (a > 10 ? a : a * 2) > 5
  ? 2 * a + 1
  : (a < 3 ? 1 : 2 * (a - 2)) > 4
    ? 5
    : a % 2 === 0
      ? 6
      : 7;

console.log("ternary:", ternaryResult);
