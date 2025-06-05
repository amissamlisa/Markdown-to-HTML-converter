# MarkdownToHTMLConverter
Markdown ファイル（.md）を HTML ファイル（.html）に変換する Python スクリプトです。

## 必要な準備
### Python・pipの確認
まず、Python と pip がインストールされていることを確認してください：
```
python3 --version
pip3 --version
```

## pip が入っていない場合（Debian系 Linux）
```
sudo apt install python3-pip
```

## 必要なパッケージ
このツールでは、markdown ライブラリを使います。以下のコマンドでインストールしてください：
```
pip3 install markdown
```

## 使い方
以下のコマンドで Markdown ファイルを HTML に変換できます：
python3 file-converter.py markdown <入力ファイルパス> <出力ファイルパス>

## 注意事項
.md ファイルは UTF-8 で保存されている必要があります。
Python 3.x が必要です。
