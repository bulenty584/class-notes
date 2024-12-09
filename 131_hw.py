def generator(array):
 for i in range(array):
  val = array[i]
  while val:
   yield cur.value
   cur = cur.next



class Iterator:
 def __init__(self, data):
  self.data = data
  self.index = 0
  self.current_node = None

 def __next__(self):
  while self.index < len(self.data):
   if not self.current_node:
    self.current_node = self.data[self.index]
    self.index += 1
   if self.current_node:
    val = self.current_node.value
    self.current_node = self.current_node.next
    return val
  
  raise StopIteration
    
  
class Node:
 def __init__(self, val):
   self.value = val
   self.next = None

class HashTable:
 def __init__(self, buckets):
   self.array = [None] * buckets
   self.buckets = buckets
   self.current_index = 0
   self.current_node = None
   self.iterator = None

 def __iter__(self):
     self.iterator = Iterator(self.array)
     return self.iterator

 def forEach(self, l):
  iterator = self.__iter__()

  try:
   while True:
    val = iterator.__next__()
    l(val)
  except StopIteration:
   pass

 def insert(self, val):
   bucket = hash(val) % len(self.array)
   tmp_head = Node(val)
   tmp_head.next = self.array[bucket]
   self.array[bucket] = tmp_head

if __name__ == "__main__":
    # Initialize a hash table with 5 buckets
    hash_table = HashTable(buckets=5)

    # Insert some values into the hash table
    values = [10, 15, 20, 25, 30]
    for value in values:
        hash_table.insert(value)

    for i in hash_table:
        print(i)

    hash_table.forEach(lambda x : print(2*x))
        
