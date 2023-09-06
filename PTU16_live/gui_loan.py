import PySimpleGUI as sg
from loan import Loan


layout = [
    [sg.Text("Loan amount", size=20), sg.Input(key="-LOAN-", justification="right", size=15)],
    [sg.Text("Duration (months)", size=20), sg.Input("12", key="-DURATION-", justification="right", size=15)],
    [sg.Text("Interest, %", size=20), sg.Input("5.0", key="-INTEREST-", justification="right", size=15)],
    [sg.Text("Downpayment", size=20), sg.Input("0", key="-DOWNPAYMENT-", justification="right", size=15)],
    [sg.Button("Calculate", key="-CALCULATE-", pad=2)],
    [sg.Text("", key="-ERRORS-", size=35, justification="center", text_color='#FF9999')],
    [sg.Text("Monthly Payment", size=20), sg.Text("", key="-MONTHLY-", justification="right", size=15)],
    [sg.Text("Price Increase", size=20), sg.Text("", key="-INCREASE-", justification="right", size=15)],
    [sg.Text("Total Reoayment", size=20), sg.Text("", key="-REPAYABLE-", justification="right", size=15)],
    [sg.Text("Total loan", size=20), sg.Text("", key="-TOTAL-", justification="right", size=15)],
]

window = sg.Window("Loan Calculator", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CALCULATE-':
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
