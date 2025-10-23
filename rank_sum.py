score_list = [100, 20, 30, 70, 70]
for score in score_list:
    rank_count = sum(1 for s in score_list if s > score)
    print(f"点数: {score}, 順位: {rank_count + 1}")