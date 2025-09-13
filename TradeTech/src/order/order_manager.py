class OrderManager:
    def __init__(self):
        self.orders = {}

    def place_order(self, order):
        order_id = order.get('id')
        self.orders[order_id] = order
        return f"Order {order_id} placed successfully."

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            return f"Order {order_id} canceled successfully."
        else:
            return f"Order {order_id} not found."

    def get_order_status(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]
        else:
            return f"Order {order_id} not found."