function calc(id) {
    temp = document.getElementById("temp").value;
    
    if(id == 0) {
        document.getElementById("result").innerHTML = (temp * 9/5) + 32;
    }
    else {
        document.getElementById("result").innerHTML = (temp - 32) * 5/9;
    }
}