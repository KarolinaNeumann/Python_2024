# jízdenky a letenky 
# Nyní je naším cílem práce pro společnost, která se zabývá prodejem jízdenek a letenek.

# Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sedadla). 
# Tato třída bude sloužit například pro cesty autobusem.

class Ticket:
    def __init__(self, 
                 base_price, 
                 seat_number):
        self.base_price = base_price
        self.seat_number = seat_number

# Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu. 
# Vytvoř třídu TrainTicket, která bude mít navíc atribut fare_class 
# (uvažujeme možnosti economy a business). Dále naprogramuj metodu get_price(), 
# která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, 
# a cenu o 30 % vyšší oproti basic_price, pokud fare_class je business.

class TrainTicket(Ticket):
    def __init__(self, 
                 base_price,
                 seat_number,
                 fare_class):
        super().__init__(base_price, 
                         seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == "economy":
            return self.base_price
        else:
            return 1.3 * self.base_price 

# U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. 
# Vytvoř třídu PlaneTicket, 
# která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, 
# který udává počet odbavených zavazadel. Naprogramuj metodu get_price(),
#  která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy,
#  a cenu o 50 % vyšší oproti basic_price, pokud fare_class je business. 
# Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

# Vytvoř jízdenku na vlak se základní cenou 150 do tříd economy i business. 
# Zkontroluj, jakou hodnotu vrací metoda get_price().
# Vytvoř letenku se základní cenou 6000 do tříd economy i business s jedním odbaveným zavazadlem. 
# Zkontroluj, jakou hodnotu vrací metoda get_price().
# Vyzkoušej vypočítat celkovou cenu dvou jízdenek různého typu, 
# tj. jedné letenky a jedné jízdenky na vlak. Celkovou cenu ulož do proměnné total_price a 
# k výpočtu použij metodu get_price().

    def get_price(self):
        price = super().get_price()
        if self.fare_class == 'business':
            price = self.basic_price * 1.5  # Cena o 50 % vyšší pro business class
        return price + (2000 * self.checkout_luggages)  # Připočet 2000 za každé zavazadlo

# Vytvoření jízdenek na vlak
train_ticket_economy = TrainTicket(150, "12A", "economy")
train_ticket_business = TrainTicket(150, "1B", "business")

# Vytvoření letenek
plane_ticket_economy = PlaneTicket(6000, "20A", "economy", 1)
plane_ticket_business = PlaneTicket(6000, "1A", "business", 1)

# Výpis cen
print("Cena jízdenky na vlak (economy):", train_ticket_economy.get_price())
print("Cena jízdenky na vlak (business):", train_ticket_business.get_price())
print("Cena letenky (economy):", plane_ticket_economy.get_price())
print("Cena letenky (business):", plane_ticket_business.get_price())

# Vypočítání celkové ceny dvou jízdenek
total_price = train_ticket_economy.get_price() + plane_ticket_business.get_price()
print("Celková cena jízdenky na vlak (economy) a letenky (business):", total_price)