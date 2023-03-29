var userYTemp = []
var userYHumid = []
var humidInput = document.getElementById("humid")
var tempInput = document.getElementById("temp")

function graphGen() {
    if(humidInput.value || humidInput.value != "") {
        userYHumid.push(parseInt(humidInput.value))
    }
    if(tempInput.value || tempInput.value != "") {
        userYTemp.push(parseInt(tempInput.value))
    }
    
    var trace1 = {
        y: userYTemp,
        type: 'scatter',
        name: 'Temperature'
    }

    var trace2 = {
        y: userYHumid,
        type: 'scatter',
        name: 'Humidity'
    }

    var data = [trace1, trace2]

    Plotly.newPlot('graph', data);
}