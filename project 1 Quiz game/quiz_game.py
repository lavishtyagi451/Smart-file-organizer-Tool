print('welcome to this computer quiz')

#asking user does he want to play or not
playing = input('Do You Want To Play? ').lower()

if playing != 'yes':
    quit()

print('lets start the quiz')

score = 0

#1st question
answer = input('1. Which of the following best describes a Minimum Viable Product (MVP)?\n'
"\nA- A fully polished product with all features"
"\nB- A prototype built without customer feedback"
"\nC- A product launched only after securing investors"
"\nD- A basic version of a product used to test assumptions  "
).lower()
if answer == 'd':
    print('correct!')

    score +=1
else:
    print('Incorrect')



    # 2nd question
answer = input('2. What is the primary goal of market validation?\n'
               
"\nA- To create a detailed business plan"
"\nB- To secure funding from investors"
"\nC- To finalize branding and design"
"\nD- To confirm that customers actually want the product  ").lower()
if answer == 'd':
    print('correct!')

    score +=1

else:
    print('Incorrect')


    # 3rd question
answer = input('3. Which trait is most strongly associated with successful entrepreneurs?\n'
               
"\nA- Taking calculated risks"
"\nB- Avoiding all risks"
"\nC- Focusing only on short-term gains"
"\nD- Waiting for perfect timing  "

).lower()
if answer == 'a':
    print('correct!')

    score +=1
else:
    print('Incorrect')


# 4th question
answer = input('4. What does “scalability” mean in a business context?\n'
               
"\nA- A business that avoids automation"
"\nB- A business model that can grow revenue faster than costs"
"\nC- A business that focuses only on local markets"
"\nD- A business that grows only with more employees  "
).lower()
if answer == 'b':
    print('correct!')
    score += 1
else:
    print('Incorrect')


    # 5th question
answer = input('5. Why is networking crucial for entrepreneurs?\n'
               
"\nA- It helps build relationships, opportunities, and resources"
"\nB- It guarantees immediate sales"
"\nC- It eliminates competition"
"\nD- It replaces the need for marketing  "
).lower()
if answer == 'a':
    print('correct!')
    score += 1
else:
    print('Incorrect')

#Result of quiz
print( "You Got " + str(score)+ " answers correct")
print( "You Got " + str((score/5)*100)+ "%.  answers correct")


