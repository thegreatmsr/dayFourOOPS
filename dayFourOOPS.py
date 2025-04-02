#Class is a blueprint for creating objects.
#Creating Class

class Student:
    collegeName= "ABC College"
    name="anonymous"  #Class attr
    
    def __init__(self, name, marks):
        self.name=name #obj attr (Obj attr> CLass attr)
        self.marks=marks
        print("Adding new student")

#Creating object(instance)
s1 =Student("Karan", 98)
print(s1.name, s1.marks)

s2 =Student("Mohit Raj Kishore", 90)
print(s2.name, s2.marks, s2.collegeName)


#All Classes have a function called _init_() which is always executed when the object is being initiated
#The Data inside the class or the object is also known as the attributes
class StudentMarks:
    def __init__(self, fullname, score):
        self.name=fullname
        self.marks=score
    def getAvg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your Avg Score is", sum/3)
s1= StudentMarks("Mohit", [99,98,97])
print(s1.getAvg)
s1.name="Mohit Rajput"
s1.getAvg()
        
        
        



