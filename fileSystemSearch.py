from pathlib import Path


def main():
    cd = input("Welke directory moet ik doorzoeken?\n> ")
    p = Path(f"{cd}")
    if p.exists():
        print("Dit is een directory. Hij bevat volgende Python files.")
        pythonFiles = list(p.glob('*.py'))
        for file in pythonFiles:
            print(file)
    else:
        print("Dit is geen directory.")

if __name__ == "__main__":
    main()


    