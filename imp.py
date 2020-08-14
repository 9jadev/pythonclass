import day2s as dy
import datetime

x = datetime.datetime.now()
print(x)

scoretally = [ {'name' : 'abdullah', 'score': 71 }, {'name' : 'solomon', 'score': 81 }, {'name' : 'jibri', 'score': 99 }]
# score[initial]
scoretally1 = [ {'name' : 'abdullah', 'score': 81 }, {'name' : 'solomon', 'score': 88 }, {'name' : 'jibri', 'score': 76 }]

scoretally2 = [ {'name' : 'abdullah', 'score': 91 }, {'name' : 'solomon', 'score': 89 }, {'name' : 'jibri', 'score': 88 }]


dy.grader(scoretally, "Biology")
dy.grader(scoretally1, "physic")
dy.grader(scoretally2, "Engineering maths")

dy.animal("dog")
print(dy.name)