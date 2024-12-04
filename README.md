# 岸田ゼミで使用するpythonのソースコード

## devcontainer
- vscodeを開き、左下の><となっている青いボタンを押す
- コンテナーで開くを押す

## devcontainer.jsonとcompose.yml
- compose.ymlでベースイメージの指定とコンテナの管理
- devcontainer.json内のfeaturesでpythonをインストール
- [pythonのfeatures](https://github.com/devcontainers/features/pkgs/container/features%2Fpython)
- [baseイメージ](https://hub.docker.com/r/microsoft/devcontainers-base)
- exteinsionsでvscode拡張機能をインストール

## packageのinstall

- 個別に追加する場合
```bash
pip install package名
```
- 一括で追加する場合
```bash
pip install -r requirements.txt
```

- requirements.txtに書き込む場合
```bash
pip freeze > requirements.txt
```

## 参考記事
- https://note.nkmk.me/python-janome-tutorial/
- https://qiita.com/teri/items/bc4e04316a1b14ae8365
- https://qiita.com/kazuki_hayakawa/items/18b7017da9a6f73eba77