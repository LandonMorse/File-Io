file_path = "Reviews.txt"
def zero():
    review = input("write here:")
    with open(file_path,"a") as file:
        file.write( review + "\n\n")
def make_review():
    print("Title")
    title = input("Please enter title of item for review:")
    with open(file_path,"a") as file:
        file.write("\n"+title+ "\n")
    print("Rating ")

    Rating = input("enter your reviwe from 1 throth 10 ")
    match Rating:
            case "0":
                with open(file_path, "a") as file:
                    file.write("0 star\n")
                zero()

            case "1":
                with open(file_path, "a") as file:
                    file.write("1 star\n")
                zero()

            case "2":
                with open(file_path, "a") as file:
                    file.write("2 star\n")
                zero()

            case "3":
                with open(file_path, "a") as file:
                    file.write("3 star\n")
                zero()

            case "4":
                with open(file_path, "a") as file:
                    file.write("4 star\n")
                zero()

            case "5":
                with open(file_path, "a") as file:
                    file.write("5 star\n")
                zero()

            case "6":
                with open(file_path, "a") as file:
                    file.write("6 star\n")
                zero()

            case "7":
                with open(file_path, "a") as file:
                    file.write("7 star\n")
                zero()

            case "8":
                with open(file_path, "a") as file:
                    file.write("8 star\n")
                zero()

            case "9":
                with open(file_path, "a") as file:
                    file.write("9 star\n")
                zero()

            case "10":
                with open(file_path, "a") as file:
                    file.write("10 star\n")
                zero()

            case _:
                print("in stars you got it isaac")
def Game():
    while True:
        print("lets make a review for your favorite games")
        print("1.) Make a review")
        print("2.) Read entry's ")
        print("9.) Exit")
        User_wants= input("what you going to do you busy bee:")
        match User_wants:
            case "1":
                make_review()
            case "2":
                with open(file_path, "r") as file3:
                    contents = file3.read()
                    print(contents)
                    Game()
            case "9":
                exit()
Game()