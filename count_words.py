def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)



def main():
    """Main function to run the program."""
    print("Welcome to the Word Counter!")
    print("-----------------------------")

    text = input("Enter a sentence or a paragraph: ")
    word_count = count_words(text)

    print(f"The total number of words is: {word_count}")

if __name__ == "__main__":
    main()
