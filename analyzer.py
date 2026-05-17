#WORKING WITH PANDAS (WE ALREADY INSTALLED IT)
import pandas as pd



def load_data(filename):
    df = pd.read_csv(filename)
    return df


def show_info(df):
    print( df.shape)
    print( df.columns)
    print(df.describe())


while True:
    filename = input("Enter your filename: ")
    try:
        df = load_data(filename)
        print(df)
        show_info(df)

    except FileNotFoundError:
        print("File not found")
        continue

    column = input("Enter what column you wanna filter or 'q' to quit:  ").upper()
    if column == "q":
        break
    else:
        value = input("Enter what value you wanna filter by: ")
        try:
            print(df[df[column] == value])
        except:
            print("IDK what happened")

    filtered = df[df[column] == value]
    Saving = input("Do you want to save the filtered result 'y' or 'N':  ").upper()
    if Saving == "Y":
        filtered.to_csv("filtered_results.csv", index = False)
        print("Saved")


