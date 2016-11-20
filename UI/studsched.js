jQuery(document).ready(function(){
    $.getJSON("challenge_example.json", function(data){
        $.each(data.students,function(key,value){
            console.log(key, value);
			$('#studentName').append('<option value="' + value.name + '">' + value.name + '</option>');
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