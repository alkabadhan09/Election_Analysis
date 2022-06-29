# Election Analysis
## Overview of Election Audit
The purpose of this project was to assist Tom, a Colorado Board of Elections employee, in performing an Election Audit of a recent local congressional elections. Tom's manager wants to know if there's a way to automate the process using Python. If done efficiently and successfully, the manager wants to use the same code for other congressional and senatorial elections.  We analyzed the dataset that was given and produced the results in following categories:
1. Total number of votes cast
2. A list of candidates in the elections
3. Total number and percentage of votes that the candidates received
4. The winner of election based on popular vote
5. The voter turnout for each county
6. The percentage of votes from each county out of the total count
7. The county with the highest turnout

## Election-Audit Results
* Total number of votes cast in the election
369,711
* Total number of votes and the percentage of votes for each county:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
* County with the largest number of votes:
Denver
* Total number of votes and percentage of votes each candidate received:
Charles Casper Stockhan: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
* Winning candidate, their vote count, and percentage of total votes:
Diana DeGette is the winner with 272,892 votes which is 73.8% of the total votes.
image

## Election-Audit Summary
This script is highly manipulable since all the variables are clearly defined and there are comments for all the steps taken. If the election comminssion wants to make any modifications for future elections, they can do so easily by changing the data file and essentially setting more suitable variables. 
This script can be used on a bigger scale to analyze the Senatorial Elections that are conducted on the state level. The possible modification from the dataset could be to switch the county with the state and an addition could be to identify the political party that the candidate represents. 
This script can also be used in analyzing small scale local elections, such as the School Board Elections. The possible modifications could be districts instead of counties but the code should still work with a little tweaking.  