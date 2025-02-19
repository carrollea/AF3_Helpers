import sys
import argparse
import json
import re
import Bio
from Bio import SeqIO

#Setting up inputs
parser = argparse.ArgumentParser()

#-f FASTA -m MSA -l ligand
parser.add_argument("-f", "--fasta",  help="Fasta file")
parser.add_argument("-m", "--msa",  help="MSA file .a3m")
parser.add_argument("-l", "--ligand", help="Ligand file")


args = parser.parse_args()

#Assigning inputs as objects 
fa1 = args.fasta
fa2 = args.msa
fa3 = args.ligand

if args.ligand is not None:
    lig=open(fa3,'r')
    ligrd=lig.readlines()
    alllig = list()
    for i in ligrd:
        name = i.split('\t')
        smile = name[1].replace("\n", "")
        smile = smile.replace("\\", "\\")
        ligadd= {"ligand": {"id": name[0],
                "smiles": smile}}
        alllig.append(ligadd)

    # We need to split the a3m file into one a3m file per msa, for large files we don't want to load the whole thing into the m#    with merged_msa.open("r") as f:
msa_dict = {}
if args.msa is not None:
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


#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle:
    JDict = {} #Higher level dictionary
    for record in SeqIO.parse(handle, "fasta"):
        fast=str(record.seq)
        fastns=fast.replace("*", "")
        ID=record.id
        if args.msa is None:
            msardrp =  ""
        else:
            msardrp = msa_dict.get(ID)
        if args.ligand is None:
            obj = [{"protein": {"id": ["A"],
                    "sequence": fastns,
                    "unpairedMsa": msardrp,
                    "pairedMsa": "",
                    "templates": []
                    }
                    }]
        else:
            obj = [{"protein": {"id": ["A"],
                    "sequence": fast,
                    "unpairedMsa": msardrp,
                    "pairedMsa": "",
                    "templates": []
                    }
                    },
                    *alllig] #the star prints the list without list brackets
        JDict['name'] = ID
        JDict['sequences'] = obj
        JDict["modelSeeds"] =  [1]
        JDict['dialect'] = "alphafold3"
        JDict['version'] = 1

#Now will output a fasta file from the ID_fasta sequecnes.
        with open(f'{ID}.json', 'w') as outfile:
            json.dump(JDict, outfile, indent=4)

