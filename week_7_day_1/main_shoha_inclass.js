console.log('hello world')
// this is a comment
// on another line

/*
this is a multi line
comment
*/

x = 1
y = 2

z = x + y
console.log(z)

// in JS, you need to declare a variable
var x = 1
var y = 2
var z = x + y;
console.log(typeof z); var w = 4.4;console.log(typeof w);

// Javascript is a compiled language.;
// you don't need to worry about indentation;

var name1 = 'Shoha'
var name2 = "Brandt"
var name3 = `Brendan`

console.log(name1, name2, name3)
console.log(typeof name1)

// Lists in JS, are known as Arrays
var names = ['Shoha', "Brandt", `Brendan`]
console.log(names)
console.log(typeof names)
// To check is something is an array
console.log(Array.isArray(name1))
console.log(Array.isArray(names))

// Dictionaries in JS are known as a JS Object (JSON)
var first_name = "Shoha"

var obj  = {
    'content-type': 'application/json',
    "Grades": [100,100,100],
    first_name : first_name,
    contenttype: 'something'

};
console.log(obj)

// JS HOISTING
console.log(random)
var random = 'random values.....'
console.log(random)

// undeclared, undefined, null
var num; // i am declaring num
console.log(num)
num = 1; // this is assigning value to num
console.log(num)
num = null
console.log(num)

// instead of using VAR, use LET and CONST
// LET and CONST do not hoist.
// console.log(random2)
// const random2 = 'random values.....'
// console.log(random2)

// LET and CONST are both used as variable declarations
// it is the newer ES6 Syntax
let fave_num = 10;
const fave_color = 'blue';

// you cannot reassign value to const
console.log(fave_num)
console.log(fave_color)
fave_num += 13
console.log(fave_num)
// fave_color = 'red'

//  use const until you have to use let
// let and const are also block level declarations


/*    --- MATH OPERATIONS --- */
// addition
console.log('===========MATH STUFF==============')
let sum = 5 + 6;
console.log(sum)
sum += 7;
console.log(sum);
sum ++;
console.log(sum)

// subtraction
let diff = 15-7;
console.log(diff);
diff -= 4;
console.log(diff);
diff --;
console.log(diff);

// multiplication
let prod = 5*5;
console.log(prod);
prod *= 2;
console.log(prod);

// division
let quo = 100/4;
console.log(quo);
quo/=5;
console.log(quo);

// exponential
let square = 5**2;
console.log(square)
square**=2;
console.log(square);

// more Math stuffs
const floor = Math.floor(24.7);
console.log(floor)
const ceil = Math.ceil(24.7)
console.log(ceil)

// interesting behavior
const num1 = 2
const num2 = "3"
const res = num1 + num2
console.log(res)
console.log(typeof res)

// parseInt() and parseFloat()
console.log(parseInt('24.7'), typeof parseInt('24.7'))
console.log(parseFloat('24.7'), typeof parseFloat('24.7'))

/*  ------ JAVASCRIPT FUNTIONS ------ */
console.log('============ Function Portion ==============')
// regulary named function
function nameOfFunction(param1, param2){
    const output = param1 + param2;
    return output
};

console.log(nameOfFunction(100,200));
console.log(nameOfFunction('Le',"Bron"));

// nameless function, but storing it to some variable
const squareMe = function (num){
    return num**2
}
console.log(squareMe(7));



// arrow function is the new ES6 syntax way of creating functions
// format:  () => {}
//  (params go here) => { this is the code block };

const cubeMe = (num)=>{
    return num **3
};
console.log(cubeMe(3))


// arrow function with no paramaters
const a1 = () => {return 'this function does nothing'};
console.log(a1())
// arrow function with ONE paramaters
// if only 1 param, the parenthesis are optional
const a2 = num => {return num**2};
console.log(a2(9))
// arrow function with TWO OR MORE paramaters
const a3 = (num1, num2) => {return num1 + num2};
console.log(a3(9, 999))
// arrow function with SINGLE LINE (meaning we only have a return line)
// the curly braces become optional.. and no return keyword needed
const a4 = (num1, num2) => num1 + num2;
console.log(a4(9, 999))

const a5 = num => num**2;
console.log(a5(100))


// scope is still a thing
let test = 1;
const testFunc = () => {
    let test = 4;
    console.log(test)

};
console.log(test)
testFunc();


// self invoking function
(()=>{
    console.log('this was self-invoked.. meaning i created a nameless function then ran it')
})();
// another one with function keyword
(function (){console.log('DJ Khaled')})();


// CLOSURES
const outer = () => {
    let counter = 0 // private variable
    const inner = () => {
        counter ++
        return counter
    };
    return inner // setter function
};

const addToCounter = outer()
console.log(addToCounter())
1 + 1

console.log(addToCounter())
console.log(addToCounter())
console.log(addToCounter())
console.log(addToCounter())


const addToCounter2 = outer()
console.log(addToCounter2())
console.log(addToCounter2())
console.log(addToCounter2())

console.log(addToCounter())
// END CLOSURES

console.log('============ IF STATEMENTS ===========')

// IF STATEMENTS
// synatx: if ( condition ) { code block }
const ifTest = num => {
    if (num<10) {
        console.log('small number')
    }
    else if ( num < 20 ) {
        console.log('medium number')
    }
    else {
        console.log('beeg number')
    };
};
ifTest(5);
ifTest(15);
ifTest(25);

// ternary operator
// PYTHON: (DO THIS IF TRUE) if CONDITION else ( DO THIS IF FALSE )
// JS:  ( CONDTION ) ? ( DO THIS IF TRUE ) : ( DO THIS IF FALSE )
const getFee1 = (isMember) => {
    return isMember ? '$2.00' : '$10.00'
};


const getFee2 = isMember => isMember ? '$2.00' : '$10.00'

console.log(getFee1(false)); // note.. in JS, boolean true is spelt lowercase
console.log(getFee2(true));

/*  ------ LOOP SECTION ------ */
console.log('============== FOR LOOPS ===============')
//for loop syntax:
// for ( let variable; condition; incrementor ) { codeblock }
const countByOne = (stop) =>  {
    for (let i=1; i<stop; i++) {
        if (i==3){
            console.log('fave number', i)
        }
        else {
            console.log(i)
        }
    }
};
countByOne(9)

const goThroughArray = (arr) => {
    for (let i = 0; i<arr.length; i++) {
        const person = arr[i]
        console.log(person, i)
    }
};

goThroughArray(['Shoha', "Brandt", "Aubrey", "Brendan"])

// ES6 VERSION
// for of SYNTAX
// copying python
const goThroughArray2 = (arr) => {
    for (let person of arr) {
        console.log(person)
    }
};
goThroughArray2(['Matt', 'Todd', "Calvin", "Laurent"])




console.log('============== WHILE LOOPS ===============')
// while loop
// syntax : while (condtion) { codeblock };
const countUpTo = num=> {
    let i = 0;
    while (i < num) {
        console.log(i);
        i++;
    }
    console.log('done')
};
countUpTo(5)

// JS has an extra feature.. Do While

//syntax: do { codeblock } while ( condition );
// do while, will alway occur once. Even if condition is not met.
const countUpToDo = num=> {
    let i = 0;
    do {
        console.log(i);
        i++;
    }
    while (i < num) 
    console.log('done')
};
countUpToDo(5);


// Array Methods
let arrNames = ['Shoha', "Brandt", "Aubrey"]
arrNames.push('Brendan')
console.log(arrNames)
console.log(arrNames[1])
console.log(arrNames[arrNames.length-1])
console.log(arrNames.toString())
console.log(arrNames.join('##'))
console.log(arrNames.slice(1,3))

// splice
const output = arrNames.splice(1, 0, 'Nicole')
console.log(output, 'output')
console.log(arrNames, 'arrNames')
