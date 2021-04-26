function clickHandler(event){
    //get desig_ex of the selected exercice
    va = event.currentTarget.parentElement.parentElement.getElementsByClassName("des")[0].textContent;
    console.log(va);    

    // Create instance
    //get exercice_id and rep_id
    theUrl = "http://127.0.0.1:8000/api/exercices?desig_ex=" + va; // url to retrieve the exercice from DB
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    va = xmlHttp.responseText;
    var jsonData = JSON.parse(va);
    console.log(jsonFile);


}