from tabulate import tabulate
import csv
import sys
import os
import yfinance as yf


if not os.path.exists('portfolio.csv'):
    with open('portfolio.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['ticker', 'shares', 'purchase_price'])


def main():
    # show menu, handle user commands
    print('Welcome to SGX Portfolio Tracker')
    while True:
        print('\n1. Add stock')
        print('2. Remove stock')
        print('3. View portfolio')
        print('4. Quit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            sys.exit('Goodbye, see you again!')
        else:
            print('Invalid option, try again')


def add_stock():
    # add stock to portoflio.csv
    # validate input, append to portfolio.csv
    while True:
        ticker = input('Ticker: ').strip().upper()
        if not validate_ticker(ticker):
            print('Invalid ticker, try again')
            continue
        try:
            stock = yf.Ticker(ticker)
            price = stock.fast_info['last_price']
            if not price:
                raise ValueError
        except Exception:
            print('Ticker not found on Yahoo Finance, try again')
            continue
        try:
            shares = int(input('Shares: '))
            if shares < 1:
                raise ValueError
        except ValueError:
            print('Invalid shares, try again')
            continue
        try:
            purchase_price = float(input('Purchase Price: $'))
            if purchase_price < 0:
                raise ValueError
        except ValueError:
            print('Invalid purchase price, try again')
            continue
        break # all inputs valid, exit loop

    # write rows into portfolio.csv
    with open('portfolio.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([ticker, shares, purchase_price])
    print(f'{ticker} added successfully!')


def remove_stock():
    # remove stock from portfolio.csv
    # validate input, append to portfolio.csv
    while True:
        ticker = input('Ticker: ').strip().upper()
        if not ticker.endswith('.SI'):
            print('Invalid ticker, try again')
            continue
        break # all inputs valid, exit loop

    # read all rows
    with open('portfolio.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # filter out the ticker
    header = rows[0]  # keep the header row
    remaining = [row for row in rows[1:] if row[0] != ticker]
    if len(remaining) == len(rows) - 1:
        print(f'{ticker} not found in portfolio')
        return

    # write remaining rows back
    with open('portfolio.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(remaining)

    print(f'{ticker} removed successfully!')


    # read portfolio.csv, fetch live prices via yfinance
def view_portfolio():
    with open('portfolio.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # validate portfolio
    if not rows:
        print('Portfolio is empty!')
        return

    # locate ticker, shares, purchase_price
    table = []
    for row in rows:
        ticker = row['ticker']
        shares = int(row['shares'])
        purchase_price = float(row['purchase_price'])

        # fetch live price
        try:
            stock = yf.Ticker(ticker)
            current_price = stock.fast_info['last_price']
        except Exception:
            print(f'Could not fetch price for {ticker}, skipping')
            continue
        # calculate current value, gain/loss
        current_value = calculate_current_value(current_price, shares)
        gain_loss = calculate_gain_loss(purchase_price, current_price, shares)

        table.append([ticker, shares, f'${purchase_price:.2f}',
                    f'${current_price:.2f}', f'${current_value:.2f}',
                    f'${gain_loss:+.2f}'])

    # print formatted table with tabulate
    print(tabulate(table,
                    headers=['Ticker', 'Shares', 'Buy Price', 'Current Price', 'Value', 'Gain/Loss'],
                    tablefmt='grid'))


# functions for test_project to validate
def validate_ticker(ticker):
    return ticker.endswith('.SI')

def calculate_gain_loss(purchase_price, current_price, shares):
    return (current_price - purchase_price) * shares

def calculate_current_value(current_price, shares):
    return current_price * shares


if __name__ == "__main__":
    main()
