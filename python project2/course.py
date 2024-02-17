class Course:
    def __init__(self, coursename):
        self.coursename = coursename
        self.student_list = []

    def display_all(self):
        for s in self.student_list:
            print(s)