---
title: Sudoku solver using Genetic Algorithm
authors: Kostas Griska (m20200744@novaims.unl.pt), Marija Grjazniha (m20201061@novaims.unl.pt)
date: May 28, 2021
---

## Structure

```
├── charles
│   ├── charles.py
│   ├── crossover.py
│   ├── mutation.py
│   ├── selection.py
│   └── utils.py
├── data
│   └── sudoku_data.py
├── sudoku.py
│------------------------
├── images
└── results
```

## Sudoku data

Sudoku data consists of six Sudoku puzzles:
- `basic` is a "typical Sudoku puzzle" from https://en.wikipedia.org/wiki/Sudoku
- `very_easy`, `easy`, `moderate`, `hard` and `very_hard` are puzzles of corresponding level of difficulty taken from https://www.7sudoku.com/ 

Each puzzle is a nested list with 9 elements of a size 9. Missing values are represented as zeros.  

```
basic
[[5, 3, 0, 0, 7, 0, 0, 0, 0],
 [6, 0, 0, 1, 9, 5, 0, 0, 0],
 [0, 9, 8, 0, 0, 0, 0, 6, 0],
 [8, 0, 0, 0, 6, 0, 0, 0, 3],
 [4, 0, 0, 8, 0, 3, 0, 0, 1],
 [7, 0, 0, 0, 2, 0, 0, 0, 6],
 [0, 6, 0, 0, 0, 0, 2, 8, 0],
 [0, 0, 0, 4, 1, 9, 0, 0, 5],
 [0, 0, 0, 0, 8, 0, 0, 7, 9]]
```
Sudoku solver aims to solve a given puzzle using Genetic Algorithm. 

### Rules
1. Sudoku grid is 9x9.
2. Only integers from 1 to 9 (included) are valid values.
3. Non-zero values of a puzzle are passed to all Individuals and can't be changed (e.g., mutated). 
4. Sudoku is solved if each row, column and box contains all digits from 1 to 9.

## Naming

- puzzle - a Sudoku grid with missing values that algorithm aims to solve.
- box - 3x3 sudoku subgrid ("block" or "region").
- cell - smallest element of a Sudoku grid that has coordinates `(x,y)` where `x ∈ [1,9]` and `y ∈ [1,9]` and contain one digit value.
- solved - optimal solution.

## Fitness

Solved Sudoku contains all 1 to 9 values in each row, column and box, or, in other words, contains maximum number (nine) of unique values in each row, column and box.  

-	`evaluate_unique` Sum of number of unique values in each row, column, and box.
    -	Target value: 243 (all unique).
    -	Theoretical minimum: 27 (all the same).
-	`evaluate_repetitions` Sum of repeated values in each row, column, and box.
    -	Target value: 0 (all unique).
    -	Maximal value: 216 (all values are same, i.e., 8 repetitions in each r/c/b).
-	`evaluate_unique_sq` Sum of squared number of unique values in each row, column, and box.
    -	Target value: 2187 (all unique).
    -	Theoretical minimum: 27 (all the same).
    -	Number of unique values in a specific r/c/b increased by 1, impacts fitness value differently depending on the initial number.
    -	Wider range of fitness values.


## Crossover

_Single point crossover_ functions split parent grids on a single point row-, column, box- or cellwise. One offspring inherit first part from parent 1 and the other from parent 2. Second offspring inherits the rest.  
Similarly, _two point crossover_ functions split parent grids on two points row-, column, box- or cellwise. One offspring inherits middle part from parent 2, and the rest from parent 1. The other one - middle of the parent 1 and the rest of parent 2.

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/crossover.png?raw=true)

## Mutation

### Swap mutation

Mutation function `swap_in_row`, `swap_in_column` and `swap_in_box` randomly selects one of nine rows (columns or boxes, depending on the function) and swaps values of two random cells that are not part of the puzzle.

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/swap_mutation.png?raw=true)

### Uniform mutation

Mutation function `uniform_one` converts one random (changeable) value to a different one.

## Utils

### Box to row

One of the essential functions that allows easily convert boxes into rows and back.

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/box_to_row.png?raw=true)

