########  Implementation of Inheritance  ######## 
 
#### Creating the class student  #### 
class student: 
    def get_student_data(self): 
        self.rollno=int(input("enter rollno")) 
        self.name=input("enter name") 
        self.clsname=input("enter class studying")  
 
    def display_student_data(self): 
        print("RollNo       : ",self.rollno) 
        print("StudentName  : ",self.name) 
        print("Class        : ",self.clsname)  
 
 
 
#### Creating a class mark1 by inheriting the class student #### 
 
class marks(student): 
     def get_marks_data(self): 
         self.get_student_data() 
         self.mark1=int(input("enter mark1"))  
         self.mark2=int(input("enter mark2"))  
         if self.mark1>49 and self.mark2>49: 
              self.result="pass" 
         else: 
              self.result="fail"  
     def display_marks_data(self): 
        self.display_student_data() 
        print("Mark1      : ",self.mark1) 
        print("Mark2      : ",self.mark2) 
        print("Result     : ",self.result)  
 
###### Creating an object of class student ##### 
 
s1=student() 
print("Enter the information of the object s1") 
s1.get_student_data() 
s1.display_student_data() 
 
##### Creating objects of class marks #### 
 
s2=marks() 
print("Enter the information of the object s2") 
s2.get_marks_data() 
s2.display_marks_data() 
 
s3=marks() 
print("Enter the information of the object s3") 
s3.get_marks_data() 
s3.display_marks_data() 
