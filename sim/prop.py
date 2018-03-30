from __future__ import division
import random


class Prop:
	def __init__(self, odds, name):
		self.name = name
		self.odds = float(odds/162)
		self.wins = 0
		self.losses = 0
		self.payout = 50

	def proceed(self):
		result = random.uniform(0,1)
		if result>self.odds:
			self.losses += 1
			self.payout -= float(1)
			if self.payout <0:
				games = self.losses + self.wins
				print(str(self.name) + " died after " + str(games) + " games.")
		else:
			self.wins += 1
			payout_odds = random.triangular(105, 310, 190)
			self.payout += float((100/payout_odds))
