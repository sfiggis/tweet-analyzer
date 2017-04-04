import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # TODO
        #create structure (list)
        self.positives = set()
        self.negatives = set()
        
        #open positive words file and read each line
        pos_file = open("positive-words.txt", "r")

        for line in pos_file:
            #find start of words and end of comments
            #ommit lines with nothing in them
            if not line.startswith(";") or not line.startswith(""):
                #extract data from txt file and send to analyze
                self.positives.add(line.rstrip("\n"))
                #print(self.positives)
        pos_file.close
        
        #do the same as above for negative file
        neg_file = open("negative-words.txt", "r")
        
        for line in neg_file:
            if not line.startswith(";") or not line.startswith(""):
                self.negatives.add(line.rstrip("\n"))
        neg_file.close
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        #tokenize text to split up into words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        #iterate through text
        score = 0
        for line in tokens:
                #iterate over tokens
            for token in tokens:
                    #if token in pos_file, assign 1
                if str.lower(token) in self.positives:
                    score += 1
                    #if token in neg_file, assign -1
                elif str.lower(token) in self.negatives:
                     score -= 1
                    #if token is not in either dict, assign 0
                else:
                    score = score
                #score = score + token
        return score
