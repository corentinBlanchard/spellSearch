import json
from os import name
from search.models import Sorts, Monster, Classes

with open('datas/sortsCarac_url.json') as f:
  sortsCarac = json.load(f)

with open('datas/sortsMonster.json') as f:
  sortsMonster = json.load(f)

print(len(sortsCarac))
print(len(sortsMonster))

# Sorts.objects.all().delete()
Monster.objects.all().delete()
# Sorts.objects.all().delete()

monstersList = []
for sort in sortsMonster:
    monsters = sort["_2"].split(";")
    for i in monsters:
      if i != ' ':
        if i[0] == " ":
          i = i[1 : : ]
        if i not in monstersList:
          monstersList.append(i)
      
for monster in monstersList:
  m = Monster.objects.get_or_create(name=monster)

classList = []

for sort in sortsCarac:
  classe = sort["level"]
  for c in classe:
    if c[0] not in classList and c[1] is not None and c[0] != "0":
      classList.append(c[0])

for c in classList:
  component = Classes.objects.get_or_create(name = c)



for sort in sortsCarac:
  name = sort["title"].lower().strip()
  spell_resistance = sort["spell_resistance"]
  components = sort["component"]
  carac = sort["level"]
  url = sort["url"]
  max_level = 0
  levelList = []
  for c in carac :
    if c[1] is not None and c[0] != "0":
      levelList.append(Classes.objects.filter(name = c[0])[0])
      if c[1] > max_level:
        max_level = c[1]
  is_verbal = False
  is_somatic = False
  is_material = False
  for c in components:
    if c[0] == "V":
      is_verbal = True
    elif c[0] == "S":
      is_somatic = True
    elif c[0] == "M":
      is_material = True
  
  exist = Sorts.objects.filter(name = name).exists()

  sort = Sorts.objects.get_or_create(name = name, is_material = is_material, is_verbal = is_verbal, is_somatic = is_somatic, max_level = max_level, url = url)
  
  if not exist:
    sort = Sorts.objects.filter(name = name)[0]
    for l in levelList:
      sort.classes.add(l)

for s in sortsMonster:
  if Sorts.objects.filter(name = s["_1"].lower().strip()).exists():
    sort = Sorts.objects.filter(name = s["_1"].lower().strip())[0]
    monsters = s["_2"].split(";")
    for i in monsters:
      if i != ' ':
        if i[0] == " ":
          i = i[1 : : ]
        monster = Monster.objects.filter(name = i)[0]
        sort.monsters.add(monster)






