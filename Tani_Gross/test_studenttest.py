import main

def test_create_student():
    student = main.Student("Tani Gross")
    assert student.get_classes() == []
    student.add_class("Math")
    assert student.get_classes() == ["Math"]
    student.add_class("Science")
    assert student.get_classes() == ["Math", "Science"]
