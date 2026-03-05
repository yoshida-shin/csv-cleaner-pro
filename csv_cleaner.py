import pandas as pd
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def log(message):
    print(message)
    
def load_csv(file_path):
    try:
        log(f"CSV読み込み: {file_path}")
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        log(f"読み込み失敗: {file_path}")
        log(e)
        return None
        
def clean_data(df):
    log("データ整形")
    
    # 列名変更（存在する場合のみ）
    rename_map = {
        "name": "商品",
        "price": "価格",
        "date": "日付"
    }
    df = df.rename(columns=rename_map)

    # 必要列だけ残す
    cols = [c for c in ["商品", "価格", "日付"] if c in df.columns]
    df = df[cols]
    
    # 重複削除
    df = df.drop_duplicates()
    
    # 並び替え    
    if "日付" in df.columns:
        df["日付"] = pd.to_datetime(df["日付"])
        df = df.sort_values("日付")
    
    return df

def save_excel(df, output_path):
    try:
        log(f"Excel保存: {output_path}")
        df.to_excel(output_path, index=False)
    except Exception as e:
        log("保存エラー")
        log(e)
        
def process_file(file_name):
    file_path = os.path.join(INPUT_DIR, file_name)
    
    df = load_csv(file_path)
    
    if df is None:
        log("スキップ\n")
        return
        
    df = clean_data(df)
    
    output_name = file_name.replace(".csv", ".xlsx")
    print(output_name)
    output_path = os.path.join(OUTPUT_DIR, output_name)
    print(output_path)
    save_excel(df, output_path)
    
    log("完了\n")
    
def main():
    log("CSV Cleaner Pro 開始\n")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    files = os.listdir(INPUT_DIR)
    
    for file in files:
        print(file)
        if file.endswith(".csv"):
            process_file(file)
            
    log("すべて完了")
        
if __name__ == "__main__":
    main()

