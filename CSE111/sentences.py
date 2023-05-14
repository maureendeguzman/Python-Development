import random
def main():
    determiner = []
    noun = []
    verb = []
    prepositional_phrase = []
    
    
    
    
    #single	past 
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
    #single	present
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
	#single	future
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
	#plural	past
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
	#plural	present
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
	#plural	future
    print(f"{determiner} {noun} {verb} {prepositional_phrase}")
    
     
   
    
def make_sentence(quantity, tense):
   
    if quantity == 1:
        determiner = "words" 
    else:
        determiner = "words1"
        
        if quantity == 1:
            noun = noun
            verb = verb
        else:
            noun = noun + "s" 
            if tense == "present":
                verb = verb + "s"
            else:
                verb = verb + "ed"
    return determiner

def get_determiner(determiner):
 
    quantity = 1
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner= (words, words)
    cap_word = determiner.capitalize(0)
    return determiner

def get_noun(quantity):
    if quantity == 1:
        get_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        prural = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        
    word1 = random.choice(get_noun, prural)
    return word1

def get_verb(quantity, tense):
    if quantity == tense:
        get_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1:
        present_p = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1:
        present_s = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        future = [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    verb = random.choice(get_verb, present_p, present_s, future)
    get_determiner = (get_verb, present_p, present_s, future)
    return verb
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase        
# Call the main function so that
# this program will start executing.
main()    