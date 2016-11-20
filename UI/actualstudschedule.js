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
	name = getUrlParameter("studentName").replace('+'," ");

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
        for (var i = 0; i < classes.length; i++) {

            stime = (parseInt(classes[i].start.substring(2,4)) - 8)*2
            stime += (parseInt(classes[i].start.substring(4)) / 30)
            etime = (parseInt(classes[i].end.substring(2,4)) - 8)*2
            etime += (parseInt(classes[i].end.substring(4)) / 30)
            /*etime - stime
            loop ^
            document.getEl*/
            day = null;
            switch(classes[i].day){
                case "MONDAY":
                    day = 100;
                    break;
                case "TUESDAY":
                    day = 200;
                    break;
                case "WEDNESDAY":
                    day = 300;
                    break;
                case "THURSDAY":
                    day = 400;
                    break;
                case "FRIDAY":
                    day = 500;
                    break;
            }
            pos = day + stime;
            for (var j = stime; j < etime; j++) {
                document.getElementById(pos + '').innerHTML = classes[i].subject;
                pos+= 1;
            }
        }
    });
});
