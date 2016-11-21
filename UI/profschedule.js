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
        document.getElementById("cname").innerHTML = className;
        $.each(data.classes,function(key,value){
            if (key == className) {
                obj = value;
            }
        });
        sections = [];
        for (var i=0; i<Object.keys(obj).length; i++) {
            sections.push(parseSection(className, Object.keys(obj)[i], Object.values(obj)[i]));
        }
        for (var i=0; i<sections.length; i++) {
            stime = (parseInt(sections[i].start.substring(2,4)) - 8)*2
            stime += (parseInt(sections[i].start.substring(4)) / 30)
            etime = (parseInt(sections[i].end.substring(2,4)) - 8)*2
            etime += (parseInt(sections[i].end.substring(4)) / 30)
            day = null;
            switch(sections[i].day){
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
                document.getElementById(pos + '').innerHTML = sections[i].subject;
                pos+= 1;
            }
        }
        for (var j= 0; j<sections[0].students.length; j++) {
            var table = document.getElementById("sec1");
            var row = table.insertRow(j+1);
            var name = row.insertCell(0);
            var id = row.insertCell(1);
            name.innerHTML = sections[0].students[j].name;
            id.innerHTML = sections[0].students[j].id;
        }
        for (var k= 0; k<sections[1].students.length; k++) {
            var table = document.getElementById("sec2");
            var row = table.insertRow(k+1);
            var name = row.insertCell(0);
            var id = row.insertCell(1);
            name.innerHTML = sections[1].students[k].name;
            id.innerHTML = sections[1].students[k].id;
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