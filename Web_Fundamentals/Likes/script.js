
function Likes(id) {
    var countElement = document.querySelector(id);
    var count = countElement.innerText
    count++;    
    countElement.innerText = count;     
}

