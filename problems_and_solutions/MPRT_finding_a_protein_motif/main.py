'''
Problem

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id

Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta

For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
Sample Dataset

A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output

B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
'''

import re
from Bio import UniProt
from time import sleep

FILEPATH = r"MPRT_finding_a_protein_motif\data.txt"

def find_n_glycosilation(sequence):
    motif = re.compile(r"(?=(N[P][ST][^P]))")
    return [str(m.start() + 1) for m in motif.finditer(sequence)]

def fetch_sequence(id, delay=2, attempts=5):
    sleep(delay)
    for _ in range(1, attempts + 1):
        query = f"(accession:{id.replace("_", " ")})"
        try:
            result = UniProt.search(query, fields=["sequence"])
            return next(result)["sequence"]["value"]
        except:
            sleep(delay)
    
def main():
    with open(FILEPATH) as file:
        ids = file.read().strip().splitlines()

    for id in ids:
        sequence = fetch_sequence(id)
        if not sequence:
            continue

        positions = find_n_glycosilation(sequence)
        if positions:
            print(f"{id}\n{" ".join(positions)}")

if __name__ == "__main__":
    main()