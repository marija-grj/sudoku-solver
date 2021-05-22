---
title: Sudoku solver using Genetic Algorithm
authors: Marija Grjazniha (m20201061@novaims.unl.pt), Kostas Griska (m20200744@novaims.unl.pt)
date: May 22, 2021
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
└── sudoku.py
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
- cell - smallest element of a Sudoku grid that has coordinates (x,y) where $`x \in [1,9]`$ and $`y \in [1,9]`$ and contain one digit value.
- solved - optimal solution.

## Fitness

### Maximization of unique values

Solved Sudoku contains all 1 to 9 values in each row, column and box, or, in other words, contains maximum number (nine) of unique values in each row, column and box.  
Fitness function `evaluate_unique` calculates number of unique values withing each row, column and box, and sums those numbers. Therefore, fitness value of the solved Sudoku is `9·9·3=243` (`9` unique values in each of `9` value of `3` dimensions (row, column, box)). (Theoretically) Minimal fitness value is `1·9·3=27` when all grid values are the same.  

## Crossover

_Single point crossover_ functions split parent grids on a single point row-, column, box- or cellwise. One offspring inherit first part from parent 1 and the other from parent 2. Second offspring inherits the rest.  
Similarly, _two point crossover_ functions split parent grids on two points row-, column, box- or cellwise. One offspring inherits middle part from parent 2, and the rest from parent 1. The other one - middle of the parent 1 and the rest of parent 2.

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/crossover.png?raw=true)

## Mutation

### Swap mutation

Mutation function `swap_in_row`, `swap_in_column` and `swap_in_box` randomly selects one of nine rows (columns or boxes, depending on the function) and swaps values of two random cells that are not part of the puzzle.

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/swap_mutation.png?raw=true)

## Utils

### Box to row

![](https://github.com/marija-grj/sudoku-solver/blob/main/images/box_to_row.png?raw=true)