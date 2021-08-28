import difflib

text1 = 'Since 1958.'

text2 = 'Since 1958'

print(str(int(difflib.SequenceMatcher(None, text1, text2).ratio()*100)))

def 