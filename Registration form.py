from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

#Field Name
firstname = Label(root, text="First Name")
lastname = Label(root, text="Last Name")
age = Label(root, text="Age")
gender = Label(root, text="Gender")
phone = Label(root, text="Phone")
email = Label(root, text="Email")

#Packing Fields
firstname.grid(row=3, column=2)
lastname.grid(row=4, column=2)
age.grid(row=5, column=2)
gender.grid(row=6, column=2)
phone.grid(row=7, column=2)
email.grid(row=8, column=2)

#Variable for storing data
firstnamevalue = StringVar
lastnamevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
phonevalue= StringVar
emailvalue = StringVar
checkvalue = IntVar

#Entry Field
firstnameentry = Entry(root, textvariable = firstnamevalue)
lastnameentry = Entry(root, textvariable = lastnamevalue)
ageentry = Entry(root, textvariable = agevalue)
genderentry = Entry(root, textvariable = gendervalue)
phoneentry = Entry(root, textvariable = phonevalue)
emailentry = Entry(root, textvariable = emailvalue)

#Packing entry Field
firstnameentry.grid(row=3, column=3)
lastnameentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)
genderentry.grid(row=6, column=3)
phoneentry.grid(row=7, column=3)
emailentry.grid(row=8, column=3)

#Checkbox
checkbtn = Checkbutton(text = "remember me", variable = checkvalue)
checkbtn.grid(row=10, column=3)

#Submit
Button(text = "Submit", command=getvals).grid(row=13,column=3)


root.mainloop()
