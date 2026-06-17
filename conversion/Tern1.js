function originalTern1(a) {
  return (a > 10 ? a : a * 2) > 5
    ? 2 * a + 1
    : (a < 3 ? 1 : 2 * (a - 2)) > 4
      ? 5
      : a % 2 === 0
        ? 6
        : 7;
}

function tern1IfElse(a) {
  let firstCheckValue;
  let result;

  if (a > 10) {
    firstCheckValue = a;
  } else {
    firstCheckValue = a * 2;
  }

  if (firstCheckValue > 5) {
    result = 2 * a + 1;
  } else {
    let secondCheckValue;

    if (a < 3) {
      secondCheckValue = 1;
    } else {
      secondCheckValue = 2 * (a - 2);
    }

    if (secondCheckValue > 4) {
      result = 5;
    } else if (a % 2 === 0) {
      result = 6;
    } else {
      result = 7;
    }
  }

  return result;
}

function tern1Switch(a) {
  let firstCheckValue;
  let result;

  switch (true) {
    case a > 10:
      firstCheckValue = a;
      break;
    default:
      firstCheckValue = a * 2;
  }

  switch (true) {
    case firstCheckValue > 5:
      result = 2 * a + 1;
      break;
    default: {
      let secondCheckValue;

      switch (true) {
        case a < 3:
          secondCheckValue = 1;
          break;
        default:
          secondCheckValue = 2 * (a - 2);
      }

      switch (true) {
        case secondCheckValue > 4:
          result = 5;
          break;
        case a % 2 === 0:
          result = 6;
          break;
        default:
          result = 7;
      }
    }
  }

  return result;
}

function demoTern1() {
  const a = Math.floor(Math.random() * 100);

  console.log(`a = ${a}`);
  console.log(`ternary: ${originalTern1(a)}`);
  console.log(`if...else: ${tern1IfElse(a)}`);
  console.log(`switch: ${tern1Switch(a)}`);
}

module.exports = {
  originalTern1,
  tern1IfElse,
  tern1Switch,
  demoTern1,
};

if (require.main === module) {
  demoTern1();
}
