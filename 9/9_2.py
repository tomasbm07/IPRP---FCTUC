
def produto_escalar(v, w):
    if len(v) == 0:
        return 0
    return (v[0] * w[0]) + produto_escalar(v[1:], w[1:])


print(produto_escalar([1, 2, 3], [5, 6, 7]))
