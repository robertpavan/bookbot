def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_character_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def remove_non_alpha_chars(char_dict):
    return {char: count for char, count in char_dict.items() if char.isalpha()}

def sort_chars_by_count(char_dict):
    sorted_list = sorted(
        [{'character': char, 'count': count} for char, count in char_dict.items()],
        key=lambda x: x['count'],
        reverse=True
    )
    return sorted_list

def generate_report(filename, word_count, sorted_alpha_char_count):
    report = []
    report.append(f"--- Begin report of {filename} ---")
    report.append(f"{word_count} words found in the document")

    for item in sorted_alpha_char_count:
        char = item['character']
        count = item['count']
        report.append(f"The '{char}' character was found {count} times")
    return "\n".join(report)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    alpha_dict = remove_non_alpha_chars(character_count)
    sorted_alpha_char_count = sort_chars_by_count(alpha_dict)
    report = generate_report(book_path, word_count, sorted_alpha_char_count)
    print(report)
main()