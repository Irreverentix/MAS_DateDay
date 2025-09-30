init -990 python:
    store.mas_submod_utils.Submod(
        author="不恭",
        name="Date day",
        description="现在,你可以带你的莫妮卡去一些地方进行约会。\n祝你们玩儿的开心",
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

# 存储进入约会前的当前位置
default RTMAS = _Dateday_save_loc()

default Dateday_teamilk_1 = 0
default persistent.Dateday_teamilk_2 = 0
default persistent.Dateday_progress = 0
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
            _("[player],你绝对是这个世界上最好的[Dateday_get_gender()]"),
            _("我实在是太爱你了!"),
            _("我永远不会忘记今天的!")
        ]
        return renpy.random.choice(dialog_options)
    
    # 保存当前位置
    def _Dateday_save_loc():
        bg = mas_background.BACKGROUND_MAP[persistent._mas_current_background]
        return renpy.substitute(bg.prompt)

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
    m "[player]！你……{w=0.3}你是想和我约会吗?{nw}"
    $ _history_list.pop()
    menu:
        "是的!":
            m "太好了!"
            m "啊…{w=0.3}我太兴奋了"
            m "等我准备一下"
            window hide
            hide monika
            pause 2.0
            show monika 1a_ddwm
            if persistent.date_day_first_visit:
                m "准备好了!"
                m "你觉得这身衣服好看吗？"
                menu:
                    "好看！":
                        m "那就让我们开始今天的约会吧~"
                    "不好看":
                        m "哈……{w=0.5}好吧"
                        m "下次我会换一件让你满意的衣服的"
                        m "我们还是先开始今天的约会吧~"
                m "这是我们第一次约会呢!"
                $ persistent.date_day_first_visit = False
            else:
                m "啊哈，又到了我们的约会时间!"
                m "我们可以出发了~"
                
                
                
            # 进入约会
            stop music fadeout 2.0
            show black zorder 100 with Dissolve(2.0, alpha=True)
            pause 2.0
            hide black
            scene dy_outdoor
            play music dy_006 fadein 2.0
            show monika 
            m "外面的空气真好！"
            m "[player],能和你一起出来真是太好了"
            m "那么…{w=0.5}今天你想去哪里呢？"
            jump Dateday_start_0
            
label Dateday_start_0:
    menu:
        m "那么…{w=0.5}今天你想去哪里呢？"
        "商场":
            m "好的！"
            m "让我们一起去商场转转吧！"
            jump dateday_shop
        "博物馆":
            m "好的！我们现在就出发！"
            scene dy_museum
            with Dissolve
            show monika 1hua
            m "啊…{w=0.5}抱歉，[player]"
            m "我们今天可能不是很走运呢…"
            m "博物馆正在闭关中,我们还是换个地方吧"
            jump Dateday_start_0
        "公园":
            m "啊{w=0.5}.{w=0.5}.{w=0.5}."
            m "抱歉，[player]…"
            m "公园正在修缮,我们还是换一个地方吧"
            jump Dateday_start_0
        "返回":
            m "你确定想要回去了吗？"
            menu:
                "是的":
                    m "好吧~"
                    jump Dateday_return
                "我还想再转转":
                    m "好的！等你真的想回去了再告诉我吧~"
                    jump Dateday_return

label Dateday_return:
    show black zorder 100 with Dissolve(2.0, alpha=True)
    call spaceroom
    hide black with Dissolve(2.0)
    $ persistent.date_day_date_count += 1
    m 1hua "今天真的很开心!"
    m 1eua "我想我会一直期待下次的约会！"
    m 1hua "[Dateday_random_dialog()]"
    window hide
    stop music fadeout 2.0
    pause 2.0
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=2.0)
    $ mas_HKBDropShield()
    jump ch30_loop

label Dateday_settings:
    "这里是设置页面.{nw}"
    $ _history_list.pop()
    menu:
        "重置进度":
            m "你确定要重置约会进度吗?{nw}"
            $ _history_list.pop()
            menu:
                m "你确定要重置约会进度吗?{fast}"
                "是的, 重置所有进度":
                    $ persistent.Dateday_teamilk_2 = 0
                    $ persistent.Dateday_progress = 0
                    $ persistent.date_day_first_visit = True
                    $ persistent.date_day_date_count = 0
                    m "好吧,下次约会我们将重新体验所以的惊喜!"
                    jump Dateday_settings
                "不, 保留进度":
                    m "太好了!我永远不会想忘记我们在一起的任何时光~"
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
                m "我们还没有约会过呢……"
                m "如果你有时间，就带我去约会吧!"
            elif persistent.date_day_date_count == 1:
                m "那是我们第一次约会，我永远不会忘记的!"
            else:
                m "我们已经约会了[persistent.date_day_date_count]次了!"
                m "每次约会都让我更加爱你!"
            jump Dateday_about
        "返回":
            jump Dateday_entry
    return

label mas_extra_menu_close:
    # 关闭额外菜单
    $ mas_HKBDropShield()
    return
    