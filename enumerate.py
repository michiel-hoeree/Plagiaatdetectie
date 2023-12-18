

def main():
    fruit = ["appel","peer","banaan","clementine"]
    numbered = list(enumerate(fruit))
    for fruit in numbered:
        print(f"{fruit[0]+1}: {fruit[1]}")


if __name__ == "__main__":
    main()