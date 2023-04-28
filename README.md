# filecounter
A program to tally parent/child files in a directory. Dependencies: os, argparse, Path from pathlib

>This program was created for academic/research workflows that require counting files within complicated folder structures. For more information please see the program's acompanying blog post.

## Help message
Running `filecounter.py -h` will show the following message. The -f and -d flags added before the path will add additional information to the general output.

```
optional arguments:
  -h, --help           show this help message and exit
  -f, --showfilenames  list files within given path

general output:
  path                 path to target directory

detailed output:
  -d, --subdircount    list totals for each directory within path
```

## Examples

**Use case**: sum all the academic PDF articles within a complicated folder structure
- To get a simple sum, run `filecounter.py path`, where path is the directory you want to run the count for. 

**Use case**: generate a list of CSV dataset files within a complicated folder structure 
- To get a simple list within a directory and its subfolders, add the `-f` flag before the path.

**Use case**: see file count for each subfolder within a directory 
- To get a summary of all subdirectories as well, add the `-d` flag before the path. This can also be used with the above-mentioned `-f` flag.

below is a simple example with a low file count... Please be aware that if files within the specified path surpass 100, or if the child directories within the specified path surpass 15, you will be asked to confirm that you want to print out a detailed summary or list the files.


#### navigate to filecounter.py file
`cd /Users/User_1/Desktop/Programs/`

#### run general output on chosen path
`python3 filecounter.py /Users/User_1/Desktop/Neuro_Lit_Review_2023`

#### output
`> 13 real | 2 hidden | 15 total files`

#### run detailed output
`python3 filecounter.py -d /Users/User_1/Desktop/Neuro_Lit_Review_2023`

#### output
```
PATH: /Users/User_1/Desktop/Neuro_Lit_Review_2023/Donald_et_al
>> 6 real | 1 hidden | 7 total files

PATH: /Users/User_1/Desktop/Neuro_Lit_Review_2023/Kirksgaad_et_al
>> 7 real | 1 hidden | 8 total files

> 13 real | 2 hidden | 15 total files
```
#### run detailed report and list files
`python3 filecounter.py -d -f /Users/User_1/Desktop/Neuro_Lit_Review_2023`

#### output
```
PATH: /Users/User_1/Desktop/Neuro_Lit_Review_2023/Donald_et_al
>> 6 real | 1 hidden | 7 total files
  - Donald_et_al_2002_Glia.pdf
  - Donald_et_al_2004_Neurogenesis.pdf
  - Donald_et_al_2007_GlilialAbr.pdf
  - Donald_et_al_2017_NeuronalFatigue.pdf
  - Donald_et_al_2022_Azdghh67.pdf
  - Article_header.png
  - .readme.txt
  
PATH: /Users/User_1/Desktop/Neuro_Lit_Review_2023/Kirksgaad_et_al
>> 7 real | 1 hidden | 8 total files
  - Kirksgaad_et_al2001_Synaptic_Reg.pdf
  - Kirksgaad_et_al_2002.pdf
  - Kirksgaad_et_al_2014.pdf
  - Kirksgaad_and_Kirby_2022.pdf
  - Donald_et_al_2022_56782hjs.pdf
  - TMS_Imagery.png
  - Neuron_at_55mm.png
  - .DStore
  
> 13 real | 2 hidden | 15 total files
```

## Thank you
Thank you for using this program, feel free to fork the code for your own use. 
