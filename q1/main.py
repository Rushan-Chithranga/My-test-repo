import json

with open('./data.json', 'r') as f:
  dice = json.load(f)

def transform(dice):
    try:
        rotatedDice = []
        for i in range(0, len(dice)):
            newRow = []
            for j in range(len(dice[i])-1, -1, -1):
                newRow.append(dice[j][i])
            rotatedDice.append(newRow)
        return rotatedDice
    except Exception as e:
        return "Invalid input"

rotatedDice = transform(dice)

with open("output.json", "w") as outfile:
    outfile.write(json.dumps(rotatedDice))
    print("Output written to output.json")