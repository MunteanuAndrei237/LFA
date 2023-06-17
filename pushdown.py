#simple python project that implements a pushdown automata and verifies if a word is accepted by it
#reads data from input.txt as follows:
#first line, pushdown's states separated by space
#second line, pushdown's input alphabet separated by space
#third line, pushdown's stack alphabet separated by space
#fourth line, pushdown's starting state
#fifth line, pushdown's starting stack(usually Z)
#sixth line, pushdown's final states separated by space
#seventh line,n(the number of transitions)
#next n lines, a transition on every line ( current state, current alphabet letter, current stack letter,new state,new stack letter(s))
#last line, a word to be validated by the pushdown
#output is either true or false,true if the word is accepted by it, and false otherwise
if __name__ == '__main__':
    dateintrare=open("input.txt","r")
    states=dateintrare.readline().replace("\n","").split(" ")
    inputalphabet=dateintrare.readline().replace("\n","").split(" ")
    stackalphabet=dateintrare.readline().replace("\n","").split(" ")
    startingstate=dateintrare.readline().replace("\n","")
    startingstack=dateintrare.readline().replace("\n","")
    finaslstates=dateintrare.readline().replace("\n","").split(" ")
    numberoftransitions=int(dateintrare.readline().replace("\n",""))
    transitions=[]
    stack=[]
    currentstates=[]
    stack.append(startingstack)
    currentstates.append(startingstate)
    for i in range(0,numberoftransitions):
        t=dateintrare.readline().replace("\n","").split(',')
        transitions.append(t)
    word=dateintrare.readline()
    newstates=[]
    for letter in word:
        if newstates != []:
            currentstates = newstates.copy()
        newstates = []
        for s in currentstates:

            for t in transitions:
                if t[0] == s and stack[len(stack)-1]==t[2]:
                    if t[1]==letter or t[1]=="lambda":
                        newstates.append(t[3])
                        stack.pop()
                        if t[4]!="lambda":
                            rev=list(t[4])
                            rev.reverse()
                            for l in rev:
                                stack.append(l)
                        break
    currentstates = newstates.copy()
    infinalstate=False
    for cs in currentstates:
        for fs in finaslstates:
            if cs==fs:
                infinalstate=True

    if stack==['Z'] and infinalstate==True:
        print(True)
    else:
        print(False)

"""
input.txt
q0 q1 q2
a b
A Z
q0
Z
q2
5
q0,a,Z,q0,AZ
q0,a,A,q0,AA
q0,b,A,q1,lambda
q1,b,A,q1,lambda
q1,lambda,Z,q2,Z
aabbs
"""




