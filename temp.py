import json
from pprint import pprint

with open('studentsByAvailability.json') as data_file:    
	    data = json.load(data_file)

dict = {}

def parseTimetoPos(time):
		if time == "NA":
			return -1
		pos = 0
		tod = time[-2:]
		hour = int(time[:2])
		if (tod == "pm" and hour != 12):
			hour += 12
		minute = int(time[3:5])/30
		pos = 2*(hour-8) + minute + 1
		return pos

def parseStudentAvailability(num):
	number = str(num)
	name = data[number][0]
	dict = {name : {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : []}}
	dict[name]["Monday"] = ["Busy"] * 27
	dict[name]["Tuesday"] = ["Busy"] * 27
	dict[name]["Wednesday"] = ["Busy"] * 27
	dict[name]["Thursday"] = ["Busy"] * 27
	dict[name]["Friday"] = ["Busy"] * 27

	for index in data[number][1].keys():
		day = data[number][1][index]["day"]
		start = parseTimetoPos(data[number][1][index]["start"])
		end = parseTimetoPos(data[number][1][index]["end"])
		print(day)
		for j in range(end - start):
			dict[name][day][start + j - 1] = "Free"
	return dict

dict = parseStudentAvailability(3)
print(dict[data["3"][0]]["Friday"])