### REGRESSION PROBLEM

### Question:
1. Finding **co-relations** of attributes ( `threshold = 0.7` means dont consider those attributes which gives corelation less than 70%)
2. Finding a **Linear Equation** ( with multiple varying attributes of form `y = b0 + b1 * x1 + ... + bn * xn` For n = No. of attributes)


### Solution:
1. **Co-relation:**
we can use **Pearson's formula** ( There are many formulas ) for finding `r`. So, this `r` is calculated between 2 attributes ( Like. x = year and y = revenue in this case )
After applying formula, using threshold we can eliminate some of the attributes `( < 0.7)`.
Regression Problem is to fine the correlation between the attributes to the dependent variable (eg: revenue depends on employees). This can be found out by using the ```Pearson's Equation``` to find the Coefficient of Correlation. Which is defined below
![Pearson's Equation](https://a8h2w5y7.rocketcdn.me/wp-content/uploads/2012/10/pearson.gif)
Using this `r`, we can select the best attribute that correlates with the Y. Hence, we can find the best fit for the regression points. This can be computed using, <br>
`Y = BX + A ` where, `Y` is dependent variable and `X` is independent variable, `B` is slope & `A` is intercept of the Linear Equation.
`  B = Sum(X) * r /Sum(Y) ` 
` A = Y - B * X` where `Y` is mean of `Y`, ` X` is mean of `X`

2. **Finding Equation:**
    1) **Linear Equation:**
	Which is of form `y = b0 + b1 * xi`. its easy to find. `b1 = (standardDev(y)/standardDev(x))*r` and then `b0 = mean(y) - mean(x) * b1` ( where b1 is already found, and mean(x) and mean(y) just finds one x,y point in which definately line passes through). This equation considers only 1 independent variable (like year, GDP etc)
    1) **Multi-Linear Equation:**
	This is similar to Linear Equation but considers more than 1 independent variable. This can be Computed using the equation `bi = inverse(transpose(xij) * xij) * xij * yj` (i = No. of attributes & j = no. of data items). Here bi contains numbers of length `n + 1` (n = how many attributes u considered).so, equation can be written as `y = b0 + b1 * x1 + ... + b(n-1) * x(n-1)`.