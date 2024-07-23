## What is this?
Blob Storage にあるファイルの SAS キー付き URL を生成するサンプル

## How to test.
- Blob Storage の Blob コンテナーにファイルを置きます
  - function_app.py では sample コンテナ / sample.docx になっているので適宜修正してください。  
```
// function_app.py
container_name = "sample"
blob_name = "sample.docx"
```
- .devcontainer を起動します
  - VSCode から「コマンドパレット」 → 「Dev Containers: Reopen in Container」
- function_app.py で下記二つの値を設定します
  - Blob Storage のアカウント名
  - Blob Storage のアカウントキー
```
// function_app.py
account_name = "<your-account-name>"
account_key = "<your-account-key>"
```
- （参考）SAS キーの有効期限は１日になっています
```
// function_app.py
expiry_time = start_time + datetime.timedelta(days=1)
```
- F5 でデバッグ実行します
- ブラウザや 同じフォルダにある `rest.http`（REST Client）で URL を実行します
- SAS キー付きの URL が出力されます
- 生成された URL をブラウザで開くとダウンロードできます
## References
- [Azure-Samples/AzureStorageSnippets | GitHub](https://github.com/Azure-Samples/AzureStorageSnippets/blob/master/blobs/howto/python/blob-devguide-py/blob_devguide_create_sas.py#L21)
- [Python を使用してアカウント SAS を作成する | Learn](https://learn.microsoft.com/ja-jp/azure/storage/common/storage-account-sas-create-python)
