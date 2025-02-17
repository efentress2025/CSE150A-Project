# CSE150A-Project
* In terms of PEAS, my agent is expected to return a correct probability result within a timely manner, which is what I am currently trying to work on. My agent is also expected to work within the confines (enviornment) of CSV files and reasonably-orderded datasets. It senses and collects this data using various "pandas" API methods within python and actuates on this data by creating and returning probabilites/CPTs using the formulas and strategies we learned in lecture.
* My agent is goal-based insofar as it takes in a specified genre and attemps to find songs that are compatible with it given that song's popularity.
* My model is set up using a music database found online and fits probabilistic modeling by providing educated estimate using inferred statistics.
* I have trained and evaluated my model, and while its runtime and probability accuracy need to be optimized, I feel like I have a strong start to what I am trying to accomplish.
* So far, I have added methods to convert the data from the CSV file into a DataFrame object (which holds the data in a double-array type of structure) and attempts to compute CPTs for various conditional statements using the general formulae derived in lecture.
* Like I mentioned previously, I need to clean up my model's performance and accuracy, but I think the current foundation for it is solid.
