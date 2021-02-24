let section_Python = document.querySelector("#Python");
let section_Javascipt = document.querySelector("#Javascipt");
let section_Cloud = document.querySelector("#Cloud");
let section_Docker = document.querySelector("#Docker");
const url = "localhost:3051/"

section_Python.addEventListener("click", function(){
    let argument = "sections/python/"
    url = url + argument
})