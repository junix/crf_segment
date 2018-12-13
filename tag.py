SOT = '<sot>'
EOT = '<eot>'

_tags = ('s', 'b', 'm', 'e', SOT, EOT)
_ix2tag = dict(enumerate(_tags))
_tag2ix = dict((tag, ix) for ix, tag in _ix2tag.items())


def tag_size():
    return len(_tags)


def tag2ix(tag):
    ix = _tag2ix.get(tag)
    if ix is None:
        raise ValueError(f'invalid tag:{tag}')
    return ix


def ix2tag(ix):
    tag = _ix2tag.get(ix)
    if tag is None:
        raise ValueError(f'invalid ix:{ix}')
    return tag
