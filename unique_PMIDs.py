thefile = open('gc_unique_PMID_list.txt', 'w')
filename = "gencode_lncRNA_PMID.txt"

with open(filename, "r") as ins:
    in_file = ins.readlines()
ins.close()
c = 0
pmid_list = []

for row in in_file:
    row = row.strip()
    col = row.split("\t")
    if ";" in col[1]:
        pmids = col[1].split(";")
        pmids[-1].strip("\n")
        pmid_list = pmid_list + pmids
    else:
        pmid_list.append(col[1])

uniq_list = list(set(pmid_list))

for each in uniq_list:
    each = each.strip("\n")
    x = each+"\n"
    thefile.write(x)

