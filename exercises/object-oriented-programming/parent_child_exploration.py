class Job():

    def __init__(self, name, employment_type):
        self.name = name
        self.employment_type = employment_type

    def job_info(self):
        return self.name + " works as " + self.employment_type 


class HumanResources(Job):

    def __init__(self, name, employment_type, hiring_status):
        super().__init__(name, employment_type)
        self.hiring_status = hiring_status

    def hiring_process(self):
        return self.name + " hiring status: " + self.hiring_status


class Recruiter(Job):

    def __init__(self, name, employment_type, candidates):
        super().__init__(name, employment_type)
        self.candidates = candidates

    def interview(self):
        return self.name + " needs to interview " + str(self.candidates) + " candidates"


jim = HumanResources("Jim", "Full-Time", "Hiring")

lucy = Recruiter("Lucy", "Part-Time", 5)

print(jim.job_info())
print(jim.hiring_process())

print(lucy.job_info())
print(lucy.interview())