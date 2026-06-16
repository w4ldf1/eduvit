const assert = require("node:assert/strict");
const { originalTern1, tern1IfElse, tern1Switch } = require("./tern1");
const { originalTern2, tern2IfElse, tern2Switch } = require("./tern2");

function checkRange(name, original, ifElseVersion, switchVersion, values) {
  for (const value of values) {
    assert.equal(
      ifElseVersion(value),
      original(value),
      `${name} if...else failed for value ${value}`,
    );
    assert.equal(
      switchVersion(value),
      original(value),
      `${name} switch failed for value ${value}`,
    );
  }
}

checkRange(
  "tern1",
  originalTern1,
  tern1IfElse,
  tern1Switch,
  Array.from({ length: 100 }, (_, index) => index),
);

checkRange(
  "tern2",
  originalTern2,
  tern2IfElse,
  tern2Switch,
  Array.from({ length: 20 }, (_, index) => index + 1),
);

console.log("All conversion checks passed.");
