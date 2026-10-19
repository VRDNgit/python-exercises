import re
class Assignment:
    
    total_assignment = 0

    def __init__(self, title, subject, is_completed = False):
        self.title = title
        self.subject = subject
        self.is_completed = is_completed
        Assignment.total_assignment += 1

    def complete(self):
        if self.is_completed:
            return "Already completed"
        else:
            self.is_completed = True
            return "Assignment completed"

    @staticmethod
    def is_valid_title(title):
        if re.match(r"^\s*$", title):
            return False
        else:
            return True

    @classmethod
    def get_total_assignments(cls):
        return cls.total_assignment