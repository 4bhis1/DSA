// Success

const getCode = (char) => char.charCodeAt(0) - "a".charCodeAt(0);

const wordToArr = (str) => {
  let arr = new Array(26).fill(0);
  for (let i of str) {
    arr[getCode(i)]++;
  }
  return arr;
};

var groupAnagrams = function (strs) {
  const obj = strs.reduce((obj, doc) => {
    if (obj[wordToArr(doc)]) {
      obj[wordToArr(doc)].push(doc);
    } else {
      obj[wordToArr(doc)] = [doc];
    }

    return obj;
  }, {});

  return Object.values(obj);
};
// @lc code=end
