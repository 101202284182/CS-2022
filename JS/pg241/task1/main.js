function submit() {
    if(!document.getElementById("output").value) {
        document.getElementById("output").innerHTML += document.getElementById("temp").value
        return
    }
    document.getElementById("output").innerHTML += ", " + document.getElementById("temp").value 
}