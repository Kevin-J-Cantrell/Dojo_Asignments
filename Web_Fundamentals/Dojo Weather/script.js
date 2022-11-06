function msg() {
    alert("Loading Weather Report....")
}
function Accept(el) {
    var confirm = document.querySelector(el)
    confirm.remove()
}

function c2f (temp) {
    return Math.round(9 / 5 * temp) + 32 
}
function f2c (temp) {
    return Math.round(5 / 9 * (temp - 32))
}

function temperture(element) {
    for (var i = 1; i < 9; i++){
        var change = document.querySelector("#temp"+i);
        var changeValue = parseInt(change.innerText);        
        if (element.value == "C" ){
            change.innerText =f2c(changeValue);
        }
        else {
            change.innerText =c2f(changeValue);            
        }
    }
}

