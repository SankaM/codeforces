from itertools import product


def ok(seq):
    k = len(seq)
    if k < 3:
        return False
    for i in range(k):
        if len({seq[i], seq[(i + 1) % k], seq[(i + 2) % k]}) == 3:
            return False
    return True


def best_perm_for_multiset(freq):

    elems = []
    for v in sorted(freq):
        elems.extend([v] * freq[v])

    n = len(elems)
    seq = [0] * n
    ctr = dict(freq)

    best = [0]

    def dfs(dep):
        if dep == n:
            if ok(tuple(seq)):
                best[0] = n
            return
        vals = sorted(x for x in ctr if ctr[x] > 0)
        for v in vals:
            ctr[v] -= 1
            seq[dep] = v
            dfs(dep + 1)
            ctr[v] += 1

    dfs(0)
    return best[0]


def brute_max(freq_list):

    best = 0
    dims = [range(c + 1) for c in freq_list]

    for take in product(*dims):
        if sum(take) < 3:
            continue
        f = {idx + 1: take[idx] for idx in range(len(take)) if take[idx] > 0}
        best = max(best, best_perm_for_multiset(f))

    return best


def fmt(freq_list):
    return brute_max(freq_list)


cases = {
    tuple([1, 1, 1, 3]): 4,
    tuple([2, 3, 4]): 9,
    tuple([1, 1, 1, 1, 3, 4]): 8,
    tuple([10**9, 10**9, 10**9]): 3 * 10**9,
}


if __name__ == '__main__':
    tiny = [(k, v) for k, v in cases.items() if sum(k) <= 12]

    for fl, expected in tiny:
        got = brute_max(list(fl))
        print(fl, got, expected, 'OK' if got == expected else 'DIFF')
