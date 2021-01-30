# sendir

bto_advanced_USBIR_cmdのPythonラッパー

## Requirements

### Docker

- Docker
- docker-compose

### Native

- USB赤外線リモコンアドバンスUNIX系環境用コマンドライン操作ツール＆GUI操作ツール Ver1.0.0 (bto_advanced_USBIR_cmd)

## Usage

### Docker

```
$ docker-compose run --rm sendir [on | off | nl | inc | red]
```

### Native

```
$ ./sendir.py [on | off | nl | inc | red]
```

## Note

- `ir_patterns/`に同梱の赤外線パターンファイルは、NEC RE0201のもの
- わざわざ本体側の機能でタイマーを使う必要は薄い為、タイマーの赤外線パターン送信機能は実装していない。
