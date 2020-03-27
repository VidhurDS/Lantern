from Bio import Entrez, Medline
import re
import xml.etree.ElementTree

with open("gc_unique_PMID_list.txt", "r") as ins:
    fullfile = ins.readlines()
ins.close()
c = 0
out_path = "/N/dc2/projects/CancerFight/Vidhur/Full_run/Step_3_abstract_extraction/abstracts/abstracts_"
dir_num = 1
outfile2 = open("no_abs.txt", 'w')

for singleid in fullfile:
    singleid = singleid.strip()
    Entrez.email = "swapdaul@iupui.edu"
    handle = Entrez.efetch(db="pubmed", id=singleid, retmode="XML")
    record = Entrez.read(handle)
    record = str(record)
    handle.close()
    abstract = re.search('AbstractText(.*?)\\]\\}\\}', record)
    if abstract:
        abstract = format(abstract.group())
        c += 1
        head = out_path + str(dir_num) + "/" + str(singleid) + "_abstract.txt"
        thefile = open(head, 'w')
        thefile.write(abstract)
        if c == 100:
            dir_num += 1
            c = 0
    else:
        outfile2.write(str(singleid) + "\n")

