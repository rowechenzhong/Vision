"""
Today, we will be explicitly enumerating the elements of the Weyl group of C3
"""

import numpy as np

SIMPLE = [
    np.array([0, 1, 1]),
    np.array([-1, -1, 0]),
    np.array([2, 0, 0]),
]


SIMPLE_REFLECTIONS = [np.identity(
    3) - 2 * np.outer(s, s) / np.dot(s, s) for s in SIMPLE]

WEYL_GROUP = [np.identity(3)]
WEYL_EXPANSION = [()]

DISC = 2 ** 16

WEYL_GROUP_SET = set([tuple(int(i) for i in w.reshape(9) * DISC + 0.5)
                     for w in WEYL_GROUP])  # for fast membership testing

i = 0
while i < len(WEYL_GROUP):
    for j, s in enumerate(SIMPLE_REFLECTIONS):
        test = np.matmul(s, WEYL_GROUP[i])
        test_tuple = tuple(int(i) for i in test.reshape(9) * DISC + 0.5)
        if test_tuple not in WEYL_GROUP_SET:
            WEYL_GROUP.append(test)
            WEYL_GROUP_SET.add(test_tuple)
            WEYL_EXPANSION.append(WEYL_EXPANSION[i] + (j,))
    i += 1

for s in WEYL_EXPANSION:
    res = " ".join(["\sigma_"+str(i+1) for i in s])
    print("&" + res + "\\\\")

print("The Weyl group of C3 has cardinality " + str(len(WEYL_GROUP)) + ".")
