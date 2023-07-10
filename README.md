

## GeneMineScan v1.0.0 :rocket:

**v1.0.0: This is a graphical user interface (GUI) application built using Tkinter for running InterProScan locally, a widely used tools for protein sequence analysis and functionall annotation using several bioinformatics tools.**

## Requirements:
- Ubuntu operating system 20.04
- Python 3.x
- Tkinter
- Pillow (PIL)
- pandas
- matplotlib
- Download of Interproscan: https://interproscan-docs.readthedocs.io/en/latest/InstallationRequirements.html

## Installation:

Clone the repository or download the code files: git clone https://github.com/mattoslmp/CNP-Ciimar.git 
Install the required python packages using the following command:

```shell
pip install pillow pandas matplotlib
```
- modify the path for interproscan in the code interproscan_gui.py

To run the InterProScan GUI application, execute the following command:

```shell
python GeneMineScan_gui.py
```
- Install perl 5:
```shell
  sudo apt-get install -y perl5
  ```
- Install java jdk version 11:
```shell
  sudo apt install default-jre
```
**Make sure to follow the installation instructions (any doubt contact us for the E-mail).**

**After run the application window will appear with several input fields and buttons. Here's a description of each component:**

**Logo: This section displays a label where you can insert your own logo image file. Click the "Select Logo" button to choose an image file (in PNG, JPG, or JPEG format). The selected image will be displayed in the label.**

## Logo:
This section displays a label where you can insert your own logo image file. Click the "Select Logo" button to choose an image file (in PNG, JPG, or JPEG format). The selected image will be displayed in the label.

## Input File (FASTA):
Use this section to select the input file in FASTA format of predicted proteome of any organisms. Click the "Select File" button to choose a file using the file dialog. The selected file path will be displayed in the entry field.

## Output Directory:
This section allows you to select the output directory where the results of InterProScan will be saved. Click the "Select Directory" button to choose a directory using the file dialog. The selected directory path will be displayed in the entry field.

## Applications:
Specify the applications to be used in InterProScan in this section. Enter the application names or codes in the entry field. Multiple applications can be separated by commas.

## CPU:
Enter the number of CPUs to be used for running InterProScan in this section.

## Disable Precalculated Results:
Check this box if you want to disable precalculated results in InterProScan.

## Disable Residue Annotation:
Check this box if you want to disable residue annotation in InterProScan.

## Run InterProScan:
Click this button to start the InterProScan process with the specified parameters. The output will be saved in the selected output directory.

## Please cite:

   - Interproscan proper citations: https://interproscan-docs.readthedocs.io/en/latest/Citing.html.
   - If GeneMineScan was useful provide proper credits for the Authors: Leandro de Mattos Pereira and Pedro Leão.
   
## License:
 - This project is licensed under the MIT License (https://github.com/mattoslmp/CNP-Ciimar/blob/main/bin/LICENSE)

## More about - Authors:

- [Junior Researcher, Leandro de Mattos Pereira](https://mattoslmp.github.io)
- [CNP team, Dr. Pedro Leão, Researcher Leader](https://leaolab.wixsite.com/leaolab)

## Acknowledgments

- The code is based on the Tkinter library (https://docs.python.org/3/library/tkinter.html) for creating the GUI.
- The InterProScan tool is developed by the InterPro team (Robert D Finn et al, 2020).
- Interproscan information here: https://interproscan-docs.readthedocs.io/en/latest/Citing.html

## Perspectives:

- New features will be available soon in the GeneMineScan v1.0.1:  Graphics with distribution of the families of identified proteins at Level of Taxonomic classification Species/Order.
____________________________________________________________________________________________________________________________________________________________________
