import json
from pprint import pprint
import time

t0 = time.time()

with open('studentsByAvailability.json') as data_file:    
	    data = json.load(data_file)

with open('classes.json') as data_file1:    
	    data1 = json.load(data_file1)

studentAvail = []
classes = []
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
	dict = {"name": name, "schedule": {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : []}, "id": number, "numOfClasses" : 0, "subjects" : []}
	dict["schedule"]["Monday"] = ["Busy"] * 27
	dict["schedule"]["Tuesday"] = ["Busy"] * 27
	dict["schedule"]["Wednesday"] = ["Busy"] * 27
	dict["schedule"]["Thursday"] = ["Busy"] * 27
	dict["schedule"]["Friday"] = ["Busy"] * 27

	for index in data[number][1].keys():
		day = data[number][1][index]["day"]
		start = parseTimetoPos(data[number][1][index]["start"])
		end = parseTimetoPos(data[number][1][index]["end"])
		for j in range(end - start):
			dict["schedule"][day][start + j] = "Free"
	return dict

def parseClasses(num):
	dict = {}
	classCode = str(num)
	name = str(data1['classes'][classCode]["name"])
	dict = {"subject": name, "times": []}
	for time in data1['classes'][classCode]["times"]:
		start = parseTimetoPos(data1['classes'][classCode]["times"][time]["start"])
		end = parseTimetoPos(data1['classes'][classCode]["times"][time]["end"])
		timeDict = {"day": str(data1['classes'][classCode]["times"][time]["day"]), "start": start, "end": end, "capacity": 20}
		dict["times"].append(timeDict)

	return dict

#section is time1 or time2's dictionary
def addClass(stud, className, section, cList, sList):
	for i in range (section["start"], section["end"]):
		stud["schedule"][section["day"]][i] = className
	section["capacity"] = section["capacity"] - 1
	#add student to class list
	cListStudNum = "student" + str(20-section["capacity"])
	cListStud = {cListStudNum: {"id": stud["id"], "name": stud["name"]}}
	cList["classes"][className][convertSectoStr(section)].update(cListStud)
	#add class to student's classes taken
	if sList["students"]["student" + stud["id"]]["classesTaken"]:
		sList["students"]["student" + stud["id"]]["classesTaken"] += "," 
	sList["students"]["student" + stud["id"]]["classesTaken"] += className + "-" + convertSectoStr(section)
	stud["numOfClasses"] += 1
	stud["subjects"].append(className)

def checkAvailable(student, section, subject):
	time = student["schedule"][section["day"]]
	for i in range (section["start"], section["end"]):
		if (time[i] != "Free"):
			return 0
	if student["numOfClasses"] >= 5:
		return 0
	if subject in student["subjects"]:
		return 0
	return 1

#updating studentAvail
for i in range(1, len(data)+1):
	studentAvail.append(parseStudentAvailability(i))

#updating classes
for j in range(0, len(data1['classes'])):
	classes.append(parseClasses(j+101))

#updating classList
for c in classes: 
	tempClass = {c["subject"]: {}}
	for i in range(0, 2):
		sec = convertSectoStr(c["times"][i])
		tempClass[c["subject"]].update({sec: {}})
	classList["classes"].update(tempClass)

#updating studList
for student in studentAvail:
	s = "student" + student["id"]
	tempStud = {s: {}}
	tempStud[s].update({"id": student["id"], "name": student["name"], "classesTaken": ""})
	studList["students"].update(tempStud)

def fillClasses():
	classNum = []
	for course in range(10):
		subject = classes[course]["times"]
		for s in range(len(subject)):
			sectionParticipants = []
			for index in range(80):
				if checkAvailable(studentAvail[index], subject[s], classes[course]["subject"]) == 1:
					sectionParticipants.append(studentAvail[index]["id"])
			classNum.append([len(sectionParticipants), (course + 101)*10 + s])

	numClasses = []
	for stdnum in range(80):
		studSched = studentAvail[stdnum]
		studClass = []
		for day in studSched["schedule"]:
			for course in range(len(classes)):
				for section in range(len(classes[course])):
					if classes[course]["times"][section]["day"] == day:
						if checkAvailable(studentAvail[stdnum], classes[course]["times"][section], classes[course]["subject"]) == 1:
							studClass.append(classes[course]["times"][section]["day"] + classes[course]["subject"])
		numClasses.append([len(studClass), studentAvail[stdnum]["id"]])

	sortedClass = sorted(classNum)
	sortedStud = sorted(numClasses)

	for c in range(len(sortedClass)):
		for s in range(len(sortedStud)):
			crse = int(str(sortedClass[c][1])[:3])
			sctn = int(str(sortedClass[c][1])[3:])
			a = studentAvail[int(sortedStud[s][1])-1]
			b = classes[crse-101]["times"][sctn]
			if checkAvailable(a,b, classes[crse-101]["subject"]) == 1:
			 	if classes[crse-101]["times"][sctn]["capacity"] > 0:
			 		addClass(a, classes[crse-101]["subject"], classes[crse-101]["times"][sctn], classList, studList)

for index in range(400):
	fillClasses()
t1 = time.time()
output = classList.copy()
output.update(studList)
with open('myAnswer.json', 'w') as outfile:
    json.dump(output, outfile)
# pprint(studentAvail)
# pprint(classes)

print(t1-t0)