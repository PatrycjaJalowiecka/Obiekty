from faker import Faker
fake = Faker('pl_PL')

fake.first_name()
fake.last_name()
fake.company()
fake.job()
fake.phone_number()
fake.email()

class Card:
    card_list = []

    def __init__(self, name, surname, company, occupation, phone, b_phone, e_mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.phone = phone
        self.b_phone = b_phone
        self.e_mail = e_mail
        self.card_list.append(self)


##print("")

class Basecontact(Card):
    basecontact_list = []

    def __init__(self, name, surname, phone, e_mail, b_phone, e_mail):
        super().__init__(self, name, surname, phone, e_mail, b_phone, e_mail)
        self.label_val = (len(self.name) + len(self.surname) + 1)
        self.basecontact_list.append(self)

    def __str__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.phone} i dzwonię do {self.surname}, {self.surname}'

    @property
    def label_lenght(self):
        return self.label_val

    ##for basecard in Basecontact.basecontact_list:
    ##  print (basecard.name, basecard.surname, buasecard.label_lenght)

##create_contacts("Base",10)
##print(basecontact_list)

class Businesscontact(Card):
    businesscontact_list = []

    def __init__(self, name, surname, company, occupation, b_phone, e_mail):
        super().__init__(self, name, surname, company, occupation, b_phone, e_mail)
        self.label_val = (len(self.name) + len(self.surname) + 1)
        self.businesscontact_list.append(self)

    def __str__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.b_phone} i dzwonię do {self.surname}, {self.surname}'

    @property
    def label_lenght(self):
        return self.label_val

    ##for businesscard in Businesscontact.businesscontact_list:
    ##  print (businesscard.name, businesscard.surname, businesscard.label_lenght)

def create_contacts(type, quantity):
    random_card = []
        
    if type == "Base":
        for _ in range(quantity):
            random_card.append(Basecontact(name=fake.first_name(), surname=fake.last_name, phone=fake.phone_number(), e_mail=fake.email()))
    elif type == "Business":
        for _ in range(quantity):
            random_card.append(Businesscontact(name=fake.first_name(), surname=fake.last_name, company=fake.company(), occupation=fake.job(), b_phone=fake.phone_number(), e_mail=fake.email()))
    else:
        print("Invalid type")
    return random_card

create_contacts("Base", 10)