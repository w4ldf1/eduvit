function originalTern2(a) {
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

function tern2IfElse(a) {
  let message = "";

  if (a > 10) {
    message += "a is bigger than 10";
  } else {
    message += "a is less than or equal to 10 ";

    if (a === 5) {
      message += "an example of a special case";
    }
  }

  if (a === 15) {
    message += "but a is not 15";
  }

  if (a > 5) {
    message += "and a is greater than 5";
  } else {
    message += "and a is less than or equal to 5 ";
  }

  if (a % 2) {
    message += " and a is odd";
  } else {
    message += " and a is even ";
  }

  return message;
}

function tern2Switch(a) {
  let message = "";

  switch (true) {
    case a > 10:
      message += "a is bigger than 10";
      break;
    default:
      message += "a is less than or equal to 10 ";

      switch (a) {
        case 5:
          message += "an example of a special case";
          break;
      }
  }

  switch (a) {
    case 15:
      message += "but a is not 15";
      break;
  }

  switch (true) {
    case a > 5:
      message += "and a is greater than 5";
      break;
    default:
      message += "and a is less than or equal to 5 ";
  }

  switch (a % 2) {
    case 0:
      message += " and a is even ";
      break;
    default:
      message += " and a is odd";
  }

  return message;
}

function demoTern2() {
  const a = Math.floor(Math.random() * 20) + 1;

  console.log(`a = ${a}`);
  console.log(`ternary: ${originalTern2(a)}`);
  console.log(`if...else: ${tern2IfElse(a)}`);
  console.log(`switch: ${tern2Switch(a)}`);
}

module.exports = {
  originalTern2,
  tern2IfElse,
  tern2Switch,
  demoTern2,
};

if (require.main === module) {
  demoTern2();
}
