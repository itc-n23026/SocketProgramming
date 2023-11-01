def gts(sport):
    ts = {
        'baseball': 9,
        'soccer': 11,
        'rugby': 15,
        'basketball': 5,
        'volleyball': 6
    }
    return ts.get(sport, "Invalid sport name")

if __name__ == '__main__':
    sport = input().strip()
    print(gts(sport))
