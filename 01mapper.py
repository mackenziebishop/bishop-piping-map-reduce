#Mackenzie Bishop
#Mapper for Student_Marks.txt

f = open("Student_Marks.txt","r")  # open file, read-only
o = open("out01.txt", "w") # open file, write
for line in f:  
    dataList = line.strip().split("\t") 
    if len(dataList) == 3:
        number_courses, time_study, marks = dataList  #assign names
        o.write("{0}\t{1}\n".format(number_courses, marks))
f.close()
o.close()