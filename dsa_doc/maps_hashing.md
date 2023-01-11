# Maps

## Set
Comparable to a list but with one big difference: it doesn't allow repeated elements and it is not ordered.

A Map is a set based data structure.<br/>
Map = <key,value> <br/>Where a group of keys is a set.<br/>
The keys of a Map needs to be unique. And the values can be many.

# Hashing
## Some consideration about Hashing
Using a data structure that employes an hash function allows you to look up in constant time. In a list or set you have to look to all the elements to find what you're looking for and stacks and queues allows you to look at the oldest or newest elements immediatly and priority queues will help you in find the element with the highest priority. If you want to find any other elements you need to do a linear search :'(.<br/>
The ability of doing constanti time lookup will do any algorithm immediatly faster.

## Hashing in detail
What is a Hash function?<br/>
The purpose of an hash function is to transofr some value into one that can be stored and retrieved easily. You give it some value, it converts the value based on some formula, and spits out a coded version of the value that's often the index in an array.<br>
Example<br/>
There is a big number 0123456. A common practise is to take the last few digits devide them for a constant number and use the reminder from that division to find a place to store that number in a array.<br>0123456-->56/10=5--> reminder = 6. The reminder in this case will be directly the index of an array.

