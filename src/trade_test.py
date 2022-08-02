
class EdgeCheckResult:

    def __init__(self):
        self.total = 0
        self.correct = 0
        self.wrong = 0

    def add_correct(self):
        self.total += 1
        self.correct += 1

    def add_wrong(self):
        self.total += 1
        self.wrong += 1

    def print_result(self):
        print("Total: {}".format(self.total))
        print("Correct: {}".format(self.correct))
        print("Wrong: {}".format(self.wrong))
        correct_percentage = (self.correct / self.total) * 100
        correct_percentage = round(correct_percentage, 2)
        print("Correct percentage: {}%".format(correct_percentage))
