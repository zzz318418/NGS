# count_words.py

from collections import Counter

# 指定要讀取的文字檔路徑
filename = "C:/Users/zzz31/Document/py/StringTie_merge.txt"


target_word = "transcript"

# 開啟並讀取檔案內容
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# 全部轉小寫，避免大小寫影響
text_lower = text.lower()

# 計算目標詞出現次數（以空白區隔為詞）
count = text_lower.split().count(target_word)

# 顯示結果
print(f"transcript in txt: {count}")