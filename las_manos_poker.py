#• P(AAAAA) = 0.0001  quintilla
#• P(AAAAB) = 0.0045  poker
#• P(AAABB) = 0.0090  full
#• P(AAABC) = 0.0720  tercia
#• P(AABBC) = 0.1080  dos_pares
#• P(AABCD) = 0.5040  un_par
#• P(ABCDE) = 0.3024  todos_diferentes

#probabilidad de distribucion
probabilidad_distribucion={'todos_diferentes':0.3024, 'un_par':0.5040,'dos_pares':0.1080, 'tercia':0.0720, 'full':0.0045, 'poker':0.0045, 'quintilla':0.0001}

def full(n):
  j=dict.fromkeys(n,0)
  for i in n:
    j[i]+=1
  if (2 in j.values() and 3 in j.values()):
    return True
  return False

def quintilla(n):
  j1=n[0]
  for j in n:
    if j!=j1:
      return False
  return True

def poker(n):
  if(tercia(n)):
    j=dict.fromkeys(n,0)
    for i in n:
      j[i]+=1
    for y in j.values():
      if y>=4:
        return True
    return False
  else:
    return False

def tercia(n):
  j=dict.fromkeys(n,0)
  for i in n:
    j[i]+=1
  for y in j.values():
    if y>=3:
      return True
  return False


def un_par(n):
  j=dict.fromkeys(n,0)
  for i in n:
    j[i]+=1
  for y in j.values():
    if y>=2:
      return True
  return False


def dos_pares(n):
  j=dict.fromkeys(n,0)
  for i in n:
    j[i]+=1
  if un_par(n):
    u=None
    for y in j.items():
      if y[1]>=2:
        u=y[0]
        break
    del j[u]
    for y in j.values():
      if y>=2:
        return True
    return False
  else:
    return False


def todos_diferentes(n):
  return not (len(n)!=len(set(n)))
def lj(n):
  if quintilla(n):
    return 'quintilla'
  elif poker(n):
    return 'poker'
  elif full(n):
    return 'full'
  elif tercia(n):
    return 'tercia'
  elif dos_pares(n):
    return 'dos_pares'
  elif un_par(n):
    return 'un_par'
  else:
    return 'todos_diferentes'




















  




