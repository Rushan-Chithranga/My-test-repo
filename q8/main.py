import json

def get_user_input_matrix(size):
    matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            if j >= i:
                value = input(f"Enter the value for element [{i}][{j}]: ")
                row.append(value)
            else:
                row.append("0")  # Fill lower part with 0s for upper triangular
        matrix.append(row)

    return matrix

def create_json_matrix(matrix):
    formatted_json = "[\n"
    for row in matrix:
        formatted_json += "    " + json.dumps(list(row)) + ",\n"
    formatted_json = formatted_json.rstrip(",\n") + "\n]"
    return formatted_json

def main():
    size = int(input("Enter the size of the square matrix: "))
    matrix = get_user_input_matrix(size)
    
    matrix_json = create_json_matrix(matrix)
    
    print("The JSON representation of the upper triangular matrix is:")
    print(matrix_json)
    
    with open('upper_triangular_matrix.json', 'w') as file:
        file.write(matrix_json)
    print("The JSON matrix has been saved to 'upper_triangular_matrix.json'.")

if __name__ == "__main__":
    main()
