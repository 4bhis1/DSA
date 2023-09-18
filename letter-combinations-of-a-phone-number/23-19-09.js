const numberObj = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

var letterCombinations = function (digits) {
    const result = []

    if (!digits) return result

    let str = ""
    const recurssiveFunction = (index) => {

        if (index === digits.length) {
            result.push(str)
            return
        }
        console.log(digits[index])
        const charcterArray = numberObj[digits[index]]
        for (let i = 0; i < charcterArray.length; i++) {
            str = str + charcterArray[i]
            recurssiveFunction(index + 1)
            str = str.slice(0, -1)
        }

    }

    recurssiveFunction(0)

    return result

};