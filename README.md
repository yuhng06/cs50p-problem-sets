# SGX Portfolio Tracker

## Video Demo: 

## Description
A command-line portfolio tracker for SGX-listed stocks.
Users can add, remove, and view their stock holdings with live prices fetched from Yahoo Finance.
The portfolio persists between sessions via a CSV file.

## Features
- Add SGX-listed stocks with purchase price and number of shares
- Remove stocks from your portfolio
- View live prices, current value, and gain/loss for each holding
- Data persists between sessions in portfolio.csv

## Usage
Run the program with:
python project.py

Proceed to choose from the menu:
1. Add stock — enter ticker (must end in .SI), shares, and purchase price
2. Remove stock — enter ticker to remove
3. View portfolio — displays a formatted table with live prices
4. Quit

## Libraries
- yfinance — fetches live stock prices from Yahoo Finance
- tabulate — formats portfolio data into a readable table
- csv, sys, os — Python built-in libraries

## Design choices
The portfolio is stored as a CSV file so data persists between sessions without needing a database.
Helper functions validate_ticker(), calculate_gain_loss(), and calculate_current_value() are separated from the main logic to keep the code clean and testable with pytest.
