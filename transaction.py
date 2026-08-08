from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_type: str
    amount: float
    from_account: int
    to_account: int
