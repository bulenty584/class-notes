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



