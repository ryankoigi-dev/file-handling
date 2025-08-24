def process_file():
    filename = input("📂 Enter the filename you want to read: ")

    try:
        # Step 1: Read file
        with open(filename, "r") as f:
            content = f.read()
            print("\n Original file content:\n")
            print(content)

        # Step 2: Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 3: Create a new filename
        output_file = "modified_" + filename

        # Step 4: Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"\n Modified file has been saved as '{output_file}'.")

    except FileNotFoundError:
        print(f" Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f" Error: You don’t have permission to access '{filename}'.")
    except Exception as e:
        print(f" Unexpected error: {e}")


if __name__ == "__main__":
    process_file()
