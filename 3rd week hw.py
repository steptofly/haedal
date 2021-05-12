class exchange_rate:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print("화폐 이름: ", self.name)
        print("현재 환율: ", self.price, "원")
        print("")



currency1 = exchange_rate("USD", 1125.50)
currency2 = exchange_rate("JPY", 1034.70)
currency3 = exchange_rate("CNY", 174.76)
currency4 = exchange_rate("EUR", 1365.34)


currency1.info()
currency2.info()
currency3.info()
currency4.info()
