# new_todoapp
日々のタスクを管理するTODOアプリです．

Python+Djangoで作成しました

Herokuにデプロイしています.

[todoアプリ](https://django-todoapp-new.herokuapp.com/list/)

# DEMO
トップ画面は以下のようになっています.
![](https://github.com/junkhp/new_todoapp/blob/master/images/demo.png)

# Features
## 機能
- ユーザー登録，ログイン，ログアウト
- ログインしているユーザーのタスク一覧表示
- ログインしているユーザーの完了済みタスク一覧表示
- タスクの作成
- タスクの更新
- タスクの削除
- タスクの詳細表示
- タスクを更新済みにする
- 作成順・締め切り順・優先度順によるタスクの並べ替え


# 開発環境
OS
* macOS Catalina バージョン 10.15.6

その他

* Python 3.7.3

# Usage
このレポジトリをクローン
```bash
git clone https://github.com/junkhp/new_todoapp.git
```
クローンしたフォルダに移動
```linux
cd new_todoapp/
```
仮想環境を起動し，必要なライブラリをインストール
```bash
pip install -r requirents.txt
```

モデルをmigrate
```python
python manage.py migrate
```

アプリを実行
```bash
python manage.py runserver
```

`http://127.0.0.1:8000/`にアクセスするとtodoアプリが起動されています．

# Note
Mac以外ではテストしていません．

Herokuにデプロイしています.

[todoアプリ](https://django-todoapp-new.herokuapp.com/list/)

