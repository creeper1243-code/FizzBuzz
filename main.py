print("hiya m8 lets play a game! insert a random number. if it divides by 3. FIZZ! and if it divides by 5. BUZZ! if both. FIZZBUZZ!")


number = int(input("enter a number here m8 ---> "))

if number % 3 == 0 and number % 5 == 0:
    print("FIZZBUZZ!")
elif number % 3 == 0:
    print("FIZZ!")
elif number % 5 == 0:
    print("BUZZ!")