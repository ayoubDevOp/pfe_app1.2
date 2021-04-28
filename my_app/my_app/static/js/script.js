function clickHandler(event) {
	//get desig_ex of the selected exercice
	va = event.currentTarget.parentElement.parentElement.getElementsByClassName(
		"des"
	)[0].textContent;
	console.log(va);

	// Create instance
	//get exercice_id and rep_id
	theUrl = "http://127.0.0.1:8000/api/exercices?desig_ex=" + va; // url to retrieve the exercice from DB
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false); // false for synchronous request
	xmlHttp.send(null);
	va = xmlHttp.responseText;
	var jsonData = JSON.parse(va);
	console.log(jsonData[0].json_file);


	//send json file to start craeting 

	/*
	var exer_id = jsonData[0].id;
	var rep_id = jsonData[0].repertoire;
	var exer_desig = jsonData[0].desig_ex;

	//var jsonText =
	//send json file to VEManager
	var insUrl = "http://127.0.0.1:8000/api/instances/";
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "", true);

	//Envoie les informations du header adaptées avec la requête
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;");

	xhr.onreadystatechange = function () {
		//Appelle une fonction au changement d'état.
		if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
			// Requête finie, traitement ici.
			console.log("done");
		}
	};
	//xhr.send(jsonText);
	// xhr.send(new Int8Array());
	// xhr.send(document);
	//console.log(exer_id + "	+	" + rep_id);

	var details = {
		desig_ins: "ins1",
		lien: "some links",
		outputgeneration: "",
		repertoire: rep_id,
		exercice: exer_id,
	};

	var formBody = [];
	for (var property in details) {
		var encodedKey = encodeURIComponent(property);
		var encodedValue = encodeURIComponent(details[property]);
		formBody.push(encodedKey + "=" + encodedValue);
	}
	formBody = formBody.join("&");

	fetch("http://127.0.0.1:8000/api/instances/", {
		method: "POST",
		headers: {
			Cookie: "csrftoken=", //+ getCookie('csrftoken').substr(0,getCookie('csrftoken').indexOf(';')),
			"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
		},
		body: formBody,
	});*/
}

function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
