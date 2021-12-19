# ioet-exercise - v2
## Problematic
The company ACME offers their employees the flexibility to work the hours they want. 
But due to some external circumstances they need to know what employees
have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees
and how often they have coincided in the office.


## What to expect?
The correct solution to this problem using functional programming 

### Input
The name of an employee and the schedule they worked, indicating the time and hours.
For example:

```text
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```

### Output (Not in the exact order)
```text
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```

## Steps to run the program locally
It is important for you to have Python 3, if you don't have it 
please install Python 3.9.2 version of [Python 3](https://www.python.org/downloads/) 
in your machine.


1. ### Clone / Download
Once you know that you have Python 3 in your machine, you will 
need to clone or download this repository:
```
git clone https://github.com/cxcarvaj/ioet-exerciseV2.git
```
Once you have downloaded or cloned it, move to the project folder
and run the following command:


2. ### Usage
If you are using Windows:
```
py .\src\main.py <data-input-file>.txt
```
If you are Using Linux or Mac:
```
python3 ./src/main.py <data-input-file>.txt
```

In this repository, you will find two data input files, 
you can use both of them  or create a new one with the same structure.

## Steps to run the tests

The tests that I made are using unittest, that is a built-in library of python3.

All the test are found in [testing/test.py](https://github.com/cxcarvaj/ioet-exerciseV2/blob/main/testing/test.py). 
To run the tests:
1. You will need to go to the testing directory inside the 
project folder. 

```
cd testing
```

Once you are there, run the following commands:

If you are using Windows:
```
py .\test.py
```
If you are Using Linux or Mac:
```
python3 .\test.py
```

## Project structure

The main code can be found in the ``src`` folder in the ``main.py`` file of 
the project folder, the functions used in this program are located 
also in the ``src`` folder, but in the ``functions.py`` file.
In the root folder, there two samples of .txt file to run the program. 
There is also a unit testing file called ``test.py`` which has 7 tests that evaluates
the functions used in the solution of the problem, this file can be found 
in the ``testing`` folder.

## Solution
### Overview
This problem was solved using functional programming, built-in Python data structures
like dictionaries and list for storing data, Boolean expressions using Boolean algebra
and the use of algorithms to solve combination problems.
The functions / algorithms that were used in this problem
can be found in [src/functions.py](https://github.com/cxcarvaj/ioet-exerciseV2/blob/main/src/functions.py),
and the logic of the main function can be found in
[src/main.py](https://github.com/cxcarvaj/ioet-exerciseV2/blob/main/src/main.py).

The approach that I used to solve this problem using functional programming
was to apply the famous ``Divide and Conquer`` strategy. The main idea of this 
strategy is to divide the hole problem into small problems or subproblems/subtasks.

#### Subproblems / subtasks
* Building Employee-Schedule data structure.
* Parsing schedule string to a dictionary.
* Parsing time string to a datetime object.
* Checking if the hour ranges are coincided.
* Calculating the times that two employees schedules have coincided.
* Comparing one employee schedule to the rest of employees schedule
(avoiding comparing the same schedule or inverted pairs).

You can see a complete documentation of each function in [functions.py](https://github.com/cxcarvaj/ioet-exerciseV2/blob/main/src/functions.py):

The general program complexity is ``O(n²*m)`` due to this problem is a combinatorial one,
since we have to compare one schedule with all the others, so we can calculate 
how many times each employee has coincided in the office. Where n is the amount 
of schedules to compare and m are the days when an employee has worked.

### Unit Test
In this project I used unittest to create the tests with different 
test cases with valid and invalid arguments.

[![testsuite.jpg](https://i.postimg.cc/3JbFrCr8/testsjpg.jpg)](https://postimg.cc/tYWx26Vw)