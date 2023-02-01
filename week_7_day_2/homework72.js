//==========Exercise #1 ===========//
/*
Write a function that parses through the below object and displays all of their
favorite food dishes as shown:
*/

let person3 = {
    pizza: ["Deep Dish", "South Side Thin Crust"],
    tacos: "Anything not from Taco bell",
    burgers: "Portillos Burgers",
    ice_cream: ["Chocolate", "Vanilla", "Oreo"],
    shakes: [
        {
            oberwise: "Chocolate",
            dunkin: "Vanilla",
            culvers: "All of them",
            mcDonalds: "Sham-rock-shake",
            cupids_candies: "Chocolate Malt",
        },
    ],
};

const listFavorites = (personObject) => {
    console.log(`Favorites:
    \nPIZZAS: ${[...personObject.pizza]}
    \nTACOS: ${personObject.tacos}
    \nBURGERS: ${personObject.burgers}
    \nICE CREAM: ${[...personObject.ice_cream]}
    \nSHAKES:`);
    for (const [key, value] of Object.entries(personObject.shakes[0])) {
        console.log(`  ${key.toUpperCase()}: ${value}`);
    }
};

listFavorites(person3);

//=======Exercise #2=========//
/*
Write an object prototype for a Person that has a name and age, has a
printInfo method, and also has a method that 
increments the persons age by 1 each time the method is called.
Create two people using the 'new' keyword, and print 
both of their infos and increment one persons
age by 3 years. Use an arrow function for both methods
*/

// Create our Person Prototype

function Person(name, age) {
    this.name = name;
    this.age = age;
    // Use an arrow to create the printInfo method
    this.printInfo = () => {
        console.log(`name = ${this.name}\nage = ${this.age}`);
    };
    // Create another arrow function for the addAge method that takes a single parameter
    this.addAge = (num = 1) => {
        this.age += num;
    };
}

let tom = new Person("Tom", 30);
let sally = new Person("Sally", 25);

// Adding to the age
tom.addAge();
tom.printInfo();

sally.addAge(3);
sally.printInfo();

/***************************************************/

class Alien {
    constructor(name, age) {
        (this.name = name), (this.age = age);
    }

    printInfo() {
        console.log(`Alien name: ${this.name}\nAlien age: ${this.age}`);
    }

    addAge(num = 100) {
        this.age += num;
    }
}

let zappy = new Alien("Zappy", 9001);
zappy.addAge();
zappy.printInfo();

// =============Exercise #3 ============//
/*
    Create a Promised based function that will check a string to determine if it's length is greater than 10.
    If the length is greater than ten console log "Big word". 
    If the length of the string is less than 10 console log "Small Number"
*/

promiseCheckLength = (string) => {
    return new Promise((resolve, reject) => {
        if (string.length > 10) {
            resolve("promise Big word");
        } else {
            reject("promise Small Number");
        }
    });
};

promiseCheckLength("0123456789") // This function logs its output AFTER the async/await version below. 
    .then((result) => {
        console.log(result);
    })
    .catch((error) => {
        console.log(error);
    });

/********************************************/

function checkLength(string) {
    if (string.length > 10) {
        console.log("async Big word");
    } else {
        console.log("async Small Number");
    }
}

async function outerCheckLength(string) {
    response = await checkLength(string);
    return response;
}

outerCheckLength("12345678910");