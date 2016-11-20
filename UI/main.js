$(document).ready(function(){
    $('#studentDropdown').hide();
    $('#profDropdown').hide();
    $('#cancel').hide();

    $("#studToggle").click(function(){
        $("#studentDropdown").show();
        $("#cancel").show();
        $("#studToggle").hide();
        $("#profToggle").hide();

    });

    $("#profToggle").click(function(){
    	$("#profDropdown").show();
    	$("#cancel").show();
    	$("#studToggle").hide();
    	$("#profToggle").hide();
    });

    $("#cancel").click(function(){
    	$('#studentDropdown').hide();
    	$('#profDropdown').hide();
    	$("#profToggle").show();
    	$("#studToggle").show();
    	$('#cancel').hide();
    });
    
    $.getJSON("challenge_example.json", function(data){
        $.each(data.students,function(key,value){
			$('#studentName').append('<option value="' + value.name + '">' + value.name + '</option>');
        });
        $.each(data.classes, function(key, value){
        	$('#className').append('<option value="' + key + '">' + key + '</option>');
        });

    });
});

function validateStud() {
	var name = document.getElementById("studentName").value;
	if (!name) {
		alert("Please select a name.");
		return false;
	}
	return true;	
}

function validateProf() {
    var className = document.getElementById("className").value;
    if (!className) {
        alert("Please select a Class.");
        return false;
    }
    return true;
}


