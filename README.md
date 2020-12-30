# Election_Analysis

## Project Overview
A Colorado Board of Election employee has given you the folowing tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code, 1.52.1

## Summary
### The analysis of the election show that:

- There were 369,711 total votes cast in the election.
**Code Snippet**
--------------------------------------------------------
#### County Data
--------------------------------------------------------
How the data was extracted from the csv file
 ![Extracting County Names](Resources/counting.countyvotes.If.png)
 
- The breakdown by county is as follows:
  * Arapahoe County had 24,801 votes, 6.7% of the total.
  * Denver County had 306,055 votes, 82.8% of the total.
  * Jefferson County has 38,885 votes, 10.5% of the total.
  
- The county with the largest turnout was Denver. 
**Code Snippet** 
An if statement that determines the county with the largest voter turnout.
![Decision Statmente for County votes](Resources/countydecisionstatement.png)

 ----------------------------------------------------------
 #### Election Results
 ----------------------------------------------------------
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
**Code Snippet**
 - The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette recieved 73.8% of the vote 272,892 number of votes.
  - Raymon Anthony Doane recieved 3.1% of the vote 11,606 number of votes
  
- The winner of the election was:
  - Candidate: Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
 
 ![Audit Results](https://github.com/Deelacole2/Election_Analysis/blob/main/Resources/results.ss.png) 

## Challenge Overview - Code Snippets and Explanations

Analysis was started by initializing the variables I would need. All were set to zero or empty.
 ![Variable Creation](Resources/variables2.png)
Outcomes
--- Election Results
--- Votes by County
--- Largest Turnout
--- Candidates and vote count
--- Winner of the Election
 This section will include code snippets for each election outcome.
 
 ## Challenge Audit Summary
 
 I am proposing that we can utilize this same script for elections in the future witha few minor modifications. As I have mentioned above the For loops and If statements can be modified. 
 For example: lets say that we have elction results from the much larger presidential election. There will be multiple columns of candidates for many positions with each Ballot ID. We can add additional variables to our loop as seen here, right up under county name. We just modify to the correct index number of the desired position.
 ![Adding a variable to iterate through new data](Resources/forloopthroughtcounty.names.png)
 
 In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
