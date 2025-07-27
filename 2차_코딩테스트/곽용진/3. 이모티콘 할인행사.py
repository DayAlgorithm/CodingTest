import itertools

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    # 모든 할인 조합 생성
    discount_combinations = list(itertools.product(discount_rates, repeat=len(emoticons)))
    
    result = []
    for discounts in discount_combinations:  # 할인율 조합마다
        plus_cnt = 0  # 이모티콘 PLUS 가입자 수
        total_sales = 0  # 매출 합계
        
        for user_discount, user_limit in users:
            user_total = 0
            for emo_price, applied_discount in zip(emoticons, discounts):
                if applied_discount >= user_discount:  # 최소 할인율 이상이면 구매
                    discounted_price = emo_price * (100 - applied_discount) // 100
                    user_total += discounted_price
            if user_total >= user_limit:
                plus_cnt += 1
            else:
                total_sales += user_total
                
        result.append([plus_cnt, total_sales])
    
    # 조건(가입자 우선, 매출액 내림차순)
    result.sort(key=lambda x: (-x[0], -x[1]))
    return result[0]
