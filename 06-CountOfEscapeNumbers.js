// https://leetcode.com/discuss/interview-question/428240/Audible-or-OA-2019-or-Number-of-characters-escaped

let str = "asa#asd!a!s!aadas!kjgdkm!ri#abhi!shi###!#anfij!e";

let ans = "";
let bool = false;
let temp = "";
for (let i in str) {
  if (str[i] === "#") {
    bool = !bool;
    ans += temp;
    temp = "";
  } else if (bool === true) {
    if (str[i] === "!" && str[+i + 1] !== "!" && str[+i + 1] !== "#")
      // temp.push(str[+i+1])
      temp += str[+i + 1];
  }
}
console.log(ans, ans.length);
