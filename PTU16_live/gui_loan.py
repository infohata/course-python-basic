import PySimpleGUI as sg
from loan import Loan
from typing import Any

def main_window() -> None:
    layout = [
        [sg.Text("Loan amount", size=20), sg.Input(key="-LOAN-", justification="right", size=15)],
        [sg.Text("Duration (months)", size=20), sg.Input("12", key="-DURATION-", justification="right", size=15)],
        [sg.Text("Interest, %", size=20), sg.Input("5.0", key="-INTEREST-", justification="right", size=15)],
        [sg.Text("Downpayment", size=20), sg.Input("0", key="-DOWNPAYMENT-", justification="right", size=15)],
        [sg.Button("Calculate", key="-CALCULATE-", pad=8), sg.Button("Show Chart", key="-SHOW-CHART-", pad=8, disabled=True)],
        [sg.Text("", key="-ERRORS-", size=35, justification="center", text_color='#FF9999')],
        [sg.Text("Monthly Payment", size=20), sg.Text("", key="-MONTHLY-", justification="right", size=15)],
        [sg.Text("Price Increase", size=20), sg.Text("", key="-INCREASE-", justification="right", size=15)],
        [sg.Text("Total Reoayment", size=20), sg.Text("", key="-REPAYABLE-", justification="right", size=15)],
        [sg.Text("Total loan", size=20), sg.Text("", key="-TOTAL-", justification="right", size=15)],
    ]
    window = sg.Window("Loan Calculator", layout)
    loan = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-CALCULATE-':
            loan = calculate_loan(values, window)
        if event == '-SHOW-CHART-':
            if isinstance(loan, Loan):
                chart_window(loan, window)

def calculate_loan(values: Any, window: sg.Window) -> Loan:
    window['-ERRORS-'].update("")
    try:
        loan = Loan(
            float(values['-LOAN-']), 
            float(values['-INTEREST-']), 
            int(values['-DURATION-']), 
            float(values['-DOWNPAYMENT-']),
        )
    except Exception as error:
        window['-ERRORS-'].update("Values must be numbers")
    else:
        window['-MONTHLY-'].update(f"{loan.monthly:,.2f}")
        window['-INCREASE-'].update(f"{loan.increase:,.2f}")
        window['-REPAYABLE-'].update(f"{loan.repayable:,.2f}")
        window['-TOTAL-'].update(f"{loan.loan_total:,.2f}")
        window['-SHOW-CHART-'].update(disabled=False)
        return loan

def chart_window(loan: Loan, main_window: sg.Window) -> None:
    main_window.hide()
    payments = []
    for month, payment in enumerate(loan.get_payment_chart()):
        payments.append([month+1, f"{payment:.2f}"])
    layout = [
        [sg.Table(
            values=payments, 
            headings=['Month', 'Amount'], 
            key='-CHART-TABLE-', 
            col_widths=[5, 15], 
            auto_size_columns=False
        )],
        [sg.Button('Close', key='-CLOSE-')],
    ]
    window = sg.Window('Payment Chart', layout)
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
    window.close()
    main_window.un_hide()

main_window()
