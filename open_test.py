filepath = r'E:\Advanced programming\2.RPG'
file = open(filepath,mode = 'rb')
content = file.read()
print(content)
file.close()