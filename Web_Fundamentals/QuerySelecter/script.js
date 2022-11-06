var count = 1;
var countElement = document.querySelector("#count")
function add (){
    count++;    
    countElement.innerText = "Your lucky number is " + count;
    
}
function subtract (){
    count--;
    countElement.innerText = "Your lucky number is " + count;    
    
    
}