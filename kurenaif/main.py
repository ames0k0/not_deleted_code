#/usr/bin/env python
# -*- coding: utf-8 -*-

# kurenaif <3
# IJ[K]LMNOPQRSTUVWXYZABCDEFGH
# ST[U]VWXYZABCDEFGHIJKLMNOPQR
# PQ[R]STUVWXYZABCDEFGHIJKLMNO
# CD[E]FGHIJKLMNOPQRSTUVWXYZAB
# LM[N]OPQRSTUVWXYZABCDEFGHIJK
# YZ[A]BCDEFGHIJKLMNOPQRSTUVWX
# GH[I]JKLMNOPQRSTUVWXYZABCDEF
# DE[F]GHIJKLMNOPQRSTUVWXYZABC


# TODO: (colored) animation ?


def find(seq, t):
    try:
        return seq.index(t)
    except ValueError:
        return -1


def main(seq: str, target: str, K: int):
    seq = list(seq)
    res = []

    def seq_p(t):
        a = ''.join(seq)
        a = a.replace(t, f'[{t}]')
        print(a)

    seq_p(seq[K])
    print('\n')

    for t in target:
        left_half = list(reversed(seq[:K]))
        right_half = seq[K:]

        t_pos = find(left_half, t)
        t_pos_r = find(right_half, t)

        if t_pos == t_pos_r:
            raise NotImplementedError(f"[{t}] is Not in the `seq`")

        if t_pos != -1:
            t_pos += 1
            res.append(t_pos)
            for _ in range(t_pos):
                seq.insert(0, seq.pop())
        else:
            res.append(t_pos_r)
            for _ in range(t_pos_r):
                seq.append(seq.pop(0))

        if seq[K] != t:
            raise ValueError(f"{seq[K]} != {t}")


        seq_p(t)

    print(' '.join([str(r) for r in res]))


if __name__ == '__main__':
    from string import ascii_uppercase

    K = 3
    seq = ascii_uppercase
    target = 'kurenaif'.upper()
    main(seq, target, K)

    exit()

    for K in range(len(seq)):
        print('\n')
        main(seq, target, K)
