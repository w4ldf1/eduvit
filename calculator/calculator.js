const display = document.querySelector("#display");
const history = document.querySelector("#history");
const buttons = document.querySelector(".buttons");

function addToHistory(expression, result) {
  const item = document.createElement("div");
  item.className = "history-entry";
  item.textContent = `${expression} = ${result}`;
  history.append(item);
}

function calculateNumbers(leftNumber, operator, rightNumber) {
  if (operator === "+") {
    return leftNumber + rightNumber;
  }

  if (operator === "-") {
    return leftNumber - rightNumber;
  }

  if (operator === "*") {
    return leftNumber * rightNumber;
  }

  if (operator === "/") {
    if (rightNumber === 0) {
      return "Ошибка: деление на ноль";
    }

    return leftNumber / rightNumber;
  }

  return "Ошибка: неизвестная операция";
}

function formatResult(result) {
  if (typeof result !== "number") {
    return result;
  }

  if (!Number.isFinite(result)) {
    return "Ошибка вычисления";
  }

  return Math.round(result * 1000000) / 1000000;
}

function calculateExpression(expression) {
  const preparedExpression = expression.replace(/\s+/g, "");
  const parts = preparedExpression.match(/^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$/);

  if (!parts) {
    return "Ошибка: неверный ввод";
  }

  const leftNumber = Number(parts[1]);
  const operator = parts[2];
  const rightNumber = Number(parts[3]);
  const result = calculateNumbers(leftNumber, operator, rightNumber);

  return formatResult(result);
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
