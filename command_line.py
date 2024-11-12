import sys
def main():
    total_sum = 0
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        try:
            total_sum += float(arg)
        except ValueError:
            pass
        i += 1
    print(total_sum)

if __name__ == "__main__":
    main()


