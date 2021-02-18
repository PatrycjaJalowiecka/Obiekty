from faker import Faker
fake = Faker('pl_PL')

fake.first_name()
fake.last_name()
fake.address()
fake.company()
fake.job()
fake.phone_number()
fake.email()

class Card:
    card_list = []

    def __init__(self, name, surname, address, company, occupation, phone_number, e_mail):
        self.name = name
        self.surname = surname
        self.address = address
        self.company = company
        self.occupation = occupation
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.card_list.append(self)


class Basecontact(Card):
    basecontact_list = []

    def __init__(self, name, surname, address, phone_number, e_mail):
        super().__init__(name, surname, address, phone_number, e_mail)
        self.label_val = (len(self.name) + len(self.surname) + 1)
        self.basecontact_list.append(self)

    def __str__(self):    
        return f' {self.name} {self.surname} {self.phone_number} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.phone_number} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.phone_number} i dzwonię do {self.surname}, {self.surname}'

    @property
    def label_lenght(self):
        return self.label_val
 
class Businesscontact(Card):
    businesscontact_list = []

    def __init__(self, name, surname, address, company, occupation, phone_number, e_mail):
        super().__init__(name, surname, address, company, occupation, phone_number, e_mail)
        self.label_val = (len(self.name) + len(self.surname) + 1)
        self.businesscontact_list.append(self)

    def __str__(self):
        return f' {self.name} {self.surname} {self.company} {self.phone_number} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.company} {self.phone_number} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.phone_number} i dzwonię do {self.surname}, {self.surname}, {self.company}'

    @property
    def label_lenght(self):
        return self.label_val

def create_contacts(type, quantity):
    random_card = []
    if type == "Base":
        for _ in range(quantity):
            random_card.append(Basecontact(name=fake.first_name(), surname=fake.last_name, address=fake.address(), phone_number=fake.phone_number(), e_mail=fake.email()))
    elif type == "Business":
        for _ in range(quantity):
            random_card.append(Businesscontact(name=fake.first_name(), surname=fake.last_name, address=fake.address(), phone_number = fake.phone_number(), company=fake.company(), occupation=fake.job(), e_mail=fake.email()))
    else:
        print("Invalid blr type")
    return random_card

create_contacts("Business",10)
