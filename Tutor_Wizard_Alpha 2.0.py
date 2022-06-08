# tutor_Wizard_Alpha.py
# A program aimed to solve generic questions students face in each designated module.
# The Alpha version only includes two subjects as of now; Maths and Cybersecurity.

import os
import math
import turtle
import Tkinter as tk

################################################################################################################################################################################################################################################

# Set size of terminal window (exe)
os.system("mode con cols=200 lines=50")

#Set ratio of splash window
root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.state('zoomed')
root.geometry('%dx%d+%d+%d' % (width*0.5, height, width, height))

#Load image
image_file = "logo.gif"
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*4, width=width*1, bg="white")
canvas.create_image(width*0.5, height*0.9/2, image=image)
canvas.pack()


#Show the splash screen for (n) number of milliseconds before running main()
root.after(3000, root.destroy)
root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to Tutor Wizard Alpha access. For help with Maths please load the module by entering ma3101. For help with Cybersecurity please load the module by entering cc3101.")
print
def main():
    r = raw_input("Please enter the module code you want to load or press 'e' to exit the program: ")
    if r == "ma3101":
        print
        print(

        '''***You have selected the MA3101 maths module tutorial wizard. There are several functions included in this Module***
        
        1# which_Triangle: Finds the type of triangle by measure of sides.

        2# draw_Triangle : Draws an accurate representation of the triangles as well as reflex triangles by measure of sides and angles.

        3# area_Triangle : Finds the area of a triangle by measure of sides.

        '''

        )

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        def which_Triangle():

            text = raw_input("Please enter the lengths of your triangle in the following order- (side ab,side ac,side bc): \n")

            # Text is split by commas
            text = text.split(",")

            # Check for 3 results 
            if len(text) != 3:
                print 'Sorry you must enter 3 values, for each side of the triangle.\n'
                return

            # Strip any spaces and convert to int
            try:
                text = [int(t.strip()) for t in text]
            except ValueError:
                print 'Sorry although you entered in 3 values, you must enter a valid integer.\n'
                return

            s1,s2,s3 = text

            if not((s1+s2>s3) and (s2+s3>s1) and (s1+s3>s2)):
                print 'Sorry, your triangle is invalid. According to the Triangle Inequality Theorem the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side. \n'
            #Triangle Inequality Theorem
         
            elif((s1**2)==(s2**2)+(s3**2) or (s2**2)==(s1**2)+(s3**2) or (s3**2)==(s2**2)+(s1**2)):
                print 'Your triangle is a Right-Angled triangle. \n'
            #Right-angled Triangle
            
            elif(s1 == s2 == s3):
                print 'Your triangle is an Equilateral triangle. \n'
            #Equilateral Triangle 

            elif(s1 != s2 != s3) and ((s1**2)>(s2**2)+(s3**2) or (s2**2)>(s1**2)+(s3**2) or (s3**2)>(s2**2)+(s1**2)):
                print 'Your triangle is an Obtuse-Angled Scalene triangle. \n'
            #Obtuse-angled Scalene Triangle

            elif((s1==s3 and s1!=s2) or (s1==s2 and s1!=s3) or (s2==s3 and s2!=s1)) and ((s1**2)>(s2**2)+(s3**2) or (s2**2)>(s1**2)+(s3**2) or (s3**2)>(s2**2)+(s1**2)):
                print 'Your triangle is an Obtused-Angled Isoceles Triangle. \n'
            #Obtused-angled Isoceles Triangle

            elif(s1 != s2 != s3) and ((s1**2)<(s2**2)+(s3**2) or (s2**2)<(s1**2)+(s3**2) or (s3**2)<(s2**2)+(s1**2)):
                print 'Your triangle is an Acute-Angled Scalene Triangle. \n'
            #Acute-angled Scalene Triangle
            
            elif ((s1==s3 and s1!=s2) or (s1==s2 and s1!=s3) or (s2==s3 and s2!=s1)) and ((s1**2)<(s2**2)+(s3**2) or (s2**2)<(s1**2)+(s3**2) or (s3**2)<(s2**2)+(s1**2)):
                print 'Your triangle is an Acute-Angled Isoceles Triangle. \n'
            #Acute-angled Iscoceles Triangle

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Turtle graphics section

        def draw_Triangle():
            string = raw_input("Please enter the lengths and angles of your triangle in the following order - (angle a,angle b,angle c,side ab,side ac,side bc): \n")

            # String is split by commas
            string = string.split(",")

            # Check for 6 results 
            if len(string) != 6:
                print 'Sorry you must enter 6 values, 3 for each side of the triangle and 3 for each angle of the triangle in any given order.\n'
                return

            # Strip any spaces and convert to int
            try:
                string = [int(t.strip()) for t in string]
            except ValueError:
                print 'Sorry although you entered in 6 values, you must enter a valid integer.\n'
                return
            anga,angb,angc,sidab,sidac,sidbc = string
            print
            print ("Entering drawing Mode..")
            print ("Press any key to continue.")
            # Wait for user input
            pause=raw_input()
            rt=turtle
            # New screen
            rt.clearscreen()
            rt.screensize(2000, 1500)
            rt.ht()
            numbers=[sidab, sidac, sidbc]
            newnumb=numbers
            # Sort sides in ascending order
            newnumb.sort()
            # Find the biggest side of triangle and adjust ratio sizer accordingly
            bigest=newnumb[2]
            if bigest is sidab:
                coll=ratiosizer(sidab, sidac, sidbc)
                if sidac!=sidab:
                    sidac=coll[1]
                else:
                    sidac=300
                if sidbc!=sidab:
                    sidbc=coll[2]
                else:
                    sidbc=300
                sidab=coll[0]
            elif bigest is sidac:
                coll=ratiosizer(sidac, sidab, sidbc)
                if sidab !=sidac:
                    sidab=coll[1]
                else:
                    sidab=300
                if  sidbc!=sidac:
                    sidbc=coll[2]
                else:
                    sidbc=300
                sidac=coll[0]
            elif bigest is sidbc:
                coll=ratiosizer(sidbc, sidac, sidab)
                if sidab != sidbc:
                    sidab = coll[2]
                else:
                    sidab = 300

                if sidac != sidbc:
                    sidac = coll[1]
                else:
                    sidac = 300
                sidbc=coll[0]
            rt.color("black", "blue")
            rt.begin_fill()
            acor=t_mover(rt, anga, sidab)
            bcor=t_mover(rt, angb, sidbc)
            ccor=t_mover(rt, angc, sidac)
            rt.end_fill()
            print ("PRESS ANY KEY TO CONTINUE")
            pause=raw_input()
            return True

#----------------------------------------------------------------------------------------------------------------------

    #Resets turtle pos for next move
        def t_mover(self, angle, distance):
            pripos=self.pos()
            self.left(angle)
            self.forward(distance)
            self.right(180)    
            return pripos

#----------------------------------------------------------------------------------------------------------------------

    #Resizes triangles
        def ratiosizer(arg, arg1, arg2):
            rat=300/arg
            frarg=arg1*rat
            secarg=arg2*rat
            return [300, frarg, secarg]

#-----------------------------------------------------------------------------------------------------------------------

    # Finds the area of the triangle given 3 inputs
        def area_Triangle():

            txt = raw_input("Please enter the lengths of your triangle in the following order to find the area for your triangle - (side ab,side ac,side bc): \n ")
            # Text is split by commas
            txt = txt.split(",")

            # Check for 3 results 
            if len(txt) != 3:
                print 'Sorry you must enter 3 values, for each side of the triangle.\n'
                return

            # Strip any spaces and convert to int
            try:
                txt = [int(t.strip()) for t in txt]
            except ValueError:
                print 'Sorry although you entered in 3 values, you must enter a valid integer.\n'
                return

            l1,l2,l3 = txt
            # Check against triangle inequality theorem 
            if not((l1+l2>l3) and (l2+l3>l1) and (l1+l3>l2)):
                print 'Sorry, your triangle is invalid. According to the Triangle Inequality Theorem the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side. \n'
                select()
            p= ((l1+l2+l3)/2)
            try:
                A= math.sqrt(p*((p-l1)*(p-l2)*(p-l3)))
                print 'The area of the triangle is',A
                return
            except ValueError:
                print 'Sorry your triangle is invalid. According to the Triangle Inequality Theorem the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side. \n'
                return
#-----------------------------------------------------------------------------------------------------------------------
        def select():
                c = str(raw_input("Please enter the corresponding number for the function you wish to use or press 'z' to return to main menu \n"))
                if c == str(1):
                    which_Triangle()
                elif c == str(2):
                    draw_Triangle()
                elif c == str(3):
                    area_Triangle()
                elif c == 'z':
                    main()
                else:
                    print "Sorry, please ensure you type in either 1 , 2 , 3 or press 4 to exit the program. \n"
        while select:
            select()


################################################################################################################################################################################################################################################

    
    elif r ==   "cc3101":
        print
        print "***You have selected the CC3101 cybersecurity module tutorial wizard. There two main functions in this module.***\n"
        print "     1# encrypt - this function will encrypt users message"
        print "     2# decrypt - this function will decrypt users message\n"
        print "User critiria:\n"
        print "*Please note that the output will be in lower cases"
        print "*Please do not use spaces or any other symbols except letters\n"

#----------------------------------------------------------------------------------------------------------------------

        def encrypt():
            m=raw_input("Please enter your message: ")
            cipher = raw_input("Please enter coefficeients (a,b,c): ")

            # Text is split by commas
            cipher = cipher.split(",")

            # Check for 3 results 
            if len(cipher) != 3:
                print 'Sorry you must enter 3 coefficients.\n'
                return

            # Strip any spaces and convert to int
            try:
                cipher = [int(t.strip()) for t in cipher]
            except ValueError:
                print 'Sorry although you entered in 3 coefficients, you must enter a valid integer.\n'
                return

            a,b,c = cipher
            
            p = ''
    #before actual encryption we will convert our coefficeints into the shift variable by using quadratic equation
            if a ==0:
                a=a+1
            d = b*b-4*a*c
            if d < 0:
                d=int(d*-1)
                if d > 25:
                    g=input("Please enter additional coefficient in range from 0 to 25: \n")
                    if g > 25 or g < 0:
                        print "Coefficient is not in corresponding range, please try again\n"
                        while choice:
                            choice()
                    else:
                        g <=25
                        d=(d/d)*g               
            else:
                if d == 0:
                    d=int((-b /(2*a))+1)
                else:
                    discRoot = math.sqrt(b*b - 4*a*c)
                    root1 = (-b + discRoot)/(2*a)
                    root2 = (-b - discRoot)/(2*a)
                    d = int(root1+root2)
                            
            for i in m.lower():
                i = (ord(i)+d)
                if i - d==26:
                    i=26
                elif i > ord('z'):
                    i-=26
                elif i < ord('a'):
                    i+=26
                i=chr(i)
                p=p+i
            print "Your message has successfully been encrypted: ",p
            print
#----------------------------------------------------------------------------------------------------------------------

#decryption part

        def decrypt():
            f=raw_input("Please enter encrypted message: ")
            decipher = raw_input("Please enter coefficeients which were used for encryption: ")

            # Text is split by commas
            decipher = decipher.split(",")

            # Check for 3 results 
            if len(decipher) != 3:
                print 'Sorry you must enter 3 coefficients.\n'
                return

            # Strip any spaces and convert to int
            try:
                decipher = [int(t.strip()) for t in decipher]
            except ValueError:
                print 'Sorry although you entered in 3 coefficients, you must enter a valid integer.\n'
                return

            a,b,c = decipher
            
            p=''
#same methode as with encryption using with decryption.
            if a ==0:
                a=a+1
            d = b*b-4*a*c

            if d < 0:
                d=int(d*-1)
                if d > 25:
                    g=input("Please enter additional coefficient which was used for encryption: \n")
                    if g > 25 or g < 0:
                        print "Coefficient is not in corresponding range, please try again\n"
                        while choice:
                            choice()
                    else:
                        g <=25
                        d=(d/d)*g               
            else:
                if d == 0:
                    d=int(-b /(2*a)+1)
                else:
                    discRoot = math.sqrt(b*b - 4*a*c)
                    root1 = (-b + discRoot)/(2*a)
                    root2 = (-b - discRoot)/(2*a)
                    d = int(root1+root2)
#changing signs in first two lines of below decryption code
                    
            for i in f.lower():
                i = (ord(i)-d)
                if i + d==26:
                    i=26
                elif i > ord('z'):
                    i-=26
                elif i < ord('a'):
                    i+=26
                i=chr(i)
                p=p+i
            print "Your message has successfully been decrypted: ",p
            print
            
#function to provide a choice between above matters

#----------------------------------------------------------------------------------------------------------------------
        def choice():
            l = str(raw_input("Please press 1 to encrypt and 2 to decrypt your message or press 'z' to go to main menu: \n "))
            if l==str(1):
                encrypt()
            elif l==str(2):
                decrypt()
            elif l== 'z':
                main()
            else:
                print "Your choice has not been defined, please try again or press 3 for exit! \n"
        while choice:
            choice()
#----------------------------------------------------------------------------------------------------------------------

    elif r == 'e':
        exit()
    else:
        print "Your choice has not been defined, please try again or press 'e' for exit. \n"
    main()
main()
###################################################################################################################################################################################################################################################
    
    
    
    
















    
     

