from  collections import Counter


# read corpus.txt 
# convert it into lowercase
# split each lines and get list of all words in lower case
wordList = open("corpus.txt").read().lower().splitlines()  

def autoComplete(query,prefix,max_count):

    if(query.lower() == "complete"): # check query is correct or not

        # find all words in wordList which are starts with prefix
        matchingWords = list(filter(lambda x: x.lower().startswith(prefix),wordList))

        # get count of occurence for each word using collections module
        # highly occered words 
        autoCompleteResult = [word[0] for word in Counter(matchingWords).most_common(int(max_count))]
        
        if(len(autoCompleteResult)>0):# if we have one or more than one suggestion return list
            return autoCompleteResult
        else:
            return [] # else return empty list
    
    else: # if query is not equal to "complete" return message
        return 'please provide "complete" as query'

