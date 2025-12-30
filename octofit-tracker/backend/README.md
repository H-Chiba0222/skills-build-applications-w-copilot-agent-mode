# OctoFit Tracker — Backend (Django)

このフォルダは Django バックエンドの最小骨組みです。

セットアップ手順（ローカル）:

```bash
# 仮想環境を作成
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate

# 依存関係をインストール
pip install -r octofit-tracker/backend/requirements.txt

# マイグレーションと管理者ユーザー作成
python octofit-tracker/backend/manage.py migrate
python octofit-tracker/backend/manage.py createsuperuser

# 開発サーバ起動
python octofit-tracker/backend/manage.py runserver
```

注意:
- MongoDB を使用する場合は `mongod` を起動し、`settings.py` の `DATABASES` を環境に合わせて調整してください。
- 本リポジトリの指示に従い、Django ORM を優先してください。
