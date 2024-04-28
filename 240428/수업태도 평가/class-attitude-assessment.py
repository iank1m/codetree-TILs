N = int(input())
mydict = {'Bessie': 0, 'Elsie': 0, 'Daisy': 0, 'Gertie': 0, 'Annabelle': 0, 'Maggie': 0, 'Henrietta': 0}

# N개만큼 학생의 이름과 추가 점수가 공백을 기준으로 부여됩니다.
for i in range(N):
    name, score = input().split(' ')
    mydict[name] += int(score)

# 가장 낮은 점수를 찾습니다.
lowest_score = min(mydict.values())

# 가장 낮은 점수를 받은 학생을 제외한 학생들 중 두 번째로 낮은 점수를 찾습니다.
second_lowest_score = min(score for score in mydict.values() if score != lowest_score)

# 두 번째로 낮은 점수를 받은 학생의 이름을 찾습니다.
second_lowest_students = [name for name, score in mydict.items() if score == second_lowest_score]

# 부가 조건 다루기
if len(second_lowest_students) > 1 or len(set(mydict.values())) == 1:
    print("Tie")
else:
    print(second_lowest_students[0])