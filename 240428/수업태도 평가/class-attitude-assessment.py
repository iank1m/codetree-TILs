N = int(input())
#자료구조는 딕셔너리가 적당해 보임
mydict = {'Bessie':0, 'Elsie':0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}
#7명 모두 value를 0으로 초기화해놓고 시작

#N개만큼 학생의 이름과 추가점수가 공백을 기준으로 부여될 거니까
name = ''
score = 0

for i in range(N):
    name, score = input().split(' ')
    mydict[name] += int(score)

#이제 두번째로 낮은 점수 갖는 사람 출력하기 위해서 일단 정렬해놔
sorted_scores = sorted(mydict.values())
target = sorted_scores[1]
#배열마냥 숫자로 인덱싱이 안돼서 value를 정렬해놓고 거기서 대응되는 key를 따로 찾아내서 출력해야할듯
target =  [name for name, score in mydict.items() if score == target]

#부가조건 다루기

if len(target) > 1:
    print("Tie")
else:
    print(target[0])