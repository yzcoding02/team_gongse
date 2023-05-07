for i in range(1,6):
    fruits={"orange":"50","banana":"100","apple":"200"}
    fruit=input("this is fruit store. What do you want?:")
    if fruit in fruits:
        print(f"we have {fruit}.{fruits[fruit]} left.")
    else:
        print(f"sorry, we don't have {fruit}")