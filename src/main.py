# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import basic
## local files
from episodes.main import ep_main
## settings
from config import DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS


## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
# Sample step:
# 1) Create the world
#       世界を作成する。
# 2) Create a new chapter
#       章の作成。
# 3) Create a episode
#       エピソード作成。
# 4) Create a new scene
#       シーン作成。物語のベース。ここに様々なActionを追加する。
# 5) Create a new stage
#       舞台作成。シーンに必須要素
# 6) Create a new day and time
#       日時作成。シーンのサブ要素
# 7) Add a scene plot
#       シーンプロットの作成。概要のないシーンは原則使えない
# 8) Add scene actions
#       シーンアクションの追加。
#
################################################################


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_main(w),
            )

def create_world():
    """Create a world.
    """
    w = World("真っ白な世界で、真っ黒な君と")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.buildDB(PERSONS,
            STAGES, ITEMS, DAYS, TIMES, WORDS,
            RUBIS, LAYERS)
    # w.setBaseDate()
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("朝目覚めたら色を失って線画みたいな世界にいた少年は、真っ黒に染まった少女と出会い、彼女を助ける為に自らを犠牲にする")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

