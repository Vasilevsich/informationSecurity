import sourceText
import statistics


class Cryptanalyses:

    def __init__(self, source_text: sourceText.SourceText, encrypted_text: str):
        self.source_text = source_text
        self.encrypted_text = encrypted_text

        self.calculated_monograms_frequencies = \
            statistics.sort_dict_by_value(
                statistics.calculate_letters_frequency(self.encrypted_text, self.source_text.alphabet))

        self.calculated_bigrams_frequencies = \
            statistics.sort_dict_by_value(
                statistics.calculate_bigram_frequency(self.encrypted_text, self.source_text.alphabet))

        self.bigram_lookup_table = self.create_bigram_prediction()

        self.letter_prediction = self.create_monogram_prediction()

    # Создание таблицы подстановки для монограмм
    def create_monogram_prediction(self) -> dict:
        encrypted_letters = list(self.calculated_monograms_frequencies.keys())
        result_letters = list(self.source_text.reference_monogram_frequency.keys())
        return {encrypted_letters[i]: result_letters[i] for i in range(len(self.source_text.alphabet))}

    # Метод дешифрования при помощи подстановки монограмм
    def decode_text_with_monograms(self, lookup_table: dict) -> str:
        output = ''
        for symbol in self.encrypted_text:
            if symbol in self.source_text.alphabet:
                output += lookup_table[symbol]
            else:
                output += symbol
        return output

    # Создание таблицы подстановки для биграмм
    def create_bigram_prediction(self) -> dict:
        encrypted_bigrams = list(self.calculated_bigrams_frequencies.keys())
        result_bigrams = list(self.source_text.source_bigram_frequency.keys())
        return {encrypted_bigrams[i]: result_bigrams[i]
                for i in range(len(self.calculated_bigrams_frequencies.keys()))}

    # Метод дешифрования текста при помощи подстановки монограмм и биграмм
    def decode_text_with_bigrams(self) -> str:
        output = ''
        i = 0
        while i < len(self.encrypted_text) - 1:
            if self.encrypted_text[i] + self.encrypted_text[i+1] in self.calculated_bigrams_frequencies.keys():
                output += self.bigram_lookup_table[self.encrypted_text[i] + self.encrypted_text[i+1]]
                i += 1
            else:
                if self.encrypted_text[i] in self.source_text.alphabet:
                    output += self.letter_prediction[self.encrypted_text[i]]
                else:
                    output += self.encrypted_text[i]
            i += 1
        return output
