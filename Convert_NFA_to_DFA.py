"""
Simple python program that takes a NFA as a input and transforms it into a DFA.
Uses data from "input.txt" as following:
on first line number of states
on second line the name of states ,separated by white space
on third line T number of transitions
on the next T lines transitions with this structure:source_state destination_state symbol
on the next line the name of the starting state
on the next line F the number of final states
on the next F lines the name of one final state
The output is a DFA written as a set of transitions(current state,next state,symbol)
"""
if __name__ == '__main__':
      dateintrare=open("input.txt","r")
      nrstari=int(dateintrare.readline())
      stari=[int(x) for x in dateintrare.readline().split(" ")]
      M=int(dateintrare.readline())
      d={}
      dfa = {}
      for i in range(0,M):
            linie=dateintrare.readline().split(" ")
            if linie[2].replace("\n","") not in d:
                  d[linie[2].replace("\n","")]=[[0] * nrstari for i in range(0, nrstari)]
                  d[linie[2].replace("\n","")][stari.index(int(linie[0]))][stari.index(int(linie[1]))]=1
            else:
                  d[linie[2].replace("\n", "")][stari.index(int(linie[0]))][stari.index(int(linie[1]))] = 1
            if linie[2].replace("\n", "") not in dfa:
                  dfa[linie[2].replace("\n","")]=[[]] * nrstari
      stareainitiala=int(dateintrare.readline())
      nrF=int(dateintrare.readline())
      starifinale=[int(x) for x in dateintrare.readline().split(" ")]

      stariprelucrat=stari.copy()
      newstari = stari.copy()
      stariinitiale = stari.copy()

      while True:
            for stare in stariprelucrat:
                  for litera in d:
                        starerez=[]
                        if type(stare) is int:
                              for dest in stari:
                                    if d[litera][newstari.index(stare)][newstari.index(dest)]==1 and dest not in starerez:
                                          starerez.append(dest)
                        else:
                              for staremembra in stare:
                                    for dest in stari:
                                          if d[litera][newstari.index(staremembra)][newstari.index(dest)] == 1 and dest not in starerez:
                                                starerez.append(dest)
                        if starerez not in newstari and len(starerez)>1:
                              newstari.append(starerez)
                              for litera2 in dfa:
                                    dfa[litera2].append([])
                        if len(starerez)>0:
                              if len(starerez) == 1:
                                    dfa[litera][newstari.index(stare)] = starerez[0]
                              else:
                                    dfa[litera][newstari.index(stare)] = starerez


            if stariinitiale==newstari:
                  break
            else:
                  stariprelucrat=[]
                  for x in newstari:
                        if x not in stari:
                              stariprelucrat.append(x)
                  stariinitiale = newstari.copy()
for stare in stariinitiale:
      for litera in dfa:
            print(stare,dfa[litera][stariinitiale.index(stare)],litera)






