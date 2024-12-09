def skip(n):
    x = n
    while True:
        yield x
        x += n
def take(n, gen):
    result = []
    for i in gen:
        result.append(i)
        if len(result) == n:
            return result
def main():
    print(take(5, skip(2)))
main()



# Question 4

# a.

# We can use concurrent programming since each operation can work independently from one another. We can make each I/O operation run separately

# b.

# We can use concurrent programming again "fork-join" paradigm

# c.

# again, concurrent programming is prob. best, since we can use fork-join

# d.

# Async. programming is prob best since we need to handle many network connections

# 5. We could have infinite recursion since right now, once we know bar(A), then we can say that baz(A) and evaluate it. If we switch the ordering we may run into infinite recursion.

