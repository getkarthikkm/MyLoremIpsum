import os
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class ReadValidate(object):
    """
    A class to maintain read and validation methods for input
    """

    def read_input_text_file(self, text_file):
        """
        A method to read and validate the input text file path
        :param text_file: Path of the text file
        :return: text
        """
        try:
            assert os.path.exists(text_file)
            text_file = text_file
            fr = open(text_file, 'r')
            text = fr.read()
            fr.close()
            logging.debug("Text :" + text)
            return text.lower()

        except AssertionError:
            raise AssertionError("No file in this path : " + str(text_file))

    def validate_text(self, text):
        """
        Validate the number of lines in a text
        :param text: string
        :return: boolean
        """

        logging.debug("No of lines in the text: " + str(text.count("\n")+1))
        if text.count("\n") == 199:
            logging.info("Input Successfully Validated..")
            return True
        else:
            raise ValueError('Invalid Input: Input text not of 200 lines')

    def get_the_keyword(self):
        """
        Get the keyword from user
        :return: string
        """
        key_word = str(raw_input("Enter the keyword to search in text:"))
        return key_word