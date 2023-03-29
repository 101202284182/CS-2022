function login() {
    username = document.getElementById("username")
    password = document.getElementById("password")

    if(!username.value || !password.value || username.value.length < 0 || username.value.length < 1) {
        alert("Error! Inputs are empty!")
    }
    else {
        document.getElementById("username").value = ""
        alert("Login successful")
    }
    document.getElementById("password").value = ""
}