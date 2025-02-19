# AF3_Helpers
Some helpful scripts for prepping files for alphafold3

Convert a fasta file into a json file. 
The following python code converts a fasta file into a json file that can be used in Alphafold3
Use AF3_json_Prep.py 

```
python3 AF3_json_Prep.py -f [fasta] -m [msa.a3m] -l [Ligand.txt]
```

### Inputs 

#### -f fasta file 
This can be a fasta file containing one or more protein files. If more than one protein is in the fasta file then a json file will be made for each protein. 

#### -m msa.a3m 
If you want to provide a msa for your protein then you can pass the -m flag with the msa in .a3m format. If your fasta file has multiple proteins then your msa can have multiple msa for each protein. If the ID is the same in both the fasta and msa file then a json file for each protein along with the corresponding msa will be made. 

#### -l ligand.txt 
The ligands can be provided in a txt file containing an ID ligand in smiles format. IDs should be uppercase.

```
B  CC(=O)[C@H]3CCC4C2CC=C1C[C@@H](O)CC[C@]1(C)C2CC[C@]34C
```

If you want multiple ligands in the json file then each line should contain a new ID and smile. 

```
B  CC(=O)[C@H]3CCC4C2CC=C1C[C@@H](O)CC[C@]1(C)C2CC[C@]34C
C  'CC(=O)[C@H]3CC[C@]4(O)C2CC=C1C[C@@H](O)CC[C@]1(C)C2CC[C@]34C
```
