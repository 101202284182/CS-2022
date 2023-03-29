function register() {
    var pass = document.getElementsById("pass");
    var passConfirmation = document.getElementsById("passConfirmation")
    
    if(pass.value.length < 8 || passConfirmation.value.length < 8) {
        alert("Password must be at least 8 characters long!")
        return
    }
    if(pass.value != passConfirmation.value) {
        alert("Passwords doesnt match!")
        pass.style.borderColor = "red"
        passConfirmation.style.borderColor = "red"
        return
    }
    alert("Account created successfully")
}