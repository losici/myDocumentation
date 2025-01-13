# Classes

## Expression-Bodied method
An expression-bodied method is a feature introduced in C# 6.0 that allows you to define methods using a concise syntax. Instead of using a block of code delimited by curly braces {} to define the method body, you can use a single expression to achieve the same result.

Here's a comparison between a traditional method and an expression-bodied method:

Traditional method:
```
public int Add(int a, int b)
{
    return a + b;
}

```

Expression-bodied method:
```
public int Add(int a, int b) => a + b;

```

In the expression-bodied method syntax, the method declaration is followed by a lambda-style arrow =>, and then the expression that computes the return value. This syntax is particularly useful for short, single-line methods, making the code more concise and readable.

## Methods
se methods for actions that cause side effects or significant computations 

## Properties
Use properties for simple state retrieval or updates