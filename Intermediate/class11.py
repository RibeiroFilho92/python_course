path = "C:\\Users\\Ribeiro\\Documents\\aula11.txt"

archive = open(path, "w")
archive.write("First line\n")
archive.write("Second line")

archive = open(path, "r")
print(archive.read())

archive.close()