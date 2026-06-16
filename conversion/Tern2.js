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
  // TODO: rewrite originalTern2 using if...else only.
  throw new Error("tern2IfElse is not implemented");
}

function tern2Switch(a) {
  // TODO: rewrite originalTern2 using switch.
  throw new Error("tern2Switch is not implemented");
}

function demoTern2() {
  const a = Math.floor(Math.random() * 20) + 1;

  console.log(`a = ${a}`);
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
