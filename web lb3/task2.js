function checkNumbers(arr) {
    for (let item of arr) {
        if (typeof item !== 'number') {throw new Error('элемент массива не является числом');}
    }
}

function sort(order, arr) {
    checkNumbers(arr);
    const newArr = [...arr];
    if (order) {newArr.sort((a, b) => a - b);} 
    else {newArr.sort((a, b) => b - a);}
    return newArr;
}

function min(arr) {checkNumbers(arr); return Math.min(...arr);}
function max(arr) {checkNumbers(arr); return Math.max(...arr);}

function find(arr, value) {checkNumbers(arr); return arr.includes(value);}
function replicaRemove(arr) {checkNumbers(arr); return [...new Set(arr)];}



