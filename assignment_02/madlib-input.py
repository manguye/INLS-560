# Mad lib example for functions.

def madlib(adverb_1,noun_1,verb_1,adverb_2,noun_2,adverb_3,noun_3,verb_2,noun_4,adverb_4,verb_3):
    """Mad lib function"""
    story =f'''
It was a {adverb_1} sunny day at the beach, and the dogs were 
having the time of their lives. They chased each other around, kicking up 
{noun_1} as they went. One dog, a golden retriever named Max, {verb_1} 
towards the water, his tail wagging {adverb_2}. Meanwhile, a small terrier 
was digging furiously in the sand, searching for the perfect {noun_2} to 
bury.

As the sun reached its peak, the dogs began to slow down. Some of them lay 
{adverb_3} on the warm sand, while others gathered around a nearby beach 
umbrella, sniffing at the {noun_3} their owners had brought along. A 
mischievous dachshund {verb_2} over to a picnic basket, trying to sneak a bite 
of someone's sandwich. The sound of the {noun_4} filled the air as the waves 
crashed gently against the shore.

By late afternoon, the dogs were exhausted but {adverb_4} content. Max and the 
terrier, now fast friends, {verb_3} together back towards their owners. They 
had spent the entire day enjoying the sun, sand, and surf, and they couldn't 
have been happier. The beach was the perfect place for a dog on a summer 
day.
'''
    
    return story

def get_user_input():
    """Prompt the user for input for the mad lib."""
    adv_1 = input("Enter an adverb: ")
    noun_1 = input("Enter a noun: ")
    verb_1 = input("Enter a verb: ")
    adv_2 = input("Enter an adverb: ")
    noun_2 = input("Enter a noun: ")
    adv_3 = input("Enter an adverb: ")
    noun_3 = input("Enter a noun: ")
    verb_2 = input("Enter a verb: ")
    noun_4 = input("Enter a noun: ")
    adv_4 = input("Enter an adverb: ")
    verb_3 = input("Enter a verb: ")

    return adv_1, noun_1, verb_1, adv_2, noun_2, adv_3, noun_3, verb_2, noun_4, adv_4, verb_3

# Get user input.
user_inputs = get_user_input()

# Print the madlib story.
print(madlib(*user_inputs))