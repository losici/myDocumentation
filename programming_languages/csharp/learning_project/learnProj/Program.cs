// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography;

Console.WriteLine("Hello, oop!");

var p1 = new Person("Scott", "Hanseleman", new DateOnly(1950,1,1));
var p2 = new Person("David", "Red", new DateOnly(1976,1,1));

p1.Pets.Add(new Dog("Fred"));
p1.Pets.Add(new Dog("Barney"));

p2.Pets.Add(new Cat("Beyonce"));

List<Person> people = [p1, p2];

foreach(var person in people)
{
    Console.WriteLine($"person {person}");
    
    foreach(var pet in person.Pets)
    {
        Console.WriteLine($" {pet}");
    }
}
Console.WriteLine(people.Count);

// class Person
// {
//     public Person(string first, string last, DateOnly bd)
//     {
//         firstName = first;
//         lastName = last;
//         birthday = bd;
//     }
    
//     private string firstName;

//     private string lastName;

//     private DateOnly birthday;
// }

class Person(string firstname, string lastname, DateOnly birthday)
{
    // only get because they are private memebers
    public string First {get;} = firstname;
    public string Last {get;} = lastname;

    public DateOnly Birthday {get;} = birthday;

    public List<Pet> Pets {get; } = new();

    public override string ToString() 
    // Every object has a tostring mwthod that returns the name of the class. 
    //I can override this to String name to give me the name of the instance of the class.
    {
        return $"{First} {Last}";
    }
}

public abstract class Pet(string firstname) 
// I use abstract because it is just a concept. You cannot declare an instance of an abstract class
{
    public string First { get;} = firstname;

    public abstract string MakeNoise();

    public override string ToString() 
    // Every object has a tostring mwthod that returns the name of the class. 
    // I can override this to String name to give me the name of the instance of the class.
    {
        return $"{First} and I am a {GetType().Name} and I {MakeNoise()}";
    }
}

// Cat is a pet : is-a relationship so we derive the class with the following syntax
public class Cat(string firstname) : Pet(firstname)
{
    public override string MakeNoise() => "meow"; // I use override 
}

// public class Cat(string firstname)
// {
//     public string First { get;} = firstname;

//     public string Meow() => "meow";
// }

public class Dog(string firstname): Pet(firstname)
{
    public override string MakeNoise() {return "bark";}
}