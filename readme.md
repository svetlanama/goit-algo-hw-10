# Comparison of Coin Change Algorithms

This document compares two approaches for solving the coin change problem: a greedy algorithm and a dynamic programming algorithm. The goal is to determine the optimal way to provide change to a customer using a given set of coins: [50, 25, 10, 5, 2, 1].

## 1. Greedy Algorithm: `find_coins_greedy`

### Description
The greedy algorithm `find_coins_greedy` works by iteratively selecting the largest possible coin denomination that is less than or equal to the remaining amount. This process continues until the amount to be changed becomes zero.

### Example
For an amount of 113, the greedy algorithm would produce:
- 50: 2 (113 - 100 = 13)
- 10: 1 (13 - 10 = 3)
- 2: 1 (3 - 2 = 1)
- 1: 1 (1 - 1 = 0)
Result: `{50: 2, 10: 1, 2: 1, 1: 1}`
**Actual Execution Time for 113: 0.000004 seconds**

### Efficiency
The time complexity of the greedy algorithm is \\(O(N)\\\), where \\(N\\) is the number of coin denominations. In practice, it's very fast because it only involves a few iterations over the fixed set of coins.

### Performance with Large Sums
For standard coin systems (where larger denominations are multiples of smaller ones, or at least a good greedy choice always leads to an optimal solution), the greedy algorithm performs exceptionally well with large sums. It maintains its linear time complexity relative to the number of coin denominations, making it very efficient.

## 2. Dynamic Programming Algorithm: `find_min_coins`

### Description
The dynamic programming algorithm `find_min_coins` builds up a solution from the bottom, starting with smaller amounts and progressively calculating the minimum number of coins for larger amounts. It uses an array (or memoization table) to store the minimum number of coins needed for each amount up to the target sum. This ensures that each subproblem is solved only once.

### Example
For an amount of 113, the dynamic programming algorithm would find the optimal solution, which is indeed the same as the greedy algorithm in this specific case with standard coin denominations.
Result: `{50: 2, 10: 1, 2: 1, 1: 1}`
**Actual Execution Time for 113: 0.000156 seconds**

### Efficiency
The time complexity of the dynamic programming algorithm is \\(O(Amount \\times N)\\\), where \\(Amount\\) is the target sum and \\(N\\) is the number of coin denominations. This is because it iterates through each amount from 1 to the target sum and for each amount, it considers all available coin denominations.

### Performance with Large Sums
For very large sums, the dynamic programming algorithm can become significantly slower due to its linear dependency on the `amount`. The `Amount` factor in its time complexity means that as the target sum grows, the execution time increases proportionally.

## Comparison and Conclusion

| Feature             | Greedy Algorithm (`find_coins_greedy`) | Dynamic Programming (`find_min_coins`) |
| :------------------ | :--------------------------------------- | :--------------------------------------- |
| **Optimality**      | Optimal only for "canonical" coin systems (like EUR, USD) | Always optimal (finds minimum coins)    |
| **Time Complexity** | \\(O(N)\\\)                                  | \\(O(Amount \\times N)\\\)                  |
| **Speed**           | Very fast, especially for large sums     | Slower for large sums due to dependence on `Amount` |
| **Actual Performance (113)** | ~0.000004 seconds | ~0.000156 seconds |
| **Actual Performance (1000)** | ~0.000004 seconds | ~0.000694 seconds |
| **Simplicity**      | Simpler to implement                     | More complex to implement                |

### Why one is more effective than the other in certain situations:

-   **Greedy Algorithm:**
    -   **More Effective When:** The coin system is "canonical" (e.g., [50, 25, 10, 5, 2, 1]), meaning that a greedy choice at each step always leads to the overall optimal solution. It is significantly faster and simpler to implement.
    -   **Less Effective When:** The coin system is non-canonical. For example, with coins [1, 3, 4] and a target of 6, greedy would give {4:1, 1:2} (3 coins), while optimal is {3:2} (2 coins).

-   **Dynamic Programming Algorithm:**
    -   **More Effective When:** The optimality of the solution is paramount, especially for arbitrary coin systems where a greedy approach might not yield the minimum number of coins. It guarantees the optimal solution.
    -   **Less Effective When:** The target sum is very large and computational time is a critical factor, as its performance degrades linearly with the target sum.

**Conclusion:** For typical currency systems like the one provided ([50, 25, 10, 5, 2, 1]), the greedy algorithm is generally preferred due to its simplicity and superior performance for large sums, as it still yields the optimal solution. However, for more general coin systems where greedy choices might not lead to an optimal solution, dynamic programming is the correct and necessary approach to guarantee the minimum number of coins.

## 3. Monte Carlo Integration: `task2.py`

### Description
This task demonstrates the Monte Carlo method for approximating definite integrals, comparing its results to those obtained from `scipy.integrate.quad` for analytical calculation. The function integrated is \(f(x) = x^2\) from \(a = 0\) to \(b = 2\).

### Results
Monte Carlo Integral Estimate: 2.677200
Analytical Integral (quad) Estimate: 2.666667
Absolute Error for quad: 2.960595e-14

--- Conclusions ---
Difference between Monte Carlo and Analytical: 0.010533
The Monte Carlo method provides an approximation of the integral. Its accuracy depends on the number of random points used. With a larger number of points (e.g., 100,000), the estimate gets closer to the true analytical value. The `scipy.integrate.quad` function provides a highly accurate (nearly exact) numerical integration result, which serves as a good benchmark for comparison.
