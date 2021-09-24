import unittest
import codecs

from labFirst import cryptanalyses, cypher, sourceText


class CypherTest(unittest.TestCase):
    def setUp(self):
        self.cypher = cypher.Cypher(3, 'шифровка')

    def test_keyword_similar_letters_exception(self):
        with self.assertRaises(cypher.KeywordException) as context:
            self.cypher.check_keyword('бб')
        self.assertTrue('Keyword contains similar letters' in str(context.exception))

    def test_incorrect_symbols_keyword(self):
        with self.assertRaises(cypher.KeywordException) as context:
            self.cypher.check_keyword('a')
        self.assertTrue('Keyword contains incorrect symbols' in str(context.exception))

    def test_text_encryption(self):
        self.assertEqual('дфжлмд', self.cypher.encrypt_text('нептун'))

    def test_text_decryption(self):
        self.assertEqual('нептун', self.cypher.decrypt_text('дфжлмд'))

    def test_war_and_peace(self):
        self.cypher.create_replacement_table()
        file = codecs.open('text.txt', 'r', 'utf_8_sig')
        text = file.read()
        print('----')
        print(text)
        print('----')
        print(self.cypher.encrypt_text(text))
        print('----')
        print(self.cypher.decrypt_text(self.cypher.encrypt_text(text)))
        file.close()

    def test_decoding(self):

        file = codecs.open('text.txt', 'r', 'utf_8_sig')
        text = file.read().lower()
        text = text.replace('ё', 'е')

        source = sourceText.SourceText(text)
        encrypted_text = self.cypher.encrypt_text(text)

        self.cryptanalyses = cryptanalyses.Cryptanalyses(source, encrypted_text)

        print(self.cryptanalyses.decode_text_with_bigrams())

        file.close()


if __name__ == '__main__':
    unittest.main()
