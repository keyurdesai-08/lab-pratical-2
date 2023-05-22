name = input('What is your name? ')
print('Welcome ' + name + ', this expert system will help you distinguish between diseases with similar symptomps like Flu, Common Cold, Covid-19 and Pneumonia depending on severity of symptomps you are showing.')
PoorComunication=0
lessINFormation=0
noDegree=0
questions=["What is Employee age?",
           "What is Employee degree",
           ]
           
yesnoqs=['Are you fresher',
         'Do you have comunnication skill',
         'Are you experiencing sneezing?',
         'Do you have work expernce',
         ]
age, body_temp, oxy_level = (0, 0, 0)
print('Answer the following questions.')
qno = 1
for q in questions:
    print(q)
    if(qno == 1):
        age = int(input())
    elif(qno == 2):
        degree = float(input())
    qno+=1

print('Answer the following questions with Y/N.')
for i in range(len(yesnoqs)):
    print(yesnoqs[i])
    ans = input()
    if(i == 0 and (ans == 'Y' or ans == 'y')):
       PoorComunication+=1
       lessINFormation+=1
       noDegree+=1
    elif(i == 1 and (ans == 'Y' or ans == 'y')):
        PoorComunication+=1
        lessINFormation+=1
    elif(i == 2 and (ans == 'Y' or ans == 'y')):
        lessINFormation+=1
        noDegree+=1
    elif(i == 3 and (ans == 'Y' or ans == 'y')):
        PoorComunication+=1
    elif(i == 4 and (ans == 'Y' or ans == 'y')):
        lessINFormation+=1
    
if( PoorComunication == 0 and lessINFormation == 0 and noDegree== 0 ):
    print('Congratulations! selected')
else:
    max_index = 0
    max = -1
    dis = [PoorComunication, lessINFormation, noDegree]
    for i in range(4):
        if(dis[i] > max):
            max_index = i
            max = dis[i]
    disease = ''
    if(max_index == 0):
        disease = 'FPoorComunication'
    elif(max_index == 1):
        disease = 'lessINFormation'
    elif(max_index == 2):
        disease = 'noDegree'
    print('Based on the symptomps, you may have ' + selected+ '.')


