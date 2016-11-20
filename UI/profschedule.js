var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};


$(document).ready(function(){
    $.getJSON("challenge_example.json", function(data){
        className = getUrlParameter("className")
        obj = null;
        $.each(data.classes,function(key,value){
            if (key == className) {
                obj = value;
            }
        });
        sections = [];
        for (var i=0; i<Object.keys(obj).length; i++) {
            sections.push(parseSection(className, Object.keys(obj)[i], Object.values(obj)[i]));
        }
        console.log(sections);
    });
});

function parseSection(subject, str, students) {
    regex1 = /^(.+?)(?=,|$)/; 
    regex2 = /^(.+?)(?=-|$)/;
    var tempObj = {
            subject: subject, 
            day: null, 
            start: null, 
            end: null,
            students: []
        }
    while (str) {
        var c = str.match(regex1)[0];
        if (str.length != 0) {
            str = str.substring(c.length + 1);
        }
        for (var i = 0; i<3; i++) {
            var val = c.match(regex2)[0];
            if (c.length != 0) {
                c = c.substring(val.length + 1);
            }
            switch(i) {
                case 0: 
                    tempObj.day = val;
                    break;
                case 1: 
                    tempObj.start = val;
                    break;
                case 2: 
                    tempObj.end = val;
                    break;
            }
        }
    }
    for (var i = 0; i< Object.values(students).length; i++){
        tempObj.students.push(Object.values(students)[i]);
    }

    return tempObj;
}