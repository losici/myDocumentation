# Indirection
They are a way to access memory
## References
A reference is an alias for something else and you can set the target when declaring it. It cannot refer to something else.
References cannot retarget.

Use reference when copying by value would be too expensive.
Pass by value sends a copy of the data stored in the variable you specify, and pass by reference sends a direct link to the variable itself. So if you pass a variable by reference and then change the variable inside the block you passed it into, the original variable will be changed.

## Pointers
It can point to something that already exists. Can point nowhere and you can change where it points to.

```
int *pA = &A; //Initiali
*pA = 5; // dereference the pointer means managing the value of the pointer. It will change the value of the variable is pointing to.

Person* pKate = &Kate;
name = (*pKate).getName();
name = pKate->getName();

```

Pointer can be initialiazed to nothing **nullptr**.

## Const
How does it work with indirection?
A way to commit to the compiler you won't change something.

### Const Before or After?
Compiler doesn't care, humand do. Always better const after.

const& --> when you want to pass literals

```
int i = 3;
int  const ci = 3;

i = 4; //ok
//ci = 4; //breaking const rules

int& ri = i;

int const & cri = i; 
//cri = 6; //error because of constant

// int& ncri = ci; //error you cannot assign a constant to something int

```

### Const reference
Reference cannot retarget, with const I cannot change their value.
Functions that take literal values need to be aware of const.

Take a const reference is not taking a reference.

### Const Pointer
Const Pointer
```
int j = 10; 
i = 3;

int * const cpI; // THis is a const pointer
cpI = &something; // error: I can't change the pointer to point somewhere else. 
*cpI = 4; // OK
cpI = &j; //Error
```
Pointer to a const
```

int const * pcI; //This is a pointer to a const. The pointer is changable but it's pointing to something const
*pcI = 2; // error: you can't change the value of the target

pcI = &j;
j = *pcI;
```
Const Pointer to a const
```
int* pI = &i;
int const * const crazy = pI;
*crazy = 4; // Error, you cannot change the integer because it must be const. Expression must be a modifiable l value.
crazy = &j;//error: Expression must be a modifiable l value.
j = *crazy;


```