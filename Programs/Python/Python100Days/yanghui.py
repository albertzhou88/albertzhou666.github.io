
def main():
    n = int(input('How many rows? '))
    row = [1]
    print(row)
    if n > 1:
        row = [1, 1]
        for i in range(2, n+1):
            print(row)
            next_row = [1]
            for j in range(i-1):
                next_row.append(row[j]+row[j+1])
            next_row.append(1)
            row = next_row

if __name__ == '__main__':
    main()
