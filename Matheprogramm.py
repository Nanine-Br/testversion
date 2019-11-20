from tkinter import *
import math

class Fenster(object):
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('Matheprogramm')
##      Layout
        self.titel = Label(master=self.fenster, text='Dies ist ein Programm mit dem sich Umfang und Fläche verschiedener geometrischer Formen berechnen lassen. \n \n Welche gemetrische Form  möchtem Sie berechnen?')
        self.titel.pack(side=TOP, padx=3, pady=3)
##      Dropdown-Menü
        self.OptionList = ['Kreis', 'Rechteck', 'Quadrat']
        self.form = StringVar()
        self.form.set('Bitte wählen')
        self.optionen = OptionMenu(self.fenster, self.form, *self.OptionList)
        self.optionen.pack()
##      Attribute
        self.r = 0
        self.seite = 0
        self.langeSeite = 0
        self.kurzeSeite = 0
        self._umfang = 0
        self._fläche = 0
        self.u = 0
        self.f = 0
  

        self.form.trace("w",self.callback)

        self.fenster.mainloop()
        
        
    def callback(self,*args):
        self.chosen_option = self.form.get()
##        print('chosen_option hat den Wert: ', self.chosen_option)
        self.ausfuehrungForm(self.chosen_option)      
                

    def ausfuehrungForm(self,chosen_option):
##        print("Die Funktion 'ausfuehrungForm' wurde aufgerufen")
        self.berechnungsFläche = Frame(self.fenster)
        self.berechnungsFläche.pack(side=BOTTOM, padx=5, pady=5)
##        print('Sie haben ein(en)',chosen_option, 'gewählt.')
        if self.chosen_option == 'Kreis':
            self.radius = Entry(self.fenster, text='Radius r: ')
            self.radius.pack(padx=10, pady=10)
##            print('Der eingegebene Radius ist: ',self.radius)
            self.radius.bind(sequence='<Return>', func=self.getEingabewert)
##            print('Der eingegebene Radius ist: ',self.radius)
            print('Der eingegebene Radius hier ist: ',self.r)
        elif self.chosen_option == 'Rechteck':
            self.langeSeite = Entry(self.fenster, text='Seite a: ')
            self.kurzeSeite = Entry(self.fenster, text='Seite b: ')
            self.langeSeite.pack(padx=10, pady=10)
            self.kurzeSeite.pack(padx=10, pady=10)
            self.langeSeite.bind(sequence='<Return>', func=self.getEingabewert)
            self.kurzeSeite.bind(sequence='<Return>', func=self.getEingabewert)
        elif self.chosen_option == 'Quadrat':
            self.seite = Entry(self.fenster, text='Seite c: ')
            self.seite.pack(padx=10, pady=10)
            self.seite.bind(sequence='<Return>', func=self.getEingabewert)
        else:
            print('Bitte wählen Sie zuerst eine Form aus.')


    def getEingabewert(self, chosen_option):
        if self.chosen_option == 'Kreis':
            self.r = float(self.radius.get())
            self.erstelleObjekt(self.chosen_option, self.r)
        elif self.chosen_option == 'Rechteck':
            self.a = float(self.langeSeite.get())
            self.b = float(self.kurzeSeite.get())
            self.erstelleObjekt(self.chosen_option, 0, self.a,self.b)
        elif self.chosen_option == 'Quadrat':
            self.c = float(self.seite.get())
            self.erstelleObjekt(self.chosen_option, 0, 0,0,self.c)
            
    def erstelleObjekt(self, chosen_option,r=0,a=0,b=0,c=0):
##        print('Die Funktion erstelleObjekt wird aufgerufen')
        if self.chosen_option == 'Kreis':
            self.kreis = Circle(1,1, self.r)
            self.u = self.kreis._umfang
            self.f = self.kreis._fläche
        elif self.chosen_option == 'Rechteck':
            self.rechteck = Rectangle(1,1, a,b)
            self.u = self.rechteck._umfang
            self.f = self.rechteck._fläche
        elif self.chosen_option == 'Quadrat':
            self.quadrat = Square(1,1,self.c)
            self.u = self.quadrat._umfang
            self.f = self.quadrat._fläche
            
        self.ausgabe(self.chosen_option, self.u, self.f)

    def ausgabe(self, chosen_option, u, f):
##            print('Die Funktion ausgabe wird aufgerufen')
            self.ausgabeFläche = Frame(self.fenster)
            self.ausgabeFläche.pack(side=BOTTOM, padx=5, pady=5)
            self.l1 = Label(self.fenster, text=('Der Umfang des', self.chosen_option, 'beträgt: ',self.u))
            self.l2 = Label(self.fenster, text=('Die Fläche des', self.chosen_option, 'beträgt: ',self.f))
            self.l1.pack()
            self.l2.pack()
##    

    
        

class Shape(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self._umfang = 0
        self._fläche = 0

##    def ausgabe(self):
##        print('Der Umfang des Objektes beträgt: ',self._umfang)
##        print('Die Fläche des Objektes beträgt: ',self._fläche)
         

    

class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.__r = r
        self.__berechneUmfang()
        self.__berechneFlaeche()
        

    def __berechneUmfang(self):
        self._umfang = 2*math.pi*self.__r
        return self._umfang
        
    def __berechneFlaeche(self):
        self._fläche = math.pi*self.__r**2
        return self._fläche


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        Shape.__init__(self, x, y)
        self.__a = a
        self.__b = b
        self.__berechneUmfang()
        self.__berechneFlaeche()
        

    def __berechneUmfang(self):
        self._umfang = 2*self.__a + 2*self.__b
        
    def __berechneFlaeche(self):
        self._fläche = self.__a*self.__b


class Square(Rectangle):
    def __init__(self, x, y, c, a=0, b=0):
        Rectangle.__init__(self, x, y, a, b)
        self.__c = c        
        self.__berechneUmfang()
        self.__berechneFlaeche()

    def __berechneUmfang(self):
        self._umfang = 4*self.__c
        
    def __berechneFlaeche(self):
        self._fläche = self.__c*self.__c


def main():

    start = Fenster()

    
    
    

    # Auf Seite 306
    #print(Kreis1.__berechneUmfang)

    
main()
