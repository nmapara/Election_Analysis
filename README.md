# Election_Analysis

## Project Overview
A Colorado Board of Elections employee asked that we complete the election audit of a recent local congressional election.  The election data was provided in the form of a CSV file format.

We were asked to:
1. Calculate the number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

We were also asked to study the counties for voter turnout, and determine:
1. Calculate the number of votes cast in each county
2. Determine the county with the greatest number of votes (or voter turnout)

##Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

##Election Audit Results

###Candidate Voting
The analysis of the slection show that:
- There were 369, 711 votes cast in the election.
- The canidates were:
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

The Candidates results were:
Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
Diana DeGette received 73.8% of the vote and 272,892 votes.
Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

-The winner of the election was
Diane DeGette who received 73.8% of the vote and 272,892 votes.

###County Voter Turnout
The analysis of the data showed that
- There were three counties involved in the election:
- Jefferson
- Denver
- Arapahoe

The county results were:
Jefferson had 38,855 votes or 10.5% of the total voter turnout.
Denver had 306,055 votes or 82.8% of the total voter turnout.
Arapahoe had 24,801 or 6.7% of the total voter turnout.

-The county with the largest voter turnout was Denver.

##Election Audit Summary
The script we used was based on the python code developed during the learning sections of module 3.
To incorporate the county data into the analysis, we followed similar algorithms that were used in the study
of the voter data information.  In most instances, variables that were used to study the voter data were just renamed to anlayze county data, with similar algoriths and calculations.  Because the county data was just another column in the original CSV file, it was relatively easy to conduct the county analysis.  
Rather then picking the candidate with the most votes, we determined the county with the most votes (or 
voter turnout).

###Use of Script for General Elections
The script developed could be used for general elections since there were no fixed variables defined
in the code that would limit the number of candidates or the number of counties.
In the figure below, we see the lines of code that were used to read the rows:

![Graph](/Resources/Input1.PNG)

If we wanted to make the code useable for general elections, the following should be considered:
1. There are no states used in this code and we would need to modify the input file, and the code to account
for the results for each state (and it's potential impact on the electoral college)

2. The code does not handle a situation where there is a tie between two candidates.  In the event that the 
candidate vote count is equal for two candidate, and new statement needs to be written requesting a recount.


