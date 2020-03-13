# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.
















## Interview Questions

<!-- Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back? -->

Adding and removing from the front or back of an array is O(1).
To find something in an array depends on if you sort it or not, unsorted it's O(n)


<!-- * What is the worse case scenario if you try to extend the storage size of a dynamic array? -->

Extending the size automatically makes anything O(n) because you have to rewrite everything in the old array into the new array.  Worst case is O(n)

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

A blockchain is structured as a chain of blocks where each block contains all the transactions which occur until a miner completes a proof of work.  When the miner does a proof of work by solving an arbitrary puzzle, he transmits his proof, the transactions, and everything else inside the block to the other miners.  If the other miners verfiy his proof AND his transactions are correct, then they build on top of his proof which is effectively "voting" for it.  The longest blockchain eventually wins.  There are many pieces of data in a blockchain.  Transactions are listed in order of reciept by the miner, but this can differ due to miners being in different timezones.  Any discrepancies are "voted upon" by all the miners in a Byzantine Generals solution (the longest chain wins).  But there are other types of data, for instance BitCoin scripting language can contain signatures (private keys) which involve scripting language (a forth-like language which is Turing complete when considering the whole network) which can create smart contracts-- which allow people to do complex transactions which might alter WHEN a coin can be spent (nLockTime for instance).  There's also metadata associated with the chain, for instance, each block has a hash, and the entire chain has a hash too, thus miners who enter the network afresh can actually mine immediately by simply verifying the hash headers.  However, this is risky bc miner gamesmanship can deliberately send out faulty things to new miners such that if the new miner doesn't take the time to verify the entire blockchain history from scratch, they might run into a prloblem where the new miner finds a proof of work but it ends up not being valid (very costly).  So most miners verify the entire chain before beginning mining.  
 
<!-- Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible? -->

A PROOF OF WORK IS AN ARBITRARY PUZZLE WHICH IS SOLVED BY THE MINING CLIENT.  TYPICALLY IN BITCOIN, MINERS MUST FIND A HASH WITH A CERTAIN NUMBER OF LEADING ZEROES.  THERE IS NO GREAT ALGO WHICH CAN SHORTEN THE STRATEGY, SO MINERS TYPICALLY REPLY ON BRUTE FORCE PLUS HIGHLY SPECIALIZED ASIC MINING RIGS TO BEAT THEIR COMPETITORS TO THE COINBASE REWARDS.   OVER TIME, HOWEVER, COINBASE REWARDS HALVEN, SUCH THAT EVENTUALLY MINERS ONLY MAKE MONEY FROM MINING FEES, THUS BITCOIN IS MEANT TO SCALE TO MANY TRANSACTIONS TO PROVIDE THE MINERS THE REVENUES TO REINVEST IN THE NETWORK-- THUS MAKING IT FASTER, CHEAPER, AND MORE SECURE OVER TIME.  A PROOF OF WORK PROTECTS THE CHAIN BC MINERS MUST INVEST REAL MONEY TO SOLVE PROOFS OF WORK AS THE NETWORK GETS BIGGER.  THUS, A MINER WOULD BE CRAZY TO CHEAT THE SYSTEM (DOUBLE SPENDING FOR INSTANCE) BC HE WOULD LOSE HIS ENTIRE INVESTMENT AS THE OTHER MINERS CALL HIM OUT ON THE CHEATS/HACKS.  THUS NO SANE MINER WOULD CHEAT, OR ELSE THEY'D LOSE THE VALUE OF THEIR ENTIRE INVESTMENT IN THEIR MINER-RIG SERVER FARMS.  

AN OFT WRITEEN-ABOUT ATTACK IS A 51% ATTACK.  IF A MINER ACHIEVES 51% OF THE HASHING POWER OF THE NETWORK, HE COULD THEORETICALLY DOUBLE-SPEND AND THEN JUST VOTE ON HIS OWN BLOCKS TO ADVANCE THEM FASTER THAN THE REST OF THE NETWORK.  IN PRACTISE, HOWEVER, THIS IS AGAIN FOOLHARDY AS OTHER MINERS WOULD SIMPLY FORK AWAY FROM THE BAD CHEATING MINER AND HE'D BE LEFT ALONE AND HAVE A BAD REPUTATION BESIDES.  CUSTOMERS WOULD LIKELY DRIFT TO THE FORK WITH THE HONEST MINERS.  SO EVEN A 51% ATTACK ISN'T REALISTIC SO LONG AS THE BLOCKCHAIN ACHIEVES PROPER SCALE (MINING RIGS = EXPENSIVE).  SHENANIGANS ARE NOT EASILY POSSIBLE, BC A MINER WITH LESS THAN 51% POWER WILL NEED TO OUTCOMPETE ALL THE OTHER MINERS COMBINED TO DOUBLE SPEND.  THE CHAIN KEEPS GETTING LONGER WHILE A HACKER MINER TRIES TO CATCH UP.  IT'S SIMPLY NOT POSSIBLE OVER ANY LENGTH OF TIME WITHOUT SPENDING/WASTING TOO MUCH MONEY.  THIS MAKES BITCOIN QUITE SECURE.















## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |

## Grading
The grade for this sprint challenge is the average of the number of points received (points/15)
