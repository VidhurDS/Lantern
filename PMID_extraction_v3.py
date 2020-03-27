from Bio import Entrez

thefile = open('gencode_lncRNA_PMID_v3.txt', 'w')

with open("lncRNA_gencode.txt", "r") as ins:
    fullfile = ins.readlines()
ins.close()
c = 0

mainarray = []

for fn in fullfile:
    c += 1
    gn = fn.strip()
    # gn = "+ gn + "[GENE] lncrna"
    # gn = "((((" + gn + " lncRNA[Title / Abstract]) OR " + gn + " long non coding RNA[Title / Abstract]) OR " + gn + " non coding RNA[Title / Abstract]) OR " + gn + " RNA[Title / Abstract]) NOT " + gn + "[Author]"
    gn = "((((lncRNA " + gn + " [Title / Abstract]) OR long non coding RNA " + gn + " [Title / Abstract]) OR non coding RNA " + gn + " [Title / Abstract]) OR RNA " + gn + " [Title / Abstract]) NOT " + gn + "[Author]"
    # print gn
    handle = ''
    Entrez.email = "swapdaul@iupui.edu"     # Always tell NCBI who you are
    handle = Entrez.esearch(db="pubmed", term=gn, retmax=150, field="Title/Abstract", sort="pub+date")
    # print handle
    record = Entrez.read(handle)
    # print record
    a = ''
    b = ''
    a = fn.strip()
    b = ";".join(record["IdList"])
    # print c
    if b:
        inst = "\t".join([a, b])
        mainarray.append(inst)
        print inst

mainarray = set(mainarray)
for x in mainarray:
    thefile.write(x)
    thefile.write("\n")
