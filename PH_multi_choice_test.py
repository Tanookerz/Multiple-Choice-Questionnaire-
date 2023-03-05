print("Type the number of the correct answer...")
x = int(input("Q1. Who is the Philippines' national hero? 10. Andres Bonifacio 20. Jose Rizal "))
score = 0
if x > 15:
    print("Correct! Jose Rizal is the National Hero of the Philippines.")
    score= score + 1
else:
    print("Wrong! Andres Bonifacio is not the National Hero of the Philippines.")
y = int(input("Q2. How many years did the Spanish Empire colonized the Philippines? 10. 333 years 20. 48 years "))
if x < 15:
    print("Wrong! It was the USA who occupied the Philippines for 48 years, not the Spanish Empire.")
else:
    print("Correct! The Spanish Empire occupied the Philippines for 333 years.")
    score = score + 1
z = int(input("Q3. What year was the start of the Philippine Revolution? 10. 1896 20. 1898 "))
if z < 15:
    print("Correct! The Philippine Revolution started in August, 23, 1896.")
    score = score + 1
else:
    print("Wrong! The Philippine Revolution ended in June, 12, 1898")
xa= int(input("Q4. Who started the Philippine Revolution? 10. Jacinto Zamora 20. Andres Bonifacio "))
if xa < 15:
    print ("Wrong! Jacinto Zamora did not start the Philippine Revolution.")
else:
    print ("Correct! Andres Bonifacio started the Philippine Revolution, with his anti-Spanish secret society the KKK (not to be confused with the white supremacist group), also known as the Katipunan. ")
    score = score + 1
yb = int(input("Q5. After the Philippine Revolution, who became the first president of the Philippines? 10. Andres Bonifacio 20. Emilio Aguinaldo "))
if yb < 15:
    print("Wrong! Andres Bonifacio wasn't the first president of the Philippines, but he was a candidate however.")
else:
    print("Correct! Emilio Aguinaldo won the election in the Tejeros Convention, Filipino historians consider this the first presidential and vice presidential election in Philippine history.")
    score = score + 1
print (score,"out of 5")
if score < 1:
    print("Failure, you got all the questions wrong. Study up and do better next time!")
elif score > 4:
    print("Perfect, You got all the questions answered correctly. Good job!")
print("Thank you for answering this short test!")