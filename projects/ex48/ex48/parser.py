class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('','') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

# note: word_list refers to word tuples of the form ('type', 'word')!
def peek(word_list):
    """Returns the type of the first word in a list"""
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """Returns a word tuple if it matches the expected type"""
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """Skips the first word in the list if it matches the given type"""
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """Parses the next word as a verb, omitting stopwords"""
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """Parses the next word as an object, omitting stopwords"""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    """Parses the next word as a subject, omitting stopwords.
    If no noun is given and a verb follows, use 'player'."""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a noun or verb next.")

def parse_sentence(word_list):
    """Parse a word list as a sentence and return a Sentence object"""
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
