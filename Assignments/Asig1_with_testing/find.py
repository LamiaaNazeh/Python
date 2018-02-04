def find(str , ch):
        result = []
        for i,char in enumerate(str):
            if char == ch:
                result.append(i)
        return result

if __name__ == '__main__':
    pass
