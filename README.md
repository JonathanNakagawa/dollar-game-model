# dollar-game-model
Models the probability of winning a LCR dollar based on starting location and number of players. 
The rules of the LCR game are as follows. 

**Rules**

N people sit in a circle.
Each person starts with three one dollar bills. 
The first player roles three specially sided dice.
Each die has "L" and "R" each marked on one side, "C" marked on two sides, and the remaining two sides left blank.
For every L rolled the roller passes a dollar to the person on the left. 
For every R rolled the roller passes a dollar to the person on the right.
For every C rolled the roller puts a dollar in the center.
After rolling and exchanging money, the roller passes the dice to the person to his or her right.
This process continues until only one person has any money left. 
This person wins all the money in the center. 

**Clarifications**

If one loses all one's money, one retains one's position in the circle.
So, if the person to the left or right passes money to the person with none left that person reenters the game.
Furthermore, the number of dice rolled is the the same number as how many dollars the player has up to three dollars.
When the player has more than three dollars, three dice are still rolled. 


**Results**

Change of winning by position over 1,000,000 trials.

| Number of players | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|-------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|3                  |0.27012|0.312865|0.417015|x|x|x|x|x|x|
|4                  |0.215831|0.229563|0.261186|0.29342|x|x|x|x|x|
|5                  |0.177088|0.180215|0.197916|0.218018|0.226763|x|x|x|x|
|6                  |0.149386|0.149315|0.157866|0.172208|0.186064|0.185161|x|x|x|
|7                  |0.128955|0.126312|0.132067|0.141594|0.152869|0.16134|0.156863|x|x|
|8                  |0.113061|0.109884|0.113643|0.120181|0.128441|0.137185|0.142253|0.135352|x|
|9                  |0.100232|0.097063|0.100443|0.104796|0.109904|0.116526|0.124323|0.127473|0.11924|


