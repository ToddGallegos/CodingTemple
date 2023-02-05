// get elements that are already on page by document.getElementBy... TagName or ID or class etc
// can add .addEventListener to it here, or in HTML as "onclick=" etc.
const h1s = document.getElementsByTagName("h1");

h1s[0].innerHTML = "I changed this from JavaScript!";

// create a function that grabs the click event's target and then changes it's class
const changeColor = (event) => {
    console.log("I WAS CLICKED");
    const colorButton = event.target;
    if (colorButton.className == "btn btn-primary") {
        colorButton.className = "btn btn-success";
    } else if (colorButton.className == "btn btn-success") {
        colorButton.className = "btn btn-danger";
    } else {
        colorButton.className = "btn btn-primary";
    }
};

// creating an element that is not already on the page, adding attributes, adding event listener
const colorButton1 = document.createElement("button");
colorButton1.id = "color";
colorButton1.innerText = "ColorChanger?";
colorButton1.addEventListener("mouseover", changeColor);
// document.body.append(colorButton1)

// selecting a specific div to append button to so that it doesn't just show up at bottom of body
buttonDiv = document.getElementById("append-here");
buttonDiv.append(colorButton1);

// adding another event listener to the same button
colorButton1.addEventListener("click", () => {
    const moreText = document.createElement('h2')
    moreText.innerText = "I am Alive!"
    buttonDiv.append(moreText)
    
})

// grab form data from submit event

const form = document.getElementById('pokeForm')

form.addEventListener('submit', (event) => {
    // for SUBMIT events: ALWAYS ALWAYS ADD event.preventDefault() otherwise the page will automatically refresh after the event and you'll lose submitted data
    event.preventDefault();
    // submit event target is the entire form.

    // grabbing info from event:
    // 2 ways to grab same data from form, both through event target
    const searchTerm1 = event.target.children[1].value // index 1 because form has 3 children: label, input, and submit. 
    const searchTerm2 = event.target.pokeName.value
    console.log(searchTerm1, searchTerm2)

    // grabbing info straight from document:
    const searchTerm3 = document.getElementById('poke_name').value
    console.log(searchTerm3)
})