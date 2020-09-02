# new_todoapp
日々のタスクを管理するTODOアプリです．

Herokuにデプロイしています.

[todoアプリ](https://django-todoapp-new.herokuapp.com/list/)

# DEMO
トップ画面は以下のようになっています.
![](https://github.com/junkhp/new_todoapp/blob/master/images/demo.png)

# Features
タスクの作成・更新・削除・一覧表示・詳細表示に加えて，一覧の並べ替え，完了済みタスクの一覧表示が可能です．


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
仮想環境を起動
```linux
source myvenv/bin/activate
```
必要なライブラリをインストール
```bash
pip install -r requirents.txt
```

```python
python manage.py migrate
```

```bash
python manage.py runserver
```

`http://127.0.0.1:8000/`にアクセスするとtodoアプリが起動されています．

# Note
Mac以外ではテストしていません．

Herokuにデプロイしています.

[todoアプリ](https://django-todoapp-new.herokuapp.com/list/)

