from pfd import convertor
from HelpPsc import models
e=convertor.f
for i in e:

    a=models.Psc(question=i,apple=e[i][0],boy=e[i][1],cat=e[i][2],dog=e[i][3],answer=e[i][4],category='Dental')
    a.save()
