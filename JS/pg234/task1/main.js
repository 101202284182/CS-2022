function checkEligible() { 
    var age = document.getElementById("age").value; 
    age = parseInt(age); 
    if( age>=17 ) { 
        document.getElementById("result").innerHTML = "Yes (Car and moped)"; 
        document.getElementById("result").style.backgroundColor = "green"
    } 
    else if( age==16 ) { 
        document.getElementById("result").innerHTML = "Moped only";
        document.getElementById("result").style.backgroundColor = "green"
    } 
    else { 
        document.getElementById("result").innerHTML ="No";
        document.getElementById("result").style.backgroundColor = "red"
    } 
} 
