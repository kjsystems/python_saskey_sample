## Descripiton
SAS キー付き URL を生成するサンプル

## HOW TO TEST
- Azure Storage にファイルを置きます
  - function_app.py では sampleコンテナ/sample.docx になっているので適宜修正してください。  
```
// function_app.py
container_name = "sample"
blob_name = "sample.docx"
```
- .devcontainer を起動します
  - VSCode から「コマンドパレット」 → Reopen in Container
- 下記二つの値を設定します
```
// function_app.py
account_name = "<your-account-name>"
account_key = "<your-account-key>"
```
- F5 でデバッグ実行します
- rest.http を開いてエンドポイントを実行します
- SAS キー付きの URL 出力されます
