"""
Simple python program that verifies if a set of symbols is validated or not by a DFA.
Uses data from "input.txt" as following:
on first line number of states
on second line the name of states ,separated by white space
on third line T number of transitions
on the next T lines transitions with this structure:source_state destination_state symbol
on the next line the name of the starting state
on the next line F the number of final states
on the next F lines the name of one final state
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
                  d[linie[2].replace("\n","")]=[[0] * nrstari for i in range(0, nrstari)]
                  d[linie[2].replace("\n","")][stari.index(int(linie[0]))][stari.index(int(linie[1]))]=1

            else:
                  d[linie[2].replace("\n", "")][stari.index(int(linie[0]))][stari.index(int(linie[1]))] = 1

      stareainitiala=int(dateintrare.readline())
      nrF=int(dateintrare.readline())
      starifinale=[int(x) for x in dateintrare.readline().split(" ")]
      nrcuv=int(dateintrare.readline())
      for i in range(0,nrcuv):
            cuv=dateintrare.readline().replace("\n","")
            starecurenta=stareainitiala
            for litera in cuv:
                  starenoua=False
                  valid=True
                  for i in range(0,nrstari):
                        if d[litera][stari.index(int(starecurenta))][i]==1:
                              starecurenta=stari[i]
                              starenoua=True
                              break;
                  if starenoua==False:
                        valid=False

            if valid==True:
                  valid = False
                  for starefinala in starifinale:
                        if starecurenta==starefinala:
                              valid=True
                  if valid==True:
                        print("DA")
                  else:
                        print("NU")
            else:
                  print("NU")




