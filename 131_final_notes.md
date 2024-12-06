# Final Notes

## Data Palooza

### Static Typing

Verifies all operations in a program are consistent with operands prior to program exec.

**To Support static typing, the language must have a fixed type bound to each variable at the time of definition**

Key Example: When we pass in a base class and try to call methods that ONLY derived classes have, our compiler generates an error.

Pros of static type checking:

    Produces faster code (since we don’t have to type check during run time)
    Allows for earlier bug detection (at compile time)
    No need to write custom type checks

Cons of static type checking:

    Static typing is conservative and may error our perfectly valid code
    It requires a type checking phase before execution, which can be slow

### Dynamic Typing

Verifying type safety at **RUN TIME**

**Types are associated with values, not variables** so the compiler stores extra info with each variable

Sometimes Statically typed languages also need to do run-time checks(WHEN DOWNCASTING)

Pros of dynamic type checking:

    Increased flexibility
    Often easier to implement generics that operate on many different types of data
    Simpler code due to fewer type annotations
    Makes for faster prototyping

Cons of dynamic type checking:

    We detect errors much later
    Code is slower due to run time type checking
    Requires more testing for the same level of assurance
    No way to guarantee safety across all possible executions (unlike static type checking)

### Duck Typing

Method that type checks based on what functionalities objects provide!

### Strong Typing (type enforcement, no implicit type conversion, consistency)

Ensures that we will never have undefined behavior at run time

Minimum Req. for language to be strongly-typed:

- language is type-safe: language prevents invalid ops on variables
- language is memory safe: language prevents inappropriate memory accesses

### Weak Typing (implicit type conversion, type flexibility, dynamic and loose checking)

**DOES NOT GUARANTEE** That all operations are invoked on objects/values of appropriate type.
Generally not type or memory safe

**KEY TO DIFFERENTIATE BTWN WEAKLY AND STRONGLY TYPED LANGUAGES: LOOK TO SEE IF SOMETHING RETURNS UNDEFINED BEHAVIOR, THEN WEAKLY TYPED, OTHERWISE STRONGLY TYPED**

## Type Casting, conversion, and coercion

### Subtypes and Supertypes

We say one type (T) is a subtype of the other (S) iff:

1. Every element in the set of values of T is also a member of the set of values of S
2. All operations that you can use on a value of Type S must also work on a value of type T

### Type Conversions and Casts

Conversion takes a value A and generates a whole new value of type B. Mainly used to convert btwn primitives

Cast takes value of type A and treats it as if it were a value of type B - no conversion, no new val

### Explicit Conversion and Casts

Telling compiler to convert compile time check to runtime

If language is strongly typed, it will perform a runtime check to ensure the type conversion is valid. In weakly typed languages, improper casts/conversions are often not checked at run time.



