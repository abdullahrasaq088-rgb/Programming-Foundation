grade= input("Enter your grade:")
match grade:
    case "A" | "A+":
        print(4.0)
    case "B" | "B+":
        print(3.0)
    case "C" "C+":
        print(2.0)
    case "D" | "D+":
        print(1.0)
    case "F" | "F+":
        print(0.0)
    case default:
        print("you entered an invalid number")