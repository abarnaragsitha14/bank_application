class AccountNotFoundError(Exception):
    pass


class DuplicateAccountError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass