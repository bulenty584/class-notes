# Final Notes

## Data-Function Palooza

### Variable Binding Semantics

1. **Value Semantics:** Variable is directly bound to storage that holds a value

2. **Reference Semantics:** Variable is directly bound to ANOTHER variable's storage that holds the value/object

3. **Object Reference Semantics:** Variable is bound to a **POINTER** that points to storage that holds the object/value

4. **Name Semantics:** Variable is bound to a **pointer** that points to an expression graph that evaluates the value

#### Value Semantics

Each variable name is DIRECTLY bound to the storage that represents that variable

Local variables are stored on the stack in an "activation record"
  - activation record is a map from variable names to direct values; the entire record lives in memory

When we reassign variables, the value is completely copied over. The only relationship btwn x and y is that their values are equal

#### Reference Semantics

Allows us to assign an alias name to an existing variable and read/write it through that alias

Example:

```
int main() {
  string role = "SWE";
  string &truth = role; // binds truth to role

  truth = "QA"; // since truth points to the same mem location as role, this updates both!

  cout << "Addr of role: "  << &role << endl;
  cout << "Addr of truth: " << &truth << endl;
}
// both role and truth will have the value "QA"
// the printed addresses will be the same!
```

&truth isn't a pointer to the role variable, it points to the **same memory location** as role. When we update truth we also update role

#### Object Reference Semantics

Binds a variable name to a pointer varaible that itself points to an object or value

In Python, the activation record maps variables to pointers to items on the heap

For reassignment, the pointer values are copied, but NOT THE MEMORY ITSELF

other variables are unaffected when we update another that had a reference, since we create a new object and change y's pointer

We need to introduce some better tools that test for equality: two pointers with different values could point to the same block of memory

We can either do **object identity:** if two object references refer to the same object at the same address in RAM

OR

**Object Equality:** Do two object references refer to objects that have equivalent values!

#### Name and Need Semantics

**Name Semantics** binds a variable name to a pointer that points to an expression graph called a "thunk"

**WHAT ARE SIDE EFFECTS??**

# Function Palooza

## Parameter Passing Semantics

**Formal parameters** refer to variables that are bound to values while **actual arguments/args** are the values we pass in!

### Pass by Value

Each argument is first evaluated to get a value, and a *copy* of the value is then passed to the function for local use

The parameter in the specific function's activation record is initially copied from s from main.

When n is modified at the end of the function, it only affects the local copy and NOT the original argument in main, or out of the scope

### Pass by Reference

When we pass by reference, our formal parameter acts as an alias for the original value/object. Each read/write of the formal parameter is directed to the original variable's storage

### Pass by Object Reference

All values/objects are passed by (copy of the) pointer to the called function. The function can use the pointer to read/mutate the pointed-to argument

We copy the object reference of our passed in variable into the formal parameter of our function. In this function, the local variable points to our original object, which can be mutated through the object reference

any assignment of n to a different variable changes where the local object reference points to in the heap. It has no impact on the original reference or the object the original reference points to

### Pass by Name/Need

Each parameter is bound to a pointer that points to an expression graph which can be used to compute the passed-in argument's value

Thunks are typically implemented as a lambda function

In pass by need, once the expression graph is evaluated, the result is cached to prevent repeat computation

### Pass by Value-Result

We pass a COPY of the argument in and once we return from our funciton we copy all changes made to that param to the original arg. **Changes are only made to orig. argument after func. returns**

### Positional and Named Parameters

Order of arguments must match the order of formal parameters

In languages that support named parameters, call can explicitly specify the name of each formal parameter (argument label) for each argument

### Default Parameters

We can specify default values for formal parameters which make them optional in the function call


### Errors

Handling Techniques: Overview

Here are the major “handling” paradigms provided by various languages:

    roll your own: The programmer must “roll their own” handling, like defining enumerated types (success,error) to communicate results.
    error objects: Error objects are used to return an explicit error result from a function to its caller, independent of any valid return value.
    optional objects: An “Optional” object can be used by a function to return a single result that can represent either a valid value or a generic failure condition.
    result objects: A “Result” object can be used by a function to return a single result that can represent either a valid value or a specific Error Object.
    assertions/conditions: An assertion clause checks whether a required condition is true, and immediately exits the program if it is not.
    exceptions and panics: f() may “throw an exception” which exits f() and all calling functions until the exception is explicitly “caught” and handled by a calling function or the program terminates.

#### Error Objects

Error is a built-in type that is returned when we have an error in a function

You can also define your own custom error type

#### Optionals

Think of it as a struct that holds two items: a value and a bool indicating whether or not the value is valid

It can also be thought of as an ADT, which contains either nothing or something with a value

#### Result Object

Can be used by a function to return a single result that can represent either a **valid value** or a **distinct error**

Can be thought of as a struct with two items in it: a value and an error object with details about the error

**USEFUL WHEN THERE ARE MULTIPLE DISTINCT FAILURE MODES THAT NEED TO BE DISTINGUISHED AND HANDLED DIFFERENTLY**

#### Assertions

Useful to verify preconditions, postconditions to guarantee some fact is true, and invariants

#### Exception Handling

An exception handler runs iff an error occurs during tried ops, and deals w the error

The catch block catches unhandled or raised errors from the try block

The **thrower** is a function that performs an operation that might result in an error. If an error occurs, the thrower creates an exception object containing details about the error and then throws it for the exception handler to deal with

If you want to create a catch-all-handler, you can specify a more basic exception class. The handler will deal with the base exception type and all of its subclassed exceptions

The **Finally** block runs no matter what!

#### Lambda Functions

##### Capture by Value

Only the values of the free variables are captured by the lambda. Any changes made to the captured variable inside the lambda will not be reflected outside

##### Capture by Reference

Values are captured by reference, use [&] in c++ for a lambda

##### Capture by Environment

Object reference to lexical env. where the lambda was created is added to the closure.

Python always uses the CURRENT lexical env.

### Polymorphism

Defining a function or class that can operate on many different types of values

#### Ad-hoc Polymorphism

We define specialized versions of a function for each type of object we wish it to support. The language decides which version of the function to call based on the types of the args

**NOT POSSIBLE IN DYNAMICALLY TYPED LANGUAGES SINCE WE DON'T SPECIFY TYPES FOR FORMAL PARAMETERS**

#### Parametric Polymorphism

We define a single parameterized version of a class or function that can operate on many, potentially unrelated types

Implemented using templates or generics

#### Templates

All at compile time. Compiler will see all the types used in each template and for each invocation, it will do type-checking. It then generates a concrete version of the function/class by subbing in the type parameter and compile the code!

#### Generics

Instead of generating a new function for each parameterized type, we compile just one version of the generic function or class (independent of types that actuall use generics)

WE CANNOT MAKE ASSUMPTIONS ABOUT WHAT TYPES MIGHT BE USING IT! WE CAN ONLY DO GENERIC OPS

We can **bound types**: adding restrictions on what types are allowed

## OOP PALOOZA

**Everytime you define a new class, it also defines a new type!**

If the class is concrete (all methods have defintions) and not abstract(not all methods have defs), then you can use this new type to define:

objects, object references/pointers, and references

### Interfaces

An interface is a related group of function prototypes (functions w out bodies) that describes behaviors that we want one or more classes to implement. It specifies what we want one or more classes to do but not how to do it!

**INTERFACES ALLOW UNRELATED CLASSES TO PROVIDE A COMMON SET OF BEHAVIORS WITHOUT INHERITING**

Every time you define an interface you define a new reference type

But you can use reference types to define all of the following: object references, pointers and references, depending on which of the above your language supports.

If each interface defines a type, and each class defines a type, and a class implements an interface – does the class have two types? The answer is Yes! For example our Square class actually has TWO types - it is of the Square type AND it is of the Shape type! And you can pass a Square to any function that accepts either a Square or a Shape object reference, pointer or reference!

when you define a class with all of its methods { implemented }, you create what’s called a “value type” or a concrete type - and you may define all of the following: objects, object references/pointers, and references.

### Class Methods

A class-level method is one that ONLY access class fields (static types). It cannot access ANY Instance fields.

In Python, we use the class name, followed by a dot to call a class method or access a class variable

Class level methods cannot call instance level methods since those methods are associated with an instance, but a class method is not!

### Access Modifiers

Enables a class to designate what parts of a class are publicly visible and to hide the class's data/impl.

Public, protected private

Java's protected keyword lets subclasses access the member/method but also lets any other class in the same file

**MAKE SURE YOU KNOW THAT _method() means protected and __method() means private in Python**

Avoid providing getters/setters for fields that are specific to your current implementation, to reduce coupling with other classes.

### Properties, Accessors, and Mutators

Why Use accessors?? We can hide a field's implementation and more easily refactor.

In Python the @property keyword designates an accessor and the @thing.setter designates a setter. Once this is done, we can call the method directly like a member variable a.age = 23, print(a.age)

**Use properties when you're exposing the state of a class (even if exposing that state needs minor computation). Use traditional methods when you're exposing behaviors of a class or exposing a state that requires heavy computation**

### Inheritance

**Interface** (creating many classes that share a common public base class interface I. A class supports interface I by providing implementations for all I's functions)

**Subtype** (Base class provides public interface and implem. for its methods. Derived class inherits both base class's interface and impl.)

**Implementation Inheritance** (reusing base class's method impl.. A derived class inherits method implementations from a base class)

**Prototypical Inheritance** (One object may inherit the fields/methods from a parent object

#### Interface Inheritance

Define a public interface, (in C++ this is a fully virtual base class (```virtual double area() const = 0```) then you can define a class that inherits/implements this interface

The main reason we do this is to have completely unrelated classes share the same common interface

We can also have a single class support multiple interfaces! (```Class Car: public Washable, public Drivable```)

Once we define an interface, we can pass in an object that inherits the interface to functions!

Ex: ```void cleanUp(Washable& w)...``` and pass in Car which implements a washable

##### Common Use cases of interfaces

1. comparing objects (ex. Java's Comparable)
2. iterating over an object (ex. Java's Iterable)
3. from class: serializing an object

**Best Practices:**

1. Use interface inheritance when you have a "can-support" relationship btwn a class and group of behaviors. (Car can support washing, kennel can support iteration)

2. Use interface inheritance when you have different classes that all need to support related behaviors, but aren't related to the same base class (Cars and dogs can both be washed, but aren't related to the same base class

#### Subclassing Inheritance

OG inheritance (base class B which has public interface and method impl., derived class D which inherits B's pub. interface and method impl., and D can override B's methods or add its own new methods)

Subclass can do anything the base class can do! Base class can be anything subclass can be

anywhere the base class is expected, you can pass in a derived class!

When to use:

1. When there's an is-a relationship (Circle is a type of Shape, car is a type of vehicle)
2. When you expect your subclass to share the entire public interface of the superclass AND maintain the semantics of the super's methods
3. When you can factor out common implementations from subclasses into a superclass:
  - Ex. All shapes share x,y coordinates and a color along w/ methods to get/set these things

When we want to inherit the functionality of a base class but don't want to inherit the full public interface, we can use composition and delegation (composition is when you make the original class a member variable of your new class. Delegation is when you call the original class's methods from the methods of the new class.)

We use the above to hide the public interface of the original class and at the same time the second class can leverage all of its functionality

Pros:

    Eliminates code duplication/facilitates code reuse
    Simpler maintenance – fix a bug once and it affects all subclasses
    If you understand the base class’s interface, you can generally use any subclass easily
    Any function that can operate on a superclass can operate on a subclass w/o changes

Cons:

    Often results in poor encapsulation (derived class uses base class details)
    Changes to superclasses can break subclasses (aka Fragile Base Class problem, which we’ll learn about in week 9)


#### Implementation Inheritance

Derived class inherits the method impl. of the base class, but not its public interface. The public interface is hidden from the outside world! Done with private or protected inheritance

```class Set: private Collection```

Since Set privately inherits from Collection, it inherits ALL of its public/protected methods but it does not expose the public interface of the base collection class publicly

**SET IS ALSO NOT A SUBTYPE OF COLLECTION!!!** Set class hides the fact that it has anything to do withe Collection base class, so you CANNOT pass a Set to a function that accepts a Collection, since they're unrelated types

#### Dive into Inheritance

##### Construction

When you instantiate an object of a derived class, this calls the derived class's constructor.

1. It calls its superclass's constructor to initialize the immediate superclass part of the objec
2. It initializes its won parts of the derived object

In most languages, you must call the superclass constructor first from the derived class constructor before doing any initialization of the derived object

##### Destruction

Derived destructor runs its code first and then implicitly calls the destructor of its superclass. This happens all the way to the base class

##### Finalization

Languages need an explicit call from a derived class finalizer to the base class. Others do it auto

#### Multiple Inheritance and Its Issues

We will create two different instances of each member variable/object!
This way, we inherit from a base class B twice

Consider what would happen if two base classes define a method with the same prototype, and then a third class inherits from both base classes. When calling that method, which version should be used? It gets complicated.

### Abstact Methods and Classes

Abstract methods are methods that define an interface but don't have an impl.

Abstract method defines "what" a method is supposed to do and its inputs and outputs

Why use abstract methods instead of dummy impl.? So that the programmer is forced to redefine the method in a derived class

**DEFINES A REFERENCE TYPE, which can ONLY be used to define pointers, references, and object references**

### Inheritance and Typing

When we use inheritance to define classes, we automatically create new subtypes and supertypes!

The base class defines a supertype and derived class defines a subtype

### Subtype Polymorphism

Ability to substitute an object of a subtype anywhere a supertype is expected (where code designed to operate on an object of type T operates on an object that is a subtype of T!

This works because the class associated with the subtype supports the same public interface as the class associated with the supertype.

This works because the subclass inherits/implements the same interface as its superclass. But that’s not enough! We also expect the methods of the subclass to have the same semantics as those in superclass.

**DERIVED CLASS SHOULD ALWAYS IMPLEMENT THE SAME SEMANTICS AS THE BASE CLASS**

### Dynamic Dispatch

Actual method to get called is determined at runtime based on the target object that var refers to

We determine which method gets called:

- based on target object's class
- by seeing if the target object has a matching method (regardless of object's type or class)

#### Statically typed language Dynamic Dispatch

Language determines class of an object at time of method call and uses this to dynamically dispatch to the class's proper method

Each object has a hidden pointer that points to the vtable for a class (array of function pointers which points to the proper method impl. to use for the current class) EVERY CLASS HAS ITS OWN VTABLE

**ONLY VIRTUAL METHODS ARE INCLUDED IN THE VTABLE**

Dynamic dispatch is not used to call regular instance or class methods. Instead we use a standard function call! A function call to these functions can be determined at compile time (statically)

#### Dynamic Dispatch in Dynamically Typed Languages

While a class may define a default set of methods, the programmer can add/remove methods at runtime to classes or sometimes individual objects.

The language stores a unique vtable in EVERY OBJECT!!!

## Control Palooza

### Expressions

If your expressions are calling functions, those functions shouldn't have side effects that could impact the execution of other functions called in the expression

### Associativity

Most languages use left to right associativity when evaluating mathematical expressions

cout << c - d + f() ; == cout << (c - d) + f() ;

### Short Circuiting

Most languages will evaluate sub-expressions left-to-right. The moment the language finds a condition that satisfies or invalidates the boolean expression, it skips the rest!

### Iteration

Counter-controlled (we use a counter (for i in range)), Condition-controlled (boolean condition to decide how long to loop, (while ...)), Collection-controlled (enum. items in a collection for (x in ...))

#### Iterable Objects vs Iterators

- Iterable object is an object like a container which can have its items iterated over

- Iterator is the thing that refers to an iterable object and can be used to iterate over the values it holds

Iterators that are used with containers and external sources like data files typically have two methods:

- iter.hasNext(): we ask the iterator whether it refers to a valid value that can be retrieved

- iter.next(): we ask the iterator to get the value that it points to and advance to the next item

#### Interface with just next() methods

Typically used for ranges!

iter.next(): iterator generates and returns the next value in the sequence, or indicates its over by returning or throwing an exception

Under the hood how iterators work:

```
for v in numbers...
val numbers = listOf(10,20,30,42)

val it = numbers.iterator()
while (it.hasNext()) {
  val v = it.next()
  println(v)
}
```

#### How are iterators impl??

Either with traditional classes, or True iterators (generators)

##### Traditional Classes

we need to define an iterable class (we need to define the __iter__() method) that creates and returns an interator object

We need to define our iterator class with a method called __next__() that gets the value of the item pointed to by the iterator, advances it and returns the value

If the iterator runs out of items to iterate over, we can throw an exception to stopIteration

##### True Iterators

Generator is simply a closure that can be paused and resumed over time

```
def our_range(a, b):
  while a > b:
    yield a
    a -= 1

print('Eat prunes!')
for t in our_range(3,0):
  print(t)
print(f'Explosive diarrhea!')
```

Generator is an iterable object

#### First-class Function-based iteration

The container contains a forEach() method that accepts one parameter - we pass in a lambda function and then operate on every element!

**NOT USING AN ITERATOR!**

We are instead passing a function as an argument that loops all over the iterable's items and does smth

### Concurrency

We decompose program into simult. executing tasks:

The tasks can:

    run in parallel on multiple cores, OR run multiplexed on a single core
    operate on independent data, OR operate on shared mutable data/systems
    be launched deterministcally through program flow, OR be lanuched to due external event (button click in UI)


#### Models for Concurrency

**Multi-threading model:** program creates multiple threads of execution that run concurrently (potent. parallel) (programmer launches one or more functions in their own thread and OS schedules the tasks across available CPU cores)

**Asynchronous Model:** Single-threaded loop manages queue of tasks executing them one at a time as they become ready. When an event occurs, it results in a new function being added to the queue!

##### Multi-Threading model

Three Key features:

1. Thread Management (each thread allows to run ops at the same time)
2. Synchronization (ensures threads don't interfere w/ shared resources)
3. Message passing (allows threads to send messages to each other safely)

###### Thread Management

####### Fork Join paradigm

Fork join is a concurrent version of divide and conquer:

1. We "fork" one or more tasks so they execute concurrently
2. We wait for all tasks to complete ("join") and then proceed

**Parallel sort would be good example for fork-join**

**Fork join is often used recursively!** For huge datasets we may choose to split a data source in two and we can keep splitting until its small enough to deal with!

####### Multi-threading in Python

ONLY ONE THREAD DOES COMPUTATION AT A TIME (Python's GC was never designed to be thread-safe)

Python has a GIL, and it can only have one owner at a time. Once the thread takes ownership of the GIL it's allowed to read/write to Python objects. After a thread runs for a while it releases the GIL to another thread and gives it ownership. If a thread is waiting for the GIL, it falls asleep until it gets its turn

We use multithreading in python **FOR IO OPERATIONS SINCE THEY DONT NEED THE GIL! NO PYTHON CODE**

###### Concurrency with Shared Mutable State

Two threads accessing the same variables that produced undefined behavior! (updating shared memory)

###### Safe Concurrency With Shared Mutable State

mutexes, semaphores, spinlocks, barriers, conditions, read write locks

In C++ we lock mutexes to indicate a section of code that only one thread can access at a given time. This is useful for managing shared mutable state across threads (counter variable)

In Java, the synchronized keyword requests exclusive ownership of syncObj. If another thread reaches this point while the original thread still has ownership, it will be blocked until ownership is released.

###### Message Passing

Some languages use built-in message queues to enable threads to safely communicate

#### Asynchronous Programming

Statements in a program are not executed top to bottom! (a module called runtime maintains a queue of coroutines to execute) A coroutine is a function that once run can be paused and resumed

I/O operations can be performed outside the queue while a coroutine is running

**VERY USEFUL WHEN WE HAVE AN IO TASK (reading from DB or downloading web data)**

While waiting for an IO operation to be completed, the runtime can suspend a coroutine and enqueue other coroutines. Very lightweight compared to threads

Multithreading 	Asynchronous Programming
Capable of true parallelism across cores |	Concurrency without true parallelism
Preemptive multitasking |	Cooperative mulitasking
Uses more memory; each thread has extensive execution context |	Uses less memory; each coroutine is lightweight
Race conditions are common, requiring synchronization |	Race conditions are less common due to single threaded nature
Best suited for CPU bound tasks |	Best suited for IO bound tasks
Complex error handling |	Easy error handling