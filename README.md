# openai-discord-bot

## 使用技術

[![Python](https://img.shields.io/badge/python-language-dimgray?style=for-the-badge&logo=python)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-discord_api-dimgray?style=for-the-badge&logo=discord)](https://discordpy.readthedocs.io/ja/latest/index.html)
[![openai](https://img.shields.io/badge/openai-openai_api-dimgray?style=for-the-badge&logo=openai)](https://platform.openai.com/overview)
[![Github Actions](https://img.shields.io/badge/github_actions-ci/cd-dimgray?style=for-the-badge&logo=github)](https://github.com/features/actions)
[![flake8](https://img.shields.io/badge/flake8-linter-dimgray?style=for-the-badge&logo=flake8)](https://flake8.pycqa.org/en/latest/)

### 開発セットアップ

### ブランチの切り方

- 基本的には`main`ブランチから切るが、規模が大きくなる場合や作業が重複する場合のみ子ブランチから切っても良い。
- ブランチ名は`feature/×××`に統一

### PR の運用

- `main`ブランチにマージする時のみ自分を除く１名の`Approved`が必須
  (Free プランなので各自でマージ出来てしまいますが、極力避けてください）
- `main`ブランチへの直 Push は禁止
- `Approved`後は PR 作成者がマージ
