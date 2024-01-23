# Decorators
## @staticmethod
We can decorate a function with @staticmethod to prevent Python from passing an instance of the object to it, as below. This can be useful when we have functionality that logically belongs in a given class, but does not do anything with the instance it's called on.