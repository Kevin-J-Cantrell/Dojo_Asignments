function changeName(id) {
    var Name = document.querySelector(id)
    var input = window.prompt("Enter your name:")
    Name.innerHTML = input
}
function hide(e) {
    console.log(e)
    e.parentNode.parentNode.style.display = "none";
    document.querySelector('.badge').innerHTML--;
;
}
function add(e) {
    console.log(e)
    e.parentNode.parentNode.style.display = "none";
    document.querySelector('.badge').innerHTML--;
    document.querySelector('.badge1').innerHTML++;
}
