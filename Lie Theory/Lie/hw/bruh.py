import itertools

import numpy as np

monomials = []
rank = []
for a in range(3**6):
    digits = [a // 3**i % 3 for i in range(6)]

    if sum(digits[:3]) <= 2 and sum(digits[3:]) <= 2:
        # turn digits into a 6-tuple
        monomials.append(tuple(digits))
        rank.append([sum(digits[:3]), sum(digits[3:])])

print(len(monomials))

monomial_to_idx = {m: i for i, m in enumerate(monomials)}

rank_to_idx = [[[] for _ in range(3)] for _ in range(3)]
for i, r in enumerate(rank):
    rank_to_idx[r[0]][r[1]].append(i)

# print num monomials of each rank
for deg_x in range(3):
    for deg_y in range(3):
        print(deg_x, deg_y, len(rank_to_idx[deg_x][deg_y]))


multiplication_table = [
    [0 for _ in range(len(monomials))] for _ in range(len(monomials))]

for i, m in enumerate(monomials):
    for j, n in enumerate(monomials):
        res = tuple(m[k] + n[k] for k in range(6))
        if res in monomial_to_idx:
            multiplication_table[i][j] = monomial_to_idx[res]
        else:
            multiplication_table[i][j] = -1


def multiply(m, n):
    # m and n are both lists of coefficients for each monomial.
    res = [0 for _ in range(len(monomials))]
    for i in range(len(monomials)):
        if m[i] == 0:
            continue
        for j in range(len(monomials)):
            if n[j] == 0:
                continue
            k = multiplication_table[i][j]
            if k != -1:
                res[k] += m[i] * n[j]
    return res


# permutations of 3 elements
permutations = list(itertools.permutations(range(3)))


def symmetrize(a):
    # a is some index in monomials
    m = monomials[a]
    res = [0 for _ in range(len(monomials))]
    for p in permutations:
        res[monomial_to_idx[tuple(m[3 * (i // 3) + p[i % 3]]
                                  for i in range(6))]] += 1
    return res


def str_polynomial(a):
    res = ""
    for i, m in enumerate(monomials):
        if a[i] != 0:
            res += f"{a[i]}*x^{''.join(map(str,m[:3]))}*y^{''.join(map(str,m[3:]))} + "
    res = res[:-3]
    return res


symmetrized_rank_to_idx = [[set() for _ in range(3)] for _ in range(3)]
for deg_x in range(3):
    for deg_y in range(3):
        for a in rank_to_idx[deg_x][deg_y]:
            res = symmetrize(a)
            print(monomials[a], " -> ", str_polynomial(res))
            symmetrized_rank_to_idx[deg_x][deg_y].add(
                tuple(res)
            )

# print num symmetric monomials
for deg_x in range(3):
    for deg_y in range(3):
        print(deg_x, deg_y, len(symmetrized_rank_to_idx[deg_x][deg_y]))

products = set()

# acceptable pairs. We are specifically trying to create (2,2).
for deg_x in range(3):
    for deg_y in range(3):
        if deg_x == deg_y == 2 or deg_x == deg_y == 0:
            continue
        for a in rank_to_idx[deg_x][deg_y]:
            for b in rank_to_idx[2 - deg_x][2 - deg_y]:
                products.add(tuple(
                    multiply(symmetrize(a), symmetrize(b)))
                )

desired = symmetrize(monomial_to_idx[(2, 0, 0, 2, 0, 0)])
print("Desired: ", str_polynomial(desired))

# place all products in a matrix and find its rank.
matrix = list(products)
matrix = np.array(matrix)
print(np.linalg.matrix_rank(matrix))

# solve the equation matrix * x = desired
x = np.linalg.solve(matrix, desired)
print(x)
