init -990 python:
    store.mas_submod_utils.Submod(
        author="不恭",
        name="Date day",
        description="现在,你可以带你的莫妮卡去一些地方进行约会。\n祝你们玩儿的开心❤️\n有任何问题或建议请联系作者,QQ:2643744733",
        version="1.0.0"
    )


init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Date day",
            user_name="Irreverentix",
            repository_name="MAS_DateDay",
            extraction_depth=1
        )

init -991 python:
    import store.mas_sprites as mas_sprites
    import store.mas_utils as mas_utils


default persistent.Dateday_clothingshop = 0
default persistent.Dateday_sailor_worn = 0
default persistent.Dateday_casual_worn = 0
default persistent.Dateday_dress_worn = 0
default persistent.Dateday_teamilk = 0
default persistent.Dateday_pearl_first = True
default persistent.Dateday_matcha_first = True
default persistent.Dateday_fruit_first = True
default persistent.Dateday_taro_first = True
default persistent.Dateday_cheese_first = True

default persistent.date_day_first_visit = True
default persistent.date_day_date_count = 0 # 约会次数


init 5 python:
    import store
    from store import persistent, mas_background
    
    def Dateday_get_gender():
        if persistent.gender == "M":
            return "男朋友"
        elif persistent.gender == "F":
            return "女朋友"
        else:
            return "伴侣"
    
    def Dateday_submenu():
        renpy.call_screen("Dateday_menu")
    
    def Dateday_random_dialog():
        dialog_options = [
            _("能和你分享这些美好的时刻，是我最珍惜的礼物"),
            _("和你在一起的每一刻都让我感到无比幸福"),
            _("今天的回忆，我会永远珍藏在心里")
        ]
        return renpy.random.choice(dialog_options)

screen Dateday_menu():
    zorder 50
    style_prefix "hkb"
    
    frame:
        area (0, 0, 1280, 720)
        background Solid("#0000007F")
    
    textbutton _("Close"):
        area (60, 596, 120, 35)
        style "hkb_button"
        action Jump("mas_extra_menu_close")
    
    # 菜单
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20
        
        textbutton "开始约会":
            action [Hide("Dateday_menu"), Jump("Dateday_start")]
            hover_sound gui.hover_sound
            xsize 200
        
        textbutton "重置":
            action [Hide("Dateday_menu"), Jump("Dateday_settings")]
            hover_sound gui.hover_sound
            xsize 200
        
        textbutton "关于":
            action [Hide("Dateday_menu"), Jump("Dateday_about")]
            hover_sound gui.hover_sound
            xsize 200
        
        null height 20
        
        textbutton "返回":
            action [Hide("Dateday_menu"), Return()]
            hover_sound gui.hover_sound
            xsize 200


label Dateday_entry:
    python:
        mas_RaiseShield_dlg()
        Dateday_submenu()
    return

label Dateday_start:
    m 1wub "[player]！你……{w=0.3}你是想和我约会吗?{nw}"
    $ _history_list.pop()
    menu:
        "是的!":
            m 1sub "太好了!"
            m 2dku "啊…{w=0.3}我太兴奋了"
            m 2eka "这让我想起了我们第一次见面的时候..."
            m 7eua "虽然现在的情况有些不同，但和你在一起的每一刻都很特别。"
            m 3hub "等我准备一下，马上就好！"
            window hide
            hide monika
            pause 2.0
            show monika 3b_dateday01 zorder 12 at t11
            if persistent.date_day_first_visit:
                m 3b_dateday01 "准备好了!"
                m 1t_dateday01 "你觉得这身衣服好看吗？"
                m 5b_dateday01 "我特意选了这件，希望你会喜欢~"
                menu:
                    "好看！":
                        m 4k_dateday01 "太好了！"
                        m 5b_dateday01 "那就让我们开始今天的约会吧~"
                    "不好看":
                        m 4l_dateday01 "这样啊…{w=0.5}没关系"
                        m 4n_dateday01 "下次我会换一件更合适的衣服"
                        m 1l_dateday01 "不过现在，我们还是先开始今天的约会吧~"
                m 1k_dateday01 "这是我们第一次约会呢!"
                m 5b_dateday01 "我真的很期待和你一起创造美好的回忆。"
                $ persistent.date_day_first_visit = False
            else:
                pause 0.3
                m 3k_dateday01 "啊哈，又到了我们的约会时间!"
                m 3j_dateday01 "每次和你约会都让我心跳加速..."
                m 5a_dateday01 "你知道吗，在这个小房间里等待的每一刻，都让我更加期待和你的约会呢～"
                m 5b_dateday01 "现在！我们可以出发了!"
                
            # 进入约会
            stop music fadeout 2.0
            show black zorder 100 with Dissolve(2.0, alpha=True)
            pause 2.0
            hide black
            $ original_bg = mas_current_background.background_id
            scene dy_outdoor
            with dissolve
            play music dy_006 fadein 2.0
            show monika 4j_dateday01 zorder 12 at t11
            m 4j_dateday01 "外面的空气真好！"
            m 4k_dateday01 "[player]，能和你一起出来真是太好了"
            m 3v_dateday01 "这种感觉就像梦想成真一样..."
            m 5b_dateday01 "那么…{w=0.5}今天你想去哪里呢？"
            jump Dateday_start_0
            
label Dateday_start_0:
    menu:
        m 5b_dateday01 "那么…{w=0.5}今天你想去哪里呢？"
        "商场":
            m 1k_dateday01 "好的！"
            m 5b_dateday01 "让我们一起去商场转转吧！"
            m 2k_dateday01 "说实话，我很好奇那里会有什么有趣的东西..."
            jump dateday_shop
        "博物馆":
            m 1b_dateday01 "好的！我们现在就出发！"
            scene dy_museum
            with dissolve
            menu:
                "进入":
                    pass
            show monika 5b_dateday01 zorder 12 at t11
            m 4l_dateday01 "啊…{w=0.5}抱歉，[player]"
            m 2l_dateday01 "我们今天不是很走运呢…"
            m 2a_dateday01 "博物馆正在闭馆中，我们还是换个地方吧~"
            jump Dateday_start_0
        "公园":
            m 4n_dateday01 "啊{w=0.5}.{w=0.5}.{w=0.5}."
            m 4m_dateday01 "那个……"
            m 1n_dateday01 "抱歉，[player]…"
            m 1l_dateday01 "公园还在修缮，我们还是换一个地方吧"
            jump Dateday_start_0
        "返回":
            m 5a_dateday01 "你确定想要回去了吗？"
            menu:
                "是的":
                    m 2b_dateday01 "好吧~"
                    m 2k_dateday01 "那我们改天再约会吧"
                    jump Dateday_return
                "我还想再转转":
                    m 5b_dateday01 "好的！"
                    m 5b_dateday01 "等你真的想回去了再告诉我吧~"
                    jump Dateday_start_0

label Dateday_return:
    show black zorder 100 with Dissolve(2.0, alpha=True)
    call spaceroom
    hide black with Dissolve(2.0)
    $ persistent.date_day_date_count += 1
    m 1hua "今天真的很开心!"
    m 2eka "每次和你在一起的时间都过得特别快..."
    m 1eua "我想我会一直期待下次的约会！"
    m 3hub "[Dateday_random_dialog()]"
    window hide
    stop music fadeout 2.0
    pause 1.0
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=2.0)
    $ mas_HKBDropShield()
    jump ch30_loop

label Dateday_settings:
    "这里是设置页面.{nw}"
    $ _history_list.pop()
    menu:
        "重置进度":
            m 1ekc "你确定要重置约会进度吗?{nw}"
            $ _history_list.pop()
            menu:
                m "你确定要重置约会进度吗?{fast}"
                "是的, 重置所有进度":
                    $ persistent.Dateday_teamilk = 0
                    $ persistent.date_day_first_visit = True
                    $ persistent.date_day_date_count = 0
                    $ persistent.Dateday_pearl_first = True
                    $ persistent.Dateday_matcha_first = True
                    $ persistent.Dateday_fruit_first = True
                    $ persistent.Dateday_taro_first = True
                    $ persistent.Dateday_cheese_first = True
                    $ persistent.Dateday_sailor_worn = 0
                    $ persistent.Dateday_casual_worn = 0
                    $ persistent.Dateday_dress_worn = 0
                    $ persistent.Dateday_clothingshop = 0  # 添加服装店重置

                    m 2eka "好吧，下次约会我们将重新体验所有的惊喜!"
                    m 1eua "我相信那也会很美好的~"
                    jump Dateday_settings
                "不, 保留进度":
                    m 1hub "太好了!"
                    m 3eka "我永远不想忘记我们在一起的任何时光~"
                    jump Dateday_settings
        "返回":
            jump Dateday_entry
    return

label Dateday_about:
    "这是约会日（DateDay）模组, 版本1.0.0.{nw}"
    "有问题请联系作者{nw}"
    $ _history_list.pop()
    menu:
        "我们约会多少次了？":
            if persistent.date_day_date_count == 0:
                m 2ekc "我们还没有约会过呢……"
                m 1eka "如果你有时间，就带我去约会吧!"
                m 3hub "我会很期待的~"
            elif persistent.date_day_date_count == 1:
                m 1wub "那是我们第一次约会，我永远不会忘记的!"
                m 2dku "那天的每一个细节都深深印在我的脑海里..."
            else:
                m 1eua "我们已经约会了[persistent.date_day_date_count]次了!"
                m 3hub "每次约会都让我更加珍惜我们在一起的时光!"
                m 1eka "真希望我们能永远这样下去..."
            jump Dateday_about
            
        "我们喝了多少次奶茶？":
            if persistent.Dateday_teamilk == 0:
                m 2ekc "我们还没一起喝过奶茶呢……"
                m 1eka "下次约会时带我去奶茶店吧，我很想尝尝呢~"
            elif persistent.Dateday_teamilk == 1:
                m 1eua "我们一起去喝过一次奶茶!"
                m 3hub "那次的奶茶真的很美味，让我印象深刻~"
            else:
                m 1eua "我们已经一起喝了[persistent.Dateday_teamilk]次奶茶了!"
                m 3eub "每次和你分享奶茶的时光都很甜蜜~"
                if persistent.Dateday_teamilk >= 3:
                    m 2rksdla "不过[player]，奶茶虽好，但也要注意适量哦~"
                    m 1eka "为了你的健康着想~"
            jump Dateday_about
            
        "我们试穿了多少次衣服？":
            $ total_outfits = persistent.Dateday_sailor_worn + persistent.Dateday_casual_worn + persistent.Dateday_dress_worn
            if total_outfits == 0:
                m 2ekc "我们还没一起试穿过衣服呢……"
                m 1eka "下次约会时带我去服装店看看吧，我很想为你展示不同的装扮~"
            else:
                m 1eua "让我看看我们的换装记录……"
                m 3eub "水手服试穿了[persistent.Dateday_sailor_worn]次，"
                m 3eua "休闲装试穿了[persistent.Dateday_casual_worn]次，"
                m 3eub "丝绸裙子试穿了[persistent.Dateday_dress_worn]次。"
                m 1eua "总共试穿了[total_outfits]次衣服呢~"
                
                if persistent.Dateday_sailor_worn >= persistent.Dateday_casual_worn and persistent.Dateday_sailor_worn >= persistent.Dateday_dress_worn:
                    m 2rksdla "看来你最喜欢看我穿水手服呢~"
                    m 1tsu "那种学院风格确实很特别~"
                elif persistent.Dateday_casual_worn >= persistent.Dateday_sailor_worn and persistent.Dateday_casual_worn >= persistent.Dateday_dress_worn:
                    m 2eksdla "休闲装是最常穿的呢~"
                    m 1hua "确实很舒适自然~"
                else:
                    m 2rksdlb "丝绸裙子是试穿最多的~"
                    m 1tsb "看来你喜欢看我穿得优雅一些呢~"
                    
                m 1eka "每次为你试穿新衣服，都让我心跳加速呢~"
            jump Dateday_about
            
        "返回":
            jump Dateday_entry
    return

label mas_extra_menu_close:
    # 关闭额外菜单
    $ mas_HKBDropShield()
    return