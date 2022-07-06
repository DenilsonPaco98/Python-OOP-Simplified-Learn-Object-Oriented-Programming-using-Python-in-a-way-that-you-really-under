class Employee:
    def setNumberWorkinghour(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)


class Trainee(Employee):
    def setNumberWorkinghour(self):
        self.numberOfWorkingHours = 45


    def resetNumberOfWorking(self):
        super().setNumberWorkinghour()


employee = Employee()
employee.setNumberWorkinghour()
print("Number of working hours of employee:", end=' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberWorkinghour()
print("Number of working hours of trainee:", end=' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorking()
print("Number of working hours of trainee after reset:", end=' ')
trainee.displayNumberOfWorkingHours()
