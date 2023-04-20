"""
Simple python program that takes a DFA as input and minimizes it, using n-equivalence algorithm.
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
      for i in range(0,M):
            linie=dateintrare.readline().split(" ")
            if linie[2].replace("\n","") not in d:
                  d[linie[2].replace("\n","")]=[0] * nrstari
                  d[linie[2].replace("\n","")][stari.index(int(linie[0]))]=int(linie[1])

            else:
                  d[linie[2].replace("\n", "")][stari.index(int(linie[0]))]=int(linie[1])

      stareainitiala=int(dateintrare.readline())
      nrF=int(dateintrare.readline())
      starifinale=[int(x) for x in dateintrare.readline().split(" ")]
      nminusoneequivalence=[]
      nminusoneequivalence.append(starifinale)
      nminusoneequivalence.append([])
      for stare in stari:
            if stare not in starifinale:
                  nminusoneequivalence[1].append(stare)
      while True:
            nequivalence=[]
            for stare in stari:
                  if nequivalence==[] or [stare] in nminusoneequivalence:
                        nequivalence.append([stare])
                  else:
                        newequiv=True
                        for nequiv in nequivalence:
                              valid=True
                              for litera in d:
                                    for nminusoneequiv in nminusoneequivalence:
                                          if d[litera][stari.index(stare)] in nminusoneequiv and d[litera][stari.index(nequiv[0])] not in nminusoneequiv and stare!=nequiv[0]:
                                                valid=False
                              if valid==True and stare!=nequiv[0]:
                                    nequiv.append(stare)
                                    newequiv=False
                                    break
                        if newequiv==True:
                              nequivalence.append([stare])
            if nminusoneequivalence==nequivalence:
                  break
            else:
                  nminusoneequivalence = nequivalence.copy()
      for equiv in nequivalence:
            for litera in d:
                  for equivdest in nequivalence:
                        if d[litera][stari.index(equiv[0])] in equivdest:
                              print(equiv if len(equiv)!=1 else int(equiv[0]),equivdest if len(equivdest)!=1 else int(equivdest[0]),litera)








