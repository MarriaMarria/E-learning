let section_Python = document.querySelector("#Python");
let section_Javascipt = document.querySelector("#Javascipt");
let section_Cloud = document.querySelector("#Cloud");
let section_Docker = document.querySelector("#Docker");
const url = "localhost:3051/"

section_Python.addEventListener("click", function(){
    let argument = "sections/python/"
    url = url + argument
});
section_Javascript.addEventListener("click", function () {
  let argument = "sections/js/";
  url = url + argument;
});
section_Cloud.addEventListener("click", function () {
  let argument = "sections/cloud/";
  url = url + argument;
});
section_Docker.addEventListener("click", function () {
  let argument = "sections/docker/";
  url = url + argument;
});