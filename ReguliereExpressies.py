import re

def main():
    find = r"\ba\w*\b"
    string = "apple, banana, avocado, cherry, apricot"
    print(f"1. {re.findall(find,string, flags=re.IGNORECASE)}")



    string = "Er zijn 12 maanden in een jaar, 24 uur in een dag."
    find = r'\d'
    print(f"2. {re.findall(find,string, flags=re.IGNORECASE)}")



    string = "I am walking while singing and eating."
    find = r'\b\w+ing\b'
    print(f"3. {re.findall(find,string, flags=re.IGNORECASE)}")



    string = "Alice wonders everywhere under the sky."
    find = r'\b[aeiou]\w*\b'
    print(f"4. {re.findall(find,string, flags=re.IGNORECASE)}")



    string = "Mijn email is voorbeeld@voorbeeld.com en info@test.be."
    find = r'\b\w+@[\w.]*\b'
    print(f"4. {re.findall(find,string, flags=re.IGNORECASE)}")







if __name__ == "__main__":
    main()