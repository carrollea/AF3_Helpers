import sys
import json
import re
import Bio
from Bio import SeqIO

#validating input
if len(sys.argv) != 4:
    print("Usage: python3 MSALigFastatoJson.py [fasta] [msa.a3m] [Ligand.txt]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]
fa2 = sys.argv[2]
fa3 = sys.argv[3]

lig=open(fa3,'r')
ligrd=lig.read()

# We need to split the a3m file into one a3m file per msa, for large files we don't want to load the whole thing into the m#    with merged_msa.open("r") as f:
msa_dict = {}
with open(fa2, 'r') as f:
    line = f.readlines()
    msa=""
    for i in range(len(line)):
        if i == 0:
            id=line[i].replace('\0', '').replace(">", "").replace("\n", "")
            msa += line[i].replace('\0', '')
        elif ('\0') in line[i]:
            msa_dict[id]=msa
            id=""
            id=line[i].replace('\0', '').replace(">", "").replace("\n", "")
            msa=""
            msa += line[i].replace('\0', '')
        else:
            msa += line[i].replace('\0', '')

with open('msaout.txt', 'w') as outfile:
    outfile.write(str(msa_dict))

#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle:
    JDict = {} #Higher level dictionary
    for record in SeqIO.parse(handle, "fasta"):
        fast=str(record.seq)
        ID=record.id
        msardrp =  msa_dict.get(ID)
        obj = [{"protein": {"id": ["A"],
                "sequence": fast,
                "unpairedMsa": msardrp,
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

