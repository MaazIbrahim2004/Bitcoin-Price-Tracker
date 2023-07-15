import requests 
import tkinter as tk #GUI 
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price_usd = response["USD"]
    price_jpy = response["JPY"]
    price_eur = response["EUR"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPriceUSD.config(text = "USD: " + str(price_usd) + "$")
    labelPriceJPY.config(text = "JPY: " + str(price_jpy) + "¥")
    labelPriceEUR.config(text = "EUR: " + str(price_eur) + "€")
    labelTime.config(text = "Updated at: " + time)

    canvas.after(1000, trackBitcoin) #refreshes the price every 1000 milliseconds

canvas = tk.Tk()
canvas.geometry("500x500")
canvas.title("Bitcoin Price Index")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text = "Bitcoin Price Index", font = f1)
label.pack(pady = 20)

labelPriceUSD = tk.Label(canvas, font = f2)
labelPriceUSD.pack(pady = 20)

labelPriceJPY = tk.Label(canvas, font = f2)
labelPriceJPY.pack(pady = 20)

labelPriceEUR = tk.Label(canvas, font = f2)
labelPriceEUR.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3) #time that the price was last updated
labelTime.pack(pady = 20)

trackBitcoin()

canvas.mainloop()
