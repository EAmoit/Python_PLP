def write_to_file():
    try:
        # Create a new file in write mode and write content
        with open('my_file.txt', 'w') as file:
            file.write("Hello World, I am Python.\n")
            file.write("Sum = 5 + 5.\n")
            file.write("Bye, World.\n")
        print("File written successfully.")
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")

def read_file():
    try:
        # Open the file in read mode and display its content
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("\nReading file content:")
        print(content)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")

def append_to_file():
    try:
        # Open the file in append mode and append additional content
        with open('my_file.txt', 'a') as file:
            file.write("Hello, I am back.\n")
            file.write("Multiply = 10 * 6.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")

def main():
    try:
        # Write initial content to the file
        write_to_file()

        # Read and display the file content
        read_file()

        # Append more content to the file
        append_to_file()

        # Read and display the updated file content
        read_file()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File handling script completed.")

if __name__ == "__main__":
    main()
