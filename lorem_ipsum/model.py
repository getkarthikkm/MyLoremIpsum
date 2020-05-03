class MatchWord(object):
    """
    A class to store the full text and the keyword to Match
    """
    def __init__(self, **args):
        self.full_text = args.get('full_text')
        self.key_word = args.get('key_word')
