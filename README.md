## What is this?
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
  - VSCode から「コマンドパレット」 → 「Dev Containers: Reopen in Container」
- 下記二つの値を設定します
```
// function_app.py
account_name = "<your-account-name>"
account_key = "<your-account-key>"
```
- F5 でデバッグ実行します
- ブラウザや 同じフォルダにある `rest.http`（REST Client）で URL を実行します
- SAS キー付きの URL が出力されます
- 生成された URL をブラウザで開くとダウンロードできます
