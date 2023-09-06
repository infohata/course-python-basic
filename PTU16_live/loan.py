from math import ceil

class Loan():
    def __init__(
            self, 
            loan: float, 
            interest_percent: float = 4, 
            duration: int = 12,
            downpayment: float = 0, 
        ) -> None:
        self.loan = loan
        self.downpayment = downpayment
        self.interest_percent = interest_percent
        self.duration = duration
        self.principal = loan - downpayment
        self.monthly_true = self.get_monthly_true()
        self.monthly = self.get_monthly_lowest()
        self.repayable = round(self.monthly_true * self.duration, 2)
        self.loan_total = downpayment + self.repayable
        self.increase = self.repayable - self.principal
        self.remaining = self.repayable
        self.penny_months = self.get_penny_months()
        self.payments = self.get_payment_chart()

    def get_monthly_true(self) -> float:
        monthly_interest = self.interest_percent / 12 / 100
        monthly = self.principal * monthly_interest \
            / (1 - (1 + monthly_interest) ** -self.duration)
        return monthly
    
    def get_monthly_lowest(self) -> float:
        return int(self.monthly_true * 100) / 100
    
    def get_penny_months(self) -> int:
        if self.repayable == self.monthly * self.duration:
            return 0
        else:
            pennies = self.repayable - self.monthly * self.duration
            return int(pennies * 100)
        
    def get_monthly(self, month=1):
        if month <= self.penny_months:
            return self.monthly + 0.01
        else:
            return self.monthly

    def get_payment_chart(self) -> list:
        payments = []
        for month in range(self.duration):
            payments.append(self.get_monthly(month+1))
        return payments

    def print_loan_info(self) -> None:
        print(f"""------ Loan stats -----
            Loan:           {self.loan:10.2f}
            Downpayment:    {self.downpayment:10.2f}
            Interest:     {self.interest_percent:10.2f} %
            Duration:        {self.duration} months
            Principal:      {self.principal:10.2f}
            Monthly:        {self.monthly:10.2f}
            Pennies:        {self.get_penny_months():10d}
            Loan Total:     {self.loan_total:10.2f}
            Increase:       {self.increase:10.2f}\n""")

    def print_monthly_payments(self) -> None:
        for period, payment in enumerate(self.payments):
            print(f"{period+1:3d}: {payment:10.2f}")
