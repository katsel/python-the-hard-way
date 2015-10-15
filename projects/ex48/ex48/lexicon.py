lexicon_tuples = [('verb', 'eat'),
                  ('verb', 'go'),
                  ('verb', 'kill'),
                  ('direction', 'east'),
                  ('direction', 'north'),
                  ('direction', 'south'),
                  ('direction', 'west'),
                  ('noun', 'bear'),
                  ('noun', 'prince'),
                  ('noun', 'princess'),
                  ('stop', 'a'),
                  ('stop', 'an'),
                  ('stop', 'in'),
                  ('stop', 'of'),
                  ('stop', 'the'),
                  ]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def word_in_lexicon(word):
    # handle capitalization and case
    word = word.lower()
    result = [ltuple for ltuple in lexicon_tuples if word == ltuple[1]]
    return result

def scan(stuff):
    """Determines the type of a group of words"""
    # handle capitalization and case
    words = stuff.split()
    results = []

    for word in words:

        # is it a number?
        if convert_number(word):
            n = ('number', convert_number(word))
            results.append(n)
            continue
        
        # recognize type of words
        result = word_in_lexicon(word)

        if(result):
            results += result
        else:
            # error-handling
            results.append(('error', word))
        
    return results
