# GUI Double or nothing game
# Samuel Robinson

from tkinter import *
import random as rd


class Dubs():

    """Initializing the main balance and the bet amount"""
    def __init__(self, beginning_balance, bets):
        self.beginning_balance = beginning_balance
        self.bets = bets

    """Creates random number and checks its size to decide if you win or lost the doubling"""
    def double(self, amount, bet):
        number = rd.randint(0, 50)

        if (number < 25):
            """create a variable to insert in entry after loss and reset bet size"""
            amount = 0
            self.set_bets(25)

            """resets the GUI bet entry to 0 after loss"""
            bet.delete(0, END)
            bet.insert(INSERT, amount)
        else:
            """doubles bet and sets it to the new bet amount"""
            amount = amount * 2
            self.set_bets(amount)

            """sets the bet entry to the new bet size after winning"""
            bet.delete(0, END)
            bet.insert(INSERT, self.get_bets())

    def cash_out(self, balance, bet):
        newbalance = self.get_bets() + self.get_balance()
        self.set_balance(newbalance)

        """sets the new main balance in the entry to show the amount after adding the winnings"""
        balance.delete(0, END)
        balance.insert(INSERT, self.get_balance())

        """resets the bet entry and bet amount"""
        self.set_bets(25)
        bet.delete(0, END)
        bet.insert(INSERT, 0)

    def betting(self, bets, beginning_balance, bet, balance):

        """deletes the base 0 in bet entry and replaces with 25 bet amount"""
        bet.delete(0, END)
        bet.insert(INSERT, self.get_bets())

        """evaluates new balance after starting bet and updates the balance"""
        beginning_balance = self.get_balance() - 25
        self.set_balance(beginning_balance)

        """deletes the entry balance and replaces with new balance"""
        balance.delete(0, END)
        balance.insert(INSERT, self.get_balance())

    """sets the balance"""
    def set_balance(self, beginning_balance):
        self.beginning_balance = beginning_balance

    """sets the bet"""
    def set_bets(self, bets):
        self.bets = bets

    """gets the balance"""
    def get_balance(self):
        return self.beginning_balance

    """gets the bet"""
    def get_bets(self):
        return self.bets

    def main(self):

        """creates the GUI window and makes its background color black"""
        root = Tk()
        root.geometry("1280x720")
        root.configure(background='black')

        """Creates a frame container to add our buttons into"""
        frame = Frame(root)
        frame.pack(side=BOTTOM)

        """font for our buttons and entries"""
        labelfont = ('times', 10, 'bold')
        labelfont2 = ('times', 40, 'bold')

        """creates new entries on the root window and assigns the fonts to each"""
        balance = Entry(root, font=labelfont2)
        bet = Entry(root, font=labelfont2)

        """inserts the base balance and base bet to the entries"""
        balance.insert(INSERT, 500)
        bet.insert(INSERT, 0)

        """Buttons to play the game and puts them in the frame container"""
        play = Button(frame, text="Play", font=labelfont, bg="grey", fg="black", height=10, width=30,
                      command=lambda: self.betting(self.get_bets(), self.get_balance(), bet, balance))
        dubbutton = Button(frame, text="Double", font=labelfont, bg="grey", fg="black", height=10, width=30,
                           command=lambda: self.double(self.get_bets(), bet))
        cashout = Button(frame, text="Cash Out", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                         command=lambda: self.cash_out(balance, bet))

        """packs these buttons to the frame and packs these entries to the root window"""
        play.pack(side=LEFT)
        dubbutton.pack(side=LEFT)
        cashout.pack(side=RIGHT)
        balance.pack(side=LEFT)
        bet.pack(side=RIGHT)

        """while loop method for the root to keep it going while its open"""
        """code doesnt go further until window closes"""
        root.mainloop()


"""While the files ran directly and not imported this segment will run first"""
if __name__ == '__main__':
    """Sets the starting balance and betting amount for each play"""
    game = Dubs(beginning_balance=500, bets=25)

    """Starts the game from the main method """
    game.main()
