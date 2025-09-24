def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    pre_pre_cnt = 0
    pre_cnt = 1

    for i in range(stair_amount):
        now_cnt = pre_pre_cnt + pre_cnt
        pre_pre_cnt = pre_cnt
        pre_cnt = now_cnt
    
    return now_cnt
