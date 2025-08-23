class Student(object):
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 0:
            return 'B'
        else:
            return 'C'
        
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    

    list(range(100))[5:10]




