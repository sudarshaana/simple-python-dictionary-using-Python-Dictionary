from Tkinter import *
import Tkinter
import tkMessageBox

top = Tk()
top.title("Python Simple Dictionary")

w = 240 # width for the Tk root
h = 100 # height for the Tk root

# get screen width and height
ws = top.winfo_screenwidth() # width of the screen
hs = top.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


# setting sizing false
top.resizable(width=False, height=False)

#fixing window size
top.minsize(300, 100)

# adding level
L0 = Label(top, text = "Type word and search to find meaning.", fg = "#000000", bg = "#acacac", font = "Verdana 10 bold")
L0.pack(side = TOP)

#adding level
L1 = Label(top, text = "Word ", font = "arial 10 bold")
L1.pack(side = LEFT)

# adding Entry
E1 = Entry(top, bd = 5)
E1.pack(side = LEFT)

# writing function to find words
def function():
    # getting user input
    a = E1.get().lower()

    # defining words using Dictionary words using dictionary
    dict = {'consider':'Deem to be',
            'minute': 'Infinitely or immeasurably small',
            'accord': 'Concurrence of opinion',
            'evident': 'Clearly revealed to the mind or the senses or judgment',
            'practice': 'A customary way of operation or behavior',
            'intend': 'Have in mind as a purpose',
            'concern': 'Something that interests you because it is important',
            'commit': 'Perform an act, usually with a negative connotation',
            'issue' : 'Some situation or event that is thought about',
            'approach' : 'Move towards',
            'establish': 'Set up or found',
            'utter' : 'Without qualification',
            'conduct' : 'Direct the course of; manage or control',
            'engage' : 'Consume all of one\'s attention or time',
            'obtain' : 'Come into possession of',
            'scarce' : 'deficient in quantity or number compared with the demand',
            'policy' : 'a plan of action adopted by an individual or social group',
            'straight' : 'successive, without a break',
            'stock': 'capital raised by a corporation through the issue of shares',
            'apparent': 'clearly revealed to the mind or the senses or judgme',
            'property' : 'a basic or essential attribute shared by members of a class',
            'fancy' : 'imagine; conceive of; see in one\'s mind',
            'concept' : 'an abstract or general idea inferred from specific instances',
            'court' : 'an assembly to conduct judicial business',
            'appoint' : 'assign a duty, responsibility or obligation to',
            'passage': 'a section of text, particularly a section of medium length',
            'vain' : 'unproductive of success',
            'instance': "an occurrence of something",
            'coast' : 'the shore of a sea or ocean',
            'project' : 'a planned undertaking',
            'commission' : 'a special group delegated to consider some matter',
            'constant' : 'a quantity that does not vary',
            'circumstances' : 'one\'s overall condition in life',
            'constitute' : 'to compose or represent',
            'level' : 'a relative position or degree of value in a graded group',
            'affect' : 'have an influence upon',
            'institute' : 'set up or lay the groundwork for',
            'render' : 'give an interpretation of',
            'appeal': 'be attractive to',
            'generate' : 'bring into existence',
            'theory' : 'a well-substantiated explanation of some aspect of the world',
            'range' : 'a variety of different things or activities',
            'campaign' : 'a race between candidates for elective office',
            'league' : 'an association of sports teams that organizes matches',
            'labor' : 'any piece of work that is undertaken or attempted',
            'confer' : 'have a meeting in order to talk something over',
            'grant' : 'allow to have',
            'dwell' : 'think moodily or anxiously about something',
            'entertain' : 'provide amusement for',
            'contract' : 'a binding agreement that is enforceable by law',
            'earnest' : 'characterized by a firm, humorless belief in one\'s opinions',
            'yield' : 'give or supply',
            'wander' : 'move or cause to move in a sinuous or circular course',
            'insist' : 'be emphatic or resolute and refuse to budge',
            'knight' : 'a person of noble birth trained to arms and chivalry',
            'convince' : 'make realize the truth or validity of something',
            'inspire' : 'serve as the inciting cause of'

            }


    if (E1.get() != ''): # input is empty or not

        if a in dict.keys(): # input key is exists or not
            tkMessageBox.showinfo("Simple Python Dictionary",  "Word: "+ E1.get() + "\nMeaning: "+ dict[a])

        else: # key is not on the list
            tkMessageBox.showinfo("Simple Python Dictionary", "Word not found" , icon='error')

    else: # input is empty
        tkMessageBox.showinfo("Simple Python Dictionary", "Type word and try again", icon='warning')

# creating button
B = Tkinter.Button(top, text = "Search" , width=10, command=function, )
B.grid_size()
B.pack(side = LEFT)

# set the dimensions of the screen
# and where it is placed
top.geometry('%dx%d+%d+%d' % (w, h, x, y))
top.mainloop();
