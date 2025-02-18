import sys
import json
import re
import Bio
from Bio import SeqIO

#validating input
if len(sys.argv) != :
    print("Usage: python3 MSALigFastatoJson.py [fasta] [Ligand.txt]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]

fa3 = sys.argv[2]

lig=open(fa3,'r')
ligrd=lig.read()


#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle:
    JDict = {} #Higher level dictionary
    for record in SeqIO.parse(handle, "fasta"):
        fast=str(record.seq)
        ID=record.id
        msardrp =  msa_dict.get(ID)
        obj = [{"protein": {"id": ["A"],
                "sequence": fast,
                "unpairedMsa": "",
                "pairedMsa": "",
                "templates": []
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

#file_name("{ID}.json")
#Now will output a fasta file from the ID_fasta sequecnes. 
        with open(f'{ID}.json', 'w') as outfile:
            json.dump(JDict, outfile, indent=4)

