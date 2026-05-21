from itertools import product


def ok(seq):
    k = len(seq)
    if k < 3:
        return False
    for i in range(k):
        if len({seq[i], seq[(i + 1) % k], seq[(i + 2) % k]}) == 3:
            return False
    return True


def best_perm(freq):
    elems = []
    for v in sorted(freq):
        elems.extend([v] * freq[v])
    n = len(elems)
    seq = [0] * n
    ctr = dict(freq)
    ans = [0]

    def dfs(dep):
        if dep == n:
            if ok(tuple(seq)):
                ans[0] = n
            return
        vals = sorted(x for x in ctr if ctr[x] > 0)
        for v in vals:
            ctr[v] -= 1
            seq[dep] = v
            dfs(dep + 1)
            ctr[v] += 1

    dfs(0)
    return ans[0]


def brute_max(freq_list):
    best = 0
    dims = [range(c + 1) for c in freq_list]
    for take in product(*dims):
        if sum(take) < 3:
            continue
        f = {idx + 1: take[idx] for idx in range(len(take)) if take[idx] > 0}
        best = max(best, best_perm(f))
    return best


def guess(S, nz_desc):
    

    nz_desc = nz_desc
    
    nz = nz_desc
    
    mx = nz[0] if nz else 0
    
    return max(nz)



if __name__ == "__main__":
    # brute all vectors n=4 sums<=11 entries 1..8 (excluding zeros?)
    mism = []

    for n in range(1, 7):
        

        stacks = []

    # manual scan for n fixed length brute small caps

        

PY
