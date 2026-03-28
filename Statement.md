# Bank Fraud Detector (Lightweight AI System)

A Python-based Bank Management System designed with a built-in **Fraud Detection Logic**. This system allows for basic banking operations while monitoring transaction safety limits to prevent unauthorized or high-risk withdrawals.

# Transaction Statement: Account A001

| Date | Description | Amount | Balance | Status |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-28 | Opening Balance | -- | $5,000 | SUCCESS |
| 2026-03-28 | Cash Deposit | +$500 | $5,500 | SUCCESS |
| 2026-03-28 | Withdrawal | -$1,000 | $4,500 | SUCCESS |
| 2026-03-28 | Withdrawal | -$4,000 | $4,500 | **BLOCKED (FRAUD)** |

### Security Report
> **Alert:** Transaction of $4,000 was flagged on Account A001. 
> **Reason:** Amount exceeds the system safety limit of $3,500. 
> **Action taken:** Funds frozen; Withdrawal denied.