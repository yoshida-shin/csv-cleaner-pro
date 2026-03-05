# CSV to Excel Converter

CSVファイルをExcelファイル（.xlsx）に変換するシンプルなPythonツールです。  
複数のCSVファイルをまとめて変換できます。

## Features

- CSV → Excel (.xlsx) 変換
- inputフォルダのCSVをまとめて処理
- outputフォルダにExcelを出力
- Python初心者でも使いやすいシンプル構成

## Directory Structure
project/  
├ input/  
│ └ sample.csv  
├ output/  
├ csv_cleaner.py  
├ requirements.txt  
└ README.md  

## Requirements

- Python 3.10+
- pandas
- openpyxl

## Usage

inputフォルダにCSVを入れて実行
```bash
python csv_cleaner.py
```

outputフォルダにExcelファイルが生成されます。  
input/sample.csv  
↓  
output/sample.xlsx  

## Example

CSV  
name,age  
Alice,25  
Bob,30  
  
Excel  
name | age  
Alice | 25  
Bob   | 30  
