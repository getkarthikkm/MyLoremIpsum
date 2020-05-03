import logging


logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class SearchWord(object):
    """
    A method to get the occurrence of a keyword in Lorem Ipsum text
    """

    def match_keyword(self, check_text, key_word):
        """
        A method to get the count of matches of keyword in a text
        :param check_text: string
        :param key_word: string
        :return: list
        """

        match_count = 0
        index = 0
        while True:
            index = check_text.find(key_word, index)

            if index == -1: return match_count if match_count == 0 else match_count - 1
            match_count += 1
            index += 1

    def write_to_csv(self, match_count, key_word, output_csv):
        """
        A method to write matches to CSV
        :param match_count: number of matches found
        :param key_word: keyword string
        :param output_csv: output csv file
        :return: None
        """
        with open(output_csv, "w") as csv_file:
            for _ in range(match_count):
                csv_file.write(key_word)
                csv_file.write('\n')
        logging.debug("Successfully generated output file {}".format(output_csv))
        csv_file.close()







