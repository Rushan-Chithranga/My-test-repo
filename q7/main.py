import json

def get_user_input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = input(f"Enter the value for element [{i}][{j}]: ")
            row.append(value)
        matrix.append(row)

    return matrix

def create_json_matrix(matrix):
    formatted_json = "[\n"
    for row in matrix:
        formatted_json += "    " + json.dumps(list(row)) + ",\n"
    formatted_json = formatted_json.rstrip(",\n") + "\n]"
    return formatted_json

def main():
    matrix = get_user_input_matrix()
    
    matrix_json = create_json_matrix(matrix)
    
    print("The JSON representation of the matrix is:")
    print(matrix_json)
    
    with open('matrix.json', 'w') as file:
        file.write(matrix_json)
    print("The JSON matrix has been saved to 'matrix.json'.")

if __name__ == "__main__":
    main()
