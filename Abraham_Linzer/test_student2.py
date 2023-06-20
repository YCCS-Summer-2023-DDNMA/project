import student2
import unittest

class StudentTests(unittest.TestCase):
    def simple_test(self):
        student = student2.Student("Avi", ["Algs", "Comp Org"])
        assert student.course_list == ["Algs", "Comp Org"]
        student.remove_course("Algs")
        student.new_course("Math")
        assert student.course_list == ["Comp Org", "Math"]
        
        
