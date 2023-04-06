def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

if __name__ == "__main__":
    for n in range(0, 15, 2):
        print("input number: {0:d}".format(n))
        print("answer: {0:d}\n".format(fact(n)))
