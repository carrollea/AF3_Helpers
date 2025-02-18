# AF3_Helpers
Some helpful scripts for prepping files for alphafold3

Convert a fasta file into a json file. 
These scripts can convert one fasta file with multiple protein sequences into multiple json files, one for each protein sequence. 
I've split these into multiple scripts because I don't have time to make one program for all of them. Maybe I'll fix this later. 

##1 Convert a fasta file into individual json files 
Use the FastatoJson.py in the command line. 
```
python3 FastatoJson.py [fasta]
```

##2 Convert a fasta file and an msa file into json files
Use MSAFastatoJson.py 
```
python3 MSAFastatoJson.py [fasta] [msa.a3m]
```

##3 Convert a fasta file, msa file, and one ligand into json files
Use MSALigFastatoJson.py 
```
python3 MSALigFastatoJson.py [fasta] [msa.a3m] [Ligand.txt]
```

##4 Convert a fasta file, msa file and two ligands into json files
Use MSALigFastatoJson.py
```
python3 MSALigFastatoJson.py [fasta] [msa.a3m] [Ligand1.txt] [Ligand2.txt]
```
