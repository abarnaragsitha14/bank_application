from dataclasses import dataclass
@dataclass
class Transaction:
    transaction_type: str
    amount: float
    from_account: int
    to_account: int
t1=Transaction("TRANSFER",1000,101,102)
print(t1)
