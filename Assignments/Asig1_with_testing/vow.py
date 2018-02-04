def vowels(str):
        newstr = str
        vow = ('a','e','i','o','u')
        for x in str.lower():
                if x in vow:
                        newstr = newstr.replace(x,"")
        return newstr

if __name__ == '__main__':
    pass
