import re
w = open('student.txt') # open students' roster file
count = 0
total = []
score = []
for x in w:
	name = ('').join(re.findall('([A-Z].+[a-z]) ', x))
	cla = ('').join(re.findall(' ([A-Z].+[0-9]) ', x))
	grade = ('').join(re.findall(' ([0-9].+)', x))
	count = count +1
	student = [name, cla, grade]
	total.append(student) #create a roster in py

for d in range(0, 2):
        for w in total:
                score.append(int(w[2]))
        s = max(score)# find max score

        for t in total:
                if t[2] == str(s):
                        print ((' ').join(t))
                        total.remove(t)
                        score.remove(s)

