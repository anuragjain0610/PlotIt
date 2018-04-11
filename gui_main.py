#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 12, 2017 07:53:45 PM

try:
    from Tkinter import *
    import tkFileDialog as fdialog
    import tkMessageBox as msgbox
except ImportError:
    from tkinter import *
    from tkinter import filedialog as fdialog
    from tkinter import messagebox as msgbox

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import gui_support
from lib import InvalidFunctionException


def vp_start_gui():
    """Starting point when module is the main routine."""

    global val, w, root
    root = Tk()
    top = New_Toplevel_1(root)
    m = Menubar(root)
    gui_support.init(root, top)
    root.protocol('WM_DELETE_WINDOW', destroy_app)
    root.mainloop()


# global colors variables for theme switch
_bgcolordark = '#000000'
_fgcolordark = '#d9d9d9'
_activebgcolordark = '#808080'
_bgcolorlight = '#ffffff'
_fgcolorlight = '#000000'
_darkwindowbackground = '#31363b'
_lightwindowbackground = '#f2f2f2'

w = None


def create_New_Toplevel_1(root, *args, **kwargs):
    """Starting point when module is imported by another program."""

    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel_1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


def destroy_app():
    global root
    root.destroy()
    exit(0)

def save_file():
    file=fdialog.asksaveasfile(mode="wb", title="Save Figure", defaultextension=".png", filetypes = (("png files","*.png"),("all files","*.*")))
    if file is None:
        return None
    img_to_save=open(".temp/generated_plot.png","rb").read()
    file.write(img_to_save)
    file.close()

def toArray(str1,str2):
    return("["+str1+"],["+str2+"]")


class Menubar:
    def __init__(self, master):
        
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save", command=save_file)
        filemenu.add_command(label="Quit", command=root.quit)


        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)


class New_Toplevel_1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        top.geometry("600x460+408+120")
        top.title("PlotIt")

        self.theme = 'light'
        self.line_style = '-'
        self.file_path = ''
        root.configure(background=_lightwindowbackground)
        self.pvalue1='' #To store enrty values from popup winodw
        self.pvaluetemp='' #To store the value of popup entry field for reploting

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.04, rely=0.05, relheight=0.70, relwidth=0.69)
        self.Canvas1.configure(background=_bgcolorlight)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=394)
        self.Canvas1.bind('<Configure>', self.resize_plot)

        self.fx = Entry(top)
        self.fx.place(relx=0.11, rely=0.82, relheight=0.05, relwidth=0.53)
        self.fx.configure(background=_bgcolorlight)
        self.fx.configure(font="TkFixedFont")
        self.fx.configure(width=296)
        self.fx.bind('<Return>', lambda x : self.toPlot(self.radiovar.get()))
        self.fx.configure(fg=_fgcolorlight)
        self.fx.configure(insertbackground=_fgcolorlight)


        self.xpoints = Entry(top)
        self.xpoints.place(relx=0.11, rely=0.92, relheight=0.04, relwidth=0.25)
        self.xpoints.configure(width=374,background=_bgcolorlight,takefocus="True")

        self.ypoints = Entry(top)
        self.ypoints.place(relx=0.39, rely=0.92, relheight=0.04, relwidth=0.25)
        self.ypoints.configure(width=374,background=_bgcolorlight,takefocus="True")
        self.ypoints.bind('<Return>', lambda x : self.toPlot(self.radiovar.get()))

        self.radiovar=StringVar()

        self.FunctionRadio = Radiobutton(top)
        self.FunctionRadio.place(relx=0.11, rely=0.76, relheight=0.05, relwidth=0.14)
        self.FunctionRadio.configure(text='''Function''',fg=_fgcolorlight,bg=_lightwindowbackground,value=1,width=72)
        self.FunctionRadio.configure(variable=self.radiovar, value="func")
        self.FunctionRadio.configure(command=lambda : (self.fx.configure(state="normal"),
                                                        self.Check.configure(state="normal"),
                                                        self.stepsize.configure(state="normal"),
                                                        self.xpoints.configure(state="disabled"),
                                                        self.ypoints.configure(state="disabled")))


        self.LineRadio = Radiobutton(top)
        self.LineRadio.place(relx=0.26, rely=0.76, relheight=0.05, relwidth=0.12)
        self.LineRadio.configure(text='''Line''',fg=_fgcolorlight,bg=_lightwindowbackground,value=2,width=72)
        self.LineRadio.configure(variable=self.radiovar, value="line")
        self.LineRadio.configure(command=lambda : (self.fx.configure(state="disabled"),
                                                self.Check.configure(state="disabled"),
                                                self.stepsize.configure(state="disabled"),
                                                self.xpoints.configure(state="normal"),
                                                self.ypoints.configure(state="normal")))
        self.chkvar=StringVar()
        self.Check= Checkbutton(top,variable=self.chkvar)
        self.Check.place(relx=0.40, rely=0.76, relheight=0.05, relwidth=0.245)
        self.Check.configure(text='''Use discrete points''',background=_lightwindowbackground,onvalue='discrete', offvalue='nodiscrete')
        self.Check.configure(state="disabled")
        self.Check.configure(command= lambda : self.stepsize.configure(state="disabled") if self.chkvar.get()=="discrete" else self.stepsize.configure(state="normal"))


        self.Label1 = Label(top)
        self.Label1.place(relx=0.77, rely=0.08, height=18, width=47)
        self.Label1.configure(text='''x lower''')
        self.Label1.configure(fg=_fgcolorlight)
        self.Label1.configure(background=_lightwindowbackground)
        

        self.x_lower = Entry(top)
        self.x_lower.place(relx=0.88, rely=0.08, relheight=0.05, relwidth=0.08)
        self.x_lower.configure(background=_bgcolorlight)
        self.x_lower.configure(font="TkFixedFont")
        self.x_lower.configure(width=46)
        self.x_lower.insert(0, '0')
        self.x_lower.configure(fg=_fgcolorlight)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.77, rely=0.13, height=18, width=51)
        self.Label2.configure(text='''x upper''')
        self.Label2.configure(fg=_fgcolorlight)
        self.Label2.configure(background=_lightwindowbackground)

        self.x_upper = Entry(top)
        self.x_upper.place(relx=0.88, rely=0.13, relheight=0.05, relwidth=0.08)
        self.x_upper.configure(background=_bgcolorlight)
        self.x_upper.configure(font="TkFixedFont")
        self.x_upper.configure(width=46)
        self.x_upper.insert(0, '100')
        self.x_upper.configure(fg=_fgcolorlight)


        self.stepLabel = Label(top)
        self.stepLabel.place(relx=0.77, rely=0.17, height=18, width=52)
        self.stepLabel.configure(text='''step size''')
        self.stepLabel.configure(fg=_fgcolorlight, background=_lightwindowbackground)

        self.stepsize = Entry(top)
        self.stepsize.place(relx=0.88, rely=0.17, relheight=0.05, relwidth=0.08)
        self.stepsize.configure(width=46, fg=_fgcolorlight, background=_bgcolorlight, font="TkFixedFont")
        self.stepsize.insert(0, '1')


        self.Label3 = Label(top)
        self.Label3.place(relx=0.04, rely=0.82, height=18, width=35)
        self.Label3.configure(text='''f(x)=''')
        self.Label3.configure(fg=_fgcolorlight)
        self.Label3.configure(background=_lightwindowbackground)


        self.bt_plot = Button(top)
        self.bt_plot.place(relx=0.67, rely=0.85, height=26, width=47)
        self.bt_plot.configure(activebackground=_activebgcolordark)    
        self.bt_plot.configure(cursor="left_ptr")
        self.bt_plot.configure(text='''Plot''')
        self.bt_plot.configure(width=47, background=_bgcolorlight, fg=_fgcolorlight)
        self.bt_plot.configure(command=lambda : (self.toPlot(self.radiovar.get())))


        self.Label4 = Label(top)
        self.Label4.place(relx=0.78, rely=0.34, height=18, width=100)
        self.Label4.configure(text=" Choose the Color ")
        self.Label4.configure(fg=_fgcolorlight)
        self.Label4.configure(background=_lightwindowbackground)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.11, rely=0.88, height=18)
        self.Label5.configure(text='''X-points''')
        self.Label5.configure(fg=_fgcolorlight)
        self.Label5.configure(background=_lightwindowbackground)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.39, rely=0.88, height=18)
        self.Label6.configure(text='''Y-points''')
        self.Label6.configure(fg=_fgcolorlight)
        self.Label6.configure(background=_lightwindowbackground)

        self.current_color = StringVar(top)
        self.current_color.set('Red')
        self.colors = {'Red', 'Blue', 'Cyan', 'Black', 'Green'}
        self.dropdown_menu = OptionMenu(top, self.current_color,
                                        *self.colors, command=self.Dropdown_Changed)
        self.dropdown_menu.pack(side='top', anchor='w')
        self.dropdown_menu.place(relx=0.78, rely=0.40, height=18, width=100)
        self.dropdown_menu.configure(activebackground=_activebgcolordark)
        self.dropdown_menu.configure(background=_bgcolorlight)
        self.dropdown_menu.configure(fg=_fgcolorlight)
        self.dropdown_menu['menu'].configure(activebackground=_activebgcolordark)
        self.dropdown_menu['menu'].configure(background=_bgcolorlight)
        self.dropdown_menu['menu'].configure(fg=_fgcolorlight)

        self.color_input = Entry(top)
        self.color_input.place(relx=0.78, rely=0.47,
                               relheight=0.05, relwidth=0.10)
        self.color_input.configure(background=_bgcolorlight)
        self.color_input.configure(font="TkFixedFont")
        self.color_input.insert(0, '#FF0000')
        self.color_input.configure(fg=_fgcolorlight)

        self.bt_go = Button(top)
        self.bt_go.place(relx=0.90, rely=0.47, height=20, width=40)
        self.bt_go.configure(activebackground=_activebgcolordark)
        self.bt_go.configure(command=lambda : self.rePlot(self.radiovar.get()))
        self.bt_go.configure(cursor="left_ptr")
        self.bt_go.configure(text='''Go''')
        self.bt_go.configure(width=47)
        self.bt_go.configure(background=_bgcolorlight)
        self.bt_go.configure(fg=_fgcolorlight)

        self.bt_themeswitch = Button(top)
        self.bt_themeswitch.place(relx=0.8, rely=0.85, height=26, width=100)
        self.bt_themeswitch.configure(activebackground=_activebgcolordark)
        self.bt_themeswitch.configure(background=_bgcolorlight)
        self.bt_themeswitch.configure(cursor="left_ptr")
        self.bt_themeswitch.configure(text='Dark Theme')
        self.bt_themeswitch.configure(command=self.changeTheme)
        self.bt_themeswitch.configure(fg=_fgcolorlight)
    
    def toPlot(self,radiovar):
        """This method determines which type of figure to plot based on value of a vriable-- pvalue1"""
        if radiovar=="func":
            if self.chkvar.get()=="discrete":
                self.popDiscreteWin()
                if len(self.pvalue1)!=0:
                    xpoints=list(map(float, self.pvalue1.split(',')))
                    gui_support.Plot(self.fx.get(),xpoints,
                        self.color_input.get(),
                        self.theme,
                        self.Canvas1, self.line_style, self.file_path,True)
                    self.pvalue1=''

                elif len(self.pvalue1)==0:
                    msgbox.showerror("Error","No Value provided in discrete value")

            else:
                if not self.check_value(self.x_lower.get(), 'x lower'):
                    return
                if not self.check_value(self.x_upper.get(), 'x upper'):
                    return
                if not self.check_value(self.stepsize.get(), 'step size'):
                    return
                try:
                    gui_support.Plot(self.fx.get(),range(int(self.x_lower.get()),
                        int(self.x_upper.get()),int(self.stepsize.get())),
                        self.color_input.get(),
                        self.theme,
                        self.Canvas1, self.line_style, self.file_path)
                except InvalidFunctionException, (instance):
                    msgbox.showerror("Error", instance.parameter)

        if radiovar=="line":
            try:
                gui_support.Plot_line(toArray(self.xpoints.get(),self.ypoints.get()),
                    self.color_input.get(),
                    self.theme,
                    self.Canvas1, self.line_style, self.file_path)
            except InvalidFunctionException, (instance):
                msgbox.showerror("Error", instance.parameter)

    def rePlot(self,radiovar):
        """This method re-plot the figure using new color scheme
         based on value of a temp vriable--pvaluetemp"""
        if radiovar=="func":
            if self.chkvar.get()=="discrete":
                if len(self.pvaluetemp)!=0:
                    xpoints=list(map(float, self.pvaluetemp.split(',')))
                    gui_support.Plot(self.fx.get(),xpoints,
                        self.color_input.get(),
                        self.theme,
                        self.Canvas1, self.line_style, self.file_path,True)
                elif len(self.pvaluetemp)==0:
                    msgbox.showerror("Error","No Value provided in discrete value")

            else:
                gui_support.Plot(self.fx.get(),range(int(self.x_lower.get()),
                    int(self.x_upper.get()),int(self.stepsize.get())),
                    self.color_input.get(),
                    self.theme,
                    self.Canvas1, self.line_style, self.file_path)
                
        if radiovar=="line":
            gui_support.Plot_line(toArray(self.xpoints.get(),self.ypoints.get()),
                self.color_input.get(),
                self.theme,
                self.Canvas1, self.line_style, self.file_path)


    def popDiscreteWin(self):
        """This is the popup Window for function plotting options.
        This function holds all the gui for this purpose"""
        global root
        pwin=self.pwin=Toplevel(root)
        pwin.geometry("420x140+470+200")
        pwin.title("Add discrete points")
        pwin.configure(background= _lightwindowbackground)
        pwin.protocol('WM_DELETE_WINDOW', lambda : (self.Check.deselect(),self.pwin.destroy()))

        #Entry for Discrete Option
        self.pentry1=Entry(pwin)
        self.pentry1.place(relx=0.10, rely=0.20, relheight=0.20, relwidth=0.80)
        self.pentry1.configure(width=374,cursor="xterm",background=_bgcolorlight)
        self.pentry1.focus()

        self.bt_submit = Button(pwin)
        self.bt_submit.place(relx=0.42, rely=0.55, height=35, width=60)
        self.bt_submit.configure(activebackground=_activebgcolordark,background=_bgcolorlight,fg=_fgcolorlight)    
        self.bt_submit.configure(text= '''Submit''',cursor= "left_ptr",width= 47)
        self.bt_submit.configure(command=lambda : (self.popupInputHandler(),
                                                    self.pwin.destroy()))
        pwin.wait_window()


    def popupInputHandler(self):
        """This method manages the input of popup window"""
        if self.pentry1.get() :
            self.pvalue1=str(self.pentry1.get())
            self.pvaluetemp=str(self.pentry1.get())


    def Dropdown_Changed(self, current_color):
        color = '#000000'
        if current_color == 'Red':
            color = '#FF0000'
        elif current_color == 'Blue':
            color = '#0000FF'
        elif current_color == 'Cyan':
            color = '#00FFFF'
        elif current_color == 'Black':
            color = '#000000'
        elif current_color == 'Green':
            color = '#008000'
        self.color_input.delete(0, 100)
        self.color_input.insert(0, color)

    def changeTheme(self):
        if self.bt_themeswitch['text'] == "Light Theme":
            self.bt_themeswitch.configure(text="Dark Theme")
            self.Canvas1.configure(background=_bgcolorlight)
            self.fx.configure(background=_bgcolorlight)
            self.fx.configure(fg=_fgcolorlight)
            self.fx.configure(insertbackground=_fgcolorlight)
            self.x_lower.configure(background=_bgcolorlight)
            self.x_lower.configure(fg=_fgcolorlight)
            self.x_upper.configure(background=_bgcolorlight)
            self.x_upper.configure(fg=_fgcolorlight)
            self.stepsize.configure(background=_bgcolorlight)
            self.stepsize.configure(fg=_fgcolorlight)
            self.xpoints.configure(background=_bgcolorlight)
            self.xpoints.configure(foreground=_fgcolorlight)
            self.ypoints.configure(background=_bgcolorlight)
            self.ypoints.configure(foreground=_fgcolorlight)
            self.bt_plot.configure(activebackground=_activebgcolordark)
            self.dropdown_menu.configure(activebackground=_activebgcolordark)
            self.color_input.configure(background=_bgcolorlight)
            self.color_input.configure(fg=_fgcolorlight)
            self.bt_go.configure(activebackground=_activebgcolordark)
            self.bt_themeswitch.configure(activebackground=_activebgcolordark)
            self.Label1.configure(background=_lightwindowbackground)
            self.Label1.configure(fg=_fgcolorlight)
            self.Label2.configure(background=_lightwindowbackground)
            self.Label2.configure(fg=_fgcolorlight)
            self.Label3.configure(background=_lightwindowbackground)
            self.Label3.configure(fg=_fgcolorlight)
            self.Label4.configure(background=_lightwindowbackground)
            self.Label4.configure(fg=_fgcolorlight)
            self.Label5.configure(background=_lightwindowbackground)
            self.Label5.configure(fg=_fgcolorlight)
            self.Label6.configure(background=_lightwindowbackground)
            self.Label6.configure(fg=_fgcolorlight)
            self.stepLabel.configure(background=_lightwindowbackground)
            self.stepLabel.configure(fg=_fgcolorlight)
            self.FunctionRadio.configure(background=_lightwindowbackground)
            self.FunctionRadio.configure(fg=_fgcolorlight)
            self.LineRadio.configure(background=_lightwindowbackground)
            self.LineRadio.configure(fg=_fgcolorlight)
            self.Check.configure(background=_lightwindowbackground)
            self.Check.configure(fg=_fgcolorlight)
            self.bt_go.configure(background=_bgcolorlight)
            self.bt_go.configure(fg=_fgcolorlight)
            self.bt_plot.configure(background=_bgcolorlight)
            self.bt_plot.configure(fg=_fgcolorlight)
            self.bt_themeswitch.configure(background=_bgcolorlight)
            self.bt_themeswitch.configure(fg=_fgcolorlight)
            self.dropdown_menu.configure(background=_bgcolorlight)
            self.dropdown_menu.configure(fg=_fgcolorlight)
            self.dropdown_menu['menu'].configure(fg=_fgcolorlight)
            self.dropdown_menu['menu'].configure(background=_bgcolorlight)
            self.dropdown_menu['menu'].configure(activebackground=_activebgcolordark)
            self.theme = 'light'
            root.configure(background=_lightwindowbackground)
        else:
            self.bt_themeswitch.configure(text="Light Theme")
            self.Canvas1.configure(background=_bgcolordark)
            self.fx.configure(background=_bgcolordark)
            self.fx.configure(fg=_fgcolordark)
            self.fx.configure(insertbackground=_fgcolordark)
            self.x_lower.configure(background=_bgcolordark)
            self.x_lower.configure(fg=_fgcolordark)
            self.x_upper.configure(background=_bgcolordark)
            self.x_upper.configure(fg=_fgcolordark)
            self.xpoints.configure(background=_bgcolordark)
            self.xpoints.configure(foreground=_fgcolordark)
            self.ypoints.configure(background=_bgcolordark)
            self.ypoints.configure(foreground=_fgcolordark)
            self.stepsize.configure(background=_bgcolordark)
            self.stepsize.configure(fg=_fgcolordark)
            self.bt_plot.configure(activebackground=_activebgcolordark)
            self.dropdown_menu.configure(activebackground=_activebgcolordark)
            self.color_input.configure(background=_bgcolordark)
            self.color_input.configure(fg=_fgcolordark)
            self.bt_go.configure(activebackground=_activebgcolordark)
            self.bt_themeswitch.configure(activebackground=_activebgcolordark)
            self.Label1.configure(background=_darkwindowbackground)
            self.Label1.configure(fg=_fgcolordark)
            self.Label2.configure(background=_darkwindowbackground)
            self.Label2.configure(fg=_fgcolordark)
            self.Label3.configure(background=_darkwindowbackground)
            self.Label3.configure(fg=_fgcolordark)
            self.Label4.configure(background=_darkwindowbackground)
            self.Label4.configure(fg=_fgcolordark)
            self.Label5.configure(background=_darkwindowbackground)
            self.Label5.configure(fg=_fgcolordark)
            self.Label6.configure(background=_darkwindowbackground)
            self.Label6.configure(fg=_fgcolordark)
            self.stepLabel.configure(background=_darkwindowbackground)
            self.stepLabel.configure(fg=_fgcolordark)
            self.FunctionRadio.configure(background=_darkwindowbackground)
            self.FunctionRadio.configure(fg=_fgcolordark)
            self.LineRadio.configure(background=_darkwindowbackground)
            self.LineRadio.configure(fg=_fgcolordark)
            self.Check.configure(background=_darkwindowbackground)
            self.Check.configure(fg=_fgcolordark)
            self.bt_go.configure(background=_bgcolordark)
            self.bt_go.configure(fg=_fgcolordark)
            self.bt_plot.configure(background=_bgcolordark)
            self.bt_plot.configure(fg=_fgcolordark)
            self.bt_themeswitch.configure(background=_bgcolordark)
            self.bt_themeswitch.configure(fg=_fgcolordark)
            self.dropdown_menu.configure(background=_bgcolordark)
            self.dropdown_menu.configure(fg=_fgcolordark)
            self.dropdown_menu['menu'].configure(fg=_fgcolordark)
            self.dropdown_menu['menu'].configure(background=_bgcolordark)
            self.theme = 'dark'
            root.configure(background=_darkwindowbackground)


        self.rePlot(self.radiovar.get())

    def resize_plot(self, event):
        if gui_support.plotted:
            gui_support.Plot(self.fx.get(), range(int(self.x_lower.get()),
                             int(self.x_upper.get())), self.color_input.get(),
                             self.theme, self.Canvas1, self.line_style, self.file_path)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

    def check_value(self, value, label):
        if value == '':
            msgbox.showerror("Error", "{} cannot be empty".format(label))
            return False

        try:
            float(value)
        except ValueError:
            msgbox.showerror("Error", "{} should be an integer".format(label))
            return False

        return True

if __name__ == "__main__":
    vp_start_gui()
