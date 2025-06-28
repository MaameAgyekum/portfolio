<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Calculator</title>
  <style>
    body {
      background-color: #ffe6f0;
      font-family: sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .calculator {
      background-color: #fff0f5;
      padding: 20px;
      border-radius: 15px;
      width: 300px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .display {
      width: 100%;
      font-size: 24px;
      padding: 10px;
      margin-bottom: 10px;
      text-align: right;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }
    button {
      padding: 15px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      background-color: #ffc0cb;
      color: #fff;
      cursor: pointer;
    }
    .clear {
      grid-column: span 4;
      background-color: #ff69b4;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <input type="text" id="display" class="display" disabled>
    <div class="buttons">
      <button onclick="addToDisplay('7')">7</button>
      <button onclick="addToDisplay('8')">8</button>
      <button onclick="addToDisplay('9')">9</button>
      <button onclick="addToDisplay('/')">/</button>

      <button onclick="addToDisplay('4')">4</button>
      <button onclick="addToDisplay('5')">5</button>
      <button onclick="addToDisplay('6')">6</button>
      <button onclick="addToDisplay('*')">*</button>

      <button onclick="addToDisplay('1')">1</button>
      <button onclick="addToDisplay('2')">2</button>
      <button onclick="addToDisplay('3')">3</button>
      <button onclick="addToDisplay('-')">-</button>

      <button onclick="addToDisplay('0')">0</button>
      <button onclick="addToDisplay('.')">.</button>
      <button onclick="calculateResult()">=</button>
      <button onclick="addToDisplay('+')">+</button>

      <button class="clear" onclick="clearDisplay()">Clear</button>
    </div>
  </div>

  <script>
    function addToDisplay(value) {
      document.getElementById('display').value += value;
    }

    function clearDisplay() {
      document.getElementById('display').value = '';
    }

    function calculateResult() {
      try {
        let result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
      } catch (error) {
        document.getElementById('display').value = 'Error';
      }
    }
  </script>
</body>
</html>
