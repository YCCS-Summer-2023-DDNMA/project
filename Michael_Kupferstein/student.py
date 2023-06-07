
class Student:
    '''class that represents a student and classes'''
    def __init__(self,name):
        self.name = name
        self.courses = set()
        self.grades = {}

    def add_course(self,course):
        self.courses.add(course)
        self.grades[course] = 'NA'

    def drop_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            del self.grades[course]

    def add_grade(self,course,grade):
        if course not in self.courses:
            self.courses.add(course)
        self.grades[course] = grade

    def get_info(self):
        results = "{:<20}{:>5}\n".format('Course', 'Grade')
        for course, grade in sorted(self.grades.items()):
            results += "{:<20}{:>5}\n".format(course, grade)
        return results


    
