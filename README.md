# Biological Data Project
MsC in Data Science - University of Padua

Commissioned by Prof. S. Tosatto and Prof. D. Piovesan for the Biological Data course (a.y. 2020/2021) 

## Files and folders

The main folders are:
* `binx/`, tha contains the binary software such as BLAST and HMMER that must be installed using the `setup.sh`. Note that all the files but `mTM-align` (which download link is obfuscated) are retrieved by `setup.sh`, thus they aren't present in this remote repository; 
* `code/`, that contains all the Python and bash scripts and the main notebook;
* `data/`;
* `results/`.

The project main file is the Jupyter Notebook `project.ipynb` contained in `../code` directory. It provides all the steps and supporting documentation, so the reader can start from here.
In addition, you can find a PDF report giving a high level explanation of the work. 

All the other folders contain auxiliary files, data and outputs that are that are entirely managed by the notebook code.


## Requirements

The script `setup.sh`, which is meant to install all the compiled code, must be ran on a Linux x64 machine. The other bash commands are feasible also for Unix-like systems.
All the rest of the code can be executed on every machine running Python 3. The whole project can be visualized on DeepNote at the following [link](https://deepnote.com/project/dab01843-4697-4e38-8601-caa4706bd153).

The parts that require the software installed by `setup.sh` can be skipped using the precomputed outputs provided in `results/` and `models/`.

The required non-builtin libraries can be found in `requirements.txt` and can be installed running the command:
```
pip install -r requirements.txt
```
in the repository folder. This can be also executed directly in the notebook.