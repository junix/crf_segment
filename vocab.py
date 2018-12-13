SOS = '<sos>'
EOS = '<eos>'
OOV = '<oov>'


def _reverse_dict(kv):
    return dict((v, k) for k, v in kv.items())


class Vocab:
    def __init__(self, char_set):
        self.ch2ix = {SOS: 0, EOS: 1, OOV: 2}
        self.ix2ch = {}
        for c in char_set:
            if c not in self.ch2ix:
                self.ch2ix[c] = len(self.ch2ix)
        self.ix2ch = _reverse_dict(self.ch2ix)

    def __len__(self) -> int:
        return len(self.ch2ix)

    def __getitem__(self, ix_or_ch):
        if isinstance(ix_or_ch, int):
            return self.ix2ch[ix_or_ch]

        if isinstance(ix_or_ch, str):
            return self.ch2ix[ix_or_ch]

        raise TypeError(f'un-support item:{ix_or_ch}')
