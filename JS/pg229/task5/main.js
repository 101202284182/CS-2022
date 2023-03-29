function login() {
    username = document.getElementById("username")
    password = document.getElementById("password")

    if(!username.value || !password.value || username.value.length < 0 || username.value.length < 1) {
        alert("Error! Inputs are empty!")
    }
    else {
        username.value = ""
        username.style.borderColor = "red"
        password.style.borderColor = "red"
        alert("Incorrect password")
    }
    password.value = ""
}