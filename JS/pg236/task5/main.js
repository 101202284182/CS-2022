function submit() {
    if(document.getElementById("chara").value > 1 || document.getElementById("chara").value < 0) {
        alert("There are must be only 1 character!")
    }
    document.getElementById("charaB").innerHTML = document.getElementById("chara").value
    var charasCount = 0

    for(var i = 0; i < document.getElementById("userString").value.length; i++) {
        if(document.getElementById("userString").value.charAt(i) == document.getElementById("chara").value) {
            charasCount++
        }
    }
    document.getElementById("output").innerHTML = charasCount
}