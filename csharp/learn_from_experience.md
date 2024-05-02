# Some basics
This page contains learning from experience tools.
[[_TOC_]]

## Create array
```
int[] sophiaScores = new int[5];
```
## lambda Expressions
`point => point.X`: This is a lambda expression. It defines an inline anonymous function that takes a single parameter (point) and returns the value of the X property of that point.
So, when you put it all together, points.Average(point => point.X) reads as "calculate the average of the X property for each element (point) in the collection of points." It's a concise way to compute the average of a specific property across all elements in a collection using LINQ.

'''
IReadOnlyList<MachinePoints> points = GetMachinePoints();
// Compute mean, min, max for X
double meanX = points.Average(point => point.X);
double minX = points.Min(point => point.X);
double maxX = points.Max(point => point.X); 
'''

## FOREACH VS ZIP IN C#
```
List<int> list1 = new List<int> { 1, 2, 3 };
List<char> list2 = new List<char> { 'a', 'b', 'c' };
// Example using a for loop
Console.WriteLine("Using a for loop:");
var resultsForLoop = new List<string>();
for (int i = 0; i < Math.Min(list1.Count, list2.Count); i++)
{
    var result = Func(list1[i], list2[i]);
    resultsForLoop.Add(result);
    Console.WriteLine(result);
}
Console.WriteLine();
// Example using Zip
Console.WriteLine("Using Zip:");
var resultsZip = list1.Zip(list2, Func).ToList();
```

## FOREACH vs FOR
TBD

## Check For Nullability
Do this
```
measurement.SurfaceError = surfaceError ?? SurfaceError.Default;
```
Instead of this:
```
if( surfaceError != null )
{
	measurement.SurfaceError = surfaceError;
}
else
{
	measurement.SurfaceError = SurfaceError.Default;
}
```
