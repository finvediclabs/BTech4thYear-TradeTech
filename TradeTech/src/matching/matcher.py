class Matcher:
    def __init__(self):
        self.matching_results = []

    def match_orders(self, order1, order2):
        if order1['type'] == 'buy' and order2['type'] == 'sell':
            if order1['price'] >= order2['price']:
                self.matching_results.append((order1, order2))
                return True
        return False

    def get_matching_results(self):
        return self.matching_results