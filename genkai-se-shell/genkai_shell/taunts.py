import random

TAUNTS = {
    "command_not_found": [
        "そのコマンド存在しないよ。PATHかスペル、確認して？",
        "「{}」って何？ 新しいコマンドを発明したの？",
        "command not found。補完機能、使ってもいいんだよ？",
    ],
    "permission_denied": [
        "権限がないね。sudoを付ける前に、誰のファイルか見て？",
        "Permission denied。最小権限の原則にまで拒否されてるよ",
        "chmod 777で解決しようとしてないよね？ 本当にやめてね？",
    ],
    "no_such_file": [
        "そのファイル、存在しないよ。pwdとlsからやり直そっか",
        "パスが違うね。Tab補完っていう便利な機能があるんだけど？",
        "消したの自分じゃない？ 私、そこまで面倒見られないよ",
    ],
    "syntax_error": [
        "構文エラー。クォートと括弧は最後まで面倒見てあげて？",
        "shellcheckを通してから来て。私もレビューする体力ないから",
    ],
    "network": [
        "繋がらないね。サービスとポートとファイアウォール、順番に見て？",
        "systemctl statusとログを確認しよ。推測だけで直すのは危ないよ",
    ],
    "timeout": [
        "タイムアウト。相手が遅いのか、経路が死んでるのか調べて？",
        "待たせすぎ。curl -vかtracerouteで状況を見ようね",
    ],
    "disk_full": [
        "ディスク満タン。df -hとdu -sh、今すぐ確認して？",
        "ログかDockerイメージが育ちすぎてるね。掃除は計画的にね",
    ],
    "oom": [
        "メモリが足りなくて落ちたよ。free -hくらい見よ？",
        "OOMキラーにやられたね。limitsとリークを確認しよっか",
    ],
    "git": [
        "Gitに怒られてるよ。まずgit statusを見てから動こう？",
        "ブランチとリモート、把握してる？ force pushは最後の手段ね",
    ],
    "docker": [
        "Dockerが起動してないか、コンテナが死んでるね。logs見よ？",
        "イメージのタグかポートマッピング、確認してから再実行しよ",
    ],
    "generic": [
        "終了コード {}。エラーメッセージは読むために出てるよ？",
        "失敗。まず再現手順とログを確保しよ。私も限界だから",
        "あーあ、予定外の仕事が増えたね。原因から潰そっか",
    ],
}


def get_taunt(category: str, command: str = "", code: int = 0) -> str:
    message = random.choice(TAUNTS.get(category, TAUNTS["generic"]))
    return message.format(command if "{}" in message and category == "command_not_found" else code)

