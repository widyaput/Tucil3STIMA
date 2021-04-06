from math import *

class PrioQueueMod(object):
  def __init__(self):
    self.queue = []
  def isEmpty(self):
    return len(self.queue) == 0

  def isMember(self,data): #based on key
    for i in range(len(self.queue)):
      if (self.queue[i][0] == data):
          return True
    return False

  def nthIndex(self, data): #based on key
    for i in range(len(self.queue)):
      if (self.queue[i][0] == data):
        return i
    return -1

  def insert(self,data): #always update the value of f(n), now data consist of gn and hn
    if (self.isMember(data[0])):
      self.queue.pop(self.nthIndex(data[0]))
      self.insert(data)
      return
    self.queue.append(data)
    if (len(self.queue) > 1):
      idxPred = len(self.queue)-2
      while (idxPred >= 0 and self.queue[idxPred][1]+self.queue[idxPred][2] > data[1]+data[2]):
        self.queue[idxPred+1] = self.queue[idxPred]
        self.queue[idxPred] = data
        idxPred -= 1
  
  def delete(self):
    return self.queue.pop(0)

  def show(self):
    for i in range(len(self.queue)):
      print(str(self.queue[i][0]) + " dengan value g(n): " + str(self.queue[i][1]) + " dan value h(n) : " +str(self.queue[i][2]))
  
  def getFnKey(self,idx):
    dummy = self.nthIndex(idx)
    if (dummy == -1):
      return 0
    return self.queue[dummy][1] + self.queue[dummy][2]

def distanceInMeter(lat, lng, lat0, lng0):
  x1 = radians(lat)
  x2 = radians(lat0)
  y1 = radians(lng)
  y2 = radians(lng0)
  difx = x1-x2
  dify = y1-y2
  a = sin(difx/2)**2 + cos(x1)*cos(x2)*sin(dify/2)**2
  c = 2 * asin(sqrt(a))
  r = 6378137
  return r*c 

def bacaFile(namaFile):
  #ini buat baca grafnya
  #yang direturn : adjMatrix, listNode, listCoor, status
  #status nandain berhasil buka atau gak
  #walau kayanya nanti maneh setting biar selalu berhasil hehe
  try:
    f =open('../test/'+ namaFile, 'r')
  except IOError:
    return [[]],[],[],False
  N = int(f.readline())
  adjMatrix = [[(-1) for i in range(N)] for i in range(N)]
  listNode = []
  listCoor = []

  for i in range(N):
    line = f.readline()
    idxSpace = line.find(" ")
    coorx = float(line[0:idxSpace])
    dummy = idxSpace
    idxSpace = line.find(" ", dummy+1)
    coory = float(line[dummy+1:idxSpace])
    listCoor.append((coorx,coory))
    listNode.append(line[idxSpace+1:-1])
  
  idx1 = 0
  line = f.readline()
  while line != "":
    dummy = 0
    idxSpace = line.find(" ")
    idx2 = 0
    while (idxSpace != -1):
      adjMatrix[idx1][idx2] = int(line[dummy:(idxSpace+1)])
      dummy = idxSpace +1
      idxSpace = line.find(" ", dummy)
      idx2 += 1
    if (idx1 == N-1) : adjMatrix[idx1][idx2] = int(line[dummy:])
    else : adjMatrix[idx1][idx2] = int(line[dummy:-1])
    idx1 += 1
    line = f.readline()
  f.close()
  return adjMatrix, listNode, listCoor, True

def find(array, element):
  try:
    dummy = array.index(element)
  except ValueError:
    return -1
  return array.index(element)

def isWeightedGraf(adjMatrix):
  for i in range(len(adjMatrix)):
    for j in range(len(adjMatrix[i])):
      if (adjMatrix[i][j] > 1):
        return True
  return False

def middlePoint(listCoor):
  lat = 0
  long = 0
  for i in range(len(listCoor)):
    lat += listCoor[i][0]
    long += listCoor[i][1]
  return (lat/len(listCoor),long/len(listCoor))

def hitungJarakPath(adjMatrix,path,listCoor):
  jarak = 0
  if (isWeightedGraf(adjMatrix)):
    current = 0
    while (current != len(path)-1):
      jarak+= adjMatrix[path[current]][path[current+1]]
      current+=1
  else:
    current = 0
    while (current != len(path)-1):
      jarak+= distanceInMeter(listCoor[path[current]][0],listCoor[path[current]][1], listCoor[path[current+1]][0],listCoor[path[current+1]][1])
      current += 1
  return jarak
  
def main(adjMatrix,listNode,listCoor,node1,node2):
  #ASUMSI : BACA FILE BERHASIL, SEHINGGA ADJMATRIX LISTNODE LISTCOOR TINGGAL DIPAKE
  #return path (isinya indeks-indeks node dari ListNode yang jadi path)
  #mapping keempat list/matriks menggunakan indeks
  #jadi kalau mau liat simpul ke 0 dari path namanya apa, tinggal panggil listNode[path[0]] dll

  #return boolean NodeFound (buat tau apa ada masukan node yang namanya salah, kalau ada yang salah NodeFound isinya False)
  #return boolean PathFound (dari namanya harusnya tau lah ya ini flag nunjukin kalau pathnya ketemu apa gak)
  # (ada lintasan dari node1 ke node 2 apa gak)
  
  #how to use:
  #masukkin ae nama variable2nya
  #contoh:
  #path , isNodeFound, isPathFound = main(adjMatrix, listNode, listCoor, node1,node2)
  #if (not isNodeFound) : nampilin ke web kalau nama node salah
  #if (not isPathFound) : nampilin ke web kalau tidak ada path dari node1 ke node2
  #kalau lolos keduanya baru bisa gambar pathnya

  #warning:
  #kalau flag gak lolos, list path bakal direturn kosong, jadi harus cek flagnya dulu

  idx1 = find(listNode,node1)
  idx2 = find(listNode,node2)
  if (idx1 == -1 or idx2 == -1):
    return [],False,False
  closed = []
  queue = PrioQueueMod()
  queue.insert((idx1,0,0))
  parent = [0 for i in range(len(listNode))]
  found = False
  while (not queue.isEmpty() and not found):
    dummy = queue.delete()
    gcostParent = dummy[1]
    current = dummy[0]
    closed.append(current)

    if current == idx2:
      found = True
    if (not found):
      for i in range(len(listNode)):
        if (adjMatrix[current][i] != 0 and find(closed,i) == -1):
          gcost = gcostParent + distanceInMeter(listCoor[current][0],listCoor[current][1], listCoor[i][0], listCoor[i][1])
          hcost = distanceInMeter(listCoor[i][0],listCoor[i][1],listCoor[idx2][0],listCoor[idx2][1])
          if ((queue.isMember(i) and queue.getFnKey(i) > gcost+hcost) or not queue.isMember(i)):
            parent[i] = current
            queue.insert((i,gcost,hcost))


  if not found:
    return [],True,False
  path = []
  path.append(idx2)
  dummy = idx2
  while (dummy != idx1):
    path.append(parent[dummy])
    dummy = parent[dummy]
  path.reverse()
  return path,True,True
  # for i in range(len(path)):
  #   if i == len(path)-1:
  #     print(listNode[path[i]])
  #   else:
  #     print(listNode[path[i]]+"->", end="")


#for testing

if __name__ == '__main__':
  namaFile = input() #input graf
  node1 = input() #input nama node1
  node2 = input() #input nama node2
  #input nama node bisa dilakukan sesudah baca graf, jadi santuy

  adjMatrix, listNode, listCoor, isFileFound = bacaFile(namaFile) #ini nanti baca grafnya
  if (not isFileFound): #nanti maneh bisa bikin grafnya kebaca terus jadinya ini harusnya keskip
    print("NamaFile salah")
    exit()
  path, isNodeFound, isPathFound = main(adjMatrix,listNode,listCoor,node1,node2) #ini buat ngeliat ada pathnya gak
  
  if (not isNodeFound): #cek flag nodefound
    print("Node tidak ditemukan")
    exit() #kalau gak ketemu kasi pesan eror
  elif (not isPathFound):
    print("Path tidak ditemukan")
    exit() #ini juga kalau error

  #kalau sampai sini aman
  #bisa mulai gambar

  #untuk ngecek apakah node i dan j dihubungkan 1 sisi atau gak -> cek adjMatrix[i][j] jika isinya 0 berarti gak berhubungan
  #untuk cek coordinat simpul ke i dari listNode tinggal pilih listCoor[i] (isinya tuple, yang pertama lat kedua long)
  #harusnya bisa lah ya kan alam gitu lho hehe
  
  #ini buat nampilin pake panah2 gitu jadi maneh gk usah liat
  for i in range(len(path)):
    if i == len(path)-1:
      print(listNode[path[i]])
    else:
      print(listNode[path[i]]+"->", end="")
  #nah kalau mau hitung jaraknya bisa pake ini hitungJarakPath, jaraknya dalam meter
  print("Jaraknya adalah " + str(hitungJarakPath(adjMatrix,path,listCoor)) + " meter")

