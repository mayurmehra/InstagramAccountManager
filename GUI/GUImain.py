from tkinter import *

root = Tk()
root.geometry('800x800')
# root.bind('<Configure>', screen_resize)

sidebar = Frame(root, bg="#352f40", width=600)
content_frame = Frame(root, bg="#534b63")

sidebar.pack(side=LEFT, fill=BOTH)
content_frame.pack(side=LEFT, fill=BOTH, expand=YES)

commentsButton = Button(sidebar, text="Comments", fg="white",bg="#352f40", relief=FLAT,pady=40)
commentsButton.pack(fill=X)
postButton = Button(sidebar, text="Post Media", fg="white",bg="#352f40",relief=FLAT)
postButton.pack(fill=X)
insightButton = Button(sidebar, text="See Insights", fg="white",bg="#352f40",relief=FLAT, padx=100,pady=40)
insightButton.pack(fill=X)

root.mainloop()
