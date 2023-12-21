def getStudents(student_nums:int=1,scores_nums:int=2) -> list[list]:
    '''
    參數: student_nums -> 學生人數\n
    參數: scores_nums -> 科目數\n
    '''


    with open("names.txt",mode="r",encoding="utf-8") as file:
        names:str = file.read()

    nameslist:list[str] = names.split("\n")
    students:list[list] = []


    names:list[str] = random.choices(nameslist,k=student_nums)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)

    return(students)
#students:list[list] = getStudents()
#print(students)

def saveToCSV(fileName:str,data:list[list],subject_num:int)-> None:
    fileName+=".csv"
    subjects=[f'科目{i+1}' for i in range(subject_num)]
    fields=['姓名'].extend(subjects)
    with open(fileName,mode='w',encoding='utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            fields=None
            writer. writerows(data)
            writer.writerows(fields)
        except:
            return False
        else:
            return True