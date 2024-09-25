words = [

  '2021182035', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 

  'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude', 

  'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor', 

  'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck', 

  'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote', 

  'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop', 

  'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise', 

  'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse', 

]

def heapify(root, size):
  left_child = root * 2 + 1
  if left_child >= size: return
  child = left_child
  right_child = root * 2 + 2
  if right_child < size:
    if words[left_child] < words[right_child]:
      child = right_child
  
  if(words[root] < words[child]):
    words[root], words[child] = words[child], words[root]
    heapify(child, size)
  pass
  
def main():
  count = len(words)
  parents_last_index = count // 2 + 1
  for i in range(parents_last_index, -1, -1):
    heapify(i, count)

  sort_last_index = count - 1
  while sort_last_index > 0:
    words[0], words[sort_last_index] = words[sort_last_index], words[0]
    heapify(0, sort_last_index)
    sort_last_index -= 1
  pass

  print("sorted: ", words)
if __name__ == '__main__':
  main()

