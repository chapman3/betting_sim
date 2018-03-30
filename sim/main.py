from __future__ import division
import prop

def main():
	output = open("output.txt", "w")
	payout = 0
	for i in range(1000):
		team1 = prop.Prop(100, "Team 1")
		team2 = prop.Prop(100, "Team 2")
		team3 = prop.Prop(100, "Team 3")
		team4 = prop.Prop(100, "Team 4")
		team5 = prop.Prop(100, "Team 5")
		teams = [team1, team2, team3, team4, team5]
		for i in range(160):
			for team in teams:
				team.proceed()
		for team in teams:
			payout += team.payout
	payout = float(payout/1000)
	print payout

if __name__ == "__main__":
	main()