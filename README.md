# openai-discord-bot

## 使用技術

[![Python](https://img.shields.io/badge/python-language-dimgray?style=for-the-badge&logo=python)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-discord_api-dimgray?style=for-the-badge&logo=discord)](https://discordpy.readthedocs.io/ja/latest/index.html)
[![railway](https://img.shields.io/badge/railway-deploy-dimgray?style=for-the-badge&logo=railway)](https://railway.app/)
[![openai](https://img.shields.io/badge/openai-openai_api-dimgray?style=for-the-badge&logo=openai)](https://platform.openai.com/overview)
[![Github Actions](https://img.shields.io/badge/github_actions-ci/cd-dimgray?style=for-the-badge&logo=github)](https://github.com/features/actions)
[![flake8](https://img.shields.io/badge/flake8-linter-dimgray?style=for-the-badge&logo=flake8)](https://flake8.pycqa.org/en/latest/)

### 開発方法

Python 3.13 を使用します(`.python-version`)。

依存ライブラリのインストール

```sh
$ python3 -m pip install -r requirements.txt
```

依存ライブラリを追加・更新する場合は `requirements.in` を編集し、ロックファイル `requirements.txt` を再生成します。

```sh
$ uv pip compile requirements.in -o requirements.txt --python-version 3.13
```

discord.bot の起動

```sh
python3 discordbot.py
```
