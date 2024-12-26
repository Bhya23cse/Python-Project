import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import  ImageTk

def generate_qr():
    data_to_encode = data_entry.get()    #get input from console

    # Create QR code instance
    qr = qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200))

    # Display the QR code image
    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

    messagebox.showinfo("QR Code Generated", "QR code has been successfully generated.")
def save_qr(event=None):
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), 
                                                                                  ("JPEG files", "*.jpg;*.jpeg"), 
                                                                                  ("Bitmap files", "*.bmp"),
                                                                                  ("All Files", "*.*")])
    if file_path:
        generate_qr()
        img = qrcode.make(data_entry.get())
        img.save(file_path)
        # Prompt user to select file path for saving the QR code image
        messagebox.showinfo("Success", "QR code has been successfully saved at:\n{}".format(file_path))

def exit_program():
    check=messagebox.askyesno('Check','Are you sure? To Exit')
    if check==True:
        exit()


root = tk.Tk()
root.title("Code Generator ")
root.geometry("450x500")
placeholder_text=("Enter Here")

heading= tk.Label(root, text="Qr-code Generator\n",font=("Helvetica", 16, "bold", "underline"))
heading.pack()
# Entry for user input -

data_label = tk.Label(root, text="Enter your data to get QR-Code:\n",font=("helvetice",13,"bold"))
data_label.pack()
data_entry = tk.Entry(root,relief="sunken",bd=2, bg="lightgrey",font=("helvetice",14))
data_entry.pack()

tk.Label(root, text="\n")

# Button to generate and save the QR code
generate_button = tk.Button(root, text="Generate",width=10, height=1,font=("helvetice",13,"bold"), command=generate_qr,bd=3, relief="ridge", padx=5, pady=5)
generate_button.pack()

# Label to display the QR code image
qr_label = tk.Label(root)
qr_label.pack()

# Button to save the QR code
save_button = tk.Button(root, text="Save",width=10, height=1,font=("helvetice",13,"bold"), command=save_qr,bd=3, relief="ridge", padx=5, pady=5)
save_button.pack()

# Button to Exit Program
exit_button = tk.Button(root, text="Exit",width=10, height=1,font=("helvetice",13,"bold"), command=exit_program,bd=3, relief="ridge", padx=5, pady=5)
exit_button.pack()

note= tk.Label(root, text="\nNote: Your can also save it by pressing CTRL+S from keyboard",font=("Helvetica", 12))
note.pack()
# Bind Ctrl+S event to save_qr function
root.bind('<Control-s>', save_qr)

root.mainloop()
