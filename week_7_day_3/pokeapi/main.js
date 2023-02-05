// using javascript to grab data from an API via http request and turn it into HTML elements for display

const getFormData = async (event) => {
    event.preventDefault()
    const pokemon = event.target.pokemon.value
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemon}`

    // fetch() built in function to make http request
    // axios.get() (need to import or install library?)

    const response = await fetch(url)

    const data = await response.json()

    const name = data['name']
    const id = data.id
    const imgUrl = data.sprites.front_default

    const myData = {
        name: name,
        id: id,
        imgUrl: imgUrl
    }

    addToPage(myData)
}

// using data passed from getForm async await http request function to add HTML
const addToPage = (p) => {
    const card = document.createElement('div')
    card.innerHTML = `
    <div class="card" style="width: 18rem;">
        <img src="${p.imgUrl}" class="card-img-top" alt="${p.name}">
    <div class="card-body">
        <h5 class="card-title">${p.name}</h5>
    </div>
    </div>
    `

    // logic to replace current pokemon with new pokemon if div is already filled
    const container = document.querySelector(".container")
    if (container.innerHTML !== ''){
        container.innerHTML = ''
    }
    container.append(card)
}

const myForm = document.getElementById('myForm')
myForm.addEventListener('submit', getFormData)