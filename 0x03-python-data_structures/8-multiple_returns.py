#!/usr/bin/python3
def multiple_returns(sentence):
	if sentence == "":
		return (0, None)
	else:
		l = len(sentence)
		a = sentence[0]
		return (l, a)
