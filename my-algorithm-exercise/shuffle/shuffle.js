// much more simple, aha
Array.prototype.shuffle = function() {
    for(var j, x, i = this.length; i; j = parseInt(Math.random() * i), x = this[--i], this[i] = this[j], this[j] = x);
    return this;
};

// a little more complicated but work the same.
Array.prototype.shuffleC = function function_name() {

  var m = this.length, t, i;

  while (m) {
    i = Math.floor(Math.random() * m--);
    t = this[m];
    this[m] = this[i];
    this[i] = t;
  }

  return this;

};

var arr = [12, 290, 278, 21,300, 89, 78, 100, 29, 7, 206];
console.log(arr);
console.log(arr.shuffle());
console.log(arr.shuffleC());
