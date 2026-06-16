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
  // TODO: rewrite originalTern1 using if...else only.
  throw new Error("tern1IfElse is not implemented");
}

function tern1Switch(a) {
  // TODO: rewrite originalTern1 using switch.
  throw new Error("tern1Switch is not implemented");
}

function demoTern1() {
  const a = Math.floor(Math.random() * 100);

  console.log(`a = ${a}`);
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
