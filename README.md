# Bitcoin Price Index Application

This is a simple Python application that uses the `tkinter` library for GUI and `requests` library to fetch real time Bitcoin prices in USD, JPY, and EUR. All the Bitcoin prices are fetched using the CryptoCompare API.

![2023-07-15-13-52-01 (1)](https://github.com/MaazIbrahim2004/Bitcoin-Price-Tracker/assets/111203880/bfbe241a-c693-48d9-ab31-fa673965069a)

## Prerequisites
* You have installed Python 3.6 or above.
* You have installed the `requests` and `tkinter` Python libraries.

## Using the Bitcoin Price Index Application

To use the Bitcoin Price Index Application:

1. Clone this repository to your local machine.
2. Run the script from the terminal using the command `python3 script_name.py`.
3. A new window will open that shows the real-time Bitcoin price in USD, JPY, and EUR. The prices are refreshed every second.
  
## Project Structure

The project has a simple structure:

* A function `track_bitcoin` that fetches the latest Bitcoin prices from the CryptoCompare API and updates them on the `tkinter` GUI.
* The main part of the script that initializes the `tkinter` GUI and continuously calls `track_bitcoin` to keep the prices updated.
* The application displays the Bitcoin price in USD, JPY, and EUR, and the time at which the price was last updated.

## Acknowledgments

This project uses the CryptoCompare API for fetching Bitcoin prices. You can find their documentation [here](https://min-api.cryptocompare.com/documentation?key=Price&cat=SingleSymbolPriceEndpoint).

