// parse data in JSON file
// might not work for other app users?
// dependent on local file
//var data = JSON.parse(./challenge_example);
//document.getElementById("test").innerHTML = data;

/*function roll(){
	var randomNumber1 = Math.floor(Math.random() * singers.length);
	var randomNumber2 = Math.floor(Math.random() * songs.length);
	var chosenSinger = singers[randomNumber1];
	var chosenSong = songs[randomNumber2];
	document.getElementById("singer").innerHTML = chosenSinger.bold();
	document.getElementById("song").innerHTML = chosenSong.bold();
}*/

function loadJSON(callback) {

	var xobj = new XMLHttpRequest();
	xobj.overrideMimeType("application/json");
	xobj.open('GET', './challenge_example.json', true);
	xobj.onreadystatechange = function() {
		if(xobj.readyState == 4 && xobj.status == "200") {
			callback(xobj.responseText);
		}
	};
	xobj.send(null);
}

function init() {
	loadJSON(function(response) {
		var data = JSON.parse(response);
		document.write(data);
	});
}

init();


