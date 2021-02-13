class Card:
    card_list = []

    def __init__(self, name, surname, company, occupation, phone, b_phone, e_mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.e_mail = e_mail
        self.card_list.append(self)
        self.label_lenght = (len(self.name) + len(self.surname) + 1)

    def create_contacts(type, quantity):
        random_Basecard = []
        random_Businesscard = []   
        from faker import Faker
        fake = Faker('pl_PL')

        if type == "Base":
            for card in range(quantity):
                random_Basecard.append(Card(name=fake.first_name(), surname=fake.last_name, company=fake.company(), occupation=fake.job(), phone=fake.phone_number(), b_phone=fake.phone(), e_mail=fake.email()))
                return random_Basecard
        elif type == "Business":
            for card in range(quantity):
                random_Businesscard.append(Card(name=fake.name(), company=fake.company(), occupation=fake.job(), phone=fake.phone_number(), e_mail=fake.email()))
                return random_Businesscard
        else:
            print("Invalid type")

    create_contacts("Base", 10)


class Basecontact(Card):
    basecontact_list = []

    def __init__(self, name, surname, phone, e_mail):
        super().__init__(name, surname, phone, e_mail)

    def __str__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.phone} i dzwonię do {self.surname}, {self.surname}'

    @property
    def label_lenght(self):
        return self.label_lenght

    ##for basecard in Basecontact.basecontact_list:
    ##  print (basecard.name, basecard.surname, buasecard.label_lenght)


class Businesscontact(Card, Basecontact):
    businesscontact_list = []

    def __init__(self, name, surname, company, occupation, b_phone):
        super().__init__(name, surname, company, occupation, b_phone)

    def __str__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def __repr__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

    def contact(self):
        return f' Wybieram numer +48 {self.b_phone} i dzwonię do {self.surname}, {self.surname}'

    @property
    def label_lenght(self):
        return self.label_lenght

    ##for businesscard in Businesscontact.businesscontact_list:
    ##  print (businesscard.name, businesscard.surname, businesscard.label_lenght)
