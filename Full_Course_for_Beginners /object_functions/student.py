class Student:

    # new data type
    def __init__(self, given_name, surname, major, gpa, is_on_probation):
        self.given_name = given_name
        self.surname = surname
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # honor roll
    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False
