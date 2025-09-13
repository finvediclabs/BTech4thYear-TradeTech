# main.py

from kafka.kafka_client import KafkaClient
from ui.ui_app import UIApp
from order.order_manager import OrderManager
from matching.matcher import Matcher
from reconciliation.reconciler import Reconciler

def main():
    # Initialize components
    kafka_client = KafkaClient()
    order_manager = OrderManager()
    matcher = Matcher()
    reconciler = Reconciler()
    ui_app = UIApp(order_manager, matcher, reconciler)

    # Set up Kafka connections
    kafka_client.setup()

    # Start the UI
    ui_app.start_ui()

if __name__ == "__main__":
    main()