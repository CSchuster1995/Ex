class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = [] 

        self.greeting_count = 0
        self.unique_greet = []
        
    def greet(self, other_person):
        print('Hello {}, I am {}!' .format(other_person.name, self.name))
        if other_person.name is not self.unique_greet:
            self.unique_greet.append(other_person.name)

        self.greeting_count = len(self.unique_greet)

    def print_contact_info(self):
        print(self.name, '\n', self.email, '\n', self.phone)
Sonny = Person('Sonny', 'sonny@hotmail.com', '483-458-4948')        
Jordan = Person('Jordan', "Jordan@aol.com", '495-586-3456')        
Jordan.greet(Sonny)
Sonny.greet(Jordan)
Sonny.print_contact_info()
Sonny.friends.append(Jordan)
print("\t",Sonny.friends[0].name)
Jordan.print_contact_info()
Jordan.friends.append(Sonny)
print('\t',Jordan.friends[0].name)
print(Jordan.greeting_count)


