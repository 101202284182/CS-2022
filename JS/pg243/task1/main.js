var userY = []

function graphGen() {
    userY.push(parseInt(document.getElementById("temp").value))
    console.log(userY)

    Plotly.newPlot(document.getElementById('graph'), 
        [{
            y: userY
        }], 
        { 
            margin: { t: 0 } 
        }, 
        {showSendToCloud:true}
    );
}