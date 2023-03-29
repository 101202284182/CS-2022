function submit() {
    if(document.getElementById("limit").value < 0) {
        alert("Limit must be over 0")
        return
    }
    
    for(var i = 0; i < document.getElementById("limit").value; i++) {
        document.getElementById("output").innerHTML += i
    }
}