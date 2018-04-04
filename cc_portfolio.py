#!/usr/bin/python
#
# Arguments and error handling

from argparse import ArgumentParser
from sys import exit
import requests
import json

parser = ArgumentParser(description='read portfolio file passed as argument')
parser.add_argument('input_file', help='the portfolio file to read')
parser.add_argument('dest_file', help='output file to write values to')
# parser.add_argument('--content-type', '-c',
#                    default='html',
#                    choices=['html', 'json'],
#                    help='the content-type of the URL being requested')
# content_type = vars(parser.parse_args())['content_type']



# variable declaration(s) and init
input_file = vars(parser.parse_args())['input_file']
dest_file = vars(parser.parse_args())['dest_file']

# globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL_base = "https://api.coinmarketcap.com/v1/ticker"

# total portfolio value - to be calculated
total = float(0)

#empty dictionary to contain output for view
portfolio = {}



# script main

try:
    target = open(input_file, 'r')
except(IOError):
    print("File does not exist")
else:
    with open(input_file) as file_object:
        lines = file_object.readlines()

# print()
for line in lines:
    coin_id, quantity = line.split(':')

    tickerURL = tickerURL_base+'/'+coin_id+'/'
    request = requests.get(tickerURL)
    coin_data = request.json()

    ticker = coin_data[0]['symbol']
    price =  coin_data[0]['price_usd']

    amount = float(price) * float(quantity)
    total += amount

    portfolio[ticker] = amount



# VIEW
# print portfolio

print "-" * 28
print "Portfolio Details: "
print "-" * 28
for coin,amount  in portfolio.items():
    print coin + "\t\t$ " + '{0:,.2f}'.format(amount)

print "-" * 28
print "Total" + "\t\t$ "+ '{0:,.2f}'.format(total)






# choice = input("Your choice: " )
#
# if choice == "all":
#     request = requests.get(tickerURL)
#     data = request.json()
#
#     for x in data:
#         ticker = x['symbol']
#         price = x['price_usd']
#
#         print(ticker + ":\t\t$" + price)
#     print()
#
# else:
#     tickerURL += '/'+choice+'/'
#     request = requests.get(tickerURL)
#     data = request.json()
#
#     ticker = data[0]['symbol']
#     price = data[0]['price_usd']
#
#     print(ticker + ":\t\t$" + price)
#     print()
