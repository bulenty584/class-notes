def skip(n):
    x = n
    while True:
        yield x
        x += n


class AlphabetIterator:

    def __init__(self):
        self.current_letter = chr(96)

    def __iter__(self):
        return self

    def __next__(self):
        if ord(self.current_letter) >= 96 and ord(self.current_letter) <= 122:
            self.current_letter = chr(ord(self.current_letter) + 1)
            return self.current_letter
        else:
            raise StopIteration


def interleave_iter(iter1, iter2):
    while True:
        try:
            yield next(iter1)
        except StopIteration:
            iter1 = None  # Mark iter1 as exhausted
        try:
            yield next(iter2)
        except StopIteration:
            iter2 = None  # Mark iter2 as exhausted
        
        if iter1 is None and iter2 is None:
            break  # Both iterators are exhausted

# Example usage:
print(list(interleave_iter(iter([1, 2, 3]), iter([4, 5, 6]))))
# Output: [1, 4, 2, 5, 3, 6]

print(list(interleave_iter(iter([2, 2]), iter([4, 4, 4, 4]))))
# Output: [2, 4, 2, 4, 4, 4]


4.

a. We can have these print calls in the background, using concurrent programming (I/O operation!)

b. Concurrent programming since we can do parallel execution of these subproblems

c. 






