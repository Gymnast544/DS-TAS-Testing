endfile = "NSMBTAS.txt"

files = ["openingmenuforshellrng.txt", "SoigNSMB.txt", "HartmannNSMB.txt"]

f = open(endfile, "w")

for file in files:
    g = open(file, "r")
    read = g.read()
    read = read.strip() #remove the whitespace at the end
    f.write(read+"\n")
    g.close()

f.close()

print("Files concatenated")
