import os
from pathlib import Path

import pyxel
import pygame


class Sample:
    def __init__(self):
        self.play_flag = False
        self.ogg_path = ""

        # pyxapp名取得
        for path in Path.cwd().rglob("*.pyxapp"):
            self.pyxapp_path = path

        # pygame初期化
        pygame.mixer.init()

        # Pyxel初期化
        pyxel.init(256, 256)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.play_flag:
            # Oggファイル格納パス生成
            self.ogg_path = os.path.join(
                "/tmp/.pyxel/play/42",
                self.pyxapp_path.stem,
                "maou_bgm_acoustic22.ogg",
            )

            # Oggファイル読み込み
            pygame.mixer.music.load(self.ogg_path)

            # Oggファイル再生
            pygame.mixer.music.play(-1)  # -1はループ再生

            self.play_flag = True

    def draw(self):
        pyxel.cls(7)

        # 再生表示
        if self.play_flag:
            pyxel.text(2, 2, "Now Playing...", 1)
            pyxel.text(2, 10, self.ogg_path, 1)


Sample()
