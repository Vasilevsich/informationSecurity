import alphabet


class Cypher:

    def __init__(self, shift: int, keyword: str):
        self.alphabet = alphabet.RUSSIAN_ALPHABET
        self.shift = self.check_shift(shift)
        self.keyword = self.check_keyword(keyword)
        self.replacement_table = self.create_replacement_table()

    # Проверка значения сдвига на удовлетворение условий
    def check_shift(self, shift: int) -> int:
        if shift < 0 or shift > len(self.alphabet):
            raise Exception('Shift out of range')
        return shift

    # Проверка значения ключевого слова на удовлетворение условий
    def check_keyword(self, keyword: str) -> str:
        keyword_letter_list = list(keyword)
        keyword_letter_set = set(keyword)
        if len(keyword_letter_set) != len(keyword_letter_list):
            raise KeywordException('Keyword contains similar letters')
        for letter in keyword:
            if letter not in self.alphabet:
                raise KeywordException('Keyword contains incorrect symbols')
        return keyword

    # Создание таблицы подстановки
    def create_replacement_table(self):
        available_letters = list(self.alphabet)
        for letter in self.keyword:
            available_letters.remove(letter)

        value_list = list(self.keyword)
        value_list += available_letters
        value_list = value_list[-self.shift:] + value_list[:-self.shift]
        return dict(zip(self.alphabet, value_list))

    # Метод шифрования текста
    def encrypt_text(self, text: str) -> str:
        text.lower()
        result = ''
        for symbol in text:
            result += self.encrypt_symbol(symbol)
        return result

    # Метод шифрования символа
    def encrypt_symbol(self, symbol: str) -> str:
        if symbol in self.alphabet:
            return self.replacement_table[symbol]
        return symbol

    # Метод дешифрования текста
    def decrypt_text(self, text: str) -> str:
        text.lower()
        result = ''
        for symbol in text:
            result += self.decrypt_symbol(symbol)
        return result

    # Метод дешифрования символа
    def decrypt_symbol(self, symbol: str) -> str:
        if symbol in self.alphabet:
            for key, value in self.replacement_table.items():
                if value == symbol:
                    return key
        return symbol


class KeywordException(Exception):
    ...
