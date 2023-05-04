from filters_parag import filterMap as filterMapByParag
from filters_krishna import filterMap as filterMapByKrishna
from filters_piyush import filterMap as filterMapByPiyush

filterMap = {}

for k in filterMapByParag.keys():
    filterMap[k] = filterMapByParag[k]

for k in filterMapByKrishna.keys():
    filterMap[k] = filterMapByKrishna[k]

for k in filterMapByPiyush.keys():
    filterMap[k] = filterMapByPiyush[k]
