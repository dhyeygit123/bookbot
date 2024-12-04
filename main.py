
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 0
            letter_counts[char] += 1
    return letter_counts

def generate_report(text):
    word_count = count_words(text)
    letter_counts = count_letters(text)
    
    # Convert to list of tuples and sort by count descending
    chars_sorted = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    report = f"--- Begin Report ---\n"
    report += f"Total Words: {word_count}\n"
    report += f"\nCharacter Counts:\n"
    
    for char, count in chars_sorted:
        report += f"The '{char}' character was found {count} times\n"
        
    report += "--- End Report ---"
    
    return report


def main():
    with open("books/dhyey.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))

if __name__ == "__main__":
    main()
