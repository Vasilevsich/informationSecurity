from labFirst import alphabet
import statistics


class SourceText:
    def __init__(self, text: str):
        self.input_text = text.lower()
        self.alphabet = alphabet.RUSSIAN_ALPHABET
        self.reference_monogram_frequency = alphabet.RUSSIAN_LETTERS_FREQUENCY
        self.source_monogram_frequency = statistics.calculate_letters_frequency(self.input_text, self.alphabet)
        self.source_bigram_frequency = statistics.calculate_bigram_frequency(self.input_text, self.alphabet)
