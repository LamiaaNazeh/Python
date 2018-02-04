#listname = ["lamiaa" , "fatma" , "marwa"]

#first solutiom
def dic(listname):
    names={}
    for i in range(len(listname)):
        names[listname[i][0]] = [listname[i]]
    print(names)


#another solution
def dic(names):
    names.sort()
    result = {}
    for name in names:
        if name[0] in result:
            result[name[0]].append(name)
        else:
            result[name[0]] = [name]
    return result
if __name__ == '__main__':
    pass
