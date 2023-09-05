from PTU16_live.loan import Loan
import unittest


class TestLoan1(unittest.TestCase):
    def setUp(self) -> None:
        self.loan = Loan(11000, 7, 12, 1000)

    def test_principal(self):
        self.assertAlmostEqual(self.loan.principal, 10000, 2)

    def test_interest(self):
        self.assertAlmostEqual(self.loan.increase, 700, 2)

    def test_totals(self):
        self.assertAlmostEqual(self.loan.loan_total, 11700, 2)
        self.assertAlmostEqual(self.loan.repayable, 10700, 2)

    def test_monthly(self):
        self.assertAlmostEqual(self.loan.monthly, 891.66, 2)

    def test_pennies(self):
        self.assertEqual(self.loan.penny_months, 8)
        self.assertAlmostEqual(
            self.loan.repayable, 
            self.loan.monthly * 12 + self.loan.penny_months / 100, 2
        )
