# Project Report - Convex Hull

## Baseline

### Design Discussion

My plan to implement this algorithm is to recursively call the convex hull function on smaller and smaller hulls, dividing the amount of work to be done in two each time. My base case for the function will be when the number of point is simply 1. This is because if there's only 1 point, it must be the hull.

To merge the hulls back together, I will simply find the upper and lower tangent. The points that make up the upper and lower tangents make up the hull. I will then continue the merging process until the whole hull is constructed. The pseudocode for doing this is quite straight forward. I will use tuples to represent points and may use the numpy to calculate the slopes of the various lines in a performative manner.

### Theoretical Analysis - Convex Hull Divide-and-Conquer

#### Time 

*Fill me in*

#### Space

*Fill me in*

## Core

### Design Discussion

For my design, my goal is to ensure that I am able to path both the baseline and core tests. I anticipate that the test with the shared tangent point will be a difficult case to handle. I will make sure that this case does not break my code by making sure that I adequately separate the point from each constituent hull that I merge.

There could be further problems when using different types of distributions to create the hull problem. The key to solving this is ensuring that my algorithm works independently of any distributional suppositions that I may have about the data.

### Empirical Data - Convex Hull Divide-and-Conquer

| N     | time (ms) |
|-------|-----------|
| 10    |           |
| 100   |           |
| 1000  |           |
| 10000 |           |
| 20000 |           |
| 40000 |           |
| 50000 |           |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

## Stretch 1

### Design Discussion

I will use the Jarvis's March gift wrapping algorithm. Instead of doing a divide and conquer that recursively split the super hull down the middle, it starts with the left most point (which is guaranteed to be on the hull) and finds the next hull point by finding the point that makes the smallest counterclockwise angle when compared to the previous point.

The idea is to continue doing this and wrap around until you arrive at the original point. This isn't as bad as a brute force algorithm but it could still technically require searching n^2 of the points. I don't expect the performance to be as good.

### Chosen Convex Hull Implementation Description

*Fill me in*

### Empirical Data

| N     | time (ms) |
|-------|-----------|
| 10    |           |
| 100   |           |
| 1000  |           |
| 10000 |           |
| 20000 |           |
| 40000 |           |
| 50000 |           |

### Comparison of Chosen Algorithm with Divide-and-Conquer Convex Hull

#### Algorithmic Differences

*Fill me in*

#### Performance Differences

*Fill me in*

## Stretch 2

I will simply use the covid-19 dataset provided to test the algorithm. I suspect that the insights will be quite interesting. It could give me an idea as to the overall size of the hull. In this case, I imagine that it would indicate how the
size and complexity of the hull increased (or decreased over time).

This would be very useful because it could provide insight into how viruses like covid-19 spread. I will parse the csv file by using the built in .split() function on python strings. I will then analyze the data using the longitude and latitude and data points.

## Project Review

*Fill me in*

