$(document).ready(function(){
    $.getJSON("challenge_example.json", function(data){
        obj = null;
        $.each(data.students,function(key,value){
            if (value.name == name) {
                obj = value;
            }
        });
        studID = obj.id;

        classStr = obj.classesTaken;
        regex1 = /^(.+?)(?=,|$)/; 
        regex2 = /^(.+?)(?=-|$)/;
        classes = [];

        while (classStr) {
            var tempObj = {subject: null, 
                day: null, 
                start: null, 
                end: null
            }
            var c = classStr.match(regex1)[0];
            if (classStr.length != 0) {
                classStr = classStr.substring(c.length + 1);
            }
            for (var i = 0; i<4; i++) {
                var val = c.match(regex2)[0];
                if (c.length != 0) {
                    c = c.substring(val.length + 1);
                }
                switch(i) {
                    case 0:
                        tempObj.subject = val;
                        break;
                    case 1: 
                        tempObj.day = val;
                        break;
                    case 2: 
                        tempObj.start = val;
                        break;
                    case 3: 
                        tempObj.end = val;
                        break;
                }
            }
            classes.push(tempObj);
        }
    });
});