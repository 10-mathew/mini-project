from tkinter import *
from tkinter import ttk

# Create a GUI window
root = Tk()

# Create global variables
variable1 = StringVar(root)
variable2 = StringVar(root)

# Initialize the variables
variable1.set("currency")
variable2.set("currency")

# Function to perform real-time conversion from one currency to another
def RealTimeCurrencyConversion():
    import requests, json

    from_currency = variable1.get()
    to_currency = variable2.get()

    api_key = "ZVD51OFR62VQGW6P"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    req_ob = requests.get(main_url)
    result = req_ob.json()

    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    amount = float(Amount1_field.get())
    new_amount = round(amount * Exchange_Rate, 3)

    Amount2_field.delete(0, END)
    Amount2_field.insert(0, str(new_amount))

# Function for clearing the Entry field
def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

# Driver code
if __name__ == "__main__":
    # Set the background color of GUI window
    root.configure(background='#f0f0f0')

    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("450x250")

    # Set the title of the window
    root.title("Real Time Currency Converter")

    # Create a main frame
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

    # Create "Welcome to Real Time Currency Converter" label
    headlabel = ttk.Label(main_frame, text="Welcome to Real Time Currency Converter", font=('Helvetica', 14, 'bold'), background='#f0f0f0')
    headlabel.grid(row=0, column=0, columnspan=3, pady=10)

    # Create a "Amount :" label
    label1 = ttk.Label(main_frame, text="Amount :", font=('Helvetica', 10), background='#f0f0f0')
    label1.grid(row=1, column=0, sticky=W, pady=5)

    # Create a "From Currency :" label
    label2 = ttk.Label(main_frame, text="From Currency :", font=('Helvetica', 10), background='#f0f0f0')
    label2.grid(row=2, column=0, sticky=W, pady=5)

    # Create a "To Currency: " label
    label3 = ttk.Label(main_frame, text="To Currency :", font=('Helvetica', 10), background='#f0f0f0')
    label3.grid(row=3, column=0, sticky=W, pady=5)

    # Create a "Converted Amount :" label
    label4 = ttk.Label(main_frame, text="Converted Amount :", font=('Helvetica', 10), background='#f0f0f0')
    label4.grid(row=5, column=0, sticky=W, pady=5)

    # Create a text entry box for Amount
    Amount1_field = ttk.Entry(main_frame, width=25, font=('Helvetica', 10))
    Amount1_field.grid(row=1, column=1, columnspan=2, pady=5, padx=10)

    # Create a text entry box for Converted Amount
    Amount2_field = ttk.Entry(main_frame, width=25, font=('Helvetica', 10))
    Amount2_field.grid(row=5, column=1, columnspan=2, pady=5, padx=10)

    # List of currency codes
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    # Create a drop-down menu for From Currency
    FromCurrency_option = ttk.Combobox(main_frame, textvariable=variable1, values=CurrenyCode_list, font=('Helvetica', 10), state='readonly')
    FromCurrency_option.grid(row=2, column=1, columnspan=2, pady=5, padx=10, sticky=W)

    # Create a drop-down menu for To Currency
    ToCurrency_option = ttk.Combobox(main_frame, textvariable=variable2, values=CurrenyCode_list, font=('Helvetica', 10), state='readonly')
    ToCurrency_option.grid(row=3, column=1, columnspan=2, pady=5, padx=10, sticky=W)

    # Create a Convert Button
    button1 = ttk.Button(main_frame, text="Convert", command=RealTimeCurrencyConversion)
    button1.grid(row=4, column=1, pady=10, padx=5, sticky=W)

    # Create a Clear Button
    button2 = ttk.Button(main_frame, text="Clear", command=clear_all)
    button2.grid(row=4, column=2, pady=10, padx=5, sticky=W)

    # Start the GUI
    root.mainloop()