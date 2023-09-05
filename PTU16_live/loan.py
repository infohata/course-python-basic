from math import ceil

class Loan():
    def __init__(
            self, 
            loan: float, 
            interest_percent: float = 4, 
            periods: int = 12,
            downpayment: float = 0, 
        ) -> None:
        self.loan = loan
        self.downpayment = downpayment
        self.interest_percent = interest_percent
        self.periods = periods
        self.principal = loan - downpayment
        self.increase = self.get_interest()
        self.repayable = self.principal + self.increase
        self.remaining = self.repayable
        self.loan_total = downpayment + self.repayable
        self.monthly, self.penny_months = self.get_monthly_payment()
    
    def get_interest(self) -> float:
        years = self.periods // 12
        last_year_months = self.periods % years
        # monthly_principal = self.principal / self.periods
        compound_interest = []
        for year in range(years):
            remaining_years = years - year
            remaining_principal = self.principal / years * remaining_years
            compound_interest.append(self.interest_percent / 100 ** remaining_years * remaining_principal)
        last_year_compound_interest = 0
        if last_year_months > 0:
            last_year_compound_interest = (self.principal - (self.principal / years * 12)) / last_year_months 
        return self.principal * self.interest_percent / 100

    def get_monthly_payment(self) -> (float, int):
        monthly = self.repayable * 100 // self.periods / 100
        pennies = (self.repayable / self.periods - monthly) * self.periods * 100
        return monthly, int(ceil(pennies))

    def get_payment_chart(self) -> list:
        return
