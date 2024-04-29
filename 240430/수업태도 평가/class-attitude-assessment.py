N = int(input())

# 딕셔너리를 초기화합니다.
mydict = {'Bessie': 0, 'Elsie': 0, 'Daisy': 0, 'Gertie': 0, 'Annabelle': 0, 'Maggie': 0, 'Henrietta': 0}

# 입력값을 받아 딕셔너리에 저장합니다.
for _ in range(N):
    name, score = input().split()
    mydict[name] += int(score)

# 점수를 오름차순으로 정렬합니다.
sorted_scores = sorted(set(mydict.values()))

# 가장 낮은 점수를 찾습니다.
lowest_score = sorted_scores[0]

# 가장 낮은 점수를 받은 학생을 제외한 학생들 중 두 번째로 낮은 점수를 찾습니다.
second_lowest_score = min(score for score in sorted_scores if score != lowest_score)

# 두 번째로 낮은 점수를 받은 학생의 이름을 찾습니다.
second_lowest_students = [name for name, score in mydict.items() if score == second_lowest_score]

# 부가 조건을 처리합니다.
if len(second_lowest_students) > 1 or len(set(mydict.values())) == 1 or N == 1:
    print("Tie" if len(second_lowest_students) > 1 or len(set(mydict.values())) == 1 else second_lowest_students[0])
else:
    print(second_lowest_students[0])