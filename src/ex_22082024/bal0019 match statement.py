# match statement
# Switch in java
# match the op and execute
# python >3.10 working

# match variable :
#   case pattern1 :
#        #code block
#   case pattern2 :
#       #code block

# write a program to ask user which browser he want to run automaticly
browser_type = input("Enter the name of browser\n")
browser_type = browser_type.lower()

match browser_type:
    case "chrome":
        print("Execute the browser chrome")
    case "google":
        print("Execute the browser google")
    case "firefox":
        print("Execute the browser firefox")
    case "safari":
        print("Execute the browser safari")
    case _:
        print("Browser not found")
