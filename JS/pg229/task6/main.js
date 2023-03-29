function changeTheme(themeId) { // id 0 - original, id 1 - bigger text, id 2 - colorblind
    if(themeId === 1) {
        document.body.style.fontSize = "1.5em";
        for(var i = 0; i < document.getElementsByClassName("container")[0].childElementCount; i++) {
            document.getElementsByClassName("card")[i].children[0].style.fontSize = "2.5em";
        }
    }
    else if(themeId === 2) {
        document.getElementsByClassName("navbar")[0].style.backgroundColor = "#58EE01";
    }
    else {
        document.getElementsByClassName("navbar")[0].style.backgroundColor = "#F05454"
        document.body.style.fontSize = "1em";
        for(var i = 0; i < document.getElementsByClassName("container")[0].childElementCount; i++) {
            document.getElementsByClassName("card")[i].children[0].style.fontSize = "1.5em";
        }
    }
}