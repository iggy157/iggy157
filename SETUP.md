# GitHub Profile README セットアップガイド

このREADMEには以下の機能が実装されています:

## ✨ 実装された機能

### 1. 🎮 ターミナル風の自己紹介
- ASCII アートヘッダー
- タイピングアニメーション（[readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg)使用）
- かっこいい黒背景のコマンドライン風デザイン

### 2. 📊 スキルのレーダーチャート可視化
- カスタムSVGレーダーチャート (`skills-chart.svg`)
- 7つのスキル領域を視覚化
- プログレスバー形式のテーブルも併用

### 3. ⛅ 天気と学年の自動更新
- **毎日自動更新**: GitHub Actionsで毎日9:00 JSTに実行
- **静岡の天気**: OpenWeather APIで取得
- **学年自動更新**: 4月1日に自動的にB3→B4→M1→M2と更新
- **ランダム名言**: AIや計算機科学の名言を日替わりで表示

### 4. 💬 多言語対応
- 日本語 🇯🇵
- English 🇬🇧
- 中文 🇨🇳
- 折りたたみ可能なセクション

### 5. ✈️ GitHub統計グラフ
- GitHub Readme Stats（全体統計）
- GitHub Streak Stats（連続記録）
- GitHub Activity Graph（1年間のアクティビティ）
- 言語統計

## 🚀 セットアップ手順

### ステップ1: リポジトリの作成

1. GitHubで **あなたのユーザー名と同じ名前** の新しいリポジトリを作成
   - 例: ユーザー名が `iggy_157` なら、リポジトリ名も `iggy_157`
   - Public リポジトリとして作成
   - "Add a README file" にチェック

### ステップ2: ファイルのアップロード

以下のファイルをリポジトリにアップロード:

```
iggy_157/
├── README.md                          # メインプロフィール
├── skills-chart.svg                   # スキルチャート
├── .github/
│   ├── workflows/
│   │   └── update-readme.yml         # 自動更新ワークフロー
│   └── scripts/
│       └── update_readme.py          # 更新スクリプト
└── SETUP.md                          # このファイル
```

### ステップ3: 天気APIの設定（オプション）

天気情報を表示したい場合:

1. [OpenWeather](https://openweathermap.org/api)でアカウント作成
2. 無料のAPI keyを取得
3. GitHubリポジトリの Settings → Secrets and variables → Actions → New repository secret
4. Name: `OPENWEATHER_API_KEY`、Value: `あなたのAPIキー`

**注意**: API keyを設定しない場合、天気情報は「N/A」と表示されますが、他の機能は正常に動作します。

### ステップ4: ユーザー名の変更

`README.md` 内の `iggy_157` を **あなたのGitHubユーザー名** に置換:

```bash
# 例: テキストエディタで一括置換
iggy_157 → your_username
```

変更が必要な箇所:
- GitHub統計のURL (`github-readme-stats.vercel.app/api?username=iggy_157`)
- プロフィールビューカウンター
- その他のユーザー名参照箇所

### ステップ5: 個人情報のカスタマイズ

`README.md` を編集して、以下を自分の情報に変更:

- **メールアドレス**: `yharada@kanolab.net`
- **ポートフォリオURL**: `https://v0-portfolio-creation-zeta-three.vercel.app/`
- **大学名**: 静岡大学
- **研究室名**: 狩野研究室
- **プロジェクト内容**
- **研究関心**

### ステップ6: スキルチャートのカスタマイズ

`skills-chart.svg` を編集して、あなたのスキルレベルに合わせて調整:

```svg
<!-- 例: Pythonのスキルを90%に変更 -->
<text>🐍 Python (90%)</text>
```

または `README.md` のスキルテーブルも編集可能:

```markdown
| 🐍 Python | ██████████ 100% |
```

### ステップ7: GitHub Actionsの有効化

1. リポジトリの **Actions** タブに移動
2. "I understand my workflows, go ahead and enable them" をクリック
3. 初回は手動実行: `Update README with Dynamic Content` → `Run workflow`

### ステップ8: 学年の開始年を調整

`update_readme.py` の74行目を編集:

```python
start_year = 2024  # あなたがB3になった年に変更
```

例:
- 2024年4月にB3 → `start_year = 2024`
- 2025年4月にB3 → `start_year = 2025`

## 🎨 カスタマイズのヒント

### カラーテーマの変更

現在のテーマカラー: `#1E90FF` (Dodger Blue)

別の色に変更する場合、`README.md` 内のすべての `1E90FF` を置換:

```bash
# 例: グリーン系に変更
1E90FF → 00FF7F
```

### アニメーションの速度調整

タイピングアニメーションのパラメータ:

```
duration=3000  # 1文字あたりの表示時間（ミリ秒）
pause=1000     # 文と文の間の停止時間（ミリ秒）
```

### 統計グラフのテーマ

GitHub Statsのテーマは[こちら](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md)から選択可能:

```
theme=transparent  # 他の例: dark, radical, merko, gruvbox, etc.
```

## 🔧 トラブルシューティング

### 画像が表示されない

- ユーザー名が正しいか確認
- リポジトリがPublicになっているか確認
- SVGファイルが正しくアップロードされているか確認

### GitHub Actionsが実行されない

- Actionsが有効化されているか確認
- リポジトリの Settings → Actions → General → Workflow permissions が "Read and write permissions" になっているか確認

### 天気が更新されない

- APIキーが正しく設定されているか確認
- OpenWeatherの無料プランの制限（60 calls/minute）を超えていないか確認

### 学年が正しく更新されない

- `update_readme.py` の `start_year` が正しいか確認
- スクリプトが4月1日に実行されるまで待つ（または手動実行）

## 📝 メンテナンス

### 定期的に更新すべき項目

- **プロジェクト**: 新しいプロジェクトが増えたら追加
- **スキル**: 新しい技術を習得したらスキルチャートを更新
- **ポートフォリオ**: URLが変更されたら更新

### 自動更新の停止

GitHub Actionsを停止する場合:

1. リポジトリの Actions タブ
2. `Update README with Dynamic Content` → `...` → `Disable workflow`

## 🌟 さらなる改善案

- **Spotifyの再生中の曲を表示**: [spotify-github-profile](https://github.com/kittinan/spotify-github-profile)
- **Twitterフィード**: [twitter-badge](https://github.com/gazedash/twitter-badge)
- **ブログ記事の自動取得**: RSS feed integration
- **Contribution Snake**: [snk](https://github.com/Platane/snk)

## 📚 参考リンク

- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [Shields.io](https://shields.io/) - バッジ作成

---

**質問や問題がある場合は、Issueを作成してください！**

Good luck with your awesome GitHub profile! 🚀
