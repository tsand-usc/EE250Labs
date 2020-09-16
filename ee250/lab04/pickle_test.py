import pickle
import os.path

notes = []

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
path = 'notes.pickle'                                    # path to pickle file
if os.path.isfile(path):                                 # checks if file exists   
   notes = pickle.load(open('notes.pickle', "rb"))       # loads file
   
# B. Print out notes
print(notes)

# C. Read in a string from the user using input() and append it to notes
addition = input("Add to Notes: ")                       # gets new addition
notes.append(addition)                                   # adds it to notes

# D. Save notes to notes.pickle
pickle.dump(notes, open("notes.pickle", "wb"))
