from tkinter import *
import math

class Fenster(object):
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title('Matheprogramm')

        self.titel = Label(master=self.fenster, text='Dies ist ein Programm mit dem sich Umfang und Fläche verschiedener geometrischer Formen berechnen lassen. \n \n Welche gemetrische Form  möchtem Sie berechnen?')
        self.titel.pack(padx=3, pady=3)

        self.OptionList = ['Kreis', 'Rechteck', 'Quadrat']
        self.form = StringVar()
        self.form.set('Bitte wählen')
        self.optionen = OptionMenu(self.fenster, self.form, *self.OptionList)
        self.optionen.pack()

        print('Am Anfang steht in "form"', self.form)

        self.form.trace("w",self.callback(self.form))
        print('Nach Ausführung von "ausfuehrungForm" steht in form: ', self.form)

        
        
    def callback(self,form):
        self.chosen_option = self.form.get()
        print('chosen_option hat den Wert: ', self.chosen_option)
        self.ausfuehrungForm(self.chosen_option)      
        

        self.fenster.mainloop()
        print('Nach Beendigung des Programms hat self.form den Wert: ', self.form)
        print('Nach Beendigung des Programms hat chosen_option den Wert: ', self.chosen_option)
        

    def ausfuehrungForm(self,chosen_option):
        print("Die Funktion 'ausfuehrungForm' wurde aufgerufen")
        self.berechnungsFläche = Frame(self.fenster)
        self.berechnungsFläche.pack()
        
        if self.chosen_option == 'Kreis':
            self.radius = input('Bitte geben Sie einen Radius ein. ')
            kreis = Circle(1,1,self.radius)
        elif self.chosen_option == 'Rechteck':
            kurzeSeite = input('Bitte geben Sie Seite a ein. ')
            langeSeite = input('Bitte geben Sie Seite b ein. ')
            rechteck = Rectangle(1,1,kurzeSeite,langeSeite)
        elif self.chosen_option == 'Quadrat':
            quadrat = Square()


def main():

    start = Fenster()

    
    
    

   

    
main()
