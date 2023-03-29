function submit() {
    var license = document.getElementById("license").value
    var age = document.getElementById("age").value
    if(license == "yes") {
        license = true
    }
    else{
        license = false
    }

    if(license == true && age >= 17) {
        alert("You can apply for driving license")
        return
    }
    alert("You can't apply for driving license")
}