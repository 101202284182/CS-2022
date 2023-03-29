function joinMailing() {
    if(!document.getElementById("email").value.includes("@") && !document.getElementById("email").value.includes(".")) {
        return false
    }
    return true
}