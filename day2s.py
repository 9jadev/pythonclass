scoretally = [ {'name' : 'abdullah', 'score': 71 }, {'name' : 'solomon', 'score': 81 }, {'name' : 'jibri', 'score': 99 }]
# score[initial]
scoretally1 = [ {'name' : 'abdullah', 'score': 81 }, {'name' : 'solomon', 'score': 88 }, {'name' : 'jibri', 'score': 76 }]

scoretally2 = [ {'name' : 'abdullah', 'score': 91 }, {'name' : 'solomon', 'score': 89 }, {'name' : 'jibri', 'score': 88 }]


def grader(score, subject):

    counts = len(score)
    initial = 0
    print('\n')
    print(subject)
    while initial < counts:
        print(score[initial]["name"])
        if score[initial]['score'] >= 50 and score[initial]['score'] <= 60:
            print(" You barly escaped " + " " + str(score[initial]['score']))
        elif score[initial]['score'] >= 60  and score[initial]['score'] <= 70 :
            print("congrats you passed with a C" + " " +  str(score[initial]['score']))
        elif score[initial]['score'] >= 70  and score[initial]['score'] <= 80 :
            print("congrats you passed with a B" +  " " + str(score[initial]['score'])) 
        elif score[initial]['score'] >= 80  and score[initial]['score'] <= 100:
            print("congrats you passed with a A" +  " " + str(score[initial]['score']) )       
        else:
            print("You failed try harder next term" + str(score[initial]['score']))

        initial += 1   

# grader(score, subject)
grader(scoretally, "Biology")
grader(scoretally1, "physic")
grader(scoretally2, "Engineering maths")