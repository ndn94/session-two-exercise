class Udacian:
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def getName(self):
        print(self.name + " " + self.city + " " + self.enrollment + " " + self.nanodegree + " " + self.status)

test = Udacian("Mohammed Bokhari", "Jeddah", "Student", "Full-Stack", "--")
test.getName()
