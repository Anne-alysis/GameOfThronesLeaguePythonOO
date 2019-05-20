# GameOfThronesLeaguePythonOO
Python object oriented version of [original GameOfThronesLeague](https://github.com/Anne-alysis/GameOfThronesLeague) 
 and [Spark/Scala version](https://github.com/Anne-alysis/GameOfThronesLeagueSpark).  


# Introduction

In honor of the final season of Game of Thrones, we put together a fantasy league!  Each participant fills
out a form we developed before the start of the season. Week by week, possible answers to each question are updated, and 
are scored by an algorithm. I developed the scoring algorithm that is in this repo. The form itself is accessible by Google 
forms and is not included here. Questions and current correct answers can be viewed in the file, `resources/correct_answers.xlsx`. 

Example questions include:
 
 * Whether a character lives or dies
 * Who rides a dragon
 * Who ends up on the Iron Throne (if it still exists)

At the end of the season, the top ranked team wins a prize and the Iron Throne. 


# General Code Structure

This code will be run weekly and scores recalculated based on new information in each week's episode.  Week by 
week the correct answers will be updated, and responses re-evaluated against changing information (e.g., 
a character dies).

0) Read in all file names from a yaml configuration file (`resources/file_paths.yaml`). 
1) The code reads in the responses from a downloaded CSV (`resources/Fantasy Game of Thrones Responses.csv`)
2) Responses are reshaped to allow for ease of scoring
3) Answers from a Excel sheet are read in (`resources/correct_answers.xlsx`)
4) Scores are computed 
5) Scores are written to a CSV (`resources/Results.csv`).  


# Running the code

Because this version of the code was written after the season was completed, the `week` input parameter is ignored.  

`> python score.py ${week_value}`

# Code

## `main.py`

Where all the action happens.  Short script that identifies only the salient points of the algorithm, with all 
implementations abstracted into classes and modules.  

## `classes` package
The bulk of this repo is based around three base object stuctures: `Team`, `Response`, and `Question`.

### `Team` Class
This object keeps track of the metadata of the teams, such as name, pay type, money split preference.  These 
instances variables are updated initially.  After scoring the total score per team is also updated incrementally.  A list
of `Team` objects is used throughout.  

### `Question` Class
This is the main object structure of the program.  Each represents a single question, which consists of a number, text, a correct
answer, point values, and a list of `Response` objects for that particular question.  When a correct answer becomes 
available, week-over-week, the `correct_answer` instance variable is updated.  

### `Response` Class
Each team and question combination has a single `Response` instance. The variables include the team, raw response, 
if the response is correct, and the point value to be used in summing up the total score.  The boolean for the instance variable
 `is_correct` will be updated as the questions become available.  Initially, the score per response is set to 0.  
 
  

## `io` package 
### `input_handling.py` module 

This is a collection of methods to handle:
* Reading in of the raw data.
* Cleaning of the questions (such as standardizing the numbers with zero-padding). 
* Writing the cleaned questions to a file for updating week-over-week with correct answers/
* Reading in the correct answers.  
* Populating the list of Question objects, including a list of Response objects (one per each team) for each question.

### `output_handling.py` module 
Converts the final list of Teams into a DataFrame for ease of ranking and writing to an output CSV.   
 
## `calculations` in the `calculations` package 
This module takes in the list of `Question` objects and the dictionary of correct answers and: 
* Populates the correct answers per question .
* Sets the boolean value for `is_correct` for each team/question combination.
* Calculates the score per team and question, based on the boolean `is_correct` 
* Sums up the total score for each `Team` and writes to an output file.  