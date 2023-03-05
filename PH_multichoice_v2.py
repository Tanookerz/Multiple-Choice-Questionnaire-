import time

print("This is a short test about Philippine History, this will test your knowledge on the subject. Good luck!")
score = 0
time.sleep(1.0)
print("Type the letter of the correct answer.")

x = input("Who is the Philippines' national hero? A. Andres Bonifacio B. Jose Rizal C. Emilio Aguinaldo ")
if x == "A" or x == "a":
    print('Wrong! Andres Bonifacio is not the National Hero of the Philippines.')
elif x == "B" or x == "b":
    print("Correct! Jose Rizal is the National Hero of the Philippines.")
    score = score + 1
elif x == "C" or x == "c":
    print("Wrong! Emilio Aguinaldo is the not the National Hero of the Philippines.")
time.sleep(1.0)

y= input("How many years did the Spanish Empire colonized the Philippines? A. 333 years B. 48 years C. 150 years ")
if y == "A" or y== "a":
    print("Correct! The Spanish Empire occupied and colonized the Philippines for 333 years.")
    score= score + 1
elif y == "B" or y == "b":
    print("Wrong! The Spanish Empire didn't colonized the Philippines for 48 years, it was the United States of America.")
elif y == "C" or y == "c":
    print("Wrong! The Spanish Empire didn't colonized the Philippines for 150 years.")
time.sleep(1.0)

z = input("What year was the start of the Philippine Revolution? A 1896 B. 1898 C. 1902 ")
if z == "A" or z == "a":
    print("Correct! The Philippine Revolution started in August, 23, 1896.")
    score = score + 1
elif z == "B" or z == "b":
    print("Wrong! The Philippine Revolution ended in June, 12, 1889.")
elif z == "C" or z == "c":
    print("Wrong! 1902 was the year the Philippine-American War ended.")
time.sleep(1.0)

xy = input("Who started the Philippine Revolution? A. Jacinto Zamora B. Andres Bonifacio C. Apolinario Mabini ")
if xy == "A" or xy == "a":
    print("Wrong! Jacinto Zamora was part of the GOMBURZA, a trio of priests falsely accused of mutiny by Spanish colonial authorities.")
elif xy == "B" or xy == "b":
    print("Correct! Andres Bonifacio was the person who started the Philippine Revolution with his secret society group, the Katipunan also known as the KKK (No relation to the white supremacist group).")
    score = score + 1
elif xy == "C" or xy == "c":
    print("Wrong! Apolinario Mabini was the first Prime Minister of the Philippines, he was a notable member of the Katipunan.")
time.sleep(1.0)

xz = input("After the Philippine Revolution, who became the first president of the Philippines? A. Andres Bonifacio B. Emilio Aguinaldo C. Mariano Trias ")
if xz == "A" or xz == "a":
    print("Wrong! Andres Bonifacio wasn't the first president of the Philippines, he was only a candidate.")
elif xz == "B" or xz == "b":
    print("Correct! Emilio Aguinaldo won the election during the Tejeros Convention, it is considered to be the first presidential and vice presidential elections in the Philippines.")
    score = score + 1
elif xz == "C" or xz == "c":
    print("Wrong! Mariano Trias wasn't the first president of the Philippines, he was only a candidate.")
time.sleep(1.0)

print("Your score is", score)
time.sleep(1.0)

if score > 4:
    print("Great Job! You got all the correct answers in the test! Congratulations!")
if score < 1:
    print("Failure! You got all the wrong answers in the test. Study up and try again next time!")
time.sleep(1.0)
print("Thank you for taking this short test. This is made by Tanookerz.")