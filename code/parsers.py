
def parsePsiBlastOutput(output_PsiBlast):
    
    #Parse psi-blast output files 

    psiblast_domain_positions = {}
    with open(output_PsiBlast, 'r') as f:
        for line in f:
            if len(line)>1:
                qseqid, sseqid, pident, length, mismatch, gapopen, \
                qstart, qend, sstart, send, evalue, bitscore = line.strip().split()
                sseqid = sseqid.split('|')[1]
                if sseqid not in psiblast_domain_positions:
                    psiblast_domain_positions[sseqid] = [{'start':int(sstart), 'end':int(send)}]
                else:
                    #if position is not in the dict insert it
                    pos = {'start':int(sstart), 'end':int(send)}

                    if pos in psiblast_domain_positions[sseqid]:
                        continue
                    else:
                        psiblast_domain_positions[sseqid].append(pos)
            else:
                break
                
    print(f"{len(psiblast_domain_positions.keys())} hits parsed")
    return psiblast_domain_positions


def parseHmmerOutput(output_hmm):

    #Parse hmmserach output file 

    hmm_domain_positions = {}
    with open(output_hmm) as f:
        for line in f:
            if line[0] != "#" and line[0] != "-":
                target, tacc, tlen, query, qacc, qlen, \
                fevalue, fscore, fbias, _, _, dcevalue, dievalue, dscore, dbias, _, _ , \
                alifrom, alito, evfrom, envto, accuracy, desc = line.strip().split()[:23]
                tacc = target.split("|")[1]

                if tacc not in hmm_domain_positions:
                    hmm_domain_positions[tacc] = [{'start':int(alifrom), 'end':int(alito)}]
                else:
                    #if position is not in the dict insert it
                    pos = {'start':int(alifrom), 'end':int(alito)}
                    if pos in hmm_domain_positions[tacc]:
                        continue
                    else:
                        hmm_domain_positions[tacc].append(pos)
    print(f"{len(hmm_domain_positions.keys())} hits parsed")
    return hmm_domain_positions

"""
three2one = {
    'ala': 'A',
    'arg': 'R',
    'asn': 'N',
    'asp': 'D',
    'asx': 'B',
    'cys': 'C',
    'glu': 'E',
    'gln': 'Q',
    'glx': 'Z',
    'gly': 'G',
    'his': 'H',
    'ile': 'I',
    'leu': 'L',
    'lys': 'K',
    'met': 'M',
    'phe': 'F',
    'pro': 'P',
    'ser': 'S',
    'thr': 'T',
    'trp': 'W',
    'tyr': 'Y',
    'val': 'V'
}


def parsePDBseq(pdb_id):

    with open("../data/structure/pdb{}.ent".format(pdb_id), "r") as f:
        sequence = ""
        for line in f:
            if line.startswith("SEQRES"):
                aa_list = line.split(" ")
                aa_list = list(filter(lambda x: x != "", aa_list))[4:-1]
                sequence += "".join(aa_list)
                
    return sequence
    """