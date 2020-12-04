# make_gallery.py
## 仕様
src/img/配下のフォルダを全て取得して、それぞれのフォルダにある画像ファイルからHTMLを生成する。
template.htmlに画像のパスを当てはめる。

## 実行方法
`python3 make_gallery.py`
※ github Actionsで起動するため、ローカルでの実行は不要

# resize.py
## 仕様
src/img/配下にある画像のサイズを変更する。
topimg以外の画像を対象に縦or横が1500px以上の画像を縦横ともに半分のサイズに変更し上書き保存する。

## パッケージのインストール
`pip install pillow`

## 実行方法
`python3 resize.py`
※ github Actionsで起動するため、ローカルでの実行は不要
