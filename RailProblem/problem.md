## RAIL PROBLEM
Create a algorithm which is able to list out all the routes from the cityA to cityB. Algorithm must list the trains order specified by, 
1. Cheapest Train on top
1. If there are many trains with same cost, then train with less connection must come top
1. If both the above criteria are same, then the ordered alphabetically.

### Input
First line contains, `cityA cityB` with single space separation in which cityA is starting location and cityB is destination.<br>
Further line contains, `someCityA someCityB cost` where cost is the fair between `someCityA` and `someCityB`.

### Output
Lines containing `cityA someCityX .... cityB cost`, which can have multiple `someCityX` separated with single space, which connects `cityA` and `cityB` at total cost `cost`.

### Examples
#### 1. Example
- input
    ```bengaluru goa
    bengaluru goa 1000
    bengaluru mangaluru 300
    mangaluru goa 400
    ```
 - output
     ```
     bengaluru mangaluru goa 700
     bengaluru goa 1000
     ```