function clickHandler(event) {
  //get desig_ex of the selected exercice
  va = event.currentTarget.parentElement.parentElement.getElementsByClassName(
    "des"
  )[0].textContent;
  console.log(va);
  //this code get the first element of the table !!! I will fix that

  theUrl = "http://127.0.0.1:8000/api/exercices?desig_ex=" + va; // url to retrieve the exercice from DB
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false); // false for synchronous request
  xmlHttp.send(null);
  va = xmlHttp.responseText;
  var jsonData = JSON.parse(va);
  jsonFile = jsonData[0].json_file;
  console.log(jsonFile);

  //send json file to VEManager
  var vemUrl = "";
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "", true);

  //Envoie les informations du header adaptées avec la requête
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function () {
    //Appelle une fonction au changement d'état.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      // Requête finie, traitement ici.
    }
  };
  xhr.send(jsonFile);
  // xhr.send(new Int8Array());
  // xhr.send(document);
}
