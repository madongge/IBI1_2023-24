class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print('Name: {}, Major: {}, Code Portfolio Score: {}, Group Project Score: {}, Exam Score: {}'.format(
            self.name, self.major, self.code_portfolio_score, self.group_project_score, self.exam_score))

# Example
student1 = Student('Ma Dongge', 'BMI', 85, 90, 80)
student1.print_details()

