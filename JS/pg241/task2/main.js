function submit() {
    document.getElementById("avg").innerHTML = document.getElementById("output").value / document.getElementById("output").innerHTML.split(", ").length
    if(!document.getElementById("output").value) {
        document.getElementById("output").innerHTML += document.getElementById("temp").value
        return
    }

    for(var i = 0; i <= document.getElementById("output").innerHTML.split(", ").length; i++) {
        var summ = summ + document.getElementById("output").innerHTML.split(", ")[i]
    }

    document.getElementById("temp").innerHTML = summ / i
    document.getElementById("output").innerHTML += ", " + document.getElementById("temp").value 
}