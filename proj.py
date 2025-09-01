class Student:
    def __init__(self,student_name,roll_no,parentage,dob):
        self.student_name=student_name
        self.roll_no=roll_no
        self.parentage=parentage
        self.dob=dob
    def __str__(self):
        return f"{self.student_name},{self.roll_no},{self.parentage},{self.dob}"

class Exam:
    def __init__(self,exam_name,sublist,submarks,max_marks):
        self.exam_name=exam_name
        self.sublist=sublist
        self.submarks=submarks
        self.max_marks=max_marks
        self.total_marks=0

    def __str__(self):
        return f"{self.exam_name},{self.sublist},{self.submarks},{self.max_marks}"

    def display_mark(self):
       display_marks = dict(zip(self.sublist, self.submarks))
       for sub, mark in display_marks.items():
           print(f"{sub}:{mark}")
           self.total_marks=self.total_marks+mark


class Student_Examination(Student,Exam):
    def __init__(self,student_name,roll_no,parentage,dob,exam_name, sublist, submarks, max_marks,total_marks):
      Student.__init__(self,student_name,roll_no,parentage,dob)
      Exam.__init__(self,exam_name,sublist,submarks,max_marks)
      self.max_marks=500
      self.percentage=0
      self.grade=""
      self.remarks=""


    def __str__(self):
        return f"{Student.__str__(self)},{Exam.__str__(self)},{self.total_marks},{self.percentage},{self.grade},{self.remarks}"
    def total_marks(self):
        return sum(self.submarks)

    def calculate_percentage(self):
        self.percentage=self.total_marks*100//self.max_marks

    def calculate_grade(self):
        if self.percentage>= 90:
            self.grade= "A"
        elif self.percentage>=80:
            self.grade="B"
        elif self.percentage>=70:
            self.grade="C"
        elif self.percentage>=60:
            self.grade= "D"
        else:
            self.grade="F"

    def set_remarks(self):
        if self.grade=="F":
          self.remarks="FAIL"
        else:
            self.remarks= "pass"

s1 = Student_Examination("ALAN STARK",14,"RAIN STARK","22/2/2007","HALF YEARLY EXAMINATION",["ENG","PHE","MATHS","HINDI","SCIENCE"],[76,89,58,70,78],431, sum([76,89,58,70,78]))
s2=  Student_Examination("ALex STARK",14,"RAIN STARK","22/2/2007","HALF YEARLY EXAMINATION",["ENG","PHE","MATHS","HINDI","SCIENCE"],[76,89,58,70,78],431, sum([76,89,58,70,78]))
s3= Student_Examination("Aman STARK",14,"RAIN STARK","22/2/2007","HALF YEARLY EXAMINATION",["ENG","PHE","MATHS","HINDI","SCIENCE"],[76,89,58,70,78],431, sum([76,89,58,70,78]))
for i in [s1,s2,s3]:
    print(i)
    i.display_mark() 
    i.calculate_percentage()
    i.calculate_grade()
    i.set_remarks()
    print(i.total_marks)
    print(i.percentage)
    print(i.grade)
    print(i.remarks)
