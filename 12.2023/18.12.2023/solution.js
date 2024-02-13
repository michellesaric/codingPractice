const solution = () => {
  let k = prompt("Enter any number:", 17);

  if (isNaN(k)) {
    alert("Your input was not a number.");
    return;
  }
  k = parseInt(k);
  const list = [10, 15, 3, 7];

  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length; j++) {
      if (list[i] + list[j] === k) {
        alert(`The sum of ${list[i]} and ${list[j]} is ${k}`);
      }
    }
  }
};

solution();
