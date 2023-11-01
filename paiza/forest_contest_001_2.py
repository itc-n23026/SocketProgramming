def cbt(hours):
    if hours <= 6:
        return "no break"
    return "45 min" if hours <= 8 else "60 min"

if __name__ == '__main__':
    h = int(input().strip())
    bt = cbt(h)
    print(bt)
