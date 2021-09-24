import codecs

from labFirst import sourceText
from labFirst.cryptanalyses import Cryptanalyses
from labFirst.cypher import Cypher


def first_lab():
    # Открытие файла с текстом и преобразование текста для работы с ним
    file = codecs.open('text.txt', 'r', 'utf_8_sig')
    text = file.read().lower()
    text = text.replace('ё', 'е')
    # Создание объекта класса cypher со сдвигом 3 и ключевым словом "шифровка"
    cypher = Cypher(3, 'шифровка')
    # Создание объекта класса SourceText, в конструктор которого передан исходный текст
    source = sourceText.SourceText(text)
    # Шифрование исходного текста при помощи метода encrypt_text класса cypher
    encrypted_text = cypher.encrypt_text(text)
    # Создание объекта класса cryptanalyses, в конструктор передается объект класса SourceText и зашифрованыый текст
    cryptanalyses = Cryptanalyses(source, encrypted_text)
    # Расшифровка зашифрованного текста
    print(cryptanalyses.decode_text_with_bigrams())

    file.close()


first_lab()
