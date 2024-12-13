# Qiita-AdventCalendar-20241214-Pyxel
Qiita Pyxel アドベントカレンダー(2024年12月14日)の投稿「[Pyxel アプリで (むりやり) Oggファイルを再生する（ローカルPC、Web、plumOS-RN）](https://qiita.com/Kazuhito/private/897e45c46f03e6980067)」で使用したソースコードです。

# Requirements 
```
pyxel==2.2.7
pygame-ce==2.5.2
```

# 1．ローカルPC

https://github.com/user-attachments/assets/ae28d019-35a0-4ff5-a52d-c685e166f913

実行コマンドは以下の通り。
```python
cd 01.Local-PC
python sample.py
```

# 2．Web
Web版のデモは以下のURLで公開しています。<br>
https://kazuhito00.github.io/Qiita-AdventCalendar-20241214-Pyxel/02.Web/

実行コマンドは以下の通り(ローカルで試す場合)
```python
cd 02.Web
pyxel package ./ sample.py
python -m http.server 8000  # http://localhost:8000
```

# 3．plumOS-RN
https://github.com/user-attachments/assets/475694b2-a004-45e6-911b-b64aa7fef91a

実行する時は以下の通り。<br>
出来上がった「03.plumOS-RN.pyxapp」をWinSCPなどで、plumOS-RNを導入した中華ゲーム機へコピーしてください。
```python:sample.py
cd 03.plumOS-RN
pyxel package ./ sample.py
```

# 使用BGM
* [魔王魂](https://maou.audio/#google_vignette) 様： [アコースティック22](https://maou.audio/bgm_acoustic22/) 

# Authors
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
Qiita-AdventCalendar-20241214-Pyxel is under [MIT License](LICENSE).
