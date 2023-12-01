var actual = document.getElementById("actualInput");
var target = document.getElementById("targetInput");
var confirmButton = document.getElementById("confirm");
var output = document.getElementById("result");

function thermostatModel() {
    if(parseInt(actual.value) < parseInt(target.value)) {
        output.value = "1";
        return 1
    }
    output.value = "0";
    return 0;
}