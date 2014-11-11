from textblob.classifiers import NaiveBayesClassifier
with open('phish.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")
while 1:
    subject = raw_input("Email subject: ")
    print cl.classify(subject)
