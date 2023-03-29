function checkVowel(char) {
    return /[aeoiu]/.test(char)
}

function submit() {
    var vowelsCount = 0

    for(var i = 0; i < document.getElementById("userString").value.length; i++) {
        if(checkVowel(document.getElementById("userString").value.charAt(i)) == true) {
            vowelsCount++
        }
    }
    document.getElementById("output").innerHTML = vowelsCount
}