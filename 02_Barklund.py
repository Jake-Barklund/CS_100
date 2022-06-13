player = input("Enter player name: ")
strength = float(input("Enter strength (0-100): "))
endurance = float(input("Enter endurance (0-100): "))
charisma = float(input("Enter charisma (0-100): "))

maxWeight = strength * 2.3
hitPoints = 100 + (endurance)
convince = 0.5 + (charisma/200.0)

print("Player name: ", player)
print("Maximum Weight: ", format(maxWeight, '.2f'))
print("Hit points: ", format(round(hitPoints)))
print("Convincing probability: ", format(convince, "0.0%"))
