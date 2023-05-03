from filters_parag import filterMap as filterMapByParag
from filters_krishna import filterMap as filterMapByKrishna

filterMap = {}

for k in filterMapByParag.keys():
    filterMap[k] = filterMapByParag[k]

for k in filterMapByKrishna.keys():
    filterMap[k] = filterMapByKrishna[k]
