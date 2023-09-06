import PySimpleGUI as sg
from loan import Loan


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
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-SHOW-CHART-':
        window.hide()
        payments = []
        for month, payment in enumerate(loan.get_payment_chart()):
            payments.append([month+1, f"{payment:.2f}"])
        chart_layout = [
            [sg.Table(values=payments, headings=['Month', 'Amount'], key='-CHART-TABLE-', col_widths=[5, 15], auto_size_columns=False)],
            [sg.Button('Close', key='-CLOSE-')],
        ]
        chart_window = sg.Window('Payment Chart', chart_layout)
        while True:
            chart_event, chart_values = chart_window.read()
            if chart_event in (sg.WIN_CLOSED, '-CLOSE-'):
                break
        chart_window.close()
        window.un_hide()
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
            window['-SHOW-CHART-'].update(disabled=False)
