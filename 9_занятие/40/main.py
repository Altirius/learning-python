import csv

FILE_NAME = 'california_housing_train.csv'
MIN_POPULATION = 0
MAX_POPULATION = 500

def main():
	with open(FILE_NAME, newline='') as csvfile:
		dictReader = csv.DictReader(csvfile)
		sumOfTargetHouseValue = 0
		targetHouseQty = 0

		for row in dictReader:
			population = float(row['population'])
			
			if isTargetPopulationReached(population):
				sumOfTargetHouseValue += float(row['median_house_value'])
				targetHouseQty += 1

	if targetHouseQty > 0:
		print(sumOfTargetHouseValue / targetHouseQty)
	else:
		print('Нет домов где кол-во людей от 0 до 500')

def isTargetPopulationReached(population):
	return (population >= MIN_POPULATION) and (population <= MAX_POPULATION)


main()
