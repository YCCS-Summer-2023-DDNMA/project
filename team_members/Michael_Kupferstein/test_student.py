from student import Student

class TestStudent:
    def test_add_course(self):
        koop = set_up()
        assert koop.courses == set(['Math','English','Computer Science','Spanish'])
        assert koop.grades == {'Math':'NA','English':'NA','Computer Science':'NA','Spanish':'NA'}
    def test_drop_course(self):
        koop = set_up()
        koop.drop_course('Math')
        assert koop.courses == set(['English','Computer Science','Spanish'])
        assert koop.grades == {'English':'NA','Computer Science':'NA','Spanish':'NA'}
        koop.drop_course('English')
        assert koop.courses == set(['Computer Science','Spanish'])
        assert koop.grades == {'Computer Science':'NA','Spanish':'NA'}
    def test_add_grade_on_existing(self):
        koop = set_up()
        add_grades(koop)
        assert koop.grades == {'Math':80,'English':90,'Computer Science':83,'Spanish':60}
        assert koop.courses == koop.grades.keys()
    def test_add_grade_on_new(self):
        koop = Student('Michael Kupferstein')
        add_grades(koop)
        assert koop.grades == {'Math':80,'English':90,'Computer Science':83,'Spanish':60}
        assert koop.courses == koop.grades.keys()




def add_courses(student):
    student.add_course('Math')
    student.add_course('English')
    student.add_course('Computer Science')
    student.add_course('Spanish')

def add_grades(student):
    student.add_grade('Math',80)
    student.add_grade('English',90)
    student.add_grade('Computer Science',83)
    student.add_grade('Spanish',60)

def set_up():
    koop = Student('Michael Kupferstein')
    assert koop.courses == set()
    add_courses(koop)
    return koop
