document.querySelector('button').addEventListener('click', getFetch)


function getPokemonData(){
    pokemonInfo = getFetch
    let pokeName = pokemonInfo['name']
    document.querySelector("#Name").value += pokeName
    document.querySelector("#frontPic").src = pokemonInfo['sprites']['frontDefault']
    document.querySelector("#backPic").src = pokemonInfo['sprites']['backDefault']
}







async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    let data = await fetch(url)
    let pokemonInfo = await data.json()

    console.log(pokemonInfo)
    return pokemonInfo
}