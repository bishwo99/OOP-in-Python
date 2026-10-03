class candidate:
    def __init__(self,name,candidate_id,department):
        self.name = name
        self.id = candidate_id
        self.department = department
        
    def intro(self):
        print(f'Hey, i am {self.name}. My id is {self.id} and i am from {self.department} department.')


candidate1 = candidate('Bishwojit',101,'CSE')
candidate2 = candidate('Raihan', 102, "EEE")
candidate3 = candidate('Saimon', 103, 'CSE')

candidate1.intro()
candidate2.intro()
candidate3.intro()


# - `class Candidate` দিয়ে একটি blueprint তৈরি করা এবং সেই class থেকে multiple objects তৈরি করা।
# - `__init__()` ব্যবহার করে প্রতিটি object-এর `name`, `id`, এবং `department` initialize করা।
# - `self` ব্যবহার করে প্রতিটি object-এর নিজস্ব attributes access করা।
# - `intro()` method তৈরি করে প্রতিটি object-এর data ব্যবহার করে আলাদা output দেখানো।