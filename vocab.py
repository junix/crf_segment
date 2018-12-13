SOS = '<sos>'
EOS = '<eos>'
OOV = '<oov>'


def _reverse_dict(kv):
    rkv = dict((v, k) for k, v in kv.items())
    assert len(kv) == len(rkv), "dict contain some duplicate values"
    return rkv


class Vocab:
    SOS_IX, EOS_IX, OOV_IX = range(3)

    def __init__(self, char_seq):
        self._ch2ix = {SOS: Vocab.SOS_IX, EOS: Vocab.EOS_IX, OOV: Vocab.OOV_IX}
        for c in char_seq:
            if c not in self._ch2ix:
                self._ch2ix[c] = len(self._ch2ix)
        self._ix2ch = _reverse_dict(self._ch2ix)

    def __len__(self) -> int:
        return len(self._ch2ix)

    def __getitem__(self, ix_or_ch):
        if isinstance(ix_or_ch, int):
            return self._ix2ch[ix_or_ch]

        if isinstance(ix_or_ch, str):
            return self._ch2ix.get(ix_or_ch, Vocab.OOV_IX)

        raise TypeError(f'un-support item:{ix_or_ch}')

    def to_ixs(self, sentence):
        return tuple(self[c] for c in sentence)

    def to_chs(self, indices):
        return ''.join(self[ix] for ix in indices)
