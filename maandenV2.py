

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    secondNewMonths = [f"{month[0]+1}: {month[1][0:3].upper()}" for month in enumerate(months) if len(month[1])<5]
    print(secondNewMonths)




if __name__ == "__main__":
    main()