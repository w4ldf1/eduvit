const display = document.querySelector("#display");
const history = document.querySelector("#history");
const buttons = document.querySelector(".buttons");

function addToHistory(expression, result) {
  // TODO: create a div, fill it with expression and result, append it to history.
  throw new Error("addToHistory is not implemented");
}

function calculateExpression(expression) {
  // TODO: parse expression and calculate result.
  // Keep validation here, for example division by zero and unknown operation.
  throw new Error("calculateExpression is not implemented");
}

function handleButtonClick(event) {
  const button = event.target.closest("button");

  if (!button) {
    return;
  }

  const value = button.dataset.value;
  const action = button.dataset.action;

  if (value) {
    display.value += value;
    return;
  }

  if (action === "clear") {
    display.value = "";
    return;
  }

  if (action === "calculate") {
    const expression = display.value;
    const result = calculateExpression(expression);

    display.value = result;
    addToHistory(expression, result);
  }
}

buttons.addEventListener("click", handleButtonClick);
