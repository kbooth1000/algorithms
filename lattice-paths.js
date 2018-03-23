// Starting in the top left corner 
// of a 2×2 grid, and only being able 
// to move to the right and down, there 
// are exactly 6 routes to the bottom 
// right corner.

How many such routes are there through a 20×20 grid? In an n x n grid?

let x = 20,
    y = 20;

let factorial = function (a) {
    let product = a;
    for (var i = 1; i < a; i++) {
        product = product * i;
    }
    return product;
};

console.log(factorial(3));
console.log(factorial(4));
console.log(factorial(5));

let paths = (x,y) => {
    return ( factorial(x+y) ) / ( factorial(x) * factorial(y) );
}

console.log('lattices paths: ' + paths(x,y));

