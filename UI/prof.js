$(document).ready(function(){
    $.getJSON("challenge_example.json", function(data){
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