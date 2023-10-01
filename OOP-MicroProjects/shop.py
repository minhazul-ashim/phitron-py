class Shop :
    def __init__(self, name) -> None:
        self.name = name;
        self.buyers = [];
    def addBuyer (self, name) : 
        new = Buyer(name, len(self.buyers) + 1);
        self.buyers.append(new);

    def updateBuyerCart(self, buyerId, item, quantity, price) :
        new = Order(item, quantity, price);
        for buyer in self.buyers :
            if(buyer.buyerId == buyerId) :
                buyer.cart.append(new);


class Buyer :
    def __init__(self, name, buyerId) :
        self.name = name;
        self.buyerId = buyerId;
        self.cart = [];


class Order :
    def __init__(self, item, qty, price) -> None:
        self.item = item;
        self.qty = qty;
        self.total = price * qty;


shop = Shop('Savdo');
shop.addBuyer('Ashim'); #BuyerID should be 1;
shop.addBuyer('Kona'); #BuyerID should be 2;
shop.updateBuyerCart(1, 'Watch', 3, 15);
shop.updateBuyerCart(2, 'Sunglass', 1, 5);
shop.updateBuyerCart(2, 'Heels', 2, 20);
shop.updateBuyerCart(1, 'Tshirt', 10, 5);
shop.updateBuyerCart(1, 'Car', 1, 100000);
shop.updateBuyerCart(1, 'Shoes', 5, 12);

for buyer in shop.buyers :
    print(f'Buyer name is {buyer.name}');
    if(len(buyer.cart) == 0) :
        print(f'{buyer.name} has no items in cart');
    for item in buyer.cart :
        print(f'Item name {item.item} with quantity {item.qty} and total is {item.total}');
    print('\n');
