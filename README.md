# Azipa Tools VPM Listing

このリポジトリは、Azipa Worksが提供するVRChat向けツールをVRChat Creator Companion（VCC）へ配布するためのVPM Listingです。

現在は次のパッケージを公開します。

- Mesh Material Combiner
  - Package ID: `com.azipaworks.mesh-material-combiner`
  - Repository: [azipappa/MeshMaterialCombiner](https://github.com/azipappa/MeshMaterialCombiner)

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
3. `Actions` タブで `Build Repo Listing` を手動実行するか、`source.json` を変更して`main`ブランチへPushする。

初回デプロイ完了後、上記のListing URLで`index.json`が取得できることを確認してください。

## Listingの更新

`source.json`が`main`ブランチへPushされると、GitHub Actionsが各GitHub RepositoryのRelease情報を取得し、`Website/index.json`を生成してGitHub Pagesへデプロイします。必要に応じて`Build Repo Listing` workflowを手動実行することもできます。

新しいパッケージを追加する場合は、`source.json`の`githubRepos`へ次の形式でリポジトリを追加してください。

```json
"githubRepos": [
  "azipappa/MeshMaterialCombiner",
  "owner/repository"
]
```

パッケージリポジトリでは、VPM packageのZIPと`package.json`をGitHub Releaseのassetとして公開してください。VCC利用者が以前のバージョンを引き続き取得できるよう、公開済みの古いReleaseおよびパッケージassetは削除しないでください。

## 自動生成について

`Website/index.json`と公開用ページはworkflow実行時に生成・更新されます。Listingの基本情報や対象リポジトリは、生成物ではなく`source.json`を編集してください。

この構成は[VRChat公式 template-package-listing](https://github.com/vrchat-community/template-package-listing)を基にしています。
