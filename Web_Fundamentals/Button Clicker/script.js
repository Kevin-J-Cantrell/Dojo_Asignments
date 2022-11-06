function changeText(element) {
    if (element.innerText == "Log in") {
        element.innerText = "Log out"
    }
    else{ element.innerText = "Log in"
    }
    console.log(element.innerText)    
}
function likes(){
    alert("ninja Was liked!")
}
function hide(element){
    element.remove()
}

