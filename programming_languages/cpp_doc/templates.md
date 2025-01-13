# Templates
They allow you to implement genericity. The function will work with any kind of types.
Templates are resolved at compile time and they don't do run time check (this increase speed).<br/>
With templates you write the class and the functions only once and they will work with any king of types.They often rely on operator overload. Much of the standard library is *template-based*.<br/>

```
template <class T>
T max(T const& t1, T const& t2) // placeholder types
{
    return t1 < t2? t2: t1;
}
```
