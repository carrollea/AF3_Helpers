import sys
import json
import re
import Bio
from Bio import SeqIO
#Note: biopython installed on our lab anaconda
#Can load by using the following in the command line before using the program
#module use -a /projects/academic/zhenw/programs/modulefiles/Allluas
#module load anaconda3
#validating input
if len(sys.argv) != 3:
    print("Usage: python3 FastatoJson.py [fasta] [Ligand.txt]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]
fa2 = sys.argv[2]

#JDict = {} #Higher level dictionary

lig=open(fa2,'r')
ligrd=lig.read()
#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle: 
    JDict = {} #Higher level dictionary
    for record in SeqIO.parse(handle, "fasta"):
        fast=str(record.seq)
        ID=record.id

        obj = [{"protein": {"id": ["A"],
                "sequence": fast
                }
                },
                {"ligand": {"id": "B",
                "smiles": ligrd
                }    # note that we used [] to create an array
         }]
        JDict['name'] = ID
        JDict['sequences'] = obj
        JDict["modelSeeds"] =  [1]
        JDict['dialect'] = "alphafold3"
        JDict['version'] = 1
#print(ligrd)

#file_name("{ID}.json")
#Now will output a fasta file from the ID_fasta sequecnes. 
        with open(f'{ID}.json', 'w') as outfile:
            json.dump(JDict, outfile)

