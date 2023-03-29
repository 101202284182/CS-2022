function calc(id) {
    num1 = parseInt(document.getElementById("num1").value);
    num2 = parseInt(document.getElementById("num2").value);

    
    if(id == 0) {
        document.getElementById("result").innerHTML = num1 + num2;
    }
    else if(id == 1) {
        document.getElementById("result").innerHTML = num1 - num2;
    }
    else if(id == 2) {
        document.getElementById("result").innerHTML = num1 * num2;
    }
    else {
        document.getElementById("result").innerHTML = num1 / num2;
    }
}