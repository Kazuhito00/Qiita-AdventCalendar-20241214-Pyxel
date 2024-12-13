import ctypes
from ctypes import c_int, c_char_p
from pathlib import Path

import pyxel


class Sample:
    def __init__(self):
        self.play_flag = False
        self.ogg_path = ""

        # Pyxel初期化
        pyxel.init(256, 256)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.play_flag:
            # Oggファイル格納パス生成
            for path in Path.cwd().rglob("maou_bgm_acoustic22.ogg"):
                self.ogg_path = str(path)

            # SDL2およびSDL2_mixerの共有ライブラリをロード
            sdl2 = ctypes.CDLL("/usr/lib/libSDL2.so")
            sdl2_mixer = ctypes.CDLL("/usr/lib/libSDL2_mixer.so")

            # SDL2およびSDL2_mixerの関数を定義
            sdl2.SDL_Init.argtypes = [c_int]
            sdl2.SDL_Init.restype = c_int
            sdl2_mixer.Mix_Init.argtypes = [c_int]
            sdl2_mixer.Mix_Init.restype = c_int
            sdl2_mixer.Mix_OpenAudio.argtypes = [c_int, c_int, c_int, c_int]
            sdl2_mixer.Mix_OpenAudio.restype = c_int
            sdl2_mixer.Mix_LoadMUS.argtypes = [c_char_p]
            sdl2_mixer.Mix_LoadMUS.restype = ctypes.c_void_p
            sdl2_mixer.Mix_PlayMusic.argtypes = [ctypes.c_void_p, c_int]
            sdl2_mixer.Mix_PlayMusic.restype = c_int

            # SDL2を初期化
            sdl2.SDL_Init(0x00000010)  # オーディオサブシステムを有効化

            # SDL_mixerのOGGサポートを有効化
            sdl2_mixer.Mix_Init(0x00000002)  # Oggの初期化フラグ

            # オーディオデバイスを初期化
            # 周波数: 44100Hz, フォーマット: 16ビット, チャンネル: ステレオ, チャンクサイズ: 1024
            sdl2_mixer.Mix_OpenAudio(44100, 0x8010, 2, 1024)

            # Oggファイル読み込み
            music = sdl2_mixer.Mix_LoadMUS(self.ogg_path.encode("utf-8"))

            # Oggファイル再生
            sdl2_mixer.Mix_PlayMusic(music, -1)  # -1はループ再生

            self.play_flag = True

        # AボタンかBボタンで終了
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            pyxel.quit()

    def draw(self):
        pyxel.cls(7)

        # 再生表示
        if self.play_flag:
            pyxel.text(2, 2, "Now Playing...", 1)
            pyxel.text(2, 10, self.ogg_path, 1)


Sample()
