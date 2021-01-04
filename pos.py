import nltk
from nltk.tokenize import PunktSentenceTokenizer

def data_to_list(data):

    pst = PunktSentenceTokenizer()
    data=data #.decode('utf-8')
    tokenized_sentence = pst.tokenize(data)
    for i in tokenized_sentence:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)
 
content =  "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal."
data_to_list(content)

 