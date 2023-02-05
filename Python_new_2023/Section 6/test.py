#file = open("files/essay.txt", 'r')
#content = file.read()
#print(content.title())

#file = open("files\essay.txt", 'r')
#content = file.read()
#print(len(content))

#add = input("Add a new member: ")

#file = open("files/members.txt", 'r')
#content = file.readlines()
#file.close()

#content.append(add + "\n")

#file = open("files/members.txt", 'w')
#content = file.writelines(content)
#file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

#for filename in filenames:
#    file = open(filename, 'w')
#    file.write("Hello")
#    file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f'files/{filename}', 'r')
    content = file.read()
    file.close()
    print(content)