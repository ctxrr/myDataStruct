Array.prototype.insertSort = function() {
  var array = this.slice(0);
  var length = array.length;

  if (length <= 1) {
    return array;
  }

  for (var i = 1; i < length; i++) {
    var temp = array[i];
    for (var j = i; j > 0 && array[j - 1] > temp; j--){
      array[j] = array[j - 1];
    }
    array[j] = temp;
  }
  return array;
};

//heap sort
Array.prototype.heapSort = function() {
  var arr = this.slice(0);
  var length = arr.length;

  function swap(i, j) {
    var tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }

  function max_heapify(start, end) {
    var parent = start;
    var child = start * 2 + 1;
    if (child >= end) {
      return;
    }
    if (child + 1 < end && arr[child] < arr[child + 1]) {
      child++;
    }
    if (arr[parent] < arr[child]) {
      swap(parent, child);
      max_heapify(child, end);
    }
  }

  for (var i = Math.floor(length / 2) - 1; i >= 0; i--) {
    max_heapify(i, length);
  }

  for(var j = length -1; j > 0; j--) {
     swap(0, j);
     max_heapify(0, j);
  }

  return arr;
};

//quick sort
Array.prototype.quickSort = function () {
  var arr = this.slice(0);

  function quick_sort(arr) {
    var len = arr.length;
    if (len <= 1) {
       return arr;
    }

    var midIndex = Math.floor(len / 2);
    var mid = arr[midIndex];
    var left = [];
    var right = [];

    for (var i = 0; i < len; i++) {
      if (i === midIndex) {
        continue;
      }

      if (arr[i] < mid) {
        left.push(arr[i]);
      } else {
        right.push(arr[i]);
      }
    }
    return quick_sort(left).concat([mid], quick_sort(right));
  }

  return quick_sort(arr);

};

Array.prototype.mergeSort = function() {

  var merge = function(left, right) {
    var arr = [];
    while (left.length && right.length)
      arr.push(left[0] <= right[0] ? left.shift() : right.shift());
    return arr.concat(left).concat(right);
  };

  var len = this.length;
  if (len < 2) return this;
  var mid = len / 2;
  return merge(this.slice(0, mid).mergeSort(),
               this.slice(mid).mergeSort());

};

var arr = [12, 290, 278, 21,300, 89, 78, 100, 29, 7, 206];
//var arr = [300, 89, 78, 100, 29, 7, 206];
var a = arr.insertSort();
var b = arr.heapSort();
var c = arr.quickSort();
var d = arr.mergeSort();
console.log(arr);
console.log(a);
console.log(b);
console.log(c);
console.log(d);
