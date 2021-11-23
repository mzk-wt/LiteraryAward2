# JSONデータおよびREST API用のページを自動生成
cd app
python main.py
cd ..

# コピー先のフォルダを削除
rm -r docs/bookdetail
rm -r docs/json

# 自動生成されたファイルをコピー
mkdir docs/bookdetail
cp -r app/output/rest/bookdetail/ docs/bookdetail/
mkdir docs/json
cp -r app/output/json/ docs/json/
