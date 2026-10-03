class candidate:
    def __init__(self,name,candidate_id,department):
        self.name = name
        self.id = candidate_id
        self.department = department


    def introduction(self): # Here introduction is the instance method because it works with distict object
        print(f"Hey,I am {self.name}. My id is {self.id} and i am from department of {self.department}.")  


    