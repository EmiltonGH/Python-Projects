def text_analysis():
    print("Welcome to the text analysis program")

    text = input("Enter a string for analysis: ")

    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] = 1

    print("Character frequency analysis:")
    for char, count in frequency.items():
        print(f"{char}: {count}")

text_analysis()