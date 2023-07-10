######## Autor: Leandro de Mattos Pereira
######## CNP Laboratory, Pedro Leao - Team Leader - Date: June, 06, 2023

from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import os
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

def import_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if logo_path:
        try:
            image = Image.open(logo_path)
            logo_image = ImageTk.PhotoImage(image)

            # Update the logo image
            logo_label.configure(image=logo_image)
            logo_label.image = logo_image
        except Exception as e:
            messagebox.showerror("Error", str(e))

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("FASTA Files", "*.fasta"), ("All Files", "*.*")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(tk.END, file_path)

def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, output_dir)

def run_interproscan():
    applications = applications_entry.get()
    cpu = cpu_entry.get()
    output_dir = output_dir_entry.get()
    disable_precalc = disable_precalc_var.get()
    disable_residue_annot = disable_residue_annot_var.get()
    input_file = input_file_entry.get()
    output_file = os.path.join(output_dir, "teste.tsv")

    ### replace the line bellow according the directory where you put the interproscan
    
    command = f"bash /home/mattoslmp/interproscan/interproscan-5.61-93.0/interproscan.sh " \
              f"-i {input_file} " \
              f"-o {output_file} " \
              f"-f tsv " \
              f"-appl {applications} " \
              f"-cpu {cpu} " \
              f"-dp {disable_precalc} " \
              f"-dra {disable_residue_annot}"

    print("Running InterProScan with command:")
    print(command)

    if os.path.isfile(output_file):
        messagebox.showerror("Error", "Output file already exists.")
        return

    os.makedirs(output_dir, exist_ok=True)

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", "InterProScan completed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"InterProScan failed with the following error:\n{e}")

# Create the main window
root = tk.Tk()
root.title("InterProScan - Run")

# Add the logo label
logo_label = tk.Label(root, text="Insert your logo", font=("Arial", 12, "bold"))
logo_label.pack()

# Create the logo button
logo_button = tk.Button(root, text="Select Logo", command=import_logo)
logo_button.pack()

# Create the input file section
input_file_frame = tk.Frame(root)
input_file_frame.pack()

input_file_label = tk.Label(input_file_frame, text="Input File (FASTA):")
input_file_label.pack(side=tk.LEFT)

input_file_entry = tk.Entry(input_file_frame, width=50)
input_file_entry.pack(side=tk.LEFT)

input_file_button = tk.Button(input_file_frame, text="Select File", command=select_input_file)
input_file_button.pack(side=tk.LEFT)

# Create the output directory section
output_dir_frame = tk.Frame(root)
output_dir_frame.pack()

output_dir_label = tk.Label(output_dir_frame, text="Output Directory:")
output_dir_label.pack(side=tk.LEFT)

output_dir_entry = tk.Entry(output_dir_frame, width=50)
output_dir_entry.pack(side=tk.LEFT)

output_dir_button = tk.Button(output_dir_frame, text="Select Directory", command=select_output_dir)
output_dir_button.pack(side=tk.LEFT)

# Create the applications section
applications_frame = tk.Frame(root)
applications_frame.pack()

applications_label = tk.Label(applications_frame, text="Applications:")
applications_label.pack(side=tk.LEFT)

applications_entry = tk.Entry(applications_frame, width=50)
applications_entry.pack(side=tk.LEFT)

# Create the CPU section
cpu_frame = tk.Frame(root)
cpu_frame.pack()

cpu_label = tk.Label(cpu_frame, text="CPU:")
cpu_label.pack(side=tk.LEFT)

cpu_entry = tk.Entry(cpu_frame, width=50)
cpu_entry.pack(side=tk.LEFT)

# Create the disable precalc section
disable_precalc_var = tk.IntVar()

disable_precalc_frame = tk.Frame(root)
disable_precalc_frame.pack()

disable_precalc_checkbox = tk.Checkbutton(disable_precalc_frame, text="Disable Precalculated Results",
                                          variable=disable_precalc_var)
disable_precalc_checkbox.pack()

# Create the disable residue annotation section
disable_residue_annot_var = tk.IntVar()

disable_residue_annot_frame = tk.Frame(root)
disable_residue_annot_frame.pack()

disable_residue_annot_checkbox = tk.Checkbutton(disable_residue_annot_frame, text="Disable Residue Annotation",
                                                variable=disable_residue_annot_var)
disable_residue_annot_checkbox.pack()

# Create the run button
run_button = tk.Button(root, text="Run InterProScan", command=run_interproscan)
run_button.pack()

# Run the main window's event loop
root.mainloop()
