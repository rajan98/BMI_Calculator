from Tkinter import*
import tkMessageBox


class GUI:
    def __init__(self):
        self.root = Tk()

        self.Name = ""
        self.Age = 0
        self.Gender = ""
        self.Weight = 0.0
        self.Height = 0.0
        self.BPLow = 0.0
        self.BPHigh = 0.0
        self.Pulse = 0.0
        self.RBC = 0.0
        self.WBC = 0.0
        self.Platelets = 0.0
        self.HB = 0.0
        self.UricAcid = 00
        self.Cholesterol = 0.0

        self.BMI = ""
        self.OutputBP = ""
        self.OutputPulse = ""
        self.OutputRBC = ""
        self.OutputWBC = ""
        self.OutputPlatelets = ""
        self.OutputHB = ""
        self.OutputUricAcid = ""
        self.OutputCholesterol = ""

        self.input_window()

    def input_window(self):
        self.root.title("BMI Calculator")

        menu = Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label="New", command=self.new_project)
        menu.add_command(label="About", command=self.about)

        self.FirstFrame = Frame(self.root, height=600, width=400)
        self.FirstFrame.pack()

        self.Title = Label(self.FirstFrame, text="Fitness", bg="black", fg="White").grid(row=0, column=0, sticky='w')

        self.l1 = Label(self.FirstFrame, text="").grid(row=1)

        self.NameLabel = Label(self.FirstFrame,text="Name:   ").grid(row=2, column=0)
        self.NameEntry = Entry(self.FirstFrame)
        self.NameEntry.grid(row=2, column=1)
        self.l2 = Label(self.FirstFrame, text="        ").grid(row=2, column=3)
        self.AgeLabel = Label(self.FirstFrame, text="Age:    ").grid(row=2, column=4)
        self.AgeEntry = Entry(self.FirstFrame)
        self.AgeEntry.bind('<KeyPress>', self.key_press_age)
        self.AgeEntry.grid(row=2, column=5)

        self.l2 = Label(self.FirstFrame, text="").grid(row=3)

        self.Gen = StringVar()
        self.GenderLabel = Label(self.FirstFrame,text="Gender: ").grid(row=4, column=0)
        self.MaleRadiobutton = Radiobutton(self.FirstFrame, text="Male", value="Male", variable=self.Gen)
        self.MaleRadiobutton.grid(row=4, column=3)
        self.FemaleRadiobutton = Radiobutton(self.FirstFrame, text="Female", value="Female", variable=self.Gen)
        self.FemaleRadiobutton.grid(row=4, column=5)

        self.l3 = Label(self.FirstFrame, text="").grid(row=5)

        self.WeightLabel = Label(self.FirstFrame, text="Weight(Kg): ").grid(row=6, column=0, sticky='w')
        self.WeightEntry = Entry(self.FirstFrame)
        self.WeightEntry.bind('<KeyPress>',self.key_press)
        self.WeightEntry.grid(row=6, column=1)

        self.HeightLabel = Label(self.FirstFrame, text="Height(m): ").grid(row=7, column=0, sticky='w')
        self.HeightEntry = Entry(self.FirstFrame)
        self.HeightEntry.bind('<KeyPress>',self.key_press)
        self.HeightEntry.grid(row=7, column=1)

        self.BPLowLabel = Label(self.FirstFrame, text="BP Low: ").grid(row=8, column=0, sticky='w')
        self.BPLowEntry = Entry(self.FirstFrame)
        self.BPLowEntry.bind('<KeyPress>',self.key_press)
        self.BPLowEntry.grid(row=8, column=1)

        self.BPHighLabel = Label(self.FirstFrame, text="BP High: ").grid(row=9, column=0, sticky='w')
        self.BPHighEntry = Entry(self.FirstFrame)
        self.BPHighEntry.bind('<KeyPress>',self.key_press)
        self.BPHighEntry.grid(row=9, column=1)

        self.PulseLabel = Label(self.FirstFrame, text="Pulse Rate : ").grid(row=10, column=0, sticky='w')
        self.PulseEntry = Entry(self.FirstFrame)
        self.PulseEntry.bind('<KeyPress>',self.key_press)
        self.PulseEntry.grid(row=10, column=1)

        self.RBCLabel = Label(self.FirstFrame, text="RBC Count(TilinCell/L): ").grid(row=11, column=0, sticky='w')
        self.RBCEntry = Entry(self.FirstFrame)
        self.RBCEntry.bind('<KeyPress>',self.key_press)
        self.RBCEntry.grid(row=11, column=1)

        self.WBCLabel = Label(self.FirstFrame, text="WBC Count(BillionCell/L) : ").grid(row=12, column=0, sticky='w')
        self.WBCEntry = Entry(self.FirstFrame)
        self.WBCEntry.bind('<KeyPress>',self.key_press)
        self.WBCEntry.grid(row=12, column=1)

        self.PlateletsLabel = Label(self.FirstFrame, text="Platelets(Bilion/L): ").grid(row=13, column=0, sticky='w')
        self.PlateletsEntry = Entry(self.FirstFrame)
        self.PlateletsEntry.bind('<KeyPress>',self.key_press)
        self.PlateletsEntry.grid(row=13, column=1)

        self.HBLabel = Label(self.FirstFrame, text="HB(g/dL): ").grid(row=14, column=0, sticky='w')
        self.HBEntry = Entry(self.FirstFrame)
        self.HBEntry.bind('<KeyPress>',self.key_press)
        self.HBEntry.grid(row=14, column=1)

        self.UricAcidLabel = Label(self.FirstFrame, text="Uric Acid(mg/dL): ").grid(row=15, column=0, sticky='w')
        self.UricAcidEntry = Entry(self.FirstFrame)
        self.UricAcidEntry.bind('<KeyPress>',self.key_press)
        self.UricAcidEntry.grid(row=15, column=1)

        self.CholesterolLabel = Label(self.FirstFrame, text="Cholesterol(mmol/L) : ").grid(row=16, column=0, sticky='w')
        self.CholesterolEntry = Entry(self.FirstFrame)
        self.CholesterolEntry.bind('<KeyPress>',self.key_press)
        self.CholesterolEntry.grid(row=16, column=1)

        self.ReportButton = Button(self.FirstFrame, text="Generate Report", bg="lightblue", command=self.assign_values)
        self.ReportButton.grid(row=15, column=5, rowspan=2)

    def key_press_age(self, event):
        if event.char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ):
            return
        elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace', 'Tab'):
            return 'break'

    def key_press(self, event):
        if event.char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            return
        elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace', 'Tab'):
            return 'break'

    def assign_values(self):
        if self.NameEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Name")
            return
        else:
            self.Name = self.NameEntry.get()

        if self.AgeEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Age")
            return
        else:
            self.Age = int(self.AgeEntry.get())

        if str(self.Gen.get()) == "":
            tkMessageBox.showerror("Error", "Select Gender")
            return
        else:
            self.Gender = str(self.Gen.get())

        if self.WeightEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Weight")
            return
        else:
            self.Weight = float(self.WeightEntry.get())

        if self.HeightEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Height")
            return
        else:
            self.Height = float(self.HeightEntry.get())

        if self.BPLowEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter BP Low")
            return
        else:
            self.BPLow = float(self.BPLowEntry.get())

        if self.BPHighEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter BP High")
            return
        else:
            self.BPHigh = float(self.BPHighEntry.get())

        if self.PulseEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Pulse")
            return
        else:
            self.Pulse = float(self.PulseEntry.get())

        if self.RBCEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter RBC")
            return
        else:
            self.RBC = float(self.RBCEntry.get())

        if self.WBCEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter WBC")
            return
        else:
            self.WBC = float(self.WBCEntry.get())

        if self.PlateletsEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Platelets")
            return
        else:
            self.Platelets = float(self.PlateletsEntry.get())

        if self.HBEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter HB")
            return
        else:
            self.HB = float(self.HBEntry.get())

        if self.UricAcidEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Uric Acid")
            return
        else:
            self.UricAcid = float(self.UricAcidEntry.get())

        if self.CholesterolEntry.get() == "":
            tkMessageBox.showerror("Error", "Enter Cholesterol")
            return
        else:
            self.Cholesterol = float(self.CholesterolEntry.get())

        self.calculate()

    def calculate(self):
        self.BMI=(self.Weight/(self.Height*self.Height))
        if self.BPHigh<=90 and self.BPLow<=60 :
            self.OutputBP = "Low"
        elif self.BPHigh<=120 and self.BPLow<=80:
            self.OutputBP = "Medium"
        else:
            self.OutputBP = "High"

        if self.Pulse<60:
            self.OutputPulse = "Low"
        elif self.Pulse>100 and self.Pulse<60:
            self.OutputPulse = "Medium"
        else:
            self.OutputPulse = "High"

        if self.Gender == "Male":
            if self.RBC <= 4.7:
                self.OutputRBC = "Low"
            elif self.RBC>4.7 and self.RBC<6.1:
                self.OutputRBC = "Medium"
            else:
                self.OutputRBC = "High"
        elif self.Gender == "Female":
            if self.RBC <= 4.2:
                self.OutputRBC = "Low"
            elif self.RBC>4.2 and self.RBC<5.4:
                self.OutputRBC = "Medium"
            else:
                self.OutputRBC = "High"

        if self.WBC<=3.5:
            self.OutputWBC = "Low"
        elif self.WBC>3.5 and self.WBC<10.5:
            self.OutputWBC = "Medium"
        else:
            self.OutputWBC = "High"

        if self.Platelets<=150:
            self.OutputPlatelets = "Low"
        elif self.Platelets>150 and self.Platelets<450:
            self.OutputPlatelets = "Medium"
        else:
            self.OutputPlatelets = "High"

        if self.Gender == "Male":
            if self.HB <= 13.5:
                self.OutputHB = "Low"
            elif self.HB>13.5 and self.HB<17.5:
                self.OutputHB = "Medium"
            else:
                self.OutputHB = "High"
        elif self.Gender == "Female":
            if self.HB <= 12.0:
                self.OutputHB = "Low"
            elif self.HB>12.0 and self.HB<15.5:
                self.OutputHB = "Medium"
            else:
                self.OutputHB = "High"

        if self.Gender == "Male":
            if self.UricAcid < 3.4:
                self.OutputUricAcid = "Low"
            elif self.UricAcid > 3.4 and self.UricAcid <7.0:
                self.OutputUricAcid = "Medium"
            else:
                self.OutputUricAcid = "High"

        elif self.Gender == "Female":
            if self.UricAcid < 2.4:
                self.OutputUricAcid = "Low"
            elif self.UricAcid > 2.4 and self.UricAcid <6.0:
                self.OutputUricAcid = "Medium"
            else:
                self.OutputUricAcid = "High"

        if self.Cholesterol <= 100:
            self.OutputCholesterol = "Low"
        elif self.Cholesterol > 100 and self.Cholesterol <200:
            self.OutputCholesterol = "Medium"
        else:
            self.OutputCholesterol = "High"

        self.output_window()

    def output_window(self):
        self.output = Tk()
        self.output.title("Output")
        self.OutputFrame = Frame(self.output, height=400, width=400)
        self.OutputFrame.pack()

        self.Topic = Label(self.OutputFrame, text="Report", bg='black', fg='white')
        self.Topic.grid(row=0, column=0, sticky='w')

        self.L0 = Label(self.OutputFrame, text="   ")
        self.L0.grid(row=1)

        self.L0.grid(row=2, column=1)
        self.L1 = Label(self.OutputFrame, text="BMI(Body Mass Index): ")
        self.L1.grid(row=2, column=2, sticky='w')
        self.OL1 = Label(self.OutputFrame, text=self.BMI, bg='white')
        self.OL1.grid(row=2, column=3, sticky='w')
        self.L0.grid(row=2, column=4)

        self.L2 = Label(self.OutputFrame, text="BP(High/Medium/Low): ")
        self.L2.grid(row=3, column=2, sticky='w')
        self.OL2 = Label(self.OutputFrame, text=self.OutputBP, bg='white')
        self.OL2.grid(row=3, column=3, sticky='w')

        self.L3 = Label(self.OutputFrame, text="Pulse Rate(High/Medium/Low): ")
        self.L3.grid(row=4, column=2, sticky='w')
        self.OL3 = Label(self.OutputFrame, text=self.OutputPulse, bg='white')
        self.OL3.grid(row=4, column=3, sticky='w')

        self.L4 = Label(self.OutputFrame, text="RBC Count(High/Medium/Low): ")
        self.L4.grid(row=5, column=2, sticky='w')
        self.OL4 = Label(self.OutputFrame, text=self.OutputRBC, bg='white')
        self.OL4.grid(row=5, column=3, sticky='w')

        self.L5 = Label(self.OutputFrame, text="WBC Count(High/Medium/Low): ")
        self.L5.grid(row=6, column=2, sticky='w')
        self.OL5 = Label(self.OutputFrame, text=self.OutputWBC, bg='white')
        self.OL5.grid(row=6, column=3, sticky='w')

        self.L6 = Label(self.OutputFrame, text="Platelets(High/Medium/Low): ")
        self.L6.grid(row=7, column=2, sticky='w')
        self.OL6 = Label(self.OutputFrame, text=self.OutputPlatelets, bg='white')
        self.OL6.grid(row=7, column=3, sticky='w')

        self.L7 = Label(self.OutputFrame, text="HB(High/Medium/Low): ")
        self.L7.grid(row=8, column=2, sticky='w')
        self.OL7 = Label(self.OutputFrame, text=self.OutputHB, bg='white')
        self.OL7.grid(row=8, column=3, sticky='w')

        self.L8 = Label(self.OutputFrame, text="Uric Acid(High/Medium/Low): ")
        self.L8.grid(row=9, column=2, sticky='w')
        self.OL8 = Label(self.OutputFrame, text=self.OutputUricAcid, bg='white')
        self.OL8.grid(row=9, column=3, sticky='w')

        self.L9 = Label(self.OutputFrame, text="Cholesterol(High/Medium/Low): ")
        self.L9.grid(row=10, column=2, sticky='w')
        self.OL9 = Label(self.OutputFrame, text=self.OutputCholesterol, bg='white')
        self.OL9.grid(row=10, column=3, sticky='w')

    def new_project(self):
        self.FirstFrame.destroy()
        self.input_window()

    def about(self):
        about_page = Tk()
        l1 = Label(about_page, text="This Project Calculates The BMI and shows the Medical State of a patient")
        l1.grid(row=0, column=1)

        l3 = Label(about_page, text="Coding Done By:  Rajan Kumar Shah.")
        l3.grid(row=2, column=1, sticky="w")

x = GUI()

x.root.mainloop()
