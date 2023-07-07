# script takes in a text file with no spaces copied from the student directory at:
    # https://apps.its.fsu.edu/StudentDirectory/StudentDirectory.html#search:
    # note: if you use #result:"your text here" you can get around having to select a name from the drop down
# and outputs a sepearted list of each student

import os
from math import floor

# read each line in from directory text file
people_list =[]

people = open('ppl_email.txt', 'r')  # put your file name here
people_list = people.readlines()
people.close()

# seperates file by every major
save = open('majors.txt','w')

index = 0
length = len(people_list)

while index<length:
    if people_list[index]=='Major\n':
        save.write(people_list[index] + people_list[index+1] + '\n')
        index+=2
    else:
        save.write(people_list[index])
        index+=1

save.close()

groups = open('majors.txt', 'r')
groups_read = groups.readlines()
groups.close()

save = open('9len.txt','w')

# loop through till at the last line before a newline and if that number is not 9,
# then add the necessary number of lines ot make it 9

# adds newlines to the end of the second major of a double major to make each major a consistent 9 lines
line_count =1
index =0
x=0
while index < len(groups_read):
    if groups_read[index]!='\n':
        save.write(groups_read[index])
        line_count+=1
        index+=1
    else:
        if line_count!=10:
            while x<4:
                save.write('\n')
                x+=1
            index+=1
            line_count=1
            x=0
        else:
            save.write('\n')
            index+=1
            line_count=1

save.close()

groups = open('9len.txt', 'r')
groups_read = groups.readlines()
groups.close()

rows = floor(len(groups_read)/10)
cols =  9

l_of_l = []

# load groups into a list variable
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(groups_read[j+(10*i)])
    l_of_l.append(col)


# delete duplicate names          
rows = len(l_of_l)
i=0

while i<rows:
    j=i+1
    while j< rows:
        if l_of_l[i][0]==l_of_l[j][0] and l_of_l[i][0]!="Career\n":
            del l_of_l[j]
            rows-=1
        j+=1
    i+=1     

# list of students should not have any duplicates now
# go in and delete any career list 

rows = len(l_of_l)
i=1
# deletes any lone majors left over when deleting duplicates
while i<rows-1:
    if l_of_l[i][0]=="Career\n" and l_of_l[i+1][0]=="Career\n" and l_of_l[i-1][0]!="Career\n":
        del l_of_l[i+1]
        del l_of_l[i]
        rows-=2   
    else:
        i+=1     
            
# check the last index
if l_of_l[len(l_of_l)-1][0]=="Career\n":
    del l_of_l[len(l_of_l)-1]

# combine remaining deouble majors into one list with two majors minus the extra newlines for consistent spacing
rows = len(l_of_l)
i=1
while i<rows:
    if l_of_l[i][0]=="Career\n":
        for j in range(len(l_of_l[i])-3):
            l_of_l[i-1].append(l_of_l[i][j])
        del l_of_l[i]
        rows-=1
    else:
        i+=1

substring = "click to hear the name\n"

for i in range(len(l_of_l)):
    if substring in l_of_l[i][0]:
        l_of_l[i][0] = l_of_l[i][0].replace(substring, "\n")

# write it out to file
save = open('student_information.txt', 'w')

for i in range(len(l_of_l)):
    for j in range(len(l_of_l[i])):
        save.write(l_of_l[i][j])
    save.write('\n')

save.close()


save = open("names.txt", 'w')

for i in range(len(l_of_l)):
    save.write(l_of_l[i][0])

save.close()

save = open("emails.txt", 'w')

for i in range(len(l_of_l)):
    save.write(l_of_l[i][2])

save.close()

os.remove("majors.txt")
os.remove("9len.txt")


