import random
import csv
import pyinputplus as pyip


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
        writer = csv.writer(file)
        #writer.writerow(['姓名',''])
        writer. writerows(data)

if __name__ == '__main__':
    students:list[list] = getStudents()
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    o_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = getStudents(student_nums=s_nums,scores_nums=o_nums)
    fileName=pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名)")
    saveToCSV(fileName=fileName,data=students,subject_num=o_nums)
    print(students)