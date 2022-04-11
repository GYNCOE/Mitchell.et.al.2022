# Mitchell.et.al.2022

Python scripts from Mitchell et al. 2022

## Malleator

### Overview

Extracts the specific Cartesian coordinates for all individual annotations from the paired .annotation files and merges them into a single XML import file.

### Steps To Run

1. Save the .annotation files for the slide together in a subfolder under the main project folder
2. Open the .XML Import script and enter the address for the main project folder between the quotes at the bottom of the script
3. Run the script to generate the .XML import file.

## Dapo

### Overview 

Merges tiles from separate annotation layers into one layer, thus significantly improving HALO analysis speed.

### Steps To Run

1. Export the multilayered annotations as a .annotation file
2. Place Dapo script in the same folder as the .annotation file
3. Copy the filename of the .annotation file
4. Open the python script and paste the filename between the quotes at the bottom of the program
5. Run the script to generate the merged annotation file
