window.onload = () => {
    updateTable()
};

const firebaseApp = firebase.initializeApp({
    projectId: "CS-2022",
    databaseURL: "https://cs-2022-2074a-default-rtdb.europe-west1.firebasedatabase.app/" 
});
const db = firebaseApp.firestore();

function sendRecord() {
    var temp = document.getElementById("tempInput").value;
    var myDB = firebase.database().ref("pg258/temps");

    record = {
        "temp": temp
    }

    myDB.push().set(record);

    updateTable()
}

function updateTable() {
    document.getElementById("tempTable").innerHTML = ""
    var myDB = firebase.database().ref();
    myDB.child("pg258").child("temps").get()
    .then((snapshot) => {
        if(snapshot.exists()) {
            snapshot.forEach(childSnapshot => {
                document.getElementById("tempTable").innerHTML += "<tr><td>" + childSnapshot.val().temp + "</td></tr>";
            });
        } 
        else {
            console.log("No data available");
        }
    })
    .catch((error) => {
        console.error(error);
    });
}