import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


rcParams['font.family'] = 'Malgun Gothic'

# 데이터 불러오기
trend_data = pd.read_csv(r'C:\Users\ehdnj\OneDrive\바탕 화면\pinkfong-analysis\trend_over_time.csv.csv', skiprows=2)
region_data = pd.read_csv(r'C:\Users\ehdnj\OneDrive\바탕 화면\pinkfong-analysis\regional_trends.csv.csv', skiprows=1)

# 2. 데이터 확인 (상위 5개 데이터 출력)
print(trend_data.head())
print(region_data.head())

# 3. 데이터 전처리

trend_data.columns = ['날짜', '아기상어', '핑크퐁', '베베핀']
trend_data['날짜'] = pd.to_datetime(trend_data['날짜'])  # 날짜 형식 변환

region_data.columns = ['지역', '아기상어', '핑크퐁', '베베핀']

# 4. 시간 흐름에 따른 검색량 시각화
plt.figure(figsize=(12, 6))
plt.plot(trend_data['날짜'], trend_data['아기상어'], label='아기상어', color='yellow')  # 아기상어 노란색
plt.plot(trend_data['날짜'], trend_data['핑크퐁'], label='핑크퐁', color='pink')  # 핑크퐁 핑크색
plt.plot(trend_data['날짜'], trend_data['베베핀'], label='베베핀', color='blue')  # 베베핀 파란색
plt.title('시간 흐름에 따른 검색 트렌드')
plt.xlabel('날짜')
plt.ylabel('검색량')
plt.legend()
plt.grid(True)
plt.show()

# 5. 키워드별 평균 검색량 비교
avg_trends = trend_data.mean(numeric_only=True)
avg_trends.plot(kind='bar', color=['yellow', 'pink', 'blue'])
plt.title('키워드별 평균 검색량')
plt.ylabel('평균 검색량')
plt.show()

# 6. 특정 키워드의 급상승 시점 분석 (아기상어)
trend_data['아기상어_증가율'] = trend_data['아기상어'].pct_change() * 100
high_increase = trend_data[trend_data['아기상어_증가율'] > 30]
print("아기상어 검색량 급상승 시점:")
print(high_increase[['날짜', '아기상어', '아기상어_증가율']])

# 7. 저장 (분석 결과 엑셀로 저장)
trend_data.to_excel(r'C:\Users\ehdnj\OneDrive\바탕 화면\pinkfong-analysis\trend_analysis_results.xlsx', index=False)
