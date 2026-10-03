class Candidate:
    university = 'Faridpur Engineering College.'

    def __init__(self,name,candidate_id,department):
        self.name = name
        self.id = candidate_id
        self.dept = department
   
    def intro(self):
        print(f"Hey there, I am {self.name}, my id is {self.id} and i am from {self.dept}")

    @classmethod
    def campus(cls): # This is class method because the method can be used in everywhere.
        print(f"My university is {cls.university}")

candidate1 = Candidate('Bishwojit',101,'CSE')
candidate2 = Candidate('Saimon',102,'CSE')

candidate1.intro()
candidate1.campus()

