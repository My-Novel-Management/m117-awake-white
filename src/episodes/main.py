# -*- coding: utf-8 -*-
"""Episode:
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer
_ = W.getWho()

## scenes
def sc_awake(w: World):
    kuro, shi = W(w.kuro), W(w.shiro)
    return w.scene("目覚めた",
            camera=w.kuro,
            )

def sc_blackgirl(w: World):
    kuro, shi = W(w.kuro), W(w.shiro)
    return w.scene("黒い少女",
            )

def sc_reason(w: World):
    kuro, shi = W(w.kuro), W(w.shiro)
    return w.scene("理由",
            w.comment("彼女は理由を語る"),
            shi.talk("$meのこと真っ黒に見えるって言ったの、あんたが初めてだ"),
            _.talk("みんな見た目で明るくて全然悩みなんかなさそうだって言うのに"),
            kuro.think("色が見えないということは黙っておいた"),
            shi.talk("中坊にはわかんないだろうけどさ、人間関係ってのがなんか大事になってくんの"),
            _.talk("本当はこんな風にいっぱいヘドロを吐き出したいのにさ、誰もがそんなの面倒、やめなって"),
            _.talk("思春期はもっとどろどろとして、鬱屈してんのに"),
            kuro.talk("だから黒くなってるの？"),
            shi.talk("本当は真っ黒。心まで全部黒く染まってる"),
            _.talk("$meはね、いつか自分が友達という名前のやつらの首をみんな締めて殺しちゃうんじゃないかって怯えてる"),
            _.talk("自分の中にバケモノを飼ってんのよ"),
            kuro.think("同じだ、と思った"),
            )

def sc_painting(w: World):
    kuro, shi = W(w.kuro), W(w.shiro)
    return w.scene("塗ればいい",
            w.comment("少年は少女の黒を引き受けた"),
            kuro.do("彼女に黒を塗られていく"),
            kuro.talk("そうだ。もっと$meにぶつけるんだ"),
            shi.talk("$meが悪いんじゃない！"),
            kuro.think("彼女の怒りと悲しみがどんどん染み込んでいくよう"),
            kuro.look("黒く染まっていく"),
            kuro.do("視界が徐々に真っ黒に染まっていく"),
            shi.talk("$meは、生きたい"),
            _.talk("バカにされても、真っ直ぐに、生きたい"),
            _.talk("生きたいよ"),
            kuro.talk("生きれるよ"),
            kuro.talk("見てごらん？", "君はもう、真っ白だ"),
            shi.do("自分を見て驚く"),
            shi.talk("でも$kuroが"),
            kuro.talk("$meは大丈夫。$meには、色は見えないから"),
            kuro.do("倒れてしまう"),
            )

def sc_blackworld(w: World):
    kuro, shi = W(w.kuro), W(w.shiro)
    return w.scene("黒い世界",
            kuro.be("歩いていた"),
            _.do("一人、真っ黒に白い線画の世界を、歩いていた"),
            _.do("白い世界を目指して、歩いていた"),
            _.think("彼女は無事に、生きただろうか"),
            _.do("と、新しい黒い少女を見つける"),
            kuro.talk("どうしたんだい？"),
            kuro.do("差し伸べた彼の腕は半分黒く染まっていた"),
            )

## episode
def ep_main(w: World):
    return w.episode("黒い少女",
            ## NOTE:
            ##  - 白い世界
            ##  - 黒い少女
            ##  - 赤い脱出
            sc_awake(w),
            sc_blackgirl(w),
            sc_reason(w),
            sc_painting(w),
            sc_blackworld(w),
            )
