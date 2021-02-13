class Card:
    card_list = []

    def __init__(self, name, surname, company, occupation, e_mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.e_mail = e_mail
        self.card_list.append(self)

from faker import Faker
fake = Faker('pl_PL')

fake.name()
fake.company()
fake.address()
fake.phone_number()
fake.job()
 
for _ in range(20):
  print(fake.name(), ",", fake.company(), ",", fake.job(),  ",", fake.address(), "," , fake.phone_number())