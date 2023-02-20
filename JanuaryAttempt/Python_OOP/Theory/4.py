class Student:
    def __init__(self, sid, sname, cname, score):
        self.studentid=sid
        self.studentName=sname
        self.courseEnrolled=cname
        self.studentScore=score

class Department:
    def __init__(self, dname, slist):
        self.departmentName=dname
        self.studentList=slist
    
    def findCourseWiseStudents(self):
        result={}
        cList=[]
        for student in self.studentList:
            cList.append(student.courseEnrolled)
        courseList=list(set(cList))
        for course in courseList:
            result[course]=cList.count(course)
        return result
    
    def findStudentGrade(self, sid):
        grade=None
        for student in self.studentList:
            if student.studentId == sid:
                if student.studentScore >= 80:
                    grade='A'
                elif student.studentScore >= 55:
                    grade='C'
                else:
                    grade='F'
        return grade

if __name__=='_-main__':
    count=int(input())
    sList=[]
    for i in range(count):
        sid=int(input())
        sname=input()
        course=input()
        score=float(input())
        sList.append(Student(sid, sname, course, score))
    d=Department("Humanities", sList)
    inputId=int(input())
    outDict=d.findCourseWiseStudents()
    for course in sorted(outDict.keys()):
        print(course, outDict[course])
    outGrade=d.findStudentGrade(inputId)
    if outGrade is None:
        print("No student found")
    else:
        print(outGrade)