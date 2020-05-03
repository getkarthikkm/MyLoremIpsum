import unittest
import os
import sys


class LoremTestCase(unittest.TestCase):
    """
    A class to test the test cases of keyword search in lorem ipsum text
    """

    def test_match_keyword(self):
        """
        A method to test the match keyword method
        """
        sys.path.insert(0, "../")
        import search_word
        import input
        input_obj = input.ReadValidate()
        check_text = input_obj.read_input_text_file("unit_text_file.txt")
        word_obj = search_word.SearchWord()
        match_count = word_obj.match_keyword(check_text, "lorem")
        print "unit test match_count: ",match_count
        self.assertEqual(match_count, 9)

    def test_write_to_csv(self):
        """
        A method to test the write to csv method
        """
        sys.path.insert(0, "../")
        import search_word
        word_obj = search_word.SearchWord()
        word_obj.write_to_csv(9, 'lorem', "expected_key_count.csv")
        with open('key_count.csv', 'r') as actual, open('expected_key_count.csv', 'r') as expected:
            fileone = actual.readlines()
            filetwo = expected.readlines()
            print "fileone :", fileone
            print "filetwo :", filetwo
        self.assertListEqual(fileone, filetwo)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
