import sys
import json
import re
import Bio
from Bio import SeqIO

#validating input
if len(sys.argv) != 2:
    print("Usage: python3 FastatoJson.py [fasta]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]


JDict = {} #Higher level dictionary


#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle: 
    JDict = {} #Higher level dictionary
    for record in SeqIO.parse(handle, "fasta"):
        fast=str(record.seq)
        ID=record.id

        obj = [{"protein": {"id": ["A"],
                "sequence": fast
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
            json.dump(JDict, outfile)

