const valid = (string) => {
  // 1.1
  if (string.length <= 1) return false;
  // 1.2
  let trimmed = string.trim();
  // 1.3
  if (/^(?=.*\d)[\d ]+$/.test(trimmed) == false) return false;
  // 2.1
  let arr = trimmed.split("");
  // 2.2
  let filtered = arr.filter((elem) => /^\d+$/.test(elem));
  // 2.3
  let doubled = [];
  for (let i = 0; i < filtered.length; i++) {
    if (i % 2 == 0) {
      let doubledElem = parseInt(filtered[i]) * 2;
      // 3.1
      if (doubledElem > 9) doubled.push(doubledElem - 9);
      // 3.2
      else doubled.push(doubledElem);
    } else {
      doubled.push(parseInt(filtered[i]));
    }
  }
  // 4
  let sum = doubled.reduce((prev, curr) => prev + curr);
  // 4.1
  if (sum % 10 == 0) return true;
  // 4.2
  return false;
};
