from Tkinter import *
import tkFileDialog
import os
from tkMessageBox import *
from EmotionDetection import EvaluateText


textfile = ""
valuefile = ""


window = Tk()  # Create instance
window.title("Emotion Detector | Group 6")  # Add a title
window.resizable(False, False)  # This code helps to disable windows from resizing


# ************************************** load tweet text for test ***************************
def tweetText():
    global textfile
    current_path = "./data/"
    textfile = tkFileDialog.askopenfilename(title='Choose text file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    tweetTextLabel.config(text=os.path.basename(textfile))
# ************************************** load tweet text for test ***************************



# ****************************** load tweet values for test ***********************************
def tweetValues():
    global valuefile
    current_path = "./data/"
    valuefile = tkFileDialog.askopenfilename(title='Choose value file', initialdir=current_path, filetypes=[("CSV files", "*.csv")])

    tweetValuesLabel.config(text=os.path.basename(valuefile))
# ****************************** End of load tweet values for test ***********************************


# ***************************** Read files test ****************************************
def test():
    global textFile, valueFile
    if valuefile and textfile is not None:
        try:
            print("\nRunning text evaluation...\n")
            with open(textfile, 'r') as textFile:
                with open(valuefile, 'r') as valueFile:
                    EvaluateText.evaluate(textFile, valueFile)
                    # progressBar()
                    # print (reset, textFile, valueFile)
                    # print(textFile, valueFile)
        except IOError:
            showerror('File not found!', 'Check file')
    else:
        showerror('Error!', 'text file or value file not selected')
        # print "text file or value file not selected!"
        # return
# ***************************** Read files test ****************************************







# ************************* Main Frame *****************************
mainFrame = Frame(window, width=550, height=220, bg='gray', bd=2, relief=GROOVE)
mainFrame.pack(fill=X, side=TOP)
mainFrame.grid_propagate(0)  # don't shrink


# ************************* Status Frame *****************************
statusFrame = Frame(window, height=50, bd=1, relief=SUNKEN)
statusFrame.pack(fill=X, side=BOTTOM)
statusFrame.grid_propagate(0)  # don't shrink




# ******************* Progress Bar Function ******************
def progressBar():
    showinfo('Info', "Evaluation Complete!")
# **************************************************************


# ******************** tweet text button and label *******************
tweetTextBtn = Button(mainFrame, text="Tweet text", width=12, command=tweetText)
tweetTextBtn.grid(row=0, column=0, pady=20)
tweetTextBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 12))

tweetTextLabel = Label(mainFrame, width=25)
tweetTextLabel.grid(row=0, column=1, ipady=5, pady=20)
tweetTextLabel.config(bd=2, font=("Arial ITALIC", 13))
# ********************End of tweet Text button and label *******************

# ******************** tweet values button and label *******************
tweetValuesBtn = Button(mainFrame, text="Tweet values", width=12, command=tweetValues)
tweetValuesBtn.grid(row=2, column=0, pady=25)
tweetValuesBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 12))

tweetValuesLabel = Label(mainFrame, width=25)
tweetValuesLabel.grid(row=2, column=1, ipady=5)
tweetValuesLabel.config(bd=2, font=("Arial ITALIC", 13))
# ********************End of tweet values button and label *******************

# test button
testBtn = Button(mainFrame, text="Test", command=test)
testBtn.grid(row=3, column=0)
testBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 13))

# cancel button
cancelBtn = Button(mainFrame, text="Cancel")
cancelBtn.grid(row=3, column=1)
cancelBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 13))

# clear button
def clear():
    tweetTextLabel['text'] = ""
    tweetValuesLabel['text'] = ""

clearBtn = Button(mainFrame, text="Clear", command=clear)
clearBtn.grid(row=3, column=2)
clearBtn.config(bd=3, relief=RAISED, font=("Arial Bold", 13))


# ******************** Centralise Window **************************
window_height = 259
window_width = 445
# specifies width and height of window1
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# specifies the co-ordinates for the screen
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))




window.mainloop()
