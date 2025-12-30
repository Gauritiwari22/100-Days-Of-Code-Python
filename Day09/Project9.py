print("Welcome to the Secret Auction Program!")


print('''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

print("\n"*2)

biddings={}
condition=True
while condition:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    others=input("Are there any other bidders? Type yes/no ").lower()
    
    if others=="no":
        condition=False
    biddings[name]=bid

max_bid=max(biddings, key=biddings.get)


print(f"The winner is {max_bid} with a bid of {biddings[max_bid]}.")


    

