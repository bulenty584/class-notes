# Midterm Prep

## Functional Programming (Haskell)

All variables in haskell have types that are fixed at compile time
  - Best practice to include types
  
We can convert any operator to a prefix operator by adding parentheses around it. (6-5 == (-) 6 5)

**Function calls in Haskell are associative**: We capture the closest parameters to the function

### If Statements

syntax: if <expr> then <expr> else <expr>

**We need to have an else clause since this is an expression. We must return a value!! Every case must be covered**

### Guards

Guards are like a bunch of if-else statements:

```
-- exam.hs
evaluateExam :: Int -> String -> String
evaluateExam    score  prof
  | score < 50 && prof == "Eggert" = 
    "Given the curve, you got a B+."
  | score < 50 = 
    "You got an F."
  | score == 100 = 
     impress prof
  | otherwise = 
     "You passed."


impress :: String -> String
impress prof = prof ++ " is impressed!"

```

**Outputs:**

ghci> :load exam
Ok, one module loaded.
ghci> evaluateExam 30 "Eggert"
"Given the curve, you got a B+"
ghci> evaluateExam 30 "Nachenberg"
"You got an F."
ghci> evaluateExam 100 "Eggert"
"Eggert is impressed!"


**Factorial**

```
fact :: Int -> Int
fact n 
  | n == 0    = 1
  | otherwise = n * fact (n - 1)
```

## Local Bindings

*let* expression allows us to define one or more bindings to local variables.

*where* expression allows us to define variables after statements

**let vs. where**:

Use let when defining a variable for a single expression and use where when defining multiple expressions

You can also define nested functions!!

**Nested functions also have access to all of the functions variables as well**

## Composite Data Types

*Tuple* is a **fixed-size** collection of values that can be of any type

*List* is a sequence of values, **EACH VALUE MUST BE OF THE SAME TYPE**

### Tuples

**Example function signatures**:

```
-- tuples.hs

-- Halves the value or neg halves it
halveOrNegate :: (Double, String) -> Double
halveOrNegate    t =
    if snd t == "neg"
    then fst t * (-1.0)
    else fst t / 2.0

-- Performs safe division
safeDivide :: Int -> Int -> (Bool, Int)
safeDivide    num    denom
  | denom /= 0 = (True, quotient)
  | otherwise  = (False, 0)
  where
    quotient = num `div` denom

```

**Note that fst and second only work on tuples of length 2! To retrieve values from larger tuples, you’ll need to use something called pattern matching, which is a beautiful feature of Haskell that we will get into soon.**


**Some things to Note**
    In halveOrNegate, we must use parenthese to surround negative numbers as in (-1.0).
    To divide Ints, as in safeDivide, you use `div`. You can also use the prefix version of div by removing the backticks as in div 20 5. The / operator only works for floating point values.
    We use /= for not equals!
    The local binding quotient is only evaluated in the case when it is needed i.e. when denom is not equal to 0. This is a result of Haskell’s lazy semantics! It comes in handy often in situations like these because it prevents a divide by zero error.
    We can use a tuple to return multiple values from a function.
    
### Lists

**Not arrays**! They have O(N) access and no predefined size

**The most commonly used list functions are head and tail; head returns the first item of the list, and tail returns a list of the rest of the items!**

Some other useful list functions:

1. null [] => returns if list is empty
2. length primes => returns length of list
3. take 3 primes => returns first three elements of a list
4. drop 4 primes => returns all elements except first 4
5. !! => gives you random access by index
6. elem "Chef" jobs => tells you if item is in list
7. sum lst and prod lst => calculates sum and product of a list
8. or lst + and lst => performs a boolean or + and over the list
9. zip creates tuples out of two lists ~ python's zip

**Like the name may imply, Haskell lists are implemented as singly-linked lists. List operations are implemented recursively! This has performance impacts, since there is no linear random access!**

```
-- example.hs
-- All #s between 1 and 10, inclusive
one_to_ten = [1..10]

-- Odd #s between 1 and 10
oddities = [1,3..10]

-- An infinite list from 42 onward!
whole_lotta_numbers = [42..]

-- An infinite cycle of 1,3,5,1,3,5,…
tricycle = cycle [1,3,5]

```

Haskell is lazily loaded, so when a list is initially declared, none of it is initialized until you need it!!


**++ and : operators are used to concatenate elements and lists to create new lists**

```ghci> strange = ["stalking", "llamas"]
ghci> strange ++ ["in, "pajamas]
["stalking", "llamas", "in, "pajamas]

ghci> "stealthily" : strange
["stealthily", "stalking", "llamas"]

ghci> "dogs" : []
["dogs"]

ghci> "barking" : "dogs" : []
["barking", "dogs"]
```

**++ takes two lists of the same type and concenates them together**

**Cons operator : takes a value and prepends it to the beginning of a list which must be the same type as the list elems**

## Strings

Strings are just list operations. Strings are just lists of characters

```
ghci> truth = "Del Taco rules"
ghci> head truth
'D'
ghci> tail truth
'el Taco rules"
ghci> truth ++ "!!!"
"Del Taco rules!!!"
ghci> :t truth
truth :: [Char]
ghci> "hey" == ['h', 'e', 'y']
True
```

```
-- Return [a^2, b^2, c^2] for input [a, b, c]
sqr_it lst 
 | lst == [] = []
 | otherwise = first_sq : (sqr_it rest)
where
  first_sq = (head lst) ^ 2
  rest = tail lst
```

## List Comprehensions

```
output_list = [ f(x) | x <- input_list, guard1(x), guard2(x)]
```

In the above, we have x be each element in the list that satisfies both guard1 and guard2, and our list is formed by passing into f(x). 

*EXAMPLES:*

```
-- comp.hs
-- Generate squares of 2 thru 7
squares = [x^2 | x <- [2..7]]

-- Generate products of two lists
prods = [x*y | x <- [3,7], y <- [2,4,6]]

-- Generate combinations of strings
nouns = ["party","exam","studying"]
adjs = ["lit","brutal","chill"]
combos = [adj ++ " " ++ noun |
          adj <- adjs, noun <- nouns]

-- Generate combinations of tuples
menu = [(oz,flavor) |
   oz <- [4,6],
  flavor <- ["Choc","Earwax","Booger"]]
```

Maps to: 

```
ghci> :load comp.hs
[1 of 1] Compiling Main             ( comp.hs, interpreted )
Ok, one module loaded.
ghci> squares
[4,9,16,25,36,49]

ghci> prods
[6,12,18,14,28,42]

ghci> combos
["lit party","lit exam","lit studying","brutal party","brutal exam","brutal studying","chill party","chill exam","chill studying"]

ghci> menu
[(4,"Choc"),(4,"Earwax"),(4,"Booger"),(6,"Choc"),(6,"Earwax"),(6,"Booger")]
```

**ADVANCED EXAMPLES:**

```
-- comp.hs

-- Generate first 5 #s divisible by 29
-- between 1000 and infinity
div_by_29 = take 5 [x | x <- [1000..],
             (mod x 29) == 0]

-- Extract all non-uppercase chars
lies = "nerds EAT rockS!"
truth = [ c | c <- lies,
          not (elem c ['A'..'Z'])] 

-- Generate right triangles
right_triangle_tuples = [ (a,b,c) | 
     a <- [1..10], b <- [a..10], c <- [b..10],
     a^2+b^2==c^2 ] 
```

### Quicksort Algo

```

-- Quicksort in eight lines! 
qsort lst 
 | lst == [] = []
 | otherwise = (qsort less_eq) ++ [pivot] ++ (qsort greater)
 where
    pivot = head lst
    rest_lst = tail lst
    less_eq = [a | a <- rest_lst, a <= pivot]    
    greater = [a | a <- rest_lst, a > pivot]
```

## Pattern Matching

we define multiple versions of the same function

each version of the function must have the same number and types of arguments

when the function is called, Haskell checks each definition in-order from top to bottom, and calls the first function which has matching parameters

**EXAMPLES OF PATTERN MATCHING**

```
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

list_len :: [a] -> Int
list_len [] = 0
list_len lst = 1 + list_len (tail lst)

exp :: (Int, Int) -> Int
exp (_, 0) = 1
exp (base, exponent) = base ^ exponent
```

**ANOTHER EXAMPLE WITH CONS:**

```
-- lists.hs
-- Extract the first item from a list
get_first_item (first:rest) = 
   "The first item is " ++ (show first)

-- Extract all but the first item of a list
get_rest_items (first:rest) = 
   "The last n-1 items are " ++ (show rest)

-- Extract the second item from a list
get_second_item (first:second:rest) = 
   "The second item is " ++ (show second)
```

**Show function in haskell converts built-in Haskell types into a String that can be printed or concatenated with another String**


**Pattern Matching with List example**

```
-- favs.hs
favorites :: [String] -> String
favorites [] = "You have no favorites."
favorites (x:[]) = "Your favorite is " ++ x
favorites (x:y:[]) = "You have two favorites: "
 ++ x ++ " and " ++ y
favorites ("chocolate":xs) =
  "You have many favs, but chocolate is #1!"
favorites (x:y:_) =
   "You have at least three favorites!"
```

**OUTPUT:**

```
ghci> :load favs
[1 of 1] Compiling Main             ( favs.hs, interpreted )
ghci> favorites []
"You have no favorites."

ghci> favorites ["chocolate"]
"Your favorite is chocolate"

ghci> favorites ["mint","earwax"]
"You have two favorites: mint and earwax"

ghci> favorites ["chocolate","egg","dirt"]
"You have many favs, but chocolate is #1!"

ghci> favorites ["tea","coffee","carrot"]
"You have at least three favorites!"
```

## Generic Types

We can pass generic types to functions (get_last_item :: [t] -> t)

They let you pass whatever type you want. 

**Ord is short for Ordered, meaning the parameter e.g. a must be of a type that is orderable through comparison (numbers, strings) Ord => a->...**

**Fractional means it must be  floating point number**

## First-Class functions and Higher-Order Functions

**Functions are treated like any other data! They can be:**

stored in variables or data structures

passed as arguments to other functions

returned as values by functions

**Higher-Order Functions:**

- a function that accepts another function as an argument, and/or

- a function that returns another function as its return value

**A function signature in the parameter list of functions**

# Intermediate Haskell

## Map, Filter, Reduce

These functions fall into three categories: mappers, filters and reducers.

    A mapper function performs a one-to-one transformation from one list of values to another list of values using a transform function
    A filter function filters out items from one list of values using a predicate function to produce another list of values
    A reducer function operates on a list of values and collapses them into a single output value

### Map function:

map :: (a -> b) -> [a] -> [b]

First arg is a function, that maps an item a to item b, second arg is list of type a, and the return value is a list of type b

**Haskell has a library function called reverse that reverses a list**

```
-- map.hs
map :: (a -> b) -> [a] -> [b]
map func [] = []      
map func (x:xs) =
  (func x) : map func xs
```

### Filter function:

Filters items from an input list to produce a new output list

Haskell provides a function called filter that accepts two parameters:

    A function that determines if an item in the input list should be included in the output list
    A list to operate on

**filter :: (a -> Bool) -> [a] -> [a]**

```
filter :: (a -> Bool) -> [a] -> [a]
filter predicate [] = []
filter predicate (x:xs)
 | (predicate x) = x : (filter predicate xs)
 | otherwise = filter predicate xs
```

### Reducers

The last of the three is called a reducer. A reducer is a function that combines the values in an input list to produce a single output value.

Each reducer takes three inputs:

    A function that processes each of the elements
    An initial “accumulator” value
    A list of items to operate on

#### Foldl

```
foldl(f, initial_accum, lst):
  accum = initial_accum
  for each x in lst:
    accum = f(accum, x)
  return accum
```

The idea is to accumulate the accum variable according to the function f.

```
foldl f accum [] = accum
foldl f accum (x:xs) =
  foldl f new_accum xs
 where new_accum = (f accum x)
```

Each new value x is folded into the accumulator as it's processed

foldl is left-associative: f( ... f(f(accum,x1),x2), ..., xn)


## Advanced Haskell

### Lambda Functions

**HIGH LEVEL EXAMPLE:**

```
squarer lst = map (\x -> x^2) lst
cuber lst = map (\x -> x^3) lst
```

```
ghci> (\x y -> x^3+y^2) 10 3
1009
ghci> map (\x -> 1/x) [3..5]
[0.3333333333333333,0.25,0.2]
ghci> map (\x -> take 2 x) ["Dog", "Cat"]
["Do","Ca"]
ghci> a_func = \x y -> x++y
ghci> a_func [1,2,3] [4,5]
[1,2,3,4,5]
```

### Closures

Combination of lambda expression with a snapshot of all "captured" variables is called a closure

**ANY FREE VARIABLE WILL BE CAPTURED**

**Free variable** is any variable that is not an explicit parameter to the lambda

E.g. in \x -> m*x + b (m and b are free parameters, x is not)

Formally, a closure is a combination of the two things:

    A function of zero or more arguments that we wish to run at some point in the future
    A list of “free” variables and their values that were captured at the time the closure was created

### Partial Function Application

Formally speaking, partial function application is an operation where we define a new function g by combining:

    An existing function f that takes one or more arguments, with
    Default values for one or more of those arguments

### Currying

By definition, currying transforms a function of multiple arguments to a series of functions of a single argument.

**EXAMPLE:**

```
function f(x, y, z) { return x + y + z; }
```

Converts to: 

```
function f(x) {
  function g(y) {
    function h(z) {
      return x + y + z;
    }
    return h;
  }
  return g;
}
```

Formally, Currying is the concept that you can represent any function that takes multiple arguments by another that takes a single argument and returns a new function that takes the next argument, etc.

```
Curry(Function f)
  e = The expression/body of function f
  For each parameter p from right to left:
    f_temp = Define a new lambda function with:
      1. p as its only parameter
      2. e as its (expression)
    e = f_temp
return f_temp
```

**When a inner lambda has the same parameter name as the outer one. The inner one takes precedence and shadows the outer one. In this case, the shadowed parameter will not get replaced. For example, when we evaluate (\x -> ((\x -> x) (x + 1))) 3, we will get ((\x -> x) (3 + 1)).**

### Algebraic Data Types

**EXAMPLE ADT**

```
data Color = Red | Green | Blue deriving Show

data Shape =
  Circle    { radius :: Float,
              color :: Color } |
  Rectangle { width :: Float, 
              height :: Float, 
              color :: Color } |
  Triangle  { base :: Float, 
              height :: Float, 
              color :: Color } |
  Shapeless
  deriving Show

my_color = Red
my_circ = Circle { radius = 5.0, 
                   color = Blue }
```

More Complex Syntax:

```
data Color = Red | Green | Blue deriving Show

data Shape =
         -- radius color
  Circle    Float  Color | 
         -- width  height color
  Rectangle Float  Float  Color |
         -- base   height color
  Triangle  Float  Float  Color |
         -- no fields
  Shapeless
  deriving Show

my_color = Red
my_circ = Circle 5.0 Blue
```

**Add the keywords “deriving Show” at the end of a definition and GHCi will let us print out the field values!**

**PATTERN MATCHING WITH ADTS**

```
-- shapes.hs

data Color = Red | Green | Blue

data Shape =
         -- radius color
  Circle    Float  Color | 
         -- width  height color
  Rectangle Float  Float  Color |
         -- base   height color
  Triangle  Float  Float  Color |
         -- no fields
  Shapeless

getArea :: Shape -> Double
getArea Shapeless = 0
getArea (Circle r _) = pi * r^2
getArea (Rectangle w h _) = w * h
```

**LINKEDLIST CLASS**

```
data List = 
  Nil | 
  Node { 
    val  :: Integer, 
    next :: List 
  } 
  deriving Show
```

```
ghci> :load list
Ok, one module loaded.
ghci> list1 = Nil
ghci> list2 = Node 5 list1
ghci> list2
Node {val = 5, next = Nil}
ghci> head = Node 3 ( Node 2 (Node 1 Nil))
ghci> head
Node {val = 3, next = Node {val = 2, next = Node {val = 1, next = Nil}}}
```

```
sumList :: List -> Integer
sumList (Nil) = 0
sumList (Node val next) = 
   val + sumList next
```

**ADDING A NEW NODE TO BT:**

```
insert Nil val =
  Node val Nil Nil

insert (Node curval left right) val
  | val == curval =
      Node curval left right
  | val < curval =
      Node curval (insert left val) right
  | val > curval =
      Node curval left (insert right val)
```

## Data Palooza

### Variables and Values

Here a is a variable, and 42 is a value.

What are the facets that make up a variable?

    names: variables almost always have a name
    types: a variable may (or may not) have a type associated with it
    values: a variable stores a value (and its type)
    binding: how a variable is connected to its current value
    storage: the slot of memory that stores the value associated with the variable
    lifetime: the timeframe over which a variable exists
    scope: when/where a variable is accessible by code
    mutability: can a variable’s value be changed?

What are the facets that make up a value?

    names: variables almost always have a name
    types: a value will always have a type associated with it
    values: a variable stores a value (and its type)
    binding: how a variable is connected to its current value
    storage: the slot of memory that stores the value
    lifetime: the timeframe over which a value exists
    scope: when/where a variable is accessible by code
    mutability: can a value be changed?

Lifetime refers to the existence of the variable, whereas scope refers to the accessibility of a variable. It is entirely possible for a variable to be out-of-scope but still be alive.

Usually local variables and function parameters are stored on the stack. Dynamically allocated objects and values are usually stored on the heap. Most languages store global and static variables in the static data area. Of course, you can also have combinations of these; for example, a pointer that is stored on the stack, but whose value lies on the heap.

Variable types

What can you infer about a value, given its type?

    The set of legal values it can hold
    The operations we can perform on it
    How much memory you need
    How to interpret the bytes stored in RAM
    How values are converted between types

### Variable Binding

 C++ variable name directly refers to the storage location holding it’s value, while in Python, a variable holds an “object reference”, which then in turn points to the actual value. We will cover the major binding approaches in detail later on.
 
**In general, many dynamically typed1 languages don’t associate variables with types. However, note that a value is always associated with a type.**

### Value Types and Reference Types

    **Value Types:** a type that can be used to directly instantiate objects/values, as well as define pointers/object references/references
    
    **Reference Types:** a type that can only be used to define pointers/object references/references, but cannot directly instantiate objects/values
    
A reference type will generally have members or an association with a complex object class



### Type Equivalence

There are two approaches:

    **Name Equivalence:** Two values/variables are of equivalent types only if their type names are identical.
    
    **Structural Equivalance:** Two values/variables are of equivalent types if their structures are identical, regardless of their type name.
    

**C++ uses name equivalence:**

```
// C++: name equivalence
struct S { string a; int b; };
struct T { string a; int b; };

int main() { 
   S s1, s2;
   T t1, t2;
   s1 = s2; // this works! 
   s1 = t1; // type mismatch error!
}
```


In general, most statically typed languages (C++, Java, …) use name equivalence while most dynamically typed languages (Python, JS) use structural equivalence. As we go through the various typing systems, look out for the two approaches!

### Type Checking

Process of verifying and enforcing constraints on types

Type checking can occur either at:

1. Compile time (static)
2. Runtime (dynamic)

We can also define strictness of type checking:

1. strong
2. weak

### Static Typing

Static typing is the process of verifying that all operations in a program are consistent with the types of the operands prior to program execution. 

Types can either be explicitly specified (like in C++) or can be inferred from code (like in Haskell). For inferred types, if the type checker cannot assign distinct types to all variables, functions, and expressions or cannot verify type safety, then it generates an error. But if a program type checks, then it means the code is (largely) type safe, and few if any run time checks need to be performed.

**To support static typing, a language must have a fixed type bound to each variable at the time of definition.**

**Static type checking is inherently conservative. This means that the static type checker will disallow perfectly valid programs that never violate typing rules.**

```
class Mammal {
public:
 virtual void makeNoise() { cout << "Breathe\n"; }
};
class Dog: public Mammal {
public:
 void makeNoise() override { cout << "Ruff\n"; }
 void bite() { cout << "Chomp\n"; }
};
class Cat: public Mammal {
public:
 void makeNoise() override { cout << "Meow!\n"; }
 void scratch() { cout << "Scrape!\n"; }
};

void handlePet(Mammal& m, bool bite, bool scratch) {
 m.makeNoise();
 if (bite)
   m.bite();
 if (scratch)
   m.scratch();
}

int main() {
 Dog spot;
 Cat meowmer;
 handlePet(spot, true, false);
 handlePet(meowmer, false, true);
}
```

An error is generated for above code, since we try to cast m to be a mammal, even though it doesn't have a scratch method

**Pros of static type checking:**

    Produces faster code (since we don’t have to type check during run time)
    Allows for earlier bug detection (at compile time)
    No need to write custom type checks

**Cons of static type checking:**

    Static typing is conservative and may error our perfectly valid code
    It requires a type checking phase before execution, which can be slow

### Dynamic Typing

Dynamic type checking is the process of verifying the type safety of a program at run time.

**Types are associated with values NOT VARIABLES**

Compiler stores the fact that the value a variable is pointing to is an int with value 10

**Sometimes statically typed languages also need to perform run time type checks. This is most often seen during down-casting (when casting an object from a child class to a parent class).**

```
class Person { ... };
class Student : public Person { ... };
class Doctor : public Person { ... };
void partay(Person *p) {
  Student *s = dynamic_cast<Student *>(p);
  if (s != nullptr)
    s->getDrunkAtParty();
}
int main() {
  Doctor *d = new Doctor("Dr. Fauci");
  partay(d);
  delete d;
}
```

dynamic_cast does a run time check to make sure that the type conversion from Person* to Student* is vald. If not, the cast will return nullptr

**Pros of dynamic type checking:**

    Increased flexibility
    Often easier to implement generics that operate on many different types of data
    Simpler code due to fewer type annotations
    Makes for faster prototyping

**Cons of dynamic type checking:**

    We detect errors much later
    Code is slower due to run time type checking
    Requires more testing for the same level of assurance
    No way to guarantee safety across all possible executions (unlike static type checking)

Sometimes, dynamic type checking is needed in statically-typed languages:

    when downcasting (in C++)
    when disambiguating variants (think Haskell!)
    (depending on the implementation) potentially in runtime generics
    
### Duck Typing

In Python, you can make any class iterable by adding the __iter__ and __next__ methods:

```
# Python duck typing for iteration
class Cubes:
  def __init__(self, lower, upper):
    self.upper = upper
    self.n = lower
  def __iter__(self):
    return self
  def __next__(self):
    if self.n < self.upper:
      s = self.n ** 3
      self.n += 1
      return s
    else:
      raise StopIteration

for i in Cubes(1, 4):
  print(i)             # prints 1, 8, 27
```

You can make any class printable by adding the __str__ function:

```
# Python duck typing for printing objects
class Duck:
 def __init__(self, name, feathers):
  self.name = name
  self.feathers = feathers

 def __str__(self):
  return self.name + " with " + \
         str(self.feathers) + " feathers."

d = Duck("Daffy", 3)
print(d)
```


You can make any complex objects comparable by adding the __eq__ method:

```
# Python duck typing for equality
class Duck:
  def __init__(self, name, feathers):
    self.name = name
    self.feathers = feathers

 def __eq__(self, other):
  return (
    self.name == other.name and
    self.feathers == other.feathers
  )

duck1 = Duck("Carey", 19)
duck2 = Duck("Carey", 19)

if duck1 == duck2:
  print("Same!")
```


## Data Palooza Part 2

### Gradual Typing

Hybrid approach btwn static and dynamic typing

```
def square(x: int):
  return x * x

def what_happens(y):
  print(square(y))
```

If you pass an untyped variable to what_happens, the type checker will check for errors at runtime. 

### Strong Typing

Strongly typed language ensures that we will NEVER have undefined behavior at runtime due to type issues

There is no possibility of an unchecked runtime error

**MINIMUM REQ. FOR A LANGUAGE TO BE STRONGLY TYPED:**


- **The language is type-safe:** the language will prevent an operation on a variable x if xs type doesn’t support that operation.

```
int x;
Dog d;
a = 5 * d; // Prevented
```

- **The language is memory safe:** the language prevents inappropriate memory accesses (e.g., out-of-bounds array accesses, accessing a dangling pointer)

```
int arr[5], *ptr;
cout << arr[10]; // Prevented
cout << *ptr; // Prevented
```

These rules can be enforced either statically or dynamically

Languages usually use a few techniques to implement strong typing:

   before an expression is evaluated, the compiler/interpreter validates that all of the operands used in the expression have compatible types.
   
   all conversions between different types are checked and if the types are incompatible (e.g., converting an int to a Dog), then an exception will be generated.
    
   pointers are either set to null or assigned to point at a valid object at creation.
   
   accesses to arrays are bounds checked; pointer arithmetic is bounds-checked.
   
   the language ensures objects can’t be used after they are destroyed.
   
#### Checked Type Casts

A checked cast is a type cast that results in an exception/error if the conversion is illegal. Let’s look at a concrete example in Java, a strongly typed language.

### Weak Typing

Weak typing is essentially the opposite of strong typing, in that it does not guarantee that all operations are invoked on objects/values of the appropriate type. Weakly typed languages are generally neither type safe nor memory safe.

#### Undefined Behavior

The way to tell if a language is strongly or weakly typed is to see if we see any undefined behavior. If you can find a pattern for the language, it is most likely strongly typed.

**EXAMPLE:**

```
# Defines a function called ComputeSum
# In this language, @_ is an array that holds
# all arguments passed to the function

sub ComputeSum {
   $sum = 0;

   foreach $item (@_) {    # loop thru args
      $sum += $item;
   }

   print("Sum of inputs: $sum\n")
}

# Function call
ComputeSum(10, "90", "cat"); #prints 100
```

#### Classify That Language: Type Checking

In a strongly typed language, we can't perform a cast. It is also statically typed since we wouldn't need a cast in a dynamically typed language

### Type Casting, Conversion and Coercion

Type casting, conversion and coercion are different ways of explicitly or implicitly changing a value of one data type into another.

More formally, given two types Tsub and Tsuper, we say that Tsub is a subtype of Tsuper if and only if

    every element belonging to the set of values of type Tsub is also a member of the set of values of Tsuper.
    
    All operations (eg +, -, *, /) that you can use on a value of type Tsuper must also work properly on a value of type Tsub.
        i.e., If I have code designed to operate on a value of type Tsuper, it must also work if I pass in a value of type Tsub.

### Switching Between Types

Type conversion and type casting are used when we want to perform an operation on a value of type A, but the operation requires a value of type B. There are two ways of converting between types - conversions and casts


This is a conversion since the compiler generates a new temporary value of a different type:
**EXAMPLE:**

```
void convert() {
  float pi = 3.141;
  cout << (int)pi; // 3
}
```

A cast takes a value of type A and treats it as if it were value of type B – no conversion takes place! No new value is created!:

**EXAMPLE:**

```
// Another casting example; treat an
// int as if it's an unsigned int!


int main() {
  int val = -42;

  cout << (unsigned int)val;
      // prints 4294967254
}
```

**Conversions and casts can be widening or narrowing.**

    Widening means the target type is a super type, and can fully represent the source type’s values.
    
    Narrowing means the target type may lose precision or otherwise fail to represent the source type’s values. The target type could be a subtype (like long and short), or the two types could also have a non-overlapping set of values (like unsigned int and int).

**Conversions and casts can also be explicit or implicit.**

    An explicit conversion requires the programmer to use explicit syntax to force the conversion/cast
    
    An implicit conversion (also called coercion) is one which happens without explicit conversion syntax.

#### Explicit Conversions and casts

When you’re using an explicit conversion or cast, you’re telling the compiler to change what would be a compile time error to a run time check.

**EXAMPLE:**

```
class Example
{
  public void askToCookFavoriteMeal(Machine m) {
    if (m.canCook() && m.canTalk()) {
      RobotChef r = (RobotChef)m; // Line 5
      r.requestMeal("seared ahi tuna");
    }
  }
}
```

In the code above, if the language is strongly typed, it will perform a runtime check to ensure that the conversion is valid.

In weakly typed languages: improper casts/conversions are often not checked at runtime, leading to bugs

#### Implicit Conversions and Casts

Most languages have a set of rules that govern implicit conversions that may occur without warnings/errors. For instance, the slides have some associated with C/C++. When learning a new language, it helps to understand its implicit conversion policy!

In such an expression with mixed types, the types of all variables must have “type compatibility” with each other.

#### Type Casting in depth

Casting is when we reinterpret the bits of the original value in a manner consistent with a different type. No new value is created by a cast, we just interpret the bits differently. The most common type of casting is from a subtype to a supertype, for example, when upcasting from a subclass to a super class to implement polymorphism. Downcasting is another example, where we go from a super class to a subclass.

**WE NEED A DYNAMIC CAST WHEN DOWNCASTING BECAUSE WE DON'T KNOW IF EVREY PERSON HAS ALL OF MAMMALS METHODS**


We can also use casting to change the interpretation of pointers and read/write memory using a different type. For example, consider the following snippet of code in C++:

```
void cast() {
  int a = 1078530000;
  int *ptr = &a;
  // Treat ptr as a float *
  cout << *reinterpret_cast<float *>(ptr); // prints 3.14159
}
```

The code treats ptr as if its a pointer to a float (using reinterpret_cast) and then when we derefence ptr, the bits are interpreted as if they were a float



**EXAMPLES:**

From this snippet of code, we can infer that the language supports type coercion, since it does a narrowing coercion from an integer value 5 to a boolean value false.

```
$a = 5;
if ($a) {
    print("5 is true!");
}
```

In the following example, we are told that the program doesn’t work if we remove the float32 conversion:

```
func main() {
  var x int = 5
  var y float32 = 10.0
  var result float32

  result = float32(x) * y // doesn't work if we remove float32()
  fmt.Printf("5 * 10.0 = %f\n", result)
}
```
From this, we can infer that the language requires explicit conversions between even comparable types (like int and float).

## Scoping

### Scoping and In-Scope

The scope of a variable is the part of a program where a variable is valid (i.e., can be accessed). The parts can be lines, statements, expressions, instructions, or other units!

A variable is “in scope” in a part of a program if it is currently accessible by name.

#### Lexical Envs.

**EXAMPLE:**

```
string dinner = "burgers";     // this variable's scope is global - it's in scope everywhere

void party(int drinks) {       // drinks is in scope for the entire party() function
  cout << "Partay! w00t";
  if (drinks > 2) {
    bool puke = true;          // bool is only in scope for this if statement
    cout << "Puked " << dinner;
  }
}

void study(int hrs) {          // hrs is in scope for the entire study() function; but, not the same hrs as main()!
  int drinks = 2;              // drinks is also in scope for study(); but, not the same drinks as party()!
  cout << "Study for " << hrs;
  party(drinks+1);
}

int main() {
  int hrs = 10;                // this hrs is only in scope in main(); different from the hrs in study()!
  study(hrs-1);
}
```

### Lifetime

A variable’s lifetime describes when a variable can be accessed. It includes times when the variable is in scope, but also times where it’s not in scope (but can be accessed indirectly).

Values also have lifetimes. Variables and the values they point to can have different lifetimes!

**EXAMPLE:**

```
void study(int how_long) {
  while (how_long-- > 0)
    cout << "Study!\n";
  cout << "Partay!\n";
}

int main() {
  int hrs = 10;
  study(hrs);
  cout << "I studied " << hrs <<
        " hours!";
}
```

The scope of hrs is only within main(); when we call into study, we can no longer access it. But, its lifetime also extends to study(), since we can access it indirectly - through the variable how_long!

### Lexical Scoping

The core tenet has to do with how your code is organized, which we’ll call the context that a variable is defined in. If we can’t find the variable in the current context, we’ll go to the enclosing context - until we run out (and hit the global context).

More strictly, languages like Python use the LEGB rule. We look for a variable in this order:

    First, look at the local scope. In Python, this is either an expression or a function.
    
    If it’s not there, look at successive enclosing scopes. Repeat this until… 
    
    You hit the global scope.
    
    If it’s still not there, look at the built-in scope - this contains things like print
    
Once a context is over, the variables in that context can't be accessed

**EXAMPLES:**

```
sum([x*x for x in range(10)])     # this works :)
sum([x*x for x in range(10)] + x) # x isn't in scope!
```

**PYTHON DOESN'T SCOPE TO BLOCKS BUT IT DOES TO FUNCTIONS**

### Shadowing

When a variable is redefined in a different context, lexical scoping languages typically use an approach called shadowing. In an inner context, the redefined variable “replaces” all uses of the outer context variable; once the inner context is finished, we return to the outer context variable.

**EXAMPLE:**

```
int main(){
  int x = 42;
  int sum = 0;

  for (int i = 0; i < 10; i++) {
    int x = i;
    std::cout << "x: " << x << '\n'; // prints values of i from 0 to 9
    sum += x;
  }

  std::cout << "sum: " << sum << '\n';
  std::cout << "x:   " << x   << '\n'; // prints out 42
}
```

### Dynamic Scoping

the value of a variable is always the most recently defined (or redefined) version, regardless of the lexical scope! For dynamic scoping, what matters is the chronological order variables are defined in: not how the code is structured.

## Memory Safety and Management

Memory safety is a key property of strongly-typed languages. In short, memory safe languages prevent any memory operations that could lead to undefined behaviour, while memory unsafe languages allow such operations. These include:

    out-of-bound array indexes and unconstrained pointer arithmetic
    
    casting values to incompatible types
    
    use of uninitialized variables and pointers
    
    use of dangling pointers to dead objects (use-after-free, double-free, …)
    
**MEMORY LEAKS DO NOT LEAD TO UNDEFINED BEHAVIOR**

**Since memory leaks only lead to unused memory not being freed, they don’t lead to undefined behaviour. Even if the system runs out of memory due to the memory leak, the program is predictably terminated. Therefore, we see no undefined behaviour.**

## Garbage Collection

Garbage collection is the automatic reclamation of memory which was allocated by a program, but is no longer referenced in code. In languages with garbage collection (like Python), the programmer does not need to explicitly control object destruction - the languages automatically handles that for the programmer. When a value or an object on the heap is no longer referrenced, the program (eventually) detects this at run time and frees the memory associated with it.

Garbage collection has multiple advantages:

    It eliminates memory leaks. This ensures memory allocated for objects is freed once it’s no longer needed
    
    It eliminates dangling pointers and the use of dead objects. This prevents access to objects after they have been de-allocated
    
    It eliminates double-free bugs. This eliminates inadvertent attempts to free memory more than once
    
    It eliminates manual memory management. This simplifies code by eliminating manual deletion of memory
    
### Approaches to Garbage Collection

A good rule of thumb is that we should only garbage collect an object when there are no longer any references to that object. For example, if an object goes out of scope, it should be destroyed.

Another example, if an object reference (pointer) is overriden, then the old value should be deleted (as long as it’s not being used anywhere else).

#### Mark and Sweep

Mark and Sweep runs in two phases: a mark phase and a sweep phase. In the mark phase, the program identifies all objects that are still referred to and thus considered to be in-use. In the sweep phase, the algorithm scans all heap memory from start to finish, and frees all blocks not marked as being ‘in-use.’

##### Mark

During the mark phase, our goal is to discover all active objects that are still being used. We consider an object in-use (and its memory not reclaimable) if it meets one of two criteria:

    it is one of a key set of root objects. Root objects include global variables, local variables across all stack frames, and parameters on the call stack.
    
    it is reachable from a root object. If an object can be transitively reached via one or more pointers/references from a root object (e.g.,robot object points to battery).

GC identifies all root objects and adds their object references to a queue

Then the GC uses the queue to BFS from the root objects and mark all the reachable objects as "in-use"

To do this, each object is augmented with a bit which is set by the GC to mark that it is in use. Once all reachable objects have been marked, all unmarked objects can be disposed of.

```
# Pseudocode for the Mark algorithm
def mark():
  roots = get_all_root_objs()
  candidates = new Queue()
  for each obj_ref in roots:
    candidates.enqueue(obj_ref)

  while not candidates.empty():
    c = candidates.dequeue()
    for r in get_obj_refs_in_object(c):
      if not is_marked(r):
        mark_as_in_use(r)
        candidates.enqueue(r)
```

##### Sweep

We traverse all memory blocks in the heap and examine each object's "in-use" flag. We free all objects that are not in-use!

```
# Pseudocode for the Sweep algorithm
def sweep():
    p = pointer_to_first_block_in_heap()
    end = end_of_heap()
    while p < end:
        if is_object_in_block_in_use(p):
            reset_in_use(p)      # remove the mark, object lives
        else:
            free(p)                        # free this block/object
        p = p.next
```

**Pros:**

    relatively simple
    
    no trouble with cyclic references (more on this later!)

**Cons:**

    program must be paused during GC, causing “freezes” (this is often called a “stop-the-world” GC)
        thus, this is bad for real-time programs
        
    dealing with large amounts of data can lead to thrashing (at the cache/page-level)
    
    can cause memory fragmentation – we’ll have chunks of empty memory (more on that in a moment!)
    
    and, it’s unpredictable!
    
#### Mark and Compact

Mark and Compact is part of the same family of algorithms as mark and sweep. The difference is the second half of the algorithm, which is designed to prevent fragmentation. Instead of sweeping, we compact all marked/in-use objects to a new contiguous memory block. Then we can adjust the pointers to the proper relocated addresses. Our original block of memory can be treated as if it’s empty, and can be reused without dealing with any sweeping.

The pros and cons are pretty similar to mark and sweep. In comparison, the only differences are:

    it much better deals with fragmentation
    
    but, it’s more complex to implement, requires more RAM, and is slower!
    
    
**THESE GC METHODS ONLY HAPPEN WHEN THERE IS MEMORY PRESSURE!(WHEN PROGRAM NEEDS MEMORY)**

GC is non-deterministic. You can't really predict when (or even if) GC will run. 

### Reference Counting

Each object has a hidden counter that tracks how many references there are to it. Everytime a reference is created or destroyed, we just change the counter

That sounds complicated - but, note that references can only change:

    with assignment (=)
    
    when an object goes out of scope
    
However, there are two hidden catches:

    cyclic references are a huge problem; since there’s a cycle, the counter will never reach zero
        
        languages that use RC need to explicitly deal with cycles in a different way.
    
    a “cascade” can happen: if one object is destroyed, it could remove the last reference to another object, which then gets destroyed; then, that removes the last reference to another object, … which could cause a large chunk of deletion (and could slow your computer down)!
        
        to remedy this, some languages amortize deletion over time – but this has similar issues with non-determinism as tracing algorithms!


**Pros:**

    simple
    usually real-time (since reclamation is usually instant)
    more efficient usage since blocks are freed immediately

**Cons:**

    updating counts needs to be thread-safe (this is a huge issue!)
    updating on every operation could be expensive (both in time and space)
    cascading deletions
    requires explicit cycle handling

### The Ownership Model

Every object is "owned" by one or more variables. When the lifetime of the last variable that owns an object ends, the object is freed

DIFF BTWN GC AND THIS:

The main difference is that garbage collection (implemented via reference counting) is done at runtime, whereas the ownership model enforces rules at compile time that allow memory to be deallocated as soon as it goes out of scope. This is known as a zero cost abstraction because it guarantees memory cleanup & safety without the additional overhead of a garbage collector at runtime!

reference counting is a way to implement the ownership model

**EVERY OBJECT CAN BE OWNED BY ONE VARIABLE AT A TIME IN RUST:**

```
fn main() {
  let s1 = String::from("I'm owned!!");

  let s2 = s1; // Ownership transferred to s2
  println!("{}", s1); // Compiler error!
}
```

#### C++'s Ownership Model: Smart Pointers

A smart pointer is a C++ class that works like a traditional pointer but also provides automatic memory management.

Each smart pointer object holds a traditional pointer that refers to a dynamically allocated object or array. Every smart pointer is an owner of its assigned object and is responsible for freeing it when it’s no longer needed. Smart pointers can also keep track of how many references (i.e. smart pointers) there are to an object.

These are both fairly self explanatory based on their names: std::unique_ptr create exclusive references to objects while objects referred to by std::shared_ptr can also be referred to by other std::shared_ptrs.

When a unique_ptr goes out of scope, it frees the memory it points to automatically.

t’s important to note that smart_pointers disallow making copies! This includes passing it to functions.

The shared_pointer is a bit more lenient. When a shared_pointer goes out of scope, we coordinate amongst all the shared_pointers that point at the same object and decrement the number of references to that object. In other words, shared_pointers are also implemented through reference counting! Once the number of references to an object hits 0, the shared_pointer will automatically free the object.

### Destructors, Finalizers and Disposers

#### Destructors

Only used in languages with manual memory management

Since the programmer can control when they run, you can use destructors to release critical resources at the right times: e.g., freeing other objects, closing network connections, deleting files, etc.

```
void doSomeProcessing() {
   TempFile *t = new TempFile();
  
   ...
 
   if (dont_need_temp_file_anymore()) 
     delete t; // explicit call to a destructor
  
   ...
}

void otherFunc() {
  NetworkConnection n("www.ucla.edu");

  ...
} // destructor for n called when it goes out of scope
```

#### Finalizers

In GC languages, memory is reclaimed automatically by the garbage collector. So finalizers are used to release unmanaged resources like file handles or network connections, which aren’t garbage collected. Unlike a destructor, a finalizer may not run at a predictable time or at all, since objects can be garbage collected at any time (or not at all). Since they can’t be counted on to run, they’re considered a last-line of defense for freeing resources, and often not used at all! We’ll 

#### Disposal Methods

A function the programmer must manually call to free non-memory resources (network connections)

You use disposal methods in GC languages because you can't count on a finalizer to run!

This is a guaranteed way to release unmanaged resources when needed

### Mutability

There are four approaches to immutability:

    Class immutability: The programmer can designate that all objects of a class are immutable after construction.
    
    Object immutability: The programmer can designate some objects of a particular class as immutable –mutations are blocked to those objects!
    
    Assignability immutability: The programmer can designate that a variable may not be re-assigned to a new value - but mutations can be made to the original referred-to object!
    
    Reference immutability: The programmer can prevent a mutable object from being mutated via a reference that’s marked as immutable
    
    There are tons of benefits!

    eliminates aliasing bugs
    
    reduces race conditions in multithreaded code
    
    eliminates identity variability bugs
    
    elminates temporal coupling bugs
    
    removes side effects, making programs easier to reason about
    
    makes testing easier
    
    enables runtime optimizations
    
    enables easy caching
    
    objects are never left in an inconsistent state by definition

