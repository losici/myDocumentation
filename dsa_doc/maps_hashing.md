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

### Collision
When the hash function produce the same number.<br/>
0123456 --> 56%10 = 6<br/>
6543216 --> 16%10 = 6<br/>
There are two main ways to fix a collision:
1. Change the value in the has function or to change the hash function completely.<br/>
![Collisions](/dsa_doc/imgs/collisions.png "Collisions")<br/>
Efficiency: O(1).<br/>
2. You can also keep the original hash function but change the structure of the array. Instead of storing one hash value it can contain a list.<br/>
![Collisions Buckets](/dsa_doc/imgs/collisions_buckets.png "Collisions Buckets")<br/>
With the buckets approach instead to store one value you can actually store collections.<br/>
Efficiency: O(n) because still you have to look inside.
![hash_inside_hash](/dsa_doc/imgs/hash_inside_hash.png "hash_inside_hash")<br/>
### Load FActor
When we're talking about hash tables, we can define a "load factor":<br/>
```Load Factor = Number of Entries / Number of Buckets```<br/>
The purpose of a load factor is to give us a sense of how "full" a hash table is. For example, if we're trying to store 10 values in a hash table with 1000 buckets, the load factor would be 0.01, and the majority of buckets in the table will be empty. We end up wasting memory by having so many empty buckets, so we may want to rehash, or come up with a new hash function with less buckets. We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.<br/>

On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions.<br/>

# Hash Maps
Hash function a re used to find a place to store keys. 
![hash_func](/dsa_doc/imgs/hash_func.png "hash_func")<br/>

MAps have keys and values.
![hash_maps.png](/dsa_doc/imgs/hash_maps.png "hash_maps.png")<br/>
key are input to has function and store the pair in the bucket. you could give then each their own unique buckets.
Constant time to look up.

# String Keys
Invidiv

