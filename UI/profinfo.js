$(document).ready(function(){
    $.getJSON("challenge_example.json", function(data){
        $.each(data.classes, function(key, value){
        	$('#className').append('<option value="' + key + '">' + key + '</option>');
        });

    });
});

function validateProf() {
    var className = document.getElementById("className").value;
    if (!className) {
        alert("Please select a Class.");
        return false;
    }
    return true;
}