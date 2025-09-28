def calculate_generalized_tax(income, limits, rates):
    """
    일반화된 누진세 계산 함수

    Args:
        income (int or float): 세금을 계산할 총소득
        limits (list): 과세표준 구간의 상한선 리스트
        rates (list): 각 구간별 세율 리스트

    Returns:
        float: 계산된 총 세금
    """
    if len(rates) != len(limits) + 1:
        return "오류: 세율(rates) 리스트의 길이는 구간(limits) 리스트의 길이보다 1 커야 합니다."

    total_tax = 0
    previous_limit = 0

    # 정의된 과세표준 구간을 순회하며 세금 계산
    for i in range(len(limits)):
        upper_limit = limits[i]
        rate = rates[i]

        if income > upper_limit:
            taxable_in_this_bracket = upper_limit - previous_limit
            total_tax += taxable_in_this_bracket * rate
            previous_limit = upper_limit
        else:
            taxable_in_this_bracket = income - previous_limit
            total_tax += taxable_in_this_bracket * rate
            return total_tax

    # 최고 소득 구간 계산
    last_rate = rates[-1]
    remaining_income = income - previous_limit
    total_tax += remaining_income * last_rate

    return total_tax


# --- 1. 데이터 정의: 과세표준 구간과 세율을 리스트로 관리 ---
TAX_BRACKET_LIMITS = [1500, 3000, 4500, 6000]
TAX_RATES = [0.06, 0.15, 0.24, 0.35, 0.38]  # 6%, 15%, 24%, 35%, 38%

# --- 2. 메인 실행 부분 ---
print("연봉을 입력하세요 ==> ")
annual_income = int(input())

# 일반화된 함수를 호출하여 세금 계산
total_tax_amount = calculate_generalized_tax(annual_income, TAX_BRACKET_LIMITS, TAX_RATES)

# 결과 출력
print("전체세금 = ", total_tax_amount)
print("순수소득 = ", annual_income - total_tax_amount)