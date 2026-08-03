'''
Problem

The novel-motif finding tool MEME can be found here.

Given: A set of protein strings in FASTA format that share some motif with minimum length 20.

Return: Regular expression for the best-scoring motif.
Sample Dataset

>Rosalind_7142
PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQ
FYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFE
WGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNM
SYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY
>Rosalind_4494
VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERY
PIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADF
QRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFL
KTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM
>Rosalind_3636
ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCF
NKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMA
GNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMM
GHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN

Sample Output

DLWWCWIPVHK[NK]PHSFLKTWSPAAGHRGWQFDHNFF
'''

from Bio import SeqIO

FILEPATH = r"MEME_new_motif_discovery\data.txt"
MIN_LENGTH = 2
MIN_LENGTH_TOTAL = 20

def consensus(sequences):
    length = len(sequences[0])
    result = []
    for i in range(length):
        seen = []
        for seq in sequences:
            if seq[i] not in seen:
                seen.append(seq[i])
        if len(seen) != 1:
            result.append(seen[0])
        else:
            result.append("[" + "".join(seen) + "]")
    return " ".join(result)

def find_motif(sequences):
    candidates = []
    shortest_sequence = min([s for s in sequences], key=len)
    for l in range(len(shortest_sequence), MIN_LENGTH, -1):
        for i in range(len(shortest_sequence) - l + 1):
            substring = shortest_sequence[i:(l - i)]
            if all(substring in s for s in sequences) and not any(substring in c for c in candidates):
                candidates.append(substring)

    positions = {}
    for c in candidates:
        positions[c] = sequences[0].find(c)
    start = min(positions, key=positions.get)
    end = max(positions, key=positions.get) 

    motifs = []
    for s in sequences:
        motif = s[s.find(start):s.find(end)+len(end)]
        if len(motif) >= MIN_LENGTH_TOTAL:
            motifs.append(motif)

    return consensus(motifs)

def main():
    sequences = [r.seq for r in list(SeqIO.parse(FILEPATH, "fasta"))]
    
    best_motif = find_motif(sequences)

    print(best_motif)

if __name__ == "__main__":
    main()