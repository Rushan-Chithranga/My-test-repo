import json

with open('./data.json', 'r') as f:
    data = json.load(f)

rotated_data = list(zip(*data[::-1]))

def custom_json_dumps(data):
    formatted_json = "[\n"
    for row in data:
        formatted_json += "    " + json.dumps(list(row)) + ",\n"
    formatted_json = formatted_json.rstrip(",\n") + "\n]"
    return formatted_json

rotated_json_data = custom_json_dumps(rotated_data)
print(rotated_json_data)


with open('output_data.json', 'w') as file:
    file.write(rotated_json_data)
    print("Output written to output_data.json")
