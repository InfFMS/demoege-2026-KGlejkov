#НОмер 16
stack.append(args)
                cache[args] = f(*args)
                stack.pop()
def G(n):
    if n<10:
        return 2*n
    if n>=10:
        return G(n-2)+1
def F(n):
    return 2*(G(n-3)+8)
print(F(15548))
