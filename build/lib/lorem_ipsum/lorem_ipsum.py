from search_word import SearchWord
from model import MatchWord
from input import ReadValidate
import logging


logging.basicConfig(format='%(message)s', level=logging.DEBUG)

__version__ = '0.0.1'
__author__ = 'Karthik KM'


def main():
    try:
        input_text_file = str(raw_input("Enter the text file path :"))

        # Create a ReadValidate class object
        input_obj = ReadValidate()

        # Get the keyword from user
        keyword = input_obj.get_the_keyword()

        # Read input from the text file
        check_text = input_obj.read_input_text_file(input_text_file)

        # Validate the number of lines in the text
        input_obj.validate_text(check_text)

        match_obj = MatchWord(full_text=check_text, key_word=keyword)

        # Create a SearchWord class object
        word_obj = SearchWord()

        # Get the count of matches of keyword in the text
        match_count = word_obj.match_keyword(match_obj.full_text, match_obj.key_word)
        logging.debug("The count of keyword matches :{}".format(match_count))

        # Write to a CSV file
        word_obj.write_to_csv(match_count, match_obj.key_word, "key_count.csv")

    except AssertionError as e:
        logging.debug("Error :{}".format(e))
    except ValueError as e:
        logging.debug("Error :{}".format(e))
    except Exception as e:
        logging.debug("Other Exception :{}".format(e))


if __name__ == "__main__":
    main()


