from nose.tools import *
from ex48.parser import *

def test_exceptions():
    assert_raises(ParserError, parse_verb, ('noun', 'princess'))
    assert_raises(ParserError, parse_object, ('verb', 'go'))
    assert_raises(ParserError, parse_subject, ('direction', 'east'))

def test_peek():
    assert_equal(peek([('noun', 'princess'), ('verb', 'go')]), 'noun')
    assert_equal(peek([]), None)

def test_match():
    assert_equal(match([('noun', 'princess'), ('verb', 'go')], 'noun'),
                        ('noun', 'princess'))
    assert_equal(match([('noun', 'princess'), ('verb', 'go')], 'verb'), None)

def test_skip():
    wordlist = [('noun', 'princess'), ('verb', 'go')]
    skip(wordlist, 'noun')
    assert_equal(wordlist, [('verb', 'go')])

def test_pverb():
    assert_equal(parse_verb([('stop', 'the'), ('verb', 'go')]), ('verb', 'go'))

def test_pobject():
    assert_equal(parse_object([('stop', 'the'), ('direction', 'south')]),
                 ('direction', 'south'))
    assert_equal(parse_object([('stop', 'the'), ('noun', 'princess')]),
                 ('noun', 'princess'))

def test_psubject():
    assert_equal(parse_subject([('stop', 'the'), ('noun', 'prince')]),
                 ('noun', 'prince'))
    assert_equal(parse_subject([('verb', 'go'), ("stop", "to")]),
                 ('noun', 'player'))

def test_psentence():
    wordlist = [('stop', 'the'), ('noun', 'prince'), ('verb', 'go'),
                ('direction', 'south')]
    sentence = parse_sentence(wordlist)
    assert_equal(sentence.subject,'prince')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.obj, 'south')
