class Student:
    def __init__(self, name):
        self.name = name
        self.classes = []
    
    def add_class(self, class_name):
        self.classes.append(class_name)
    
    def get_classes(self):
        return self.classes