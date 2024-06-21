import java.util.*;

public class MatrixRotation {

    public static void main(String[] args) {
        // Sample matrix (2D array)
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        // Rotate the matrix by 90 degrees clockwise
        int[][] rotatedMatrix = rotateMatrix(matrix);

        System.out.println("\nRotated Matrix:");
        printMatrix(rotatedMatrix);
    }

    // Function to rotate a matrix by 90 degrees clockwise
    public static int[][] rotateMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        // Create a new matrix for rotated data
        int[][] rotatedMatrix = new int[cols][rows];

        // Perform the rotation
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rotatedMatrix[j][rows - 1 - i] = matrix[i][j];
            }
        }

        return rotatedMatrix;
    }

    // Utility function to print a matrix
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
