function calc() {
    height = document.getElementById("height").value;
    radius = document.getElementById("radius").value;

    if(isNaN(height) == true || isNaN(radius) == true) {
        alert("Error! NaN")
    }
    else {
        alert(Math.PI * Math.pow(radius, 2) * height)
    }
}