def main():
    print("This program counts the number of letters in the phrase.")
    lettersToCount = input("Enter the letters to count in phrase: (e.g., 'aeoie')").lower()
    inputPhrase = input("Enter your phrase: ").lower()

    totalOccurrencesOfLettersToCount = 0
    for character in inputPhrase:
        if character in lettersToCount:
            totalOccurrencesOfLettersToCount = totalOccurrencesOfLettersToCount + 1
    
    print("Total occurrences '{}' in your phrase: {}".format(lettersToCount, totalOccurrencesOfLettersToCount))

if __name__ ==  "__main__":
   main()