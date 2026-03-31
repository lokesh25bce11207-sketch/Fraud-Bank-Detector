import pandas as pd
Students={'Admission number':['Roll no','Name','DOB','Gender','Class','Section','Contact','Address',"Father's name","Mother's name"]}
Teachers={'Employee ID':['Name','DOB','Gender','Contact','Address','Subject','Qualification','DOJ','Designation']}
 
def Add(field):
    no=int(input(f"How many {field} do you want to add"))
    while no>0:
        if field=='Students':
            try:
                ano=int(input("Enter admission number"))
                if ano not in Students:
                    sroll=int(input("Enter student's roll number"))
                    sname=input("Enter student's name")
                    sdob=input("Enter DOB")
                    sgen=input("Enter gender")
                    scla=int(input("Enter class"))
                    ssec=input("Enter the section")
                    scon=int(input("Enter contact"))
                    sadd=input("Enter address")
                    sfat=input("Enter father's name")
                    smot=input("Enter mother's name")
                    details=[sroll,sname,sdob,sgen,scla,ssec,scon,sadd,sfat,smot]
                    Students.setdefault(ano,details)
                    print("Student data added sucessfully")
                else:
                    print("Admission number already exist")
            except ValueError:
                print("Invalid input")
        else:
            try:
                empid=int(input("Enter employee id"))
                if empid not in Teachers:
                    tname=input("Enter teacher's name")
                    tdob=input("Enter DOB (dd/mm/yyyy)")
                    tgen=input("Enter gender")
                    tpho=int(input("Enter teacher's contact"))
                    tadd=input("Enter teacher's address")
                    tsubj=input("Enter teacher's specific subject")
                    tqua=input("Enter teacher's qualification")
                    tdoj=input("Enter date of joining (dd/mm/yyyy)")
                    tdes=input("Enter the teacher's designation")
                    details=[tname,tdob,tgen,tpho,tadd,tsubj,tqua,tdoj,tdes]
                    Teachers.setdefault(empid,details)
                    print("Teacher's added sucessfully")
                else:
                    print("Employee ID already exist")
            except ValueError:
                print("Invalid input")
        no-=1

def Displayall(field):
    df_vertical=pd.DataFrame(field)
    df_horizontal=df_vertical.T
    df_horizontal.columns=df_horizontal.iloc[0]
    df_final=df_horizontal[1:]
    print(df_final.to_markdown(tablefmt="grid", stralign="center"))

def Search(tempfield,field,index=None,search=None):
    found=False
    if search==None:
        for i in field:
            if i==index:
                tempfield.setdefault(i,field[i])
                found=True
    else:
        for i in field:
            if str(field[i][index]).lower()==search.lower():
                tempfield.setdefault(i,field[i])
                found=True
    if found:
        Displayall(tempfield)
    else:
        print("No records found")
            
def Select(field):
    while True:
        if field=='Students':
            tempfield={'Admission number':['Roll no','Name','DOB','Gender','Class','Section','Contact','Address',"Father's name","Mother's name"]}
            try:
                ch0=int(input("What do you want:-\n1)Select student's by a category\n2)Select a specific student\n3)Quit"))
                if ch0==1:
                    ch1=int(input("Enter your choice:-\n1)Search by student's name\n2)Search by class\n3)Search by gender\n4)Search by address"))
                    if ch1==1:
                        name=input("Enter student's name")
                        Search(tempfield,Students,1,name)
                    elif ch1==2:
                        cla=int(input("Enter class"))
                        Search(tempfield,Students,4,str(cla))
                    elif ch1==3:
                        gen=input("Enter gender")
                        Search(tempfield,Students,3,gen)
                    elif ch1==4:
                        add=input("Enter address")
                        Search(tempfield,Students,7,add)
                    else:
                        print("Invalid Choice")
                elif ch0==2:
                    tempid=int(input("Enter admission number"))
                    Search(tempfield,Students,tempid)
                elif ch0==3:
                    print("Quitting...")
                    break
                else:
                    print("Invalid Choice\nTry again")
            except ValueError:
                print("Invalid input\nTry Again...")
        else:
            tempfield={'Employee ID':['Name','DOB','Gender','Contact','Address','Subject','Qualification','DOJ','Designation']}
            try:
                ch0=int(input("What do you want:-\n1)Select Teachers by a category\n2)Select a specific member\n3)Quit"))
                if ch0==1:
                    ch1=int(input("Enter your choice:-\n1)Search by Teacher's name\n2)Search by gender\n3)Search by address \n4)Search by subject\n5)Search by qualification\n6)Search by designation"))
                    if ch1==1:
                        tname=input("Enter Teacher's name")
                        Search(tempfield,Teachers,0,tname)
                    elif ch1==2:
                        tgen=input("Enter gender")
                        Search(tempfield,Teachers,2,tgen)
                    elif ch1==3:
                        tadd=input("Enter address")
                        Search(tempfield,Teachers,4,tadd)
                    elif ch1==4:
                        tsub=input("Enter subject")
                        Search(tempfield,Teachers,5,tsub)
                    elif ch1==5:
                        tqua=input("Enter qualification")
                        Search(tempfield,Teachers,6,tqua)
                    elif ch1==6:
                        tdes=input("Enter designation")
                        Search(tempfield,Teachers,8,tdes)
                    else:
                        print("Invalid Choice")
                elif ch0==2:
                    tempid=int(input("Enter employee id"))
                    Search(tempfield,Teachers,tempid)
                elif ch0==3:
                    print("Quitting...")
                    break
                else:
                    print("Invalid Choice\nTry again")
            except ValueError:
                print("Invalid input\nTry Again...")

def check(field,te_id):
    if te_id in field:
        return True
    else:
        print("No records found")
        return False
        
def Update(field,te_id,index,value):
    field[te_id][index]=value
    print("Updated successfully")


def Modify(field):
    while True:
        if field=='Students':
            try:
                ch2=int(input("What do you want to do\n1)Update roll no\n2)Update name\n3)Update DOB\n4)Update gender\n5)Update class\n6)Update section\n7)Update contact\n8)Update address\n9)Update Father's name\n10)Update Mother's name\n11)Quit"))
                if ch2==1:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newroll=int(input("Enter new roll no"))
                        Update(Students,tempid,0,newroll)
                elif ch2==2:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newname=input("Update name")
                        Update(Students,tempid,1,newname)
                elif ch2==3:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newdob=input("Update DOB (dd/mm/yyyy)")
                        Update(Students,tempid,2,newdob)
                elif ch2==4:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newgen=input("Update gender")
                        Update(Students,tempid,3,newgen)
                elif ch2==5:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newcla=int(input("Enter new class"))
                        Update(Students,tempid,4,newcla)
                elif ch2==6:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newsec=input("Enter new section")
                        Update(Students,tempid,5,newsec)
                elif ch2==7:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newcon=int(input("Enter new contact"))
                        Update(Students,tempid,6,newcon)
                elif ch2==8:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newadd=input("Enter new address")
                        Update(Students,tempid,7,newadd)
                elif ch2==9:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newfna=input("Update father's name")
                        Update(Students,tempid,8,newfna)
                elif ch2==10:
                    tempid=int(input("Enter admission number"))
                    if check(Students,tempid):
                        newmna=input("Update mother's name")
                        Update(Students,tempid,9,newmna)
                elif ch2==11:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Choice\nTry Again...")
            except ValueError:
                print("Invalid Input")
        else:
            try:
                ch2=int(input("What do you want to do\n1)Update name\n2)Update DOB\n3)Update gender\n4)Update Contact\n5)Update Address\n6)Update Subject\n7)Update Qualification\n8)Update DOJ\n9)Update Designation\n10)Quit"))
                if ch2==1:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newname=input("Update name")
                        Update(Teachers,tempid,0,newname)
                elif ch2==2:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newdob=input("Update DOB")
                        Update(Teachers,tempid,1,newdob)
                elif ch2==3:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newgen=input("Update gender")
                        Update(Teachers,tempid,2,newgen)
                elif ch2==4:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newcon=int(input("Enter new contact"))
                        Update(Teachers,tempid,3,newcon)
                elif ch2==5:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newadd=input("Enter new address")
                        Update(Teachers,tempid,4,newadd)
                elif ch2==6:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newsub=input("Update subject")
                        Update(Teachers,tempid,5,newsub)
                elif ch2==7:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newqua=input("Update qualification")
                        Update(Teachers,tempid,6,newqua)
                elif ch2==8:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newdoj=input("Update DOJ")
                        Update(Teachers,tempid,7,newdoj)
                elif ch2==9:
                    tempid=int(input("Enter employee id"))
                    if check(Teachers,tempid):
                        newdes=input("Update designation")
                        Update(Teachers,tempid,8,newdes)
                elif ch2==10:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Choice\nTry Again...")
            except ValueError:
                print("Invalid Input")


def Delete(field):
    if field=='Students':
        try:
            tempid=int(input("Enter admission number"))
            if tempid in Students:
                remove=Students.pop(tempid)
                print(tempid,':',remove,"has been removed")
            else:
                print("Records doesn't exist")
        except ValueError:
            print("Invalid input")
    else:
        try:
            tempid=int(input("Enter employee id"))
            if tempid in Teachers:
                remove=Teachers.pop(tempid)
                print(tempid,':',remove,"has been removed")
            else:
                print("Records doesn't exist")
        except ValueError:
            print("Invalid input")

print("Welcome to the Smart School Management System!")
print("You can tell me what to do in plain English.")
print("(e.g., 'I want to add a student', 'show all teachers', 'modify a student', or 'quit')")

while True:
    try:
        command = input("\nChatbot: What would you like to do?\n> ").lower()
        if "quit" in command or "exit" in command:
            print("Quitting the program. Goodbye!")
            break

        elif "add" in command or "insert" in command:
            if "student" in command:
                print("Accessing Student admission...")
                Add('Students')
            elif "teacher" in command:
                print("Accessing Teacher recruitment...")
                Add('Teachers')
            else:
                print("Did you want to add a 'student' or a 'teacher'? Please clarify.")

        elif "show" in command or "display" in command or "view" in command:
            if "student" in command:
                Displayall(Students)
            elif "teacher" in command:
                Displayall(Teachers)
            else:
                print("Did you want to display 'students' or 'teachers'?")

        elif "search" in command or "find" in command or "select" in command:
            if "student" in command:
                Select('Students')
            elif "teacher" in command:
                Select('Teachers')
            else:
                print("Did you want to search for a 'student' or a 'teacher'?")

        elif "modify" in command or "update" in command or "change" in command:
            if "student" in command:
                Modify('Students')
            elif "teacher" in command:
                Modify('Teachers')
            else:
                print("Did you want to modify a 'student' or a 'teacher'?")

        elif "delete" in command or "remove" in command:
            if "student" in command:
                Delete('Students')
            elif "teacher" in command:
                Delete('Teachers')
            else:
                print("Did you want to delete a 'student' or a 'teacher'?")

        else:
            print("I didn't quite catch that. Try saying something like 'add a student' or 'search for a teacher'.")
    except ValueError:
        print("Invalid Input")