import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv')

# 計算文章數量
total_articles = len(df)

# 計算每篇文章的字數
df['word_count'] = df['body'].str.split().str.len()

# 儲存含有字數的新 CSV 檔案
output_csv = 'output/trump_xi_meeting_fulltext_with_wordcount.csv'
df.to_csv(output_csv, index=False)

# 建立輸出目錄
import os
os.makedirs('output', exist_ok=True)

# 繪製字數分布圖
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='word_count', bins=30)
plt.title('Distribution of Article Word Counts')
plt.xlabel('Word Count')
plt.ylabel('Number of Articles')
plt.savefig('output/word_count_distribution.png')
plt.close()

# 繪製每月文章數量趨勢圖
df['published'] = pd.to_datetime(df['published'])
df['month'] = df['published'].dt.to_period('M')
monthly_counts = df.groupby('month').size()

plt.figure(figsize=(12, 6))
monthly_counts.plot(kind='bar')
plt.title('Number of Articles Published per Month')
plt.xlabel('Month')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/monthly_article_count.png')
plt.close()

# 生成統計報告
report = f"""# 基本統計報告

## 數據概覽
- 總文章數: {total_articles}
- 平均字數: {df['word_count'].mean():.2f}
- 最短文章字數: {df['word_count'].min()}
- 最長文章字數: {df['word_count'].max()}
- 字數中位數: {df['word_count'].median()}

## 視覺化圖表
1. 文章字數分布圖 (word_count_distribution.png)
2. 每月文章數量趨勢圖 (monthly_article_count.png)

## 資料處理說明
- 輸入檔案: trump_xi_meeting_fulltext_dedup-1657.csv
- 輸出檔案: trump_xi_meeting_fulltext_with_wordcount.csv (新增 word_count 欄位)
- 分析日期: {datetime.now().strftime('%Y-%m-%d')}
"""

# 儲存報告
with open('output/basic_stats_report.md', 'w', encoding='utf-8') as f:
    f.write(report)