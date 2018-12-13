from itertools import chain, islice
from collections import Counter

_training_data = "/Users/junix/nlp/icwb2-data/training/msr_training.utf8"


def tagging_token(token):
    token_len = len(token)
    if token_len == 0:
        return ''

    if token_len == 1:
        return 's'

    return f'b{"m" * (token_len - 2)}e'


def tagging_sentence(sentence):
    sentence = sentence.strip('\r\n')
    tokens = sentence.split(' ')
    return ''.join(tokens), \
           ''.join(tagging_token(t) for t in tokens)


def load_corpus():
    with open(_training_data, encoding='utf-8') as f:
        for line in f:
            yield tagging_sentence(line)


def load_charset(training_set, min_freq=2):
    def _char_seq():
        for sentence, _tag in training_set:
            yield from sentence

    return set(
        ch for ch, freq in Counter(_char_seq()).items()
        if freq >= min_freq
    )
