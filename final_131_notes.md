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



