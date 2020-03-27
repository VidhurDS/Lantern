# ont = "GO"
# ont = "HP"
# ont = "DOID"
ont = "SNOMEDCT"
# ont = "NCIT"

file_name = "uid_" + ont + "_annotation_table.txt"

with open(file_name, "r") as ins:
    anno = ins.readlines()
ins.close()

ofn = "uid_" + ont + "_frequency_table.txt"
outfile = open(ofn, 'w')

# read file and generate 2 hashes: hash_go_anno hash_go_pmid
hash_go_pmid = {}
hash_go_anno = {}


def count(sequence, item):
    cont = 0
    for i in sequence:
        if item == i:
            cont += 1
    return cont


for each in anno:               # generating annotaions hash
    each = each.strip()
    ele = each.split("\t")
    ont_ids = []
    annos = []
    pm = ele[2]
    if "," in ele[4]:
        ont_ids = ele[4].split(",")
        annos = ele[3].split(",")       # stripping space
        annos = [x.strip(' ') for x in annos]
        ont_ids = [x.strip(' ') for x in ont_ids]
        for x in range(0, len(ont_ids)):
            ont_ids[x] = ont_ids[x].strip(" ")
            annos[x] = annos[x].strip(" ")
            com = pm + ont_ids[x]
            hash_go_pmid[com] = 1
            if ont_ids[x] in hash_go_anno:
                if hash_go_anno[ont_ids[x]] != annos[x]:
                    hash_go_anno[ont_ids[x]] = hash_go_anno[ont_ids[x]] + "," + annos[x]
            else:
                hash_go_anno[ont_ids[x]] = annos[x]
    else:
        ele[4] = ele[4].strip(" ")
        ele[3] = ele[3].strip(" ")
        com = pm + ele[4]
        hash_go_pmid[com] = 1
        if ele[4] in hash_go_anno:
            if hash_go_anno[ele[4]] != ele[3]:
                hash_go_anno[ele[4]] = hash_go_anno[ele[4]] + "," + ele[3]
        else:
            hash_go_anno[ele[4]] = ele[3]

for key in hash_go_anno:        # removing duplicates from annotations hash
    arr = []
    arr = hash_go_anno[key].split(",")
    arr = set(arr)
    hash_go_anno[key] = ",".join(arr)

uid = 1
block = []
freq = {}
num = 0

for line in anno:
    line = line.strip()
    cols = line.split("\t")
    if cols[1] == uid:
        block.append(line)
    else:
        go_arr = []
        pmid_arr = []
        for el in block:
            el = el.strip()
            ecol = el.split("\t")
            pmid_arr.append(ecol[2])        # getting pmids from block
            if "," in ecol[4]:              # getting go ids from block
                tem = ecol[4].split(",")
                go_arr.extend(tem)
            else:
                go_arr.append(ecol[4])
        go_arr = [x.strip(' ') for x in go_arr]         # removing space from beginging and ending of each element
        pmid_arr = set(pmid_arr)
        go = set(go_arr)

        for gud in go:
            gud = gud.strip(" ")
            freq = count(go_arr, gud)
            num += 1
            outfile.write(str(num) + "\t" + str(ecol[1]) + "\t" + gud + "\t" + hash_go_anno[gud] + "\t" + str(freq)+ "\t")
            for eaid in pmid_arr:
                kcom = eaid+gud
                if kcom in hash_go_pmid:
                    if hash_go_pmid[kcom] == 1:
                        outfile.write(eaid + ";")
            outfile.write("\n")
        block = []
        block.append(line)
        uid = cols[1]

