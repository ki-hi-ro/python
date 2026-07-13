# WordPress記事URL取得ツール

WordPress REST APIを使用して、`ki-hi-ro.com`で**2026年5月27日以降に公開された記事のURL**を取得し、テキストファイルに保存するPythonスクリプトです。

## 概要

WordPress REST APIの投稿取得エンドポイントへアクセスし、次の条件に一致する記事URLを取得します。

- 公開済みの記事
- 2026年5月27日以降に公開された記事
- 投稿日の新しい順

取得したURLは、1行につき1件の形式で `wp_article_urls.txt` に保存します。

WordPress REST APIでは、一度に取得できる記事数に上限があります。そのため、レスポンスヘッダーの `X-WP-TotalPages` を使用して、対象記事を全ページ分取得します。

## ファイル構成

```text
.
├── get_wp_urls.py
├── README.md
├── requirements.txt
└── wp_article_urls.txt
```

`wp_article_urls.txt` は、スクリプトを実行した後に生成されます。

## 動作環境

- Python 3.9以上
- WordPress REST APIが有効なWordPressサイト

## 使用ライブラリ

- `requests`

## セットアップ

### 1. 仮想環境を作成する

```bash
python3 -m venv .venv
```

### 2. 仮想環境を有効にする

macOS / Linuxの場合：

```bash
source .venv/bin/activate
```

Windowsの場合：

```bash
.venv\Scripts\activate
```

### 3. 必要なライブラリをインストールする

```bash
pip install requests
```

`requirements.txt` を使用する場合：

```bash
pip install -r requirements.txt
```

`requirements.txt` の内容：

```text
requests
```

## 設定

### WordPress REST APIのURL

```python
API_URL = "https://ki-hi-ro.com/wp-json/wp/v2/posts"
```

### 出力ファイル名

```python
OUTPUT_FILE = "wp_article_urls.txt"
```

### 取得開始日

```python
START_DATE = "2026-05-27T00:00:00"
```

この設定により、2026年5月27日の午前0時より後に公開された記事を取得します。

取得開始日を変更する場合は、ISO 8601形式で指定します。

```python
START_DATE = "2026-06-01T00:00:00"
```

## 実行方法

```bash
python get_wp_urls.py
```

環境によっては、次のコマンドを使用します。

```bash
python3 get_wp_urls.py
```

## 実行結果

実行中は、取得状況がターミナルに表示されます。

```text
1/2ページを取得しました
2/2ページを取得しました
2026年5月27日以降の公開記事URLを125件、wp_article_urls.txt に保存しました
```

実行後、`wp_article_urls.txt` にURLが保存されます。

```text
https://ki-hi-ro.com/article-3/
https://ki-hi-ro.com/article-2/
https://ki-hi-ro.com/article-1/
```

## WordPress REST APIへ渡す条件

| パラメータ | 値 | 内容 |
|---|---|---|
| `status` | `publish` | 公開済み記事のみ取得 |
| `after` | `2026-05-27T00:00:00` | 2026年5月27日以降の記事に限定 |
| `per_page` | `100` | 1回につき最大100件取得 |
| `page` | ページ番号 | 取得対象ページ |
| `orderby` | `date` | 投稿日で並び替え |
| `order` | `desc` | 新しい記事から取得 |
| `_fields` | `link` | 記事URLのみ取得 |

## 処理の流れ

1. WordPress REST APIへGETリクエストを送信する
2. 2026年5月27日以降の公開済み記事を100件ずつ取得する
3. 各記事の `link` をURL一覧へ追加する
4. `X-WP-TotalPages` から全ページ数を取得する
5. 最後のページまで取得を繰り返す
6. URLを `wp_article_urls.txt` に保存する

## 注意事項

- WordPress REST APIが無効なサイトでは使用できません。
- サイト側のセキュリティ設定により、APIへのアクセスが拒否される場合があります。
- 同じ名前の出力ファイルが存在する場合は上書きされます。
- 固定ページは取得対象に含まれません。
- `after` は指定日時より後の記事を取得する条件です。2026年5月27日の記事をすべて含めるため、午前0時を指定しています。