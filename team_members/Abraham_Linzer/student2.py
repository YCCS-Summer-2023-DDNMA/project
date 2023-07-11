class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def new_course(self, course):
        self.courses.append(course)
    def remove_course(self,course):
        self.courses.remove(course)
        
    def course_list(self):
        return self.courses
        
