import string

INPUT_FILE = "input.txt"
CLEANED_FILE = "cleaned.txt"


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    return text


def write_cleaned_text():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    cleaned = clean_text(text)

    with open(CLEANED_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned)

    return cleaned


def count_word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def print_top_words(freq: dict[str, int], top_n: int = 10) -> None:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    print(f"Top {top_n} words:")
    for word, count in sorted_items[:top_n]:
        print(f"{word}: {count}")


def main():
    cleaned = write_cleaned_text()
    frequencies = count_word_frequency(cleaned)
    print_top_words(frequencies, top_n=10)


if __name__ == "__main__":
    main()
