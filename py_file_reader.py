def main():
    tries = 4  # Number of allowed attempts

    while tries > 0:
        try:
            # Ask user to enter file path
            print("Enter your absolute file path")
            print(f"You have {tries} tries left")
            print("Example: D:/1-python/moaz.py")
            the_file_input = input("File name: =>  ").strip().strip('"')

            if the_file_input:
                # Check if file exists
                with open(the_file_input, "r") as f:
                    pass  

                # Ask if user wants to open the file
                print("File found. Want to open file? (yes, no)")
                check = input("write: ").lower().strip()

                if check in ("yes", "y"):
                    # Open file and read content
                    with open(the_file_input, "r") as the_file:
                        content = the_file.read()
                        print("\nFile content:\n")
                        print(content)
                    print("File is closed.\n")
                    break

                elif check in ("no", "n"):
                    print("Exiting without opening the file.")
                    break

                else:
                    print("Error: please write (yes or no)\n")

        except FileNotFoundError:
            # File not found error
            tries -= 1
            print(f"File not found. You have {tries} tries left.\n")

        except Exception as e:
            # Handle any other errors
            tries -= 1
            print(f"An error occurred: {e}\n")

    else:
        # show when all attempts are finished
        print("All tries finished. Try again later.")


if __name__ == "__main__":
    main()