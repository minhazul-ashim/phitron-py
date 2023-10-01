class Teacher :
    def __init__(self, name, age, subject) :
        self.name = name;
        self.age = age; 
        self.subject = subject;
    def __repr__ (self) -> str:
        return f'Name is {self.name}, Age is {self.age} and teaches {self.subject}'
    
class Student :
    def __init__(self, name, cls, section) :
        self.name = name;
        self.cls = cls;
        self.section = section;
    def __repr__(self) -> str:
        return f'Student name is {self.name}, admitted into class {self.cls} and section {self.section}';

class School :
    name = "";
    teachers = [];
    students = [];
    def __init__(self, name) :
        School.name = name;

    def hireTeacher(self, name, age, sub) :
        newTeacher = Teacher(name, age, sub);
        School.teachers.append(newTeacher);
        print(f'Congratulations, {name} is hired to teach {sub}');
    
    def enrolStudent(self, name, cls, section) :
        newStudent = Student(name, cls, section);
        School.students.append(newStudent);
        print(f'Congratulations, {name} is enrolled in class {cls} and section {section}');
    
    def __repr__(self) -> str :
        return f'School name is {self.name}, with total {len(School.teachers)} teachers and total {len(School.students)} students.' #We can directly access class attributes;

school = School('Comilla Modern High School');
school.hireTeacher('Sohel', 45, 'English');
school.hireTeacher('Selim', 40, 'Mathematics');
school.hireTeacher('Masuk', 35, 'Arts');
school.enrolStudent('Ashim', 6, 'A');
school.enrolStudent('Kona', 6, 'A');
school.enrolStudent('Shahrina', 7, 'A');
school.enrolStudent('Hayat', 8, 'A');
school.enrolStudent('Naziba', 9, 'A');

while True :
    print(f'Welcome to {school.name}');
    print('Enter your choice');
    print('1 : View School Prospect');
    print('2 : Hire a Teacher');
    print('3 : Enrol a Student');
    print('0 : Exit');
    c = int(input());
    if c == 1 :
        print(school);
    elif c == 2 :
        print('Enter teacher name');
        x = input();
        print('Enter teacher age');
        y = int(input());
        print('What will he teach?');
        z = input();
        school.hireTeacher(x, y, z);
    elif c == 3 :
        print('Enter student name');
        x = input();
        print('Enter enrolment class');
        y = int(input());
        print('Enter enrolment section');
        z = input();
        school.enrolStudent(x, y, z);
    elif c == 0 :
        break;
    else :
        print('Sorry invalid choice. Check and try again.');