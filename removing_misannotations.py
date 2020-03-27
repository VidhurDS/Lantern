# read the misannotations into a dict
with open("remove_onts.txt", "r") as ins:
    ont_file = ins.readlines()
ins.close()

ont_dict = {}
onts = []
ont_ids = []
for line in ont_file:
    line = line.strip()
    ele = line.split("\t")
    ont_dict[ele[0]] = ele[1]
    ont_ids.append(ele[0].upper())
    temp = ele[1].split(",")
    onts = onts + temp

onts = list(set(onts))
onts = [x.lower() for x in onts]
ont_ids = list(set(ont_ids))

# parse through each ontology file and remove the misannotations

list_onts = ["GO", "HP", "DOID", "SNOMEDCT"]
ofn2 = "all_annotations_v3.txt"
outfile2 = open(ofn2, 'w')
al_ano = []

for o in list_onts:
    file_name = "uid_" + o + "_frequency_table.txt"
    with open(file_name, "r") as ins:
        pmid_anno = ins.readlines()
    ins.close()

    # write to v3 of the same files
    ofn = "uid_" + o + "_frequency_table_v3.txt"
    outfile = open(ofn, 'w')

    for line in pmid_anno:
        line = line.strip()
        e = line.split("\t")
        if e[2].upper() not in ont_ids:
            outfile.write(line + "\n")
            al_ano.append(e[2] + "\t" + e[3])

al_ano = list(set(al_ano))
for li in al_ano:
    outfile2.write(li + "\n")