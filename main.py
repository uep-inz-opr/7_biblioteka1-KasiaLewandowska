class Ksiazka:
  def __init__(self,lista):
    self.lista=lista
  def dodaj_egzemplarz_ksiazki(self):
    pojedynczalista=set(self.lista)
    informacjaoksiazce=[]
    for i in pojedynczalista:
      tytul=i[0]
      autor=i[1]
      liczbaegzemplarzy=self.lista.count(i)
      informacjaoksiazce.append((tytul,autor,liczbaegzemplarzy))
      informacjaoksiazce.sort(key=lambda x:x[0],reverse=False)
    for j in informacjaoksiazce:
      print (j)

n=int(input())
lista=[]
for a in range(n):
    ksiazka=eval(input())
    tytul=ksiazka[0]
    autor=ksiazka[1]
    lista.append((tytul,autor))
    ksiazka1=Ksiazka(lista)
ksiazka1.dodaj_egzemplarz_ksiazki()