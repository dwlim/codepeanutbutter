import json
from pprint import pprint

with open('studentsByAvailability.json') as data_file:    
	    data = json.load(data_file)

with open('classes.json') as data_file1:    
	    data1 = json.load(data_file1)

studentAvail = []
classes = {}
classList = {"classes": {}}
studList = {"students": {}}

def parseTimetoPos(time):
		if time == "NA":
			return -1
		pos = 0
		tod = time[-2:]
		hour = int(time[:2])
		if (tod == "pm" and hour != 12):
			hour += 12
		minute = int(time[3:5])/30
		pos = 2*(hour-8) + minute 
		return pos 

def convertPostoTime(pos):
	time = ""
	if pos > 7:
		time += "PM"
	else:
		time += "AM"
	hour = (pos/2)+8
	if hour < 10:
		time += "0"
	time += str(hour)
	if pos % 2 == 0:
		time += "00"
	else: 
		time += "30"
	return time

def convertSectoStr(sec):
	s = sec["day"].upper() + "-"
	s += convertPostoTime(sec["start"]) + "-"
	s += convertPostoTime(sec["end"])
	return s



def parseStudentAvailability(num):
	dict = {}
	number = str(num)
	name = str(data[number][0])
	dict = {name : {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : []}, "id": number}
	dict[name]["Monday"] = ["Busy"] * 27
	dict[name]["Tuesday"] = ["Busy"] * 27
	dict[name]["Wednesday"] = ["Busy"] * 27
	dict[name]["Thursday"] = ["Busy"] * 27
	dict[name]["Friday"] = ["Busy"] * 27

	for index in data[number][1].keys():
		day = data[number][1][index]["day"]
		start = parseTimetoPos(data[number][1][index]["start"])
		end = parseTimetoPos(data[number][1][index]["end"])
		for j in range(end - start):
			dict[name][day][start + j] = "Free"
	return dict

def parseClasses(num):
	dict = {}
	classCode = str(num)
	name = str(data1['classes'][classCode]["name"])
	dict = {name: {"times": []}}
	for time in data1['classes'][classCode]["times"]:
		start = parseTimetoPos(data1['classes'][classCode]["times"][time]["start"])
		end = parseTimetoPos(data1['classes'][classCode]["times"][time]["end"])
		timeDict = {"day": str(data1['classes'][classCode]["times"][time]["day"]), "start": start, "end": end, "capacity": 20}
		dict[name]["times"].append(timeDict)

	return dict

#section is time1 or time2's dictionary
def addClass(stud, className, section, cList, sList):
	for i in range (section["start"], section["end"]):
		stud.values()[0][section["day"]][i] = className
	section["capacity"] = section["capacity"] - 1
	#add student to class list
	cListStudNum = "student" + str(20-section["capacity"])
	cListStud = {cListStudNum: {"id": stud["id"], "name": stud.keys()[0]}}
	cList["classes"][className][convertSectoStr(section)].update(cListStud)
	#add class to student's classes taken
	if sList["students"]["student" + stud["id"]]["classesTaken"]:
		sList["students"]["student" + stud["id"]]["classesTaken"] += "," 
	sList["students"]["student" + stud["id"]]["classesTaken"] += className + "-" + convertSectoStr(section)


def checkAvailable(time, section):
	for i in range (section["start"], section["end"]):
		if (time[i] != "Free"):
			return 0
	return 1



for i in range(1, len(data)+1):
	studentAvail.append(parseStudentAvailability(i))

for j in range(0, len(data1['classes'])):
	classes.update(parseClasses(j+101))

for className in classes: 
	tempClass = {className: {}}
	for i in range(0, 2):
		sec = convertSectoStr(classes[className]["times"][i])
		tempClass[className].update({sec: {}})
	classList["classes"].update(tempClass)


for student in studentAvail:
	s = "student" + student["id"]
	tempStud = {s: {}}
	tempStud[s].update({"id": student["id"], "name": student.keys()[0], "classesTaken": ""})
	studList["students"].update(tempStud)
