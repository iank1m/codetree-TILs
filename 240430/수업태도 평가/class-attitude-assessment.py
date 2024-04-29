def find_second_lowest(scores):
    # 점수를 기준으로 정렬하여 두 번째로 낮은 점수를 찾습니다.
    sorted_scores = sorted(scores.values())
    second_lowest_score = sorted_scores[1]

    # 두 번째로 낮은 점수를 가진 학생들을 찾습니다.
    second_lowest_students = [student for student, score in scores.items() if score == second_lowest_score]

    return second_lowest_students


if __name__ == "__main__":
    students = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
    scores = {student: 0 for student in students}

    N = int(input().strip())
    for _ in range(N):
        student, score = input().strip().split()
        scores[student] += int(score)

    # 두 번째로 낮은 점수를 가진 학생들을 찾습니다.
    second_lowest_students = find_second_lowest(scores)

    # 결과 출력
    if len(second_lowest_students) == 1:
        print(second_lowest_students[0])
    elif len(second_lowest_students) > 1:
        print("Tie")
    else:
        print("No students found.")