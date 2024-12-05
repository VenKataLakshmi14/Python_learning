if __name__ == '__main__':
    n = int(input())  
    scores = list(map(int, input().split()))  
    max_score = max(scores)
    scores = [score for score in scores if score != max_score]
    runner_up = max(scores)
    print(runner_up)
