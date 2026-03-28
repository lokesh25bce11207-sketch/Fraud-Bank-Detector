# Bank Fraud Detector (Lightweight AI System)

A Python-based Bank Management System designed with a built-in **Fraud Detection Logic**. This system allows for basic banking operations while monitoring transaction safety limits to prevent unauthorized or high-risk withdrawals.

##  Features
**Account Management:** View all registered accounts with balance and branch details.
**Secure Deposits:** Add funds to any valid account with input validation.
**AI Fraud Check:** Automatically blocks any withdrawal attempt exceeding the safety threshold ($3,500).
**Balance Inquiry:** Real-time balance checking for specific account numbers.
**Error Handling:** Robust protection against invalid numerical inputs and non-existent account IDs.

## Technical Stack
**Language:** Python 3.x
**Data Structure:** Nested Dictionaries (for fast account lookups).
**Logic:** Procedural programming with conditional security gates.

## How to Use
1. Run the script: `python bank_system.py`
2. Select an option from the main menu (1-5).
3. Follow the on-screen prompts to enter Account Numbers (e.g., `A001`).
4. To test the **Fraud Detector**, try withdrawing an amount greater than **$3,500**.

## Security Logic
The system uses a `fraud_check` function that acts as a middleware between the user request and the database. 
- **Threshold:** $3,500
- **Action:** If `amount >= threshold`, the transaction is killed instantly and a `SECURITY ALERT` is logged.

## License
Open-source for educational and training purposes.