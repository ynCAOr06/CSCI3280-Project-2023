from tkinter import *


class MultipleScrollingListbox(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Scrolling Multiple Listboxes')

        #the shared scrollbar
        self.scrollbar = Scrollbar(self, orient='vertical')

        #note that yscrollcommand is set to a custom method for each listbox
        self.list1 = Listbox(self, yscrollcommand=self.yscroll1)
        self.list1.pack(fill='y', side='left')

        self.list2 = Listbox(self, yscrollcommand=self.yscroll2)
        self.list2.pack(expand=1, fill='both', side='left')

        self.scrollbar.config(command=self.yview)
        self.scrollbar.pack(side='right', fill='y')

        #fill the listboxes with stuff
        for x in range(30):
            self.list1.insert('end', x)
            self.list2.insert('end', x)

    #I'm sure there's probably a slightly cleaner way to do it than this
    #Nevertheless - whenever one listbox updates its vertical position,
    #the method checks to make sure that the other one gets updated as well.
    #Without the check, I *think* it might recurse infinitely.
    #Never tested, though.
    def yscroll1(self, *args):
        if self.list2.yview() != self.list1.yview():
            self.list2.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self, *args):
        if self.list1.yview() != self.list2.yview():
            self.list1.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yview(self, *args):
        self.list1.yview(*args)
        self.list2.yview(*args)


if __name__ == "__main__":
    root = MultipleScrollingListbox()
    root.mainloop()
