# dictionary can be expanded as required
print("Welcome to my personal dictionary.")

d1 = {"considered":"deem to be", "minute":"infinitely or immeasurably small", "accord":"concurrence of opinion",
        "autosomal":"occurring on or transmitted by a chromosome other than one of the sex chromosomes", "TBH":"To Be Honest", "because":"by reason of",
        "FTW":"for the win"}

print(d1.keys())

a = input("Enter any of the words above to know its meaning : \n")

print(f"The meaning of above word is : {[d1[a]]}")