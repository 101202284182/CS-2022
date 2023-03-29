function submit() {
    document.getElementById("output").innerHTML = ""
    if(parseInt(document.getElementById("limit").value) < 0 || parseInt(document.getElementById("increment").value) < 0 || parseInt(document.getElementById("start").value < 0)) {
        alert("Limit/increment/starting point must be over 0")
        return
    }

    for(var i = parseInt(document.getElementById("start").value); i <= parseInt(document.getElementById("limit").value); i += parseInt(document.getElementById("increment").value)) {
        document.getElementById("output").innerHTML += i
    }
}