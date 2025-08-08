import numpy as np

def input_matrix(name):
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
        print(f"Enter values for {name}:")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            if len(row) != cols:
                raise ValueError("Column size mismatch")
            matrix.append(row)
        return np.array(matrix)
    except Exception as e:
        print("Error:", e)
        return input_matrix(name)

def main():
    print("==== Matrix Calculator ====")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")

    while True:
        print("\nChoose operation:")
        print("1. A + B")
        print("2. A - B")
        print("3. A * B")
        print("4. Inverse of A")
        print("5. Inverse of B")
        print("6. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == '1':
                print("Result:\n", A + B)
            elif choice == '2':
                print("Result:\n", A - B)
            elif choice == '3':
                print("Result:\n", A @ B)
            elif choice == '4':
                print("Inverse of A:\n", np.linalg.inv(A))
            elif choice == '5':
                print("Inverse of B:\n", np.linalg.inv(B))
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
