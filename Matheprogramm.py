from tkinter import *
import math

class Fenster(object):
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('Matheprogramm')
        self.scrollbar=Scrollbar(self.fenster)
        self.scrollbar.pack(side =RIGHT,fill =Y)

        self.titel = Label(master=self.fenster, text='Dies ist ein Programm mit dem sich Umfang und Fläche verschiedener geometrischer Formen berechnen lassen. \n \n Welche gemetrische Form  möchtem Sie berechnen?')
        self.titel.pack(padx=3, pady=3)

        self.optionList = ['Kreis', 'Rechteck', 'Quadrat',]
        self.form = StringVar()
        self.optionen = OptionMenu(self.fenster, self.form, *self.optionList)
        self.optionen.pack()

        
        self.fenster.mainloop()

        self.ausfuehrungForm(self.form)

        def ausfuehrungForm(self, form):
            self.berechnungsFläche = Frame(self.fenster)
            self.berechnungsFläche.pack()
            
            if self.form == 'Kreis':
                kreis = Circle()
            elif self.form == 'Rechteck':
                rechteck = Rectangle()
            elif self.form == 'Quadrat':
                quadrat = Square()
         

        

class Shape():
    def __init__(self, x, y, form):
        self.__x = x
        self.__y = y
        self.__form = form
        self._umfang = 0
        self._fläche = 0

        

    def ausgabe(self):
        print('Der Umfang des Objektes beträgt: ',self._umfang)
        print('Die Fläche des Objektes beträgt: ',self._fläche)

    

class Circle(Shape):
    def __init__(self, x, y , form, radius):
        Shape.__init__(self, x, y, form)
        self.__radius = radius
        self.__berechneUmfang()
        self.__berechneFlaeche()

    def __berechneUmfang(self):
        self._umfang = 2*math.pi*self.__radius
        
    def __berechneFlaeche(self):
        self._fläche = math.pi*self.__radius**2


class Rectangle(Shape):
    def __init__(self, x, y, form, kurzeSeite, langeSeite):
        Shape.__init__(self, x, y, form)
        self.__kurzeSeite = kurzeSeite
        self.__langeSeite = langeSeite
        self.__berechneUmfang()
        self.__berechneFlaeche()

    def __berechneUmfang(self):
        self._umfang = 2*self.__kurzeSeite + 2*self.__langeSeite
        
    def __berechneFlaeche(self):
        self._fläche = self.__kurzeSeite*self.__langeSeite


class Square(Rectangle):
    def __init__(self, x, y, Seite, kurzeSeite=0, langeSeite=0):
        Rectangle.__init__(self, x, y,form, kurzeSeite, langeSeite,)
        self.__Seite = Seite        
        self.__berechneUmfang()
        self.__berechneFlaeche()

    def __berechneUmfang(self):
        self._umfang = 4*self.__Seite
        
    def __berechneFlaeche(self):
        self._fläche = self.__Seite*self.__Seite


def main():

    start = Fenster()

    
    
    

    # Auf Seite 306
    #print(Kreis1.__berechneUmfang)

    
main()
