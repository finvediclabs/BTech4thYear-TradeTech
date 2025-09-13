# TradeTech: Build an End-to-End Electronic Trading System

## Project Description
TradeTech is an end-to-end electronic trading system designed to facilitate order placement, matching, and reconciliation. The system leverages Kafka for efficient message passing and provides a user-friendly interface for traders. This project aims to streamline the trading process, ensuring that orders are managed effectively and accurately.

## Project Structure
```
TradeTech
├── src
│   ├── main.py
│   ├── order
│   │   └── order_manager.py
│   ├── matching
│   │   └── matcher.py
│   ├── reconciliation
│   │   └── reconciler.py
│   ├── kafka
│   │   └── kafka_client.py
│   └── ui
│       └── ui_app.py
├── requirements.txt
├── README.md
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd TradeTech
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To start the TradeTech application, run the following command:
```
python src/main.py
```
This will initialize the trading system, set up Kafka connections, and launch the user interface.

## Resolving Common Bugs
Here are some common issues you might encounter while developing or deploying the TradeTech system, along with their solutions:

1. **Kafka Connection Issues:**
   - Ensure that the Kafka server is running and accessible.
   - Check the configuration settings in `kafka_client.py` for the correct broker address.

2. **Order Placement Errors:**
   - Verify that the order format is correct when using the `place_order` method in `order_manager.py`.
   - Check for any validation errors in the order data.

3. **UI Not Displaying:**
   - Ensure that Flask is installed and running properly.
   - Check the console for any error messages related to the UI.

4. **Matching Algorithm Not Working:**
   - Review the logic in `matcher.py` to ensure that the matching criteria are correctly implemented.
   - Test with sample buy and sell orders to verify functionality.

5. **Reconciliation Report Generation Fails:**
   - Ensure that the order list passed to `reconcile_orders` is not empty.
   - Check for any exceptions thrown during the report generation process.

If you encounter any other issues, please refer to the documentation or seek help from the community.

## License
This project is licensed under the MIT License - see the LICENSE file for details.