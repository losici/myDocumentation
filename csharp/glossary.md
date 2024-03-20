# Glossary
[[_TOC_]]

## static
Indicates that the method belongs to the class itself rather than to instances of the class. Static methods can be called without creating an instance of the class.

The following keywords define the accessibility of the method
## public
Public means the method can be accessed from outside the class.
## private
Private means the method can only be accessed within the class
## protected: 
Protected means the method can be accessed within the class and its derived classes.

## readonly: 
Indicates that the field (ProductDesign in this case) can only be assigned a value during initialization or in the constructor, and its value cannot be changed thereafter.

## sealed
In this case, MyMethod is declared as sealed, which means that it cannot be overridden by subclasses. This is useful for preventing further specialization of behavior in subclasses or ensuring that certain critical methods retain their implementation throughout the inheritance hierarchy.
However, please note that sealed is typically used with override, meaning it's used in the context of inheritance and overriding methods from a base class. It's not typically used with static methods or non-overridden instance methods because they cannot be overridden in the first place.

```
public sealed override void MyMethod()
{
    // Method body
}

```