import os
import numpy as np


# chars = ["😠", "🤢", "😀", "😨", "😞", "😱"]
chars = ["a", "b", "c", "d", "e", "f"]
n_lists = 12
task_len = 20

def count_nback(a,n):
    """
    count how many n-back matches in array a.
    """
    if n == 0: return 5 # a hack for the sampler
    c = 0
    for i, x in enumerate(a):
        if i < n:
            continue
        if x == a[i-n]:
            c += 1
    return c
    # return sum(1 for i, x in enumerate(a) if (i > n) and (x == a[i-n]))

tasks = []
for l in range(n_lists):
    name = f"trial{l:02d}.csv"
    n = l%4
    if n == 0:
        k = np.random.choice(chars)
        a = np.append(np.random.choice([i for i in chars if i != k], 15), [k] * 5)
        np.random.shuffle(a)
        tg = [1 if x==k else -1 for x in a]
    else:
        k = 0
        a = np.random.choice(chars, 20)
        while count_nback(a, n) != 5: # Rejection sampling because it's a small problem ;)
            a = np.random.choice(chars, 20)
            # print(count_nback(a, n))
        # NOTE: rejection sampling is with replacement, so a trial can be repeated in two lists.
        tg = np.concatenate(([0]*(n), a[:-n]))  # Mask first n chars
        tg = (((tg == a).astype(np.int) - 1) * 2) + 1  # Compare the reset and relabel (-1, 1)
        tg[:n] = [0]*(n)  # Mask again
    tasks.append([n,k,name])
    outf = f"para/lists/trials/{name}"
    with open(outf, "w") as fp:
        fp.write("x,tg\n") # Header
        fp.writelines([f"{x},{t}\n" for x, t in zip(a, tg)]) # Data
with open(f"para/lists/tasks.csv", "w") as fp:
    fp.write("n,k,trial_list\n")
    fp.writelines([f"{a},{k},{name}\n" for a, k, name in tasks])

    
