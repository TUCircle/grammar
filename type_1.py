# V = Variable
# T = Terminal
# R = Rules
# q = wanted string (query)
# s = current string (Default = 'S')
def type1Grammar(V,T,R,q,s='S',counter=0,ar='S'):
	# find first variable
	pos = findVariablePos(s);
	nrOfRules = len(R.get(s[pos]))
	c = ['']*nrOfRules
	cg = ['']*nrOfRules
	counter += 1
	for i in range(nrOfRules):
		if (pos == 0):
			c[i] = ''
		else:
			c[i] = s[0:pos]
		if (pos+1 < len(s)):
			c[i] += R.get(s[pos])[i]+s[pos+1:]
		else:
			c[i] += R.get(s[pos])[i]

		if (c[i] == q):
			return ar+'->'+c[i]

		posV = findVariablePos(c[i])

		if (posV is None):
			continue

		posVb = findVariablePos(c[i],-1)
		# the first/last terminals must be correct and the current string must be shorter than the query
		if ((posV == 0 or c[i][0:posV] == q[0:posV]) and (posVb == len(c[i])-1 or c[i][posVb+1:] == q[posV+1:]) and len(s) <= len(q)):
			cg[i] = type1Grammar(V,T,R,q,c[i],counter,ar+'->'+c[i])
		else:
			cg[i] = False

	# Is at least one rule possible?
	varbreak = True
	for i in range(len(R.get(s[pos]))):
		if (cg[i]):
			return cg[i]
			break
	if (varbreak):
		return False

	return False


def findVariablePos(s,direction=1):
	if direction == 1:
		A = range(len(s))
	else:
		A = range(len(s)-1,-1,-1)
	for i in A:
		if s[i].isupper():
			return i
	return None


variables 	= ['S','A','B','C','D']
terminals 	= ['a','b','c']
rules 		= {'S':['AB','AC'],'A':['aBD','Cb'],'B':['BBc','cc','C'],'C':['cAb','aCa','bc'],'D':['a','Ca']}
query 		= 'aabcacccabcaabc'
result = type1Grammar(variables,terminals,rules,query)
print(result)
