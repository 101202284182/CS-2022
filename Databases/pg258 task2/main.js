window.onload = () => {
    updateTable()
};

const firebaseApp = firebase.initializeApp({
    projectId: "CS-2022",
    databaseURL: "https://cs-2022-2074a-default-rtdb.europe-west1.firebasedatabase.app/" 
});
const db = firebaseApp.firestore();

function sendRecord() {
    var quantity = document.getElementById("quantityInput").value;
    var price = document.getElementById("priceInput").value;
    var description = document.getElementById("descriptionInput").value;
    var myDB = firebase.database().ref("pg258/goods");

    record = {
        "Quantity": quantity,
        "Price": price,
        "Description": description
    }

    myDB.push().set(record);

    updateTable()
}

function updateTable() {
    document.getElementById("goodsTable").innerHTML = ""
    var myDB = firebase.database().ref();
    myDB.child("pg258").child("goods").get()
    .then((snapshot) => {
        if(snapshot.exists()) {
            snapshot.forEach(childSnapshot => {
                document.getElementById("goodsTable").innerHTML += "<tr>" + "<td>" + childSnapshot.val().Quantity + "</td>" + "<td>" + childSnapshot.val().Price + "€</td>" + "<td>" + childSnapshot.val().Description + "</td>" + "</tr>";
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