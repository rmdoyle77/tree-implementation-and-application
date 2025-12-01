StockScope — A Segment Tree Range Query Application

StockScope is a command-line application that uses a Segment Tree to analyze stock market time-series data. The program loads a CSV file containing dates and closing prices, builds a Segment Tree, and performs fast range queries including sum, min, max, and supports point updates. The purpose of this project is to demonstrate how a tree data structure provides major performance benefits when working with repeated range operations.


I implemented a Segment Tree, stored in an array-backed, iterative structure.
It supports:

Building from a dataset

Fast range sum queries

Fast range minimum and maximum queries

Point updates

Summary queries over all data

"What Does Your Application Do?"

Loads stock price data from a CSV file

Converts date strings into index positions

Builds a Segment Tree using the closing prices

Allows the user to run:

Range sum queries

Range min queries

Range max queries

Point updates

Full summary queries

Prints the results directly to the terminal

"Who Would Use This and Why?"

Students learning data structures who want to see a Segment Tree in action

Developers working with time-series data

Anyone needing fast repeated queries on large or frequently changing datasets

The application highlights when and why a Segment Tree is superior to scanning arrays.

Team Members

This project was completed individually.

Installation & Setup
Prerequisites

Python 3.10 or higher

CSV file with the columns:

date (YYYY-MM-DD format)

close (float)

Step-by-Step Setup

Create a project folder

Add the following files:

segment_tree.py

application.py

test_segment_tree.py

TREE_DESIGN.md

README.md

Create a data/ folder and place your CSV file inside

Open the folder in Visual Studio Code

(Optional) Create and activate a virtual environment:

python -m venv .venv


Windows: .venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

No additional Python libraries are required.

How to Run the Application

Run commands from the project folder with:

python application.py --data data/AAPL_sample.csv <command> <arguments>


Example:

python application.py --data data/AAPL_sample.csv sum 2024-01-02 2024-01-05

Usage Guide


1. Range Sum Query
python application.py --data data/AAPL_sample.csv sum 2024-01-02 2024-01-05


Output Example:

SUM 2024-01-02..2024-01-05 = 742.73


Returns the total sum of closing prices in the date range.

2. Range Minimum Query
python application.py --data data/AAPL_sample.csv min 2024-01-02 2024-01-08


Output Example:

MIN 2024-01-02..2024-01-08 = 183.63


Shows the lowest closing price in the range.

3. Range Maximum Query
python application.py --data data/AAPL_sample.csv max 2024-01-02 2024-01-08


Output Example:

MAX 2024-01-02..2024-01-08 = 190.11


Shows the highest closing price in the range.

4. Update a Price
python application.py --data data/AAPL_sample.csv update 2024-01-03 190.00


Output Example:

Updated 2024-01-03 -> 190.0


Changes a single day’s price in memory.

5. Summary of All Data
python application.py --data data/AAPL_sample.csv all


Output Example:

ALL: sum=XXXXXX.xx, min=XXX.xx, max=XXX.xx


Prints the overall total sum, min, and max for the entire dataset.

Tree Implementation Details
How the Segment Tree Works

Stores values in a complete binary tree represented as a Python list

Leaves hold the price data

Internal nodes store:

Sum of their range

Min of their range

Max of their range

The tree is built bottom-up in O(n) time

Queries and updates run in O(log n) time

Time & Space Complexity
Operation	Time	Space
Build	O(n)	O(n)
Range Sum	O(log n)	O(1)
Range Min	O(log n)	O(1)
Range Max	O(log n)	O(1)
Update	O(log n)	O(1)
Query All	O(1)	O(1)
Interesting Implementation Choices

Fully iterative approach avoids recursion overhead

Uses a power-of-two base to simplify indexing

Maintains three parallel arrays (sum, mn, mx) to avoid tuples and reduce overhead

Evolution of the Interface
Initial Design

Originally included only:

build()

query_sum()

update()

Added During Development

query_min() and query_max()
Needed for more complete analysis.

query_all()
Required for the all command to quickly summarize the dataset.

size()
Useful for validation and future enhancements.

Lessons Learned !

Interfaces evolve naturally when building real applications

Initial assumptions rarely cover all needed functionality

Segment Trees become more powerful when extended beyond simple sums

Challenges & Solutions
Challenge 1: Mapping Dates to Indices

Solution: A dictionary (date_to_idx) maps date strings to tree indices.

Challenge 2: Validating Dates

Solution: datetime.strptime checks proper formatting; missing dates produce clear error messages.

Challenge 3: Avoiding Off-by-One Errors

Solution: Standardized all queries to inclusive ranges [l, r].

Challenge 4: Verifying Correctness

Solution: Created test_segment_tree.py that checks all operations against Python’s built-in sum, min, and max.

Future Enhancements

Add lazy propagation for range updates

Add argmin/argmax functions to return the index of min/max values

Add CSV export to save updated values

Add a graphical or web-based interface

Provide more analytics such as moving averages or volatility