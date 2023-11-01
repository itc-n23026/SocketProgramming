def cm(v, d):
    return d // v

if __name__ == '__main__':
    v, d = map(int, input().strip().split())
    m = cm(v, d)
    print(m)
