/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const flatArr = (arr, n) => {
        if(n <= 0) return arr;
        const newArr = [];
        let hasMoreSubArr = false;
        for(let el of arr){
            if(Array.isArray(el)) {
                hasMoreSubArr = true;
                newArr.push(...el);
            }
            else newArr.push(el);
        }
        if(hasMoreSubArr) return flatArr(newArr, n-1);
        else return newArr;
    }
    return flatArr(arr, n);
};