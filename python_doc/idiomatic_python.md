# Idiomatic learnings

## IF
### Use if and else as short ternary operator replacement
```
foo = True
value = 1 if foo else 0
print(value)
```

## FOR
### Use the enumerate function in loops instead of creating an "index" variable. 
```
my_container = ['apple', 'banana', 'orange']
for index, element in enumerate(my_container):
    print('{} {}'.format(index, element))
```

### Use the in keyword to iterate over an iterable
```
my_list = ['apple', 'banana', 'orange']
for element in my_list:
    print(element)
```
### Use `else` to execute code after a for loop concludes
A for loop can include an else clause that is executed after the iterator is exhausted, unless the loop ended earlier due to a break statement.

## Function
