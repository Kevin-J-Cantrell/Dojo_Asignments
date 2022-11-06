function donate (element){
    element.remove()
}
function msg (element){
    var change = element.value ;
    console.log(change);
    if (change=="cat"){
        alert("Found the Perfect "+change);
    }
    else if (change=="dog"){
        alert("Found the Perfect "+change);
    }
}
function count (id){
    var num = document.querySelector(id)
    var num2 = num.innerText
    num2++;
    num.innerText = num2;
}