N = int(input())
mydict = {'Bessie': 0, 'Elsie': 0, 'Daisy': 0, 'Gertie': 0, 'Annabelle': 0, 'Maggie': 0, 'Henrietta': 0}


for i in range(N):
    name, score = input().split(' ')
    mydict[name] += int(score)

lowest_score = min(mydict.values())

second_lowest_score = min(score for score in mydict.values() if score != lowest_score)

second_lowest_students = [name for name, score in mydict.items() if score == second_lowest_score]


if len(second_lowest_students) > 1:
    print(second_lowest_students[0])
elif len(set(mydict.values())) == 1:
    print("Tie")
else:
    print(second_lowest_students[0])