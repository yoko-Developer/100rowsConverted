# ファイル名 
new_args_file = "args.txt"   # 引数リスト（入力）
output_file = "output.txt"   # 出力ファイル（結果）

# 引数を読み込む
with open(new_args_file, "r", encoding="utf-8") as f:
    new_args = [line.strip() for line in f.readlines() if line.strip()]  # 空白行を除外

# コマンドテンプレート
command1 = "C:\\AIRead_ETL\\script\\CallFsAccountApi.ps1 {}"
command2 = "C:\\AIRead_ETL\\script\\OcrKanjyouMapper.ps1 {} 1"

# 100個の引数だけ使う（足りない場合はある分だけ使う）
args_subset = new_args[:100]

# 出力ファイルを作成
with open(output_file, "w", encoding="utf-8") as f:
    for arg in args_subset:
        f.write(command1.format(arg) + "\n")  # 1つ目のコマンド
    for arg in args_subset:
        f.write(command2.format(arg) + "\n")  # 2つ目のコマンド

print("✅ 出力完了！output.txt に書き込まれたよ！")


## 実行コマンド
## python convert_script.py
