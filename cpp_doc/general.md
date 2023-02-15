# Compiler stuff
The compiler checks that you do what you wanted to do. 
Cpp has a type safety feature: when you call a function, the arguments you supply might be coneerted to the parameters the function takes. So the compiler warns you.

# Multiple files
Splitting the code in multple files allows you to decrease the compiling time.
You need the declarations where you use the functions. To use a function implemented in the other files, you must tell the compiler about it (name, what it takes, what it retrns: you declare it). But keeping pasting declarations is painful. The solution is the **header files**.<br\>
In the header file you put the declarations in that file and then you include that file. 
- **#**: preprocessor directive is used for "including".
When you include the header file the inter content is pasted where the include is. 
- declarations are in headers;
- implementations are in cpp files, include here also the headers.
- headers must be icluded where the functions are used. 

