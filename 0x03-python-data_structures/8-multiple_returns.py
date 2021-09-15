#!/usr/bin/python3
def multiple_returns(sentence):
	l = len(sentence)
	a = sentence[0]
	if sentence == ():
		return (l, None)
	else:
		return (l, a)
