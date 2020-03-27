# ont = "GO"
# ont = "HP"
# ont = "DOID"
# ont = "NCIT" # no files
ont = "SNOMEDCT"

path = "E:/Academic_SoIC/SCJ/Lantern/Full_run/Step_4_annotation_extraction/all_annotation_files/" + ont + "_annotations/"
hash_anno = {}
hash_ids = {}
ofn = ont + "_all_annotaions.txt"
outfile = open(ofn, 'w')

for num in range(1,71):
    file_name = path + ont + "_annotaion_" + str(num) + ".txt"
    with open(file_name, "r") as ins:           #add if file exists
        fullfile = ins.readlines()[1:]
    ins.close()
    if len(fullfile) > 0:
        print "parsing " + ont + str(num) + " file"
        for line in fullfile:
            line = line.strip()
            elements = line.split("\t")
            pmid = elements[0]
            anno = elements[6]
            ids = elements[7]
            if pmid in hash_anno and pmid in hash_ids:
                hash_anno[pmid] = hash_anno[pmid] + ", " + anno
                hash_ids[pmid] = hash_ids[pmid] + ", " + ids
            else:
                hash_anno[pmid] = anno
                hash_ids[pmid] = ids


outfile.write("PMID\tAnnotations\tOntology_IDs\n")
for pm in hash_anno:
    oline = pm + "\t" + hash_anno[pm] + "\t" + hash_ids[pm] + "\n"
    outfile.write(oline)

