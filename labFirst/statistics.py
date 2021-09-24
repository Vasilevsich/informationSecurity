# Вычисляет вероятность появления букв в тексте
def calculate_letters_frequency(text: str, alphabet: dict) -> dict:
    letter_frequencies = dict.fromkeys(alphabet, 0)
    for symbol in text:
        if symbol in alphabet:
            letter_frequencies[symbol] += 1
    for letter in letter_frequencies.keys():
        letter_frequencies[letter] /= len(text)
    letter_frequencies = sort_dict_by_value(letter_frequencies)
    return letter_frequencies


# Вычисляет вероятность появления биграмм в тексте
def calculate_bigram_frequency(text: str, alphabet: dict) -> dict:
    bigram_frequencies = {}
    bigram_count = 0
    for i in range(len(text) - 1):
        if text[i] in alphabet and text[i + 1] in alphabet:
            if bigram_frequencies.get(text[i] + text[i + 1]) is None:
                bigram_frequencies[text[i] + text[i + 1]] = 1
            else:
                bigram_frequencies[text[i] + text[i + 1]] += 1
            bigram_count += 1
    for bigram in bigram_frequencies.keys():
        bigram_frequencies[bigram] /= bigram_count
    bigram_frequencies = sort_dict_by_value(bigram_frequencies)
    return bigram_frequencies


# Сортировка словаря по значению
def sort_dict_by_value(dictionary: dict) -> dict:
    sorted_dict = {}
    freq_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for key, value in freq_dict:
        sorted_dict[key] = value
    return sorted_dict
