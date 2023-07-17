def count_characters(paragraph):
    """Counts the number of characters in a paragraph."""
    return len(paragraph.replace(" ", ""))

def main():
    """Main function to run the program."""
    print("Welcome to the Character Counter!")
    print("--------------------------------")

    paragraph = input("Enter a paragraph: ")
    character_count = count_characters(paragraph)

    print(f"The total number of characters (excluding spaces) is: {character_count}")

if __name__ == "__main__":
    main()
