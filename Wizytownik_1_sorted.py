class Card:
    card_list = []

    def __init__(self, name, surname, company, occupation, e_mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.e_mail = e_mail
        self.card_list.append(self)

    def __str__(self):
        return f' {self.name} {self.surname} {self.e_mail}' 
      
    def __repr__(self):
        return f' {self.name} {self.surname} {self.e_mail}'

card1 = Card(name = "Ludmita", surname = "Czerwińska", company = "Endicott Shoes", occupation = "Personal appearance worker", e_mail = "LudmitaCzerwinska@dayrep.com" )
card2 = Card(name = "Jadwiga", surname = "Zając", company = "Alpha Beta", occupation = "Process metallurgical engineer", e_mail =  "JadwigaZajac@armspy.com")
card3 = Card(name = "Wisław", surname = "Piotrowski", company = "LoRay", occupation = "Internal auditor", e_mail = "WislawPiotrowski@dayrep.com")
card4 = Card(name = "Jarogniew", surname = "Wieczorek", company = "Sound Warehouse", occupation = "Taper", e_mail = "JarogniewWieczorek@armyspy.com")
card5 = Card(name = "Bogumiła", surname = "Sawicka", company = "Blockbuster Music", occupation = "health inspector", e_mail = "BogumilaSawicka@armyspy.com")
cards = [card1, card2, card3, card4, card5]
print(cards)

by_name = sorted(cards, key=lambda card: card.name)
print(by_name)

by_surname = sorted(cards, key=lambda card: card.surname)
print(by_surname)

by_mail = sorted(cards, key=lambda card: card.e_mail)
print(by_mail)

##for card in Card.card_list:
  ##  print(card.name, card.surname, "," ,card.e_mail)

