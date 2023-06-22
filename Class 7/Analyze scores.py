def score_analysis():
    scores = input("Enter the scores separated by a space: ").split()

    
    scores = [float(score) for score in scores]

    total_scores = len(scores)
    sum_scores = sum(scores)
    average = sum_scores / total_scores

    above_average = 0
    below_average = 0

    for score in scores:
        if score >= average:
            above_average += 1
        else:
            below_average += 1

    
    print("Average is:", average)
    print("Number of scores above or equal to average:", above_average)
    print("Number of scores below average:", below_average)


score_analysis()
