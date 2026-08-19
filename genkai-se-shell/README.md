# 限界SEお姉さんシェル

コマンドの標準出力をいったん捕まえて、最後に限界SEお姉さんがコメントを返す Bash CLI。

```bash
./genkai-se-shell/genkai-se echo "本番デプロイ完了"
./genkai-se-shell/genkai-se --pattern review npm test
./genkai-se-shell/genkai-se --pattern incident false
```

## 対話シェル

標準出力へリアルタイムに割り込ませたい場合は、専用シェルを起動する。

```bash
./genkai-se-shell/genkai-se --interactive
```

起動後は普通にコマンドを入力できる。`cd`、`exit`、`quit`、`help` に対応。

## zsh版

`mesgaki-shell` に近い構成で、zshの `preexec` / `precmd` フックを使う版。

```bash
./genkai-se-shell/genkai-zsh
```

既存のzshをそのまま使う場合は、`~/.zshrc` に次を追加してもよい。

```zsh
export PYTHONPATH="/home/yy/genkai-se-shell:${PYTHONPATH}"
source /home/yy/genkai-se-shell/genkai-zshrc
```

専用の `ZDOTDIR` で起動するため、既存の `~/.zshrc` は変更しない。`zsh` が未インストールの場合は、先にOSのパッケージマネージャーで導入する。

stdoutはそのまま流し、stderrを一時ファイルへ退避してコマンド終了後に復元する。失敗時だけstderrと終了コードを分類して台詞を出す。

構成は `mesgaki-shell` を参考に、分類器・台詞DB・hook・zsh統合を分離している。

```text
genkai_shell/
├── classifier.py  # stderr / 終了コード / コマンドから分類
├── taunts.py      # 限界SEの台詞DB
└── hook.py        # zshから呼ばれる出力担当
```

コマンドの終了コードはそのまま返すので、CI の後ろに置いても判定を壊さない。
