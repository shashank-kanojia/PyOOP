class Bill:
    """
    Object containing data about the Bill, such as total amount and period of bill.
    """

    def __init__(self, amount: float, period: str) -> None:
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate (person) instance who stays in the flat and pays its share of the bill.
    """

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flat_mates: list) -> float:
        total_days_other_flatmates: int = 0
        for flatmate in other_flat_mates:
            total_days_other_flatmates += flatmate.days_in_house
        weight: float = self.days_in_house / (self.days_in_house + total_days_other_flatmates)
        return round(bill.amount * weight, 2)