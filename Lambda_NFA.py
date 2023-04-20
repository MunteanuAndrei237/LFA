"""
Simple python program that verifies if a set of symbols is accepted or not by a Lambda-NFA.
Uses data from "input.txt" as following:
on first line number of states
on second line the name of states ,separated by white space
on third line T number of transitions
on the next T lines transitions with this structure:source_state destination_state symbol('lambda' for Λ−Transitions)
on the next line the name of the starting state
on the next line F the number of final states
on the next F lines the name of one final state
on the next line W the number of "words" to be verified
on the next W lines one set of symbols
For every word there will be one otuput(yes if the word is accepted, no if the word is rejected)
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

      if "lambda" in d:
            copylambda=d["lambda"]
            while True:
                  for i in range(0,nrstari):
                        for j in range(0,nrstari):
                              for k in range(0,nrstari):
                                    if d["lambda"][i][j]==1 and d["lambda"][j][k]==1:
                                          copylambda[i][k]=1
                  if d["lambda"]==copylambda:
                        d["lambda"]=copylambda
                        break;
                  d["lambda"] = copylambda

      stareainitiala=int(dateintrare.readline())
      nrF=int(dateintrare.readline())
      starifinale=[int(x) for x in dateintrare.readline().split(" ")]
      nrcuv=int(dateintrare.readline())
      for i in range(0,nrcuv):
            cuv=dateintrare.readline().replace("\n","")
            staricurente=[0]
            staricurente[0]=stareainitiala
            for litera in cuv:
                  starenoua=False
                  valid=True
                  v=[]
                  for starecurenta in staricurente:
                        for i in range(0,nrstari):
                              if d["lambda"][stari.index(int(starecurenta))][i]==1:
                                    v.append(stari[i])
                                    starenoua=True
                  staricurente = v
                  for starecurenta in staricurente:
                        for i in range(0,nrstari):
                              if d[litera][stari.index(int(starecurenta))][i]==1:
                                    v.append(stari[i])
                                    starenoua=True
                  staricurente=v
                  if starenoua==False:
                        valid=False
            if valid==True:
                  valid = False
                  for starefinala in starifinale:
                        for starecurenta in staricurente:
                              if starecurenta==starefinala:
                                    valid=True
                  if valid==True:
                        print("YES")
                  else:
                        print("NO")
            else:
                  print("NO")



