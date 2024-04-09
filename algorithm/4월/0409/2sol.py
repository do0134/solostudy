# HackerRank basic Python test2

class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):

        total_price = self.item_price * req_items

        if req_items > self.num_items:
            return "Not enough items in the machine"
        elif money < total_price:
            return "Not enough coins"
        else:
            self.num_items -= req_items

            return money - total_price

    pass


if __name__ == '__main__':