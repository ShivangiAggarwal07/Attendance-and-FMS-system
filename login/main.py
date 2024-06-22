from tkinter import *
from tkinter import messagebox
from transitions import Machine
import ast
import cv2
import os
import tkinter as tk
from tkinter import simpledialog

import os
from tkinter import Tk, PhotoImage, Label

# Print the current working directory
print("Current working directory:", os.getcwd())

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the image
image_path = os.path.join(script_dir, 'login.png')

# Print the full path for debugging purposes
print("Full image path:", image_path)

# Initialize Tkinter
root = Tk()

try:
    # Load the image
    img = PhotoImage(file=image_path)
    # Display the image in a label
    label = Label(root, image=img)
    label.pack()
except Exception as e:
    print("Error loading image:", e)

# Run the Tkinter main loop

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
       

        Label(screen,text='Hello User',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0, ).place(x=35,y=330)
        
        

        screen.mainloop
    else:
        messagebox.showerror('Invalid','Invalid username or password')
##########
def signup_command():
    window=Toplevel(root)
    window.title("Sign Up")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()
        if password==conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
            

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))
                messagebox.showinfo('Signup','Sucessfully sign up')
                window.destroy()
                
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
    
        else:
            messagebox.showerror('Invalid',"Both Password should match")

    def signin():
        window.destroy()


    img = PhotoImage(file='login1.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)
    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading= Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=0)

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name =='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name =='':
            code.insert(0,'Username')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        name=conform_code.get()
        if name =='':
            conform_code.insert(0,'Conform Password')

    conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,' Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
##################
    def webcam():
        def capture_face_image():
    # Initialize the Tkinter window
            root = tk.Tk()
            root.withdraw()  # Hide the root window

    # Ask the user for the image name
            image_name = simpledialog.askstring("Input", "Enter your mobile number(without space)")

    # Validate the input
            if not image_name:
                print("No name provided. Exiting.")
                return

    # Directory to save the image
            save_directory = "face.data"

    # Create the directory if it doesn't exist
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

    # Add the file extension and directory to the image name
            image_path = os.path.join(save_directory, image_name + ".jpg")

    # Check if the file already exists
            if os.path.exists(image_path):
                print(f"You are already registered")
                return

    # Load the pre-trained Haar cascade for face detection
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                print("Error: Could not open camera.")
                return

            face_detected_frames = 0
            required_detected_frames = 10  # Number of frames the face must be detected to capture the image

            while True:
        # Read a frame from the camera
                ret, frame = cap.read()

                if not ret:
                    print("Error: Could not read frame.")
                    break

        # Convert the frame to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the frame with detected faces
                cv2.imshow("Face Detection", frame)

        # If a face is detected, increase the counter
                if len(faces) > 0:
                    face_detected_frames += 1
                else:
                    face_detected_frames = 0

        # Check if the face has been detected in the required number of frames
                if face_detected_frames >= required_detected_frames:
            # Crop the first detected face
                    (x, y, w, h) = faces[0]
                    face = frame[y:y+h, x:x+w]

            # Save the captured face to a file
                    cv2.imwrite(image_path, face)
                    print(f"Image saved as {image_path}")
                    break

        # Check if the user pressed the 'q' key to exit manually
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Exiting without saving.")
                    break

    # Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()

        if __name__ == "__main__":
            capture_face_image()

##############################
    Button(frame,width=19,pady=1,text='Take picture',bg='#57a1f8',fg='white',border=0,command=webcam ).place(x=95,y=280)
    


    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup ).place(x=35,y=330)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=370)

    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
    signin.place(x=200,y=370)

    window.mainloop()






#####

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=0)




def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name =='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)


sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)

root.mainloop()
