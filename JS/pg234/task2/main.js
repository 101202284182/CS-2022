function register() {
    if(document.getElementById("pass").value != document.getElementById("passConfirmation").value) {
        alert("Passwords doesnt match!")
        document.getElementById("pass").style.borderColor = "red"
        document.getElementById("passConfirmation").style.borderColor = "red"
    }
    else {
        alert("Account created successfully")
    }
}