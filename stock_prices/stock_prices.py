#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # we need to find the max profit.
  # we have to find the diffence between the min price and max price
  # how can i go over it and keep track of min price and maxprofit.
  min_price = prices[0]
  max_profit = prices[1] - min_price
  for p in range(len(prices)):
    for x in range(p + 1,len(prices)):
      if  prices[x] - prices[p] > max_profit:
        max_profit = prices[x] - prices[p]

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
