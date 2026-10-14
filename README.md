# Azipa Tools VPM Listing

このリポジトリは、Azipa Worksが提供するVRChat向けツールをVRChat Creator Companion（VCC）へ配布するためのVPM Listingです。

現在は次のパッケージを公開します。

- Mesh Material Combiner
  - Package ID: `com.azipaworks.mesh-material-combiner`
  - Repository: [azipappa/MeshMaterialCombiner](https://github.com/azipappa/MeshMaterialCombiner)
- Auto Save
  - Package ID: `com.azipaworks.auto-save`
  - Repository: [azipappa/Auto-Save](https://github.com/azipappa/Auto-Save)
- Blendshape Editor
  - Package ID: `com.azipaworks.blendshape-editor`
  - Repository: [azipappa/BlendshapeEditor](https://github.com/azipappa/BlendshapeEditor)

- DistanceFadeController (Beta)
  - Package ID: `com.azipa.distance-fade-controller`
  - Repository: [azipappa/DistanceFadeController](https://github.com/azipappa/DistanceFadeController)

## VCCへの登録

VCCの `Settings` > `Packages` > `Add Repository` で、次のListing URLを登録してください。

```text
https://azipappa.github.io/azipa-tools-vpm/index.json
```

公開後は、[Azipa Tools Listing](https://azipappa.github.io/azipa-tools-vpm/) の `Add to VCC` ボタンからも登録できます。

## 初回のGitHub Pages設定

GitHub上で次の設定を一度だけ手動で行ってください。追加のSecretやアクセストークンは不要です。

1. このリポジトリの `Settings` > `Pages` を開く。
2. `Build and deployment` の `Source` を **GitHub Actions** に設定する。
3. `Actions` タブで `Build Repo Listing` を手動実行するか、`source.json` を変更して既定ブランチへPushする。

初回デプロイ完了後、上記のListing URLで`index.json`が取得できることを確認してください。

## Listingの更新

`source.json`が既定ブランチへPushされると、GitHub Actionsが各GitHub RepositoryのRelease情報を取得し、`Website/index.json`を生成してGitHub Pagesへデプロイします。必要に応じて`Build Repo Listing` workflowを手動実行することもできます。

新しいパッケージを追加する場合は、`source.json`の`githubRepos`へ次の形式でリポジトリを追加してください。

```json
"githubRepos": [
  "azipappa/MeshMaterialCombiner",
  "azipappa/Auto-Save",
  "azipappa/BlendshapeEditor",
  "azipappa/DistanceFadeController"
]
```

パッケージリポジトリでは、ルートに`package.json`を含むVPM packageのZIPをGitHub Releaseのassetとして公開してください。VCC利用者が以前のバージョンを引き続き取得できるよう、公開済みの古いReleaseおよびパッケージassetは削除しないでください。

## 自動生成について

`Website/index.json`と公開用ページはworkflow実行時に生成・更新されます。Listingの基本情報や対象リポジトリは、生成物ではなく`source.json`を編集してください。

この構成は[VRChat公式 template-package-listing](https://github.com/vrchat-community/template-package-listing)を基にしています。

## DistanceFadeControllerの初回公開

DistanceFadeControllerを追加済みです。Release未公開のリポジトリはCIの取り込み前チェックで一時的に除外するため、初回Releaseを待っている間も既存パッケージのListingを維持します。公開済みPre-releaseも取り込み対象です。

1. DistanceFadeControllerの変更をcommit・pushし、`v0.1.0`タグをpushする。
2. GitHubのReleaseにパッケージZIPが添付されていることを確認する。
3. このリポジトリの変更をcommit・pushする。
4. `Build Repo Listing`を手動実行するか、毎時の自動更新を待つ。

両リポジトリともSettings > Secrets and variables > Actionsへの追加登録は不要です。自動発行のGITHUB_TOKENを使用します。Listing側ではSettings > Pages > SourceをGitHub Actionsにしてください。

同一バージョンの公開済みZIPは差し替えず、更新時は新しいバージョンのReleaseを追加してください。
