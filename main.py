def create_and_write_file():
  """Creates a new text file and writes content to it."""
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line.\n")
      file.write("Here are some numbers: 10, 20, 30\n")
      file.write("This is the last line for now.\n")
    print("Successfully created and wrote to my_file.txt")
  except PermissionError:
    print("Error: You lack permission to create the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def read_and_display_file():
  """Reads the contents of the file and displays them."""
  try:
    with open("my_file.txt", "r") as file:
      content = file.read()
      print("Contents of my_file.txt:")
      print(content)
  except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
  except Exception as e:
    print(f"An unexpected error occurred while reading: {e}")

def append_to_file():
  """Opens the file in append mode and writes additional content."""
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending new lines:\n")
      file.write("Line 4: This is some additional text.\n")
      file.write("Line 5: You can add more information here.\n")
      file.write("Line 6: The possibilities are endless!\n")
    print("Successfully appended content to my_file.txt")
  except PermissionError:
    print("Error: You lack permission to modify the file.")
  except Exception as e:
    print(f"An unexpected error occurred while appending: {e}")

if __name__ == "__main__":
  create_and_write_file()
  read_and_display_file()
  append_to_file()
  read_and_display_file()  # Read again to see the appended content
