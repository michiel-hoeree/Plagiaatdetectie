

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    newMonths = list(map(lambda month: f"{month[0]+1}: {month[1][0:3].upper()}", enumerate(months)))        #eerste oplossing met lambda
    print(newMonths)


    secondNewMonths = [f"{month[0]+1}: {month[1][0:3].upper()}" for month in enumerate(months)]             # tweede oplossig met for.
    print(secondNewMonths)




if __name__ == "__main__":
    main()