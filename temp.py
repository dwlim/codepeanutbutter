import json
from pprint import pprint

with open('studentsByAvailability.json') as data_file:    
	    data = json.load(data_file)

with open('classes.json') as data_file1:    
	    data1 = json.load(data_file1)

studentAvail = []
classes = {}

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
def addClass(stud, className, section):
	for i in range (section["start"], section["end"]):
		stud.values()[0][section["day"]][i] = className
	section["capacity"] = section["capacity"] - 1

def checkAvailable(time, section):
	for i in range (section["start"], section["end"]):
		if (time[i] != "Free"):
			return 0
	return 1


for i in range(1, len(data)+1):
	studentAvail.append(parseStudentAvailability(i))

for j in range(0, len(data1['classes'])):
	classes.update(parseClasses(j+101))


#addClass(studentAvail[0], "Mathematics", classes["Mathematics"]["times"][0])
#addClass(studentAvail[0], "Mathematics", classes["Mathematics"]["times"][1])

print studentAvail[0]
#print studentAvail[0]
