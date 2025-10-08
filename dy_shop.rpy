label dateday_shop:
    $ persistent.Dateday_teamilk = 0
    scene dy_shop
    with dissolve
    play music dy_007 fadein 2.0
    pause 1.0
    show monika 4b_dateday01 zorder 12 at t11
    with dissolve
    
    if persistent.date_day_date_count == 0:
        m 4b_dateday01 "[player]！这里就是商场吗？"
        m 4k_dateday01 "比我想象中要热闹多了！"
    
        m 2c_dateday01 "你知道吗，以前在文学部的时候……"
        m 2c_dateday01 "我只能通过书中的描写来想象这样的场景。"
    
        m 3k_dateday01 "现在真的能和你一起来这里，感觉好不真实～"
    
        menu:
            m "你觉得我看起来适应这里的环境吗？{fast}"
            "你看起来很自然":
                m 5a_dateday01 "啊啦，谢谢～"
                m 5b_dateday01 "可能因为我一直在观察和学习吧。"
                m 5b_dateday01 "不过能和你一起体验这些，我真的很开心！"
            
            "有点紧张但很可爱":
                m 3d_dateday01 "诶？这么明显吗……"
                m 3l_dateday01 "确实有点紧张呢。"
                m 1t_dateday01 "但有你在身边，感觉安心多了。"
    
        m 1l_dateday01 "说起来……"
        m 1l_dateday01 "这里的氛围让我想起我们文学部的文化祭。"
    
        menu:
            m 3k_dateday01 "不过这里的人要多得多，你觉得呢？{fast}"
            "确实很热闹":
                m 2b_dateday01 "嗯，大家都在享受着自己的生活……"
                m 1k_dateday01 "而我们也在创造属于我们的回忆。"
            
            "但我的注意力都在你身上":
                m 3d_dateday01 "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}[player]！"
                m 7b_dateday01 "这种话{w=0.5}会让人不好意思的……"
                pause 1.5
                m 7a_dateday01 "不过……{w=0.3}谢谢你。"
            
        m 4r_dateday01 "其实{w=0.3}我一直在期待……"
        m 4k_dateday01 "能像现在这样和你一起约会。"
        m 4j_dateday01 "而现在，这个愿望终于实现了。"
        
    else:
        m 3k_dateday01 "又来到商场了呢，[player]。"
        m 3j_dateday01 "每次和你一起来，感觉都很新鲜！"
    
    m 5b_dateday01 "那么，亲爱的……"
    
    menu:
        m "今天想带我去哪里呢？{fast}"
        "我想先听听你的想法":
            m 4d_dateday01 "让我来决定吗？"
            m 4l_dateday01 "嗯……每个地方看起来都很有趣。"
            m 5a_dateday01 "不过我相信你的选择……"
            m 5b_dateday01 "无论去哪里，只要是和你一起就很好。"
            
        "我已经有计划了":
            m 3b_dateday01 "真的吗？"
            m 3k_dateday01 "看来你准备了惊喜呢！"
            m 1k_dateday01 "我很期待哦～"
            
        "让我再想想":
            m 1d_dateday01 "正在考虑要去哪里吗？"
            m 1j_dateday01 "不用着急，我们可以慢慢决定。"
    
    m 3i_dateday01 "让我看看周围……"
    m 3k_dateday01 "似乎有很多有趣的地方呢。"
    m 3k_dateday01 "那么……"
    
    jump dateday_shop_choice

label dateday_shop_choice:
    menu:
        m "今天想带我去哪里呢？{fast}"
        "电影院":
            m 4d_dateday01 "电影院？"
            m 4l_dateday01 "话说回来，我还没有在电影院里看过电影呢。"
            m 3v_dateday01 "如果能和你一起看场电影……"
            m 3k_dateday01 "一定会是很特别的体验。"
            m 3l_dateday01 "不过可惜，今天好像没有合适的场次……"
            m 1k_dateday01 "我们下次再来看吧？"
            jump dateday_shop_choice
            
        "奶茶店":
            if persistent.Dateday_teamilk == 0:
                m 2b_dateday01 "奶茶店啊……"
                m 2k_dateday01 "我听说现在的年轻人都喜欢去那里。"
                m 2v_dateday01 "能和你一起体验这些……"
                m 4k_dateday01 "感觉会很开心！"
                jump dateday_teashop
            elif persistent.Dateday_teamilk == 1:
                m 4j_dateday01 "还想再喝奶茶吗？"
                m 4k_dateday01 "好的，不过要适量哦～"
                jump dateday_teashop
            elif persistent.Dateday_teamilk == 2:
                m 3s_dateday01 "[player]！你已经喝了两次了！"
                m 1s_dateday01 "喝太多对身体不好……"
                m "你真的还想再喝吗？"
                menu:
                    "是的":
                        m 3p_dateday01 "{w=0.5}.{w=0.5}.{w=0.5}."
                        m 3r_dateday01 "好吧，但这是最后一次了！"
                        jump dateday_teashop
                    "不了":
                        m 3k_dateday01 "好的，那我们去别处看看吧！"
                        jump dateday_shop_choice
            else:
                m 4l_dateday01 "啊啦～"
                m 4l_dateday01 "你已经喝了很多奶茶了！"
                m 1g_dateday01 "我真的会担心你的健康……"
                m 1j_dateday01 "我们还是先去别处转转吧～"
                jump dateday_shop_choice
            
        "女装店":
            m 4m_dateday01 "女装店……"
            m 4n_dateday01 "说实话，我有点紧张呢。"
            m 2v_dateday01 "不过如果是和你一起的话……"
            m 2l_dateday01 "我愿意试试看！"
            jump dateday_clothingshop
            
        "电玩厅":
            m 3b_dateday01 "电玩厅啊～"
            m 3a_dateday01 "看起来很有活力的地方。"
            m 4l_dateday01 "不过那里人好像有点多……"
            m 2l_dateday01 "我们还是先去别处转转吧～"
            jump dateday_shop_choice
            
        "再聊聊":
            m 4e_dateday01 "还想再聊一会儿吗？"
            
            menu:
                m 4b_dateday01 "想聊些什么呢？{fast}"
                "你觉得这里怎么样":
                    m 3r_dateday01 "嗯……{w=0.5}这里很热闹，充满生活气息……"
                    m 1t_dateday01 "最重要的是，能和你一起体验这些。"
                    m 1k_dateday01 "平凡的日常也变得特别起来。"
                    jump dateday_shop_choice
                    
                "你看起来很开心":
                    m 4l_dateday01 "这么明显吗？"
                    m 3j_dateday01 "可能……{w=0.5}是因为能和你在这样的地方约会……"
                    m 3j_dateday01 "是我一直期待的事情呢～"
                    jump dateday_shop_choice
                    
                "想和你一起静静的站一会":
                    m 4j_dateday01 "就这样安静地待在一起……"
                    m 4k_dateday01 "感觉也很美好。"
                    
                    play music dy_009 fadein 2.0
                    jump shop_quiet_moment
                    
        "返回":
            m 2d_dateday01 "想离开商场吗？"
            m 2a_dateday01 "好的，我们走吧。"
            scene dy_outdoor
            with dissolve
            play music dy_006 fadein 2.0
            show monika 4j_dateday01 zorder 12 at t11
            jump Dateday_start_0

label shop_quiet_moment:
    window hide
    hide monika
    # 计时器
    show screen touch_interceptor
    $ wait_time = renpy.random.randint(5, 15)
    $ ui.timer(wait_time, _jump="show_shop_comment")
    
    # 等待点击或计时器结束
    $ result = ui.interact(suppress_overlay=True, suppress_underlay=True)
    
    if result == "touch_interrupt":
        hide screen touch_interceptor
        window show
        show monika 4d_dateday01 at t11
        m 4d_dateday01 "[player]？"
        jump shop_quiet_choice

label show_shop_comment:
    hide screen touch_interceptor
    window show
    call monika_shop_comments from _call_monika_shop_comments
    window hide
    jump shop_quiet_moment

# 随机评论
label monika_shop_comments:
    $ comment = renpy.random.choice([
        "就这样和你静静地站着……感觉很安心。",
        "能听到你的呼吸声就好了呢……",
        "商场里的背景音乐很悦耳，但比不上你的声音。",
        "和你在一起的每一刻都很珍贵。",
        "真希望时间能慢一点……",
        "感受到你在身边，让我觉得很踏实。",
        "即使什么都不说，只要在你身边就很幸福。",
        "这个时刻，只属于我们两个人……"
    ])
    
    # 显示评论并设置自动消失时间（可中断）
    show screen touch_interceptor
    m "[comment]"
    $ ui.timer(3.0, _jump="end_shop_comment")
    
    $ result = ui.interact(suppress_overlay=True, suppress_underlay=True)
    
    if result == "touch_interrupt":
        hide screen touch_interceptor
        window show
        show monika 2a_dateday01 at t11
        m 2a_dateday01 "需要我做什么吗？"
        jump shop_quiet_choice

label end_shop_comment:
    hide screen touch_interceptor
    return

label shop_quiet_choice:
    menu:
        m "要继续这样静静地待着吗？{fast}"
        "再站一会":
            m 2j_dateday01 "好的，继续享受这宁静的时光吧～"
            
            jump shop_quiet_moment
            
        "不了，去别的地方吧":
            m 2j_dateday01 "感觉怎么样，[player]？"
            m 2k_dateday01 "和你一起度过的时光总是很美好..."
            jump dateday_shop_choice

screen touch_interceptor():
    zorder 100
    key "mouseup_1" action Return("touch_interrupt")  # 鼠标
    key "touch_up" action Return("touch_interrupt")   # 触摸屏
    key "K_SPACE" action Return("touch_interrupt")   # 空格键
    
    
    # 透明按钮覆盖整个屏幕
    button:
        xfill True
        yfill True
        background None
        action Return("touch_interrupt")
       
       
label dateday_teashop:
    $ persistent.Dateday_teamilk += 1
    
    scene dy_teashop
    with dissolve
    play music dy_009 fadein 2.0
    show monika 4b_dateday01 zorder 12 at t11
    
    if persistent.date_day_date_count == 1:
        m 4d_dateday01 "……[player]，这里就是奶茶店吗？"
        m 2j_dateday01 "比我想象中要温馨呢～"
    
        m 2e_dateday01 "你知道吗，以前……"
        m 2e_dateday01 "我只能通过图片来想象奶茶的味道。"
        m 2j_dateday01 "现在能亲自品尝，感觉很奇妙……"
    else:
        m 4j_dateday01 "又来到奶茶店了呢，[player]。"
        m 4v_dateday01 "每次闻到这里的香味，都会想起和你在一起的温暖时光～"
    
    # 随机讨论
    $ random_drink = renpy.random.choice([
        "pearl_milk_tea",
        "matcha_latte", 
        "fruit_tea",
        "taro_milk_tea",
        "cheese_foam_tea"
    ])
    
    call expression "teashop_discussion_" + random_drink
    
    m 4l_dateday01 "[player]……"
    pause 0.5
    
    jump dateday_teashop_choice

label teashop_discussion_pearl_milk_tea:
    m 4b_dateday01 "啊！是珍珠奶茶～"
    m 4k_dateday01 "那些珍珠在杯子里滚动，很有趣呢。"
    
    m 2j_dateday01 "我有点好奇这些珍珠的口感……"
    m 2k_dateday01 "会不会很有弹性呢？"
    
    m 1i_dateday01 "[player]，你知道吗……"
    m 1k_dateday01 "我觉得珍珠奶茶就像我们的关系～"
    m 1b_dateday01 "奶茶的甜代表着我们的日常……"
    m 2k_dateday01 "而珍珠就像那些特别的回忆，点缀其中。"
    
    menu:
        m "你觉得这个比喻怎么样？{fast}"
        "很贴切":
            m 4j_dateday01 "太好了！我就知道你能理解～"
            m 4k_dateday01 "我们的想法总是很接近呢！"
            
        "有点太诗意了":
            m 2l_dateday01 "啊啦～被你看出来了。"
            m 2j_dateday01 "我的诗人本性又显露出来了呢～"
            m 1a_dateday01 "不过，这就是真实的我。"
            
        "不太理解":
            m 4l_dateday01 "啊啦~"
            m 2j_dateday01 "没关系，能和你分享这些想法就很开心了～"
    
    m 2n_dateday01 "不过说实话……"
    m 2l_dateday01 "我有点担心会被珍珠呛到呢～"
    m 5a_dateday01 "到时候可要提醒我小心点哦，[player]！"
    return

label teashop_discussion_matcha_latte:
    m 4b_dateday01 "哇！是抹茶拿铁！"
    m 2k_dateday01 "这种绿色，让我想起了文学部窗外的景色……"
    
    m 2a_dateday01 "抹茶有一种独特的味道……"
    m 2b_dateday01 "苦中带甜，就像生活一样。"
    
    m 2b_dateday01 "但是和你在一起之后……"
    m 2k_dateday01 "我的生活就像这杯抹茶拿铁～"
    m 5b_dateday01 "即使偶尔有苦涩，也因为你而变得甜美。"
    
    menu:
        m "你觉得抹茶的颜色如何？{fast}"
        "很漂亮，让人平静":
            m 4a_dateday01 "嗯，这种绿色确实很治愈呢～"
            m 2k_dateday01 "看着它心情都会变好！"
            
        "给人一种宁静的感觉":
            m 1k_dateday01 "和我想的一样呢！"
            m 1a_dateday01 "静静地看着抹茶的颜色……"
            m 1l_dateday01 "感觉时间都慢下来了～"
    
    m 4b_dateday01 "你知道，为什么我最喜欢的颜色会是绿色吗？"
    m 4k_dateday01 "因为我的眼睛同样是绿色的！"
    m 2d_dateday01 "说起来……"
    m 2d_dateday01 "如果我喝了抹茶拿铁，会不会变得更温柔呢？"
    m 4j_dateday01 "开玩笑的啦～"
    return

label teashop_discussion_fruit_tea:
    m 4b_dateday01 "看看这杯水果茶！"
    m 3k_dateday01 "五彩缤纷的水果在里面漂浮，很漂亮呢。"
    
    m 3b_dateday01 "每种水果都有自己独特的味道……"
    m 3a_dateday01 "就像每个人都有自己独特的个性。"
    
    m 1k_dateday01 "但是当它们融合在一起……"
    m 1l_dateday01 "就创造出了一种和谐的美味～"
    m 4t_dateday01 "就像……{w=0.3}我们两个人，虽然不同却很合适"
    
    menu:
        m 2j_dateday01 "你最喜欢什么水果呢？{fast}"
        "草莓":
            m 2d_dateday01 "草莓！"
            m 2l_dateday01 "甜甜的红色，很可爱呢～"
            
        "芒果":
            m 2b_dateday01 "芒果啊……"
            m 2k_dateday01 "有种热带的风情，让人心情愉悦！"
            
        "橙子":
            m 4a_dateday01 "橙子……"
            m 2j_dateday01 "是明亮的颜色呢，让人感到温暖～"
    
    m 2v_dateday01 "不过说真的……"
    m 2v_dateday01 "我可能会想把水果捞出来尝尝呢～"
    m 2l_dateday01 "你不会笑话我吧，[player]？"
    return

label teashop_discussion_taro_milk_tea:
    m 4b_dateday01 "哇！这个紫色的奶茶……"
    m 4k_dateday01 "是香芋奶茶！"
    
    m 2j_dateday01 "这种柔和的紫色，让我想起了傍晚的天空……"
    m 2k_dateday01 "或者说，像我们第一次约会时的氛围？"
    
    m 1k_dateday01 "芋头的味道很特别……"
    m 1b_dateday01 "既不是纯粹的水果甜，也不是传统的茶香。"
    m 1t_dateday01 "就像我们的感情一样，独一无二～"
    
    menu:
        m 4a_dateday01 "你喜欢紫色吗？{fast}"
        "喜欢，很优雅":
            m 2k_dateday01 "太好了！"
            m 2j_dateday01 "看来我们的审美很一致呢～"
            
        "不太确定":
            m 2l_dateday01 "啊，没关系……"
            m 2l_dateday01 "每个人都有自己的偏好嘛～"
            m 1k_dateday01 "重要的是我们能互相理解。"
    
    m 2b_dateday01 "说起来……"
    m 2k_dateday01 "如果我喝了芋头奶茶，会不会也会变成紫色呢？"
    m 2j_dateday01 "开个玩笑啦～"
    return

label teashop_discussion_cheese_foam_tea:
    m 4d_dateday01 "看看这个芝士奶盖茶！"
    m 4j_dateday01 "上面的奶盖像云朵一样，很可爱呢。"
    
    m 2k_dateday01 "咸甜的奶盖和清香的茶底……"
    m 2j_dateday01 "这种组合很特别。"
    
    m 2b_dateday01 "你知道吗……"
    m 2b_dateday01 "喝这种茶需要一点技巧哦～"
    m 2a_dateday01 "要先品尝奶盖的浓郁，再感受茶底的清爽……"
    m 2k_dateday01 "就像我们相处的每一天，有甜蜜也有平淡，但都很珍贵。"
    
    menu:
        m "你觉得这种咸甜组合如何？{fast}"
        "很有趣的组合":
            m 2b_dateday01 "对吧！"
            m 2t_dateday01 "就像我们一样，看似不同却很相配～"
            
        "只是有点特别":
            m 4l_dateday01 "嗯……需要一点时间来适应呢。"
            m 2l_dateday01 "不过尝试新事物也是约会的乐趣之一嘛～"
    
    m 5a_dateday01 "不过说实话……"
    m 5a_dateday01 "我有点担心奶盖会沾到脸上呢～"
    m 5b_dateday01 "到时候可要提醒我哦，[player]！"
    return

label dateday_teashop_choice:
    m 4l_dateday01 "说了这么多，我也有点渴了呢～"
    m 4k_dateday01 "那么{w=0.3}.{w=0.3}.{w=0.3}."
    menu:
        m 2t_dateday01 "今天你想品尝什么样的奶茶呢？{fast}"
        "经典珍珠奶茶":
            m 4d_dateday01 "珍珠奶茶！"
            m 2b_dateday01 "很经典的选择呢。"
            m 2a_dateday01 "和你一起分享第一杯珍珠奶茶……"
            m 2j_dateday01 "一定会是很特别的回忆～"
            $ chosen_drink = "pearl_milk_tea"
            jump dateday_teashop_cg
            
        "抹茶拿铁":
            m 4b_dateday01 "抹茶拿铁……"
            m 4k_dateday01 "啊~原来你也喜欢这个颜色呢~"
            m 2j_dateday01 "谢谢你能考虑到我的喜好……"
            $ chosen_drink = "matcha_latte"
            jump dateday_teashop_cg
            
        "水果茶":
            m 4b_dateday01 "水果茶啊……"
            m 4k_dateday01 "你该不会是想让我尝尝各种水果吧？"
            m 2t_dateday01 "听起来很有趣呢！"
            $ chosen_drink = "fruit_tea"
            jump dateday_teashop_cg
            
        "芋头奶茶":
            m 4b_dateday01 "芋头奶茶！"
            m 2k_dateday01 "那种温柔的紫色很漂亮呢～"
            m 2k_dateday01 "我很期待品尝它的味道！"
            $ chosen_drink = "taro_milk_tea"
            jump dateday_teashop_cg
            
        "芝士奶盖茶":
            m 4b_dateday01 "芝士奶盖茶！"
            m 2k_dateday01 "上面的奶盖看起来很有趣～"
            m 2k_dateday01 "让我们一起试试这个特别的组合吧！"
            $ chosen_drink = "cheese_foam_tea"
            jump dateday_teashop_cg

label dateday_teashop_cg:
    play music dy_008 fadein 2.0
    hide monika
    if chosen_drink == "pearl_milk_tea":
        call dateday_teashop_cg_pearl from _call_dateday_teashop_cg_pearl
    elif chosen_drink == "matcha_latte":
        call dateday_teashop_cg_matcha from _call_dateday_teashop_cg_matcha
    elif chosen_drink == "fruit_tea":
        call dateday_teashop_cg_fruit from _call_dateday_teashop_cg_fruit
    elif chosen_drink == "taro_milk_tea":
        call dateday_teashop_cg_taro from _call_dateday_teashop_cg_taro
    elif chosen_drink == "cheese_foam_tea":
        call dateday_teashop_cg_cheese from _call_dateday_teashop_cg_cheese
        
    play music dy_009 fadein 2.0
    scene dy_teashop with Dissolve(2.0)
    show monika 4j_dateday01 zorder 12 at t11
    with dissolve
    m 2j_dateday01 "今天真的很开心呢，[player]～"
    m 2k_dateday01 "谢谢你带我来体验这么美好的事物。"
    m 5b_dateday01 "我们下次再来{w=0.5}好吗？"
    
    scene dy_shop
    with dissolve
    play music dy_007 fadein 2.0
    pause 1.0
    show monika 4a_dateday01 zorder 12 at t11
    with dissolve
    
    m 1a_dateday01 "那么，接下来想去哪里呢？"
    jump dateday_shop_choice


label dateday_teashop_cg_pearl:
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    if persistent.Dateday_pearl_first:
        m "哇！这就是传说中的珍珠奶茶吗？"
        m "看起来比我在网上看到的图片还要诱人呢～"
        m "你知道吗，在文学部独处的时候……"
        m "我经常看到年轻人们在社交媒体上分享奶茶的照片。"
        m "那时候我就在想，如果有一天能和你一起品尝该多好。"
        m "[player]，这就像梦想成真一样……"
        m "那些只能在屏幕另一端羡慕的场景，现在我也能亲身体验了。"
        m "而且最重要的是……"
        m "是和你一起分享这个特别的第一次。"
        $ persistent.Dateday_pearl_first = False
    else:
        m "又选择了我们最爱的珍珠奶茶呢～"
        m "看来我们都对这个经典口味有着特别的偏爱！"
        m "每次看到这些黑色的珍珠在杯底轻轻滚动……"
        m "都会让我想起我们第一次来这里时的那种新奇与期待。"
        m "时间在流逝，但有些感觉却越来越深刻……"
        m "比如和你在一起的安心感，还有分享奶茶时的甜蜜。"
        m "说起来……"
        m "你还记得我们第一次来这里时我说了什么吗？"
        m "我说这些珍珠像在跳圆舞曲呢～"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "光是捧着这杯温暖的奶茶……"
        m "手心传来的温度就让我感到无比安心。"
        m "这种简单而真实的触感……"
        m "让我确信这一切都不是梦。"
        m "你真的就在我身边。"
    else:
        m "熟悉的手感……"
        m "熟悉的温度……"
        m "熟悉的幸福感……"
        m "每次捧着这杯奶茶……"
        m "都像是握住了我们共同的回忆。"
        m "那些点点滴滴，都变得如此珍贵。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "看看这些小珍珠～"
    m "它们像不像在杯子里跳着优雅的华尔兹？"
    m "我突然想到一个很有趣的想象……"
    m "如果这些珍珠有自己的思想，它们会怎么看待我们呢？"
    
    menu:
        m "你觉得呢，[player]？{fast}"
        "可能在祝福我们":
            m "诶？那样的话……"
            m "它们会不会是我们在奶茶世界里的小小见证者？"
            m "啊，我的想象力是不是太丰富了～"
        "可能在开庆祝会":
            m "庆祝会吗？"
            m "那它们一定是今天最快乐的小珍珠了～"
            m "因为有我们陪着它们一起创造美好回忆。"
        "可能在安静观察":
            m "安静地观察着我们的幸福……"
            m "就像我们现在这样，享受着宁静而珍贵的二人时光。"
            m "感觉这样温馨的画面也很美好呢。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "第一次和你分享奶茶的体验……"
        m "比我想象的还要美好千百倍。"
        m "在文学部独自一人的那些日夜……"
        m "我常常对着屏幕想象这样的场景。"
        m "但真实的感受，远比想象更加温暖。"
    else:
        m "又一次和你分享奶茶的温暖……"
        m "每一次都让我更加确信自己的选择。"
        m "这些看似平凡的日常瞬间……"
        m "却是构成我们爱情的最美篇章。"
        m "每一个细节都值得被永远珍藏。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "[player]，我刚刚又想到了一个比喻……"
    m "你觉得这杯珍珠奶茶像不像我们爱情的缩影？"
    m "奶茶本身的甜美，就像我们在一起时的快乐时光……"
    m "而这些珍珠，就像我们共同创造的每一个特别回忆……"
    m "它们点缀在日常的甜蜜中，让每一口都有惊喜。"
    
    if persistent.Dateday_teamilk == 1:
        m "啊，我是不是又在用过于诗意的比喻了？"
        m "抱歉抱歉，一遇到美好的事物，我的作家本性就控制不住了～"
    else:
        m "看来我的比喻风格还是一如既往地充满诗意呢……"
        m "不过你应该已经习惯我这种表达方式了吧？"
        m "毕竟，这就是真实的我啊。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    m "真希望时间能走得慢一点……"
    
    if persistent.Dateday_teamilk == 1:
        m "让这一刻的幸福感停留得更久一些。"
        m "让我能好好品味这份初次的甜蜜。"
        m "把每一个细节都深深印在心底。"
    else:
        m "让这份熟悉的温暖持续得更久一些。"
        m "让我能好好珍藏这份历久弥新的美好。"
        m "每一次重复，都让感情更加深厚。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "说起来……"
    m "你觉得我捧着奶茶的样子看起来怎么样？"
    
    menu:
        m "会不会显得有点笨拙？{fast}"
        "很可爱":
            m "[player]！"
            m "这么直白的夸奖会让人心跳加速的……"
            m "不过……听到你这么说，我真的很开心。"
        "很有文艺气息":
            m "啊啦～又被你看穿了呢。"
            m "看来我的文学少女气质还是很明显的嘛。"
            m "不过在你面前，我想要展现最真实、最放松的自己。"
        "看起来非常幸福":
            m "因为和你在一起啊～"
            m "能和你分享这些看似普通却珍贵的日常……"
            m "就是我此生最大的幸福。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "今天的一切……"
        m "从进入奶茶店的那一刻起……"
        m "到捧着这杯温暖的奶茶……"
        m "每一个瞬间，我都会深深记在心里。"
        m "和你一起的第一次奶茶店约会……"
        m "将成为我人生故事中最美的章节之一。"
    else:
        m "又一次美好的共同回忆……"
        m "又一次心灵的温暖交流……"
        m "又一次感情的甜蜜加深……"
        m "和你分享的每一杯奶茶……"
        m "都在我们共同的故事书中添上新的一页。"
        m "让我们的爱情故事更加丰富多彩、感人至深。"
    
    hide dy_cg_1a
    hide dy_cg_1
    with dissolve
    pause 2.0
    return

label dateday_teashop_cg_matcha:
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    if persistent.Dateday_matcha_first:
        m "抹茶拿铁的绿色真是太美了！"
        m "这种温柔的绿色，让我想起了文学部窗外那片初夏的树叶……"
        m "你知道吗，抹茶有着深厚的文化底蕴……"
        m "就像一首优美的诗歌，需要静下心来细细品味。"
        m "每一口都能感受到历史的沉淀和匠心的传承。"
        m "而现在，我能和你一起品味这份传统之美……"
        m "感觉像是跨越了时空的浪漫。"
        $ persistent.Dateday_matcha_first = False
    else:
        m "又选择抹茶拿铁了呢～"
        m "这个宁静的绿色总是能瞬间抚平我的心绪。"
        m "每次看到这个温柔的颜色……"
        m "都会想起我们在这里度过的那些宁静而美好的时光。"
        m "有些颜色会随着时间褪色……"
        m "但这个绿色，每次看到都让我感到同样的安心和温暖。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "这种温柔的绿色……"
        m "就像你给我的理解和包容。"
        m "平静中带着深沉的温暖……"
        m "细腻中蕴含着无限温柔。"
        m "就像我们之间的感情，不需要太多言语。"
    else:
        m "熟悉的绿色……"
        m "熟悉的感觉……"
        m "熟悉的安心……"
        m "每次看到这个颜色……"
        m "都让我想起你给予我的那份不变的理解和支持。"
        m "就像这个颜色一样，始终如一。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "[player]，在你眼中，抹茶的颜色让你联想到什么？"
    
    menu:
        m "我很想听听你的感受～{fast}"
        "像初春的新叶":
            m "和我的想法不谋而合呢！"
            m "充满生机和希望，就像我们对未来的憧憬。"
        "像宁静的湖面":
            m "很诗意的比喻……"
            m "平静而深邃，让人感到心灵的安宁。"
            m "就像和你在一起时的那种踏实感。"
        "像你的气质":
            m "[player]！"
            m "这种联想太让人害羞了……"
            m "不过……我很开心你在我们之间找到这样的联系。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    m "在日本茶道中，有一个概念叫'一期一会'……"
    
    if persistent.Dateday_teamilk == 1:
        m "意思是珍惜每一次相遇的独特性……"
        m "因为每一次都是独一无二、无法重来的。"
        m "就像我珍惜与你的每一次相处，每一个瞬间。"
    else:
        m "即使是看似重复的体验……"
        m "因为发生在不同的时间，与不同心境下的我们……"
        m "所以每一次也都有着独特的意义。"
        m "因为每次都是和你一起创造回忆……"
        m "所以每次都值得被好好珍惜和铭记。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "说起来……"
    m "如果我经常品味抹茶，会不会也感染上它的宁静气质呢？"
    m "啊，这只是个天真的想法啦～"
    m "不过这种宁静的颜色确实有种魔力，能让人心情变得平和呢！"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "第一次体验抹茶的深邃风味……"
        m "因为有你在身边分享而变得意义非凡。"
        m "这个瞬间，将永远留在我的记忆里。"
    else:
        m "又一次品味抹茶的宁静韵味……"
        m "又一次感受有你在身边的幸福安心。"
        m "每一次重复，都让这份感情更加醇厚。"
    
    hide dy_cg_1a
    hide dy_cg_1b
    with dissolve
    pause 2.0
    return

label dateday_teashop_cg_fruit:
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    if persistent.Dateday_fruit_first:
        m "哇！水果茶的颜色真是太鲜艳了！"
        m "像一个小小的水果乐园在杯子里欢快舞动～"
        m "每种水果都有自己独特的颜色、形状和味道……"
        m "就像世界上每个人都有自己独特的个性和魅力。"
        m "但当它们融合在一起，却能创造出和谐的美味。"
        m "这让我想到了我们……"
        m "虽然来自不同的世界，却因为爱而变得如此契合。"
        $ persistent.Dateday_fruit_first = False
    else:
        m "又选择水果茶了呢～"
        m "这种多彩的颜色总是能瞬间点亮我的心情！"
        m "看着这些水果在茶中轻盈漂浮……"
        m "就像看到我们共同经历的丰富多彩的回忆在眼前重现。"
        m "有些味道会随着时间变淡……"
        m "但这种多彩的视觉盛宴，每次看到都让我感到同样的愉悦。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "多彩的水果……"
        m "多彩的生活……"
        m "多彩的爱情……"
        m "自从有你走入我的世界……"
        m "原本单调的生活变得像这杯水果茶一样丰富多彩。"
        m "每一个日子都充满了新的惊喜和期待。"
    else:
        m "熟悉的多彩……"
        m "熟悉的清新……"
        m "熟悉的幸福感……"
        m "每次看到这些鲜艳的水果……"
        m "都让我感恩有你的每一天。"
        m "是你让我的世界变得如此绚烂。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "[player]，在这些水果中，你最喜欢哪一种？"
    
    menu:
        m "我想更了解你的喜好～{fast}"
        "草莓":
            m "草莓！"
            m "那种心形的可爱模样和甜甜的味道，就像初恋的感觉呢～"
        "橙子":
            m "橙子啊……"
            m "明亮的颜色就像阳光一样，能驱散所有的阴霾！"
        "芒果":
            m "芒果……"
            m "热情的颜色和香甜的味道，就像你对我的真挚心意。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    m "不同水果的完美融合……"
    
    if persistent.Dateday_teamilk == 1:
        m "创造出和谐而丰富的口感……"
        m "就像我们的相遇，看似来自不同世界……"
        m "却因为爱而变得如此合适和完美。"
    else:
        m "创造出熟悉而美好的味道……"
        m "就像我们的相处，自然而和谐……"
        m "每一次交流都让感情更加深厚。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "看着这些色彩缤纷的水果……"
    m "感觉它们在杯子里举办一场热闹的嘉年华呢！"
    m "如果它们真的有生命……"
    m "会不会在争论谁的颜色最漂亮、谁的味道最甜美？"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "第一次体验水果茶的清新活力……"
        m "因为有你在身边分享而变得终生难忘。"
        m "这个多彩的瞬间，将永远鲜艳在我的记忆中。"
    else:
        m "又一次感受水果茶的清新活力……"
        m "又一次感恩有你的温暖陪伴。"
        m "每一次重复，都让我们的爱情更加鲜活。"
    
    hide dy_cg_1a
    hide dy_cg_1b
    with dissolve
    pause 2.0
    return

label dateday_teashop_cg_taro:
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    if persistent.Dateday_taro_first:
        m "哇！这个紫色真是太特别了！"
        m "香芋奶茶啊……"
        m "这种温柔的紫色，让我想起了傍晚时分天边的晚霞……"
        m "或者说，更像我们第一次约会时那种温馨而浪漫的氛围？"
        m "神秘中带着温柔，含蓄中蕴含深情。"
        m "紫色在色彩心理学中代表灵性和直觉……"
        m "也许这就是为什么一看到这个颜色，就让我想到我们之间那种难以言喻的默契。"
        $ persistent.Dateday_taro_first = False
    else:
        m "又选择芋头奶茶了呢～"
        m "这种温柔的紫色总是能瞬间让我感到内心的平静！"
        m "每次看到这个神秘而温柔的颜色……"
        m "都会想起我们在这里度过的那些温馨而深刻的时刻。"
        m "有些颜色会随着潮流改变……"
        m "但这个紫色，每次看到都让我感到同样的安心和温暖。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "温柔的紫色……"
        m "温柔的感情……"
        m "温柔的你……"
        m "就像我对你的心意……"
        m "虽然不常挂在嘴边，却深沉而真挚。"
        m "每一个细节都用心经营，每一份感情都真诚以待。"
    else:
        m "熟悉的紫色……"
        m "熟悉的温暖……"
        m "熟悉的安心感……"
        m "每次看到这个颜色……"
        m "都让我想起你给我的那种不变的安全感。"
        m "就像这个颜色一样，始终温柔地守护着我。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "[player]，你对紫色有什么特别的感受吗？"
    
    menu:
        m "我很想知道你对这个颜色的看法～{fast}"
        "喜欢，感觉很优雅":
            m "太好了！"
            m "看来我们在审美上也有很多共同点呢～"
        "不太确定":
            m "啊，没关系……"
            m "每个人对颜色都有自己独特的感受和偏好嘛～"
            m "重要的是我们能互相理解和尊重彼此的差异。"
        "感觉很神秘浪漫":
            m "紫色确实有一种神秘而浪漫的气质……"
            m "就像爱情一样，需要用心去探索和体会其中的深意。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    m "芋头的味道很特别……"
    
    if persistent.Dateday_teamilk == 1:
        m "既不是纯粹的水果甜，也不是传统的茶香……"
        m "而是一种独特而温暖的味道。"
        m "就像我们的感情一样，独一无二、无可替代。"
    else:
        m "既熟悉又特别……"
        m "既温暖又安心……"
        m "就像我们的日常，平凡中蕴含着珍贵的幸福。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "说起来……"
    m "如果我经常喝芋头奶茶，会不会也感染上它的温柔气质呢？"
    m "啊，这只是个异想天开的想法啦～"
    m "不过这个颜色真的很美，有种让人心情平静的魔力呢！"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "第一次体验芋头的独特风味……"
        m "因为有你在身边分享而变得意义非凡。"
        m "这个温柔的瞬间，将永远珍藏在我的心底。"
    else:
        m "又一次感受芋头的温暖味道……"
        m "又一次感恩有你的每一天。"
        m "每一次重复，都让我们的感情更加深厚温柔。"
    
    hide dy_cg_1a
    hide dy_cg_1b
    with dissolve
    pause 2.0
    return

label dateday_teashop_cg_cheese:
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    if persistent.Dateday_cheese_first:
        m "哇！芝士奶盖茶的分层真是太漂亮了！"
        m "上面的奶盖像柔软的云朵一样，让人忍不住想触摸～"
        m "咸甜的奶盖和清香的茶底……"
        m "这种看似对立却又和谐的组合真的很特别。"
        m "就像诗歌中的对比修辞，通过反差创造出独特的美感。"
        m "这让我想到了我们之间的关系……"
        m "虽然来自不同的世界，却因为爱而找到了完美的平衡。"
        $ persistent.Dateday_cheese_first = False
    else:
        m "又选择芝士奶盖茶了呢～"
        m "这种特别的口感和视觉享受总是让人难忘！"
        m "每次看到这个精致的分层……"
        m "都会想起我们第一次尝试时的惊喜和感动。"
        m "有些体验会随着重复而变得平淡……"
        m "但这种独特的分层，每次看到都让我感到同样的新奇和愉悦。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "精致的层次……"
        m "精致的感情……"
        m "精致的瞬间……"
        m "就像我对你的心意……"
        m "层层叠叠，丰富而真挚。"
        m "每一个层面都用心经营，每一份感情都真诚以待。"
    else:
        m "熟悉的层次……"
        m "熟悉的特别……"
        m "熟悉的感动……"
        m "每次看到这个精致的分层……"
        m "都让我想起我们感情的深度和丰富。"
        m "就像这杯茶一样，每一层都有独特的风味。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "[player]，你对这种咸甜结合的独特口感有什么看法？"
    
    menu:
        m "我很想听听你的感受～{fast}"
        "很有趣的组合":
            m "对吧！"
            m "就像我们一样，看似来自不同世界，却意外地相配～"
        "确实需要适应":
            m "嗯……确实需要一点时间来适应这种独特的口感呢。"
            m "不过尝试新事物、接受差异，也是爱情的美好之处嘛～"
        "很新奇特别":
            m "新奇的事物……"
            m "特别的体验……"
            m "就像我们的相遇，独特而美好，值得永远珍惜。"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
    
    m "……"
    m "品尝这种茶需要特别的技巧……"
    
    if persistent.Dateday_teamilk == 1:
        m "就像经营感情需要用心和理解……"
        m "每一层都有独特的韵味，需要细细品味。"
        m "不能急于求成，而要享受整个过程。"
    else:
        m "就像维持感情需要耐心和包容……"
        m "每一口都有不同的感受，需要用心体会。"
        m "在重复中寻找新意，在熟悉中发现美好。"
    
    scene dy_cg_1b zorder 13 with Dissolve(2.0)
    
    m "看着这个精致的分层……"
    m "感觉像在欣赏一件精心创作的艺术品呢！"
    m "如果奶盖有意识……"
    m "它会不会为自己的独特美丽而感到自豪？"
    
    scene dy_cg_1a zorder 13 with Dissolve(2.0)
   
    
    m "……"
    if persistent.Dateday_teamilk == 1:
        m "第一次体验芝士奶盖的独特风味……"
        m "因为有你在身边分享而变得终生难忘。"
        m "这个特别的瞬间，将永远铭刻在我的记忆中。"
    else:
        m "又一次感受芝士奶盖的特别口感……"
        m "又一次感恩有你的温暖陪伴。"
        m "每一次重复，都让我们的爱情更加独特而珍贵。"
    
    hide dy_cg_1a
    hide dy_cg_1b
    with dissolve
    pause 2.0
    return
    

label dateday_clothingshop:
    $ persistent.Dateday_clothingshop += 1
    
    scene dy_clothingshop
    with dissolve
    play music dy_009 fadein 2.0
    show monika 3a_dateday01 zorder 12 at t11
    
    if persistent.Dateday_clothingshop == 1:
        m 3b_dateday01 "哦...{w=0.5}这里就是商场里的服装店啊。"
        m 3k_dateday01 "比我想象中要明亮整洁呢。"
        m 4l_dateday01 "说实话...{w=0.3}我有点紧张。"
        m 4l_dateday01 "在俱乐部的时候，我从来不需要考虑穿校服以外的衣服。"
        m 4l_dateday01 "但现在..."
        m 1b_dateday01 "能和你一起挑选衣服，感觉很有意义。"
        
        m 2l_dateday01 "你知道吗？"
        m 2l_dateday01 "我以前只能在书中读到这样的场景。"
        m 2j_dateday01 "现在能亲身体验，感觉很奇妙。"
    else:
        m 4j_dateday01 "啊，又回到服装店了。"
        m 2k_dateday01 "和你一起来这里总是很愉快～"
        m 2k_dateday01 "每次都能发现新的乐趣。"
        
        m 2a_dateday01 "比起第一次..."
        m 2b_dateday01 "我感觉更自在了。"
        m 2a_dateday01 "也许是因为有你在身边的缘故……"
    m 2b_dateday01 "能和你一起体验这些日常小事..."
    m 2k_dateday01 "让我感到很幸福。"
    
    m 2b_dateday01 "让我看看周围..."
    pause 1.0
    m 2a_dateday01 "这里的陈列很有条理，按风格和颜色分类得很清楚。"
    
    m 4v_dateday01 "其实..."
    m 4v_dateday01 "我注意到几件不错的衣服。"
    m 2j_dateday01 "如果你想看的话，我可以试穿一下。"
    
    jump dateday_clothingshop_dress_choice

label dateday_clothingshop_dress_choice:
    menu:
        m "你想看我试穿哪一件呢？{fast}"
        "蓝色水手服":
            if persistent.Dateday_sailor_worn > 0:
                m 4d_dateday01 "啊，这件水手服..."
                if persistent.Dateday_sailor_worn == 1:
                    m 2b_dateday01 "我记得上次穿过一次呢。"
                    m 2l_dateday01 "那种学院风的感觉还挺新鲜的。"
                else:
                    m 2k_dateday01 "我们已经穿过好几次了。"
                    m 2l_dateday01 "感觉越来越熟悉这种风格了。"
                m 3t_dateday01 "你想再看我穿一次吗？"
                menu:
                    "是的，我想再看一次":
                        m 3b_dateday01 "好啊～"
                        m 3k_dateday01 "既然你喜欢，我很乐意再穿给你看。"
                    "不用了，看看别的":
                        m 4b_dateday01 "好吧。"
                        m 4a_dateday01 "那我们看看其他款式吧。"
                        jump dateday_clothingshop_dress_choice
            else:
                m 4l_dateday01 "这件水手服吗？"
                m 4n_dateday01 "设计很经典呢..."
                m 2n_dateday01 "让我想起了那些描写校园生活的文学作品。"
                m 2l_dateday01 "不过……{w=0.5}这种风格对我来说可能有点太可爱了？"
                m 2k_dateday01 "但既然你想看，我很乐意试试。"
            jump dateday_clothingshop_sailor
            
        "浅蓝色休闲套装":
            if persistent.Dateday_casual_worn > 0:
                m 4d_dateday01 "这套休闲装..."
                if persistent.Dateday_casual_worn == 1:
                    m 2b_dateday01 "上次穿感觉很舒适呢。"
                else:
                    m 2a_dateday01 "已经穿过好几次了。"
                    m 2j_dateday01 "就像老朋友一样熟悉了呢~"
                m 2b_dateday01 "想看我再穿一次吗？"
                menu:
                    "是的，很适合日常穿着":
                        m 3a_dateday01 "好啊～"
                        m 3b_dateday01 "这种休闲风格确实很适合平时的我。"
                    "不用了，看看别的":
                        m 4a_dateday01 "好的。"
                        m 4j_dateday01 "那我们看看其他款式吧。"
                        jump dateday_clothingshop_dress_choice
            else:
                m 3a_dateday01 "这套休闲装看起来很舒适呢。"
                m 1b_dateday01 "浅蓝色的搭配很清新。"
                m 1k_dateday01 "感觉比另外两件要日常一些。"
                m 1s_dateday01 "应该会比较容易驾驭。"
            jump dateday_clothingshop_casual
            
        "白色丝绸吊带裙":
            if persistent.Dateday_dress_worn > 0:
                m 4b_dateday01 "这条白色丝绸裙子..."
                if persistent.Dateday_dress_worn == 1:
                    m 3k_dateday01 "我们上次试过呢。"
                    m 1k_dateday01 "丝绸的触感真的很特别。"
                else:
                    m 4a_dateday01 "已经穿过好几次了。"
                    m 4j_dateday01 "感觉越来越熟悉这种优雅的风格了。"
                m 2v_dateday01 "你还想看我穿吗？"
                menu:
                    "是的，请再穿一次":
                        m 2k_dateday01 "当然可以～"
                        m 2t_dateday01 "能让你开心，我很愿意。"
                    "不用了，换一件吧":
                        m 4a_dateday01 "好的。"
                        m 4b_dateday01 "我们看看其他的吧。"
                        jump dateday_clothingshop_dress_choice
            else:
                m 4v_dateday01 "这条裙子..."
                m 2n_dateday01 "丝绸的质感和光泽都很美。"
                m 2l_dateday01 "只是设计可能有点大胆..."
                m 2v_dateday01 "说实话，我有点害羞。"
                m 4k_dateday01 "但为了你，我愿意尝试。"
            jump dateday_clothingshop_dress
            
        "再逛逛看":
            m 4d_dateday01 "想多看看吗？"
            m 2b_dateday01 "好啊，我很享受和你一起的时光。"
            
            
            if persistent.Dateday_clothingshop == 1:
                m 2l_dateday01 "说实话，我还在熟悉这里的氛围..."
                m 2a_dateday01 "多逛逛也能让我更放松一些。"
            else:
                m 2b_dateday01 "每次来都能发现新的细节。"
                m 2k_dateday01 "和你一起探索总是很有趣。"
                
            m 2a_dateday01 "每个瞬间都很珍贵。"
            jump dateday_clothingshop_more
            
        "离开这里":
            m 2d_dateday01 "想走了吗？"
            
            if persistent.Dateday_clothingshop == 1:
                m 2b_dateday01 "第一次来服装店，感觉怎么样？"
                m 2k_dateday01 "我很感谢你带我来体验这些。"
            else:
                m 2k_dateday01 "今天试衣服开心吗？"
                m 2b_dateday01 "我每次都很享受和你一起的时光。"
                
            m 2a_dateday01 "我们走吧。"
            m 4j_dateday01 "和你一起真的很开心。"
            scene dy_shop
            with dissolve
            play music dy_007 fadein 2.0
            pause 1.0
            show monika 4a_dateday01 zorder 12 at t11
            with dissolve
            jump dateday_shop_choice

label dateday_clothingshop_sailor:
    $ persistent.Dateday_sailor_worn += 1
    hide monika
    pause 3.0
    show monika 3d_dateday04 zorder 12 at t11
    with dissolve
    
    if persistent.Dateday_sailor_worn == 1:
        m 3d_dateday04 "嗯...{w=0.5}这件水手服的领口设计很特别。"
        m 3j_dateday04 "灯笼袖的褶皱也很可爱。"
        
        m 3j_dateday04 "这种学院风格..."
        m 3k_dateday04 "让我想起那些描写校园生活的青春小说。"
        m 3l_dateday04 "不过说实话，可能不太适合平时的我。"
        
        m 3n_dateday04 "这些蓝色的条纹和蝴蝶结..."
        m 3v_dateday04 "感觉有点过于可爱了。"
    else:
        m 5a_dateday04 "又穿上这件水手服了。"
        if persistent.Dateday_sailor_worn == 2:
            m 5b_dateday04 "第二次穿感觉熟悉一些了。"
            m 3l_dateday04 "虽然还是不太习惯这种风格..."
            m 3a_dateday04 "但至少不会那么紧张了。"
        else:
            m 5a_dateday04 "已经穿这么多次了，感觉很自然了。"
            m 5b_dateday04 "甚至开始欣赏这种风格的青春活力。"
    
    menu:
        m "你觉得怎么样？{fast}"
        "很可爱":
            m 7a_dateday04 "啊..."
            m 7b_dateday04 "可爱什么的..."
            if persistent.Dateday_sailor_worn == 1:
                m 7c_dateday04 "第一次听到这样的评价，有点不好意思。"
            else:
                m 7c_dateday04 "每次听你这么说都会心跳加速呢。"
            m 7a_dateday04 "虽然不太习惯，但……{w=0.3}听到你这么说我很开心。"
            
        "这种青春风格很适合你":
            m 3k_dateday04 "真的吗？"
            if persistent.Dateday_sailor_worn == 1:
                m 5a_dateday04 "看来偶尔尝试不同风格也不错。"
            else:
                m 5b_dateday04 "看来你很喜欢这种青春的风格呢。"
            m 5b_dateday04 "能让你看到不一样的我，我很高兴。"
            
        "很美，但不太像平时的你":
            m 3n_dateday04 "嗯..."
            m 3l_dateday04 "我也觉得平时的自己更自然。"
            if persistent.Dateday_sailor_worn == 1:
                m 3b_dateday04 "不过尝试新事物也是约会的乐趣之一。"
            else:
                m 3b_dateday04 "但偶尔换个风格也挺有趣的，对吧？"


    if persistent.Dateday_sailor_worn == 1:
        m 7c_dateday04 "在文学部时，我的形象是固定的。"
        m "就像被设定好的角色一样。"
        m 7b_dateday04 "但现在..."
        m 7c_dateday04 "我可以自由地探索不同的自己。"
        m "这种感觉很奇妙。"
    else:
        m 3v_dateday04 "每次穿这件衣服..."
        m "都会让我想起我们第一次在这里的约会。"
        m 3j_dateday04 "那些珍贵的回忆..."
        m 3k_dateday04 "让这件衣服变得特别起来。"

    m 3j_dateday04 "你知道吗..."
    m 3k_dateday04 "也许下次约会的时候..."
    m 3b_dateday04 "我就可以穿着这件衣服呢～"
    
    if persistent.Dateday_sailor_worn == 1:
        m 3v_dateday04 "虽然可能需要一点勇气..."
        m 3k_dateday04 "但为了你，我愿意尝试。"
    else:
        m 3v_dateday04 "现在穿起来感觉自然多了。"
        m 3l_dateday04 "应该不会太奇怪吧？"
    
    m 5b_dateday04 "那样一定会是很特别的回忆。"
    hide monika
    with dissolve
    pause 3.0
    show monika 4a_dateday01 zorder 12 at t11
    with dissolve
    
    m 4a_dateday01 "那么，还想看其他衣服吗？"
    m 3k_dateday01 "或者...你已经找到最喜欢的了？"
    jump dateday_clothingshop_dress_choice

label dateday_clothingshop_casual:
    $ persistent.Dateday_casual_worn += 1
    hide monika
    pause 3.0
    show monika 6a_dateday03 zorder 12 at t11
    with dissolve
    m "哒哒~"
    m "我穿好了！"
    if persistent.Dateday_casual_worn == 1:
        m 3j_dateday03 "这套休闲装..."
        m 3j_dateday03 "穿起来比想象中要舒服。"
        
        m 3a_dateday03 "浅蓝色和白色的搭配..."
        m 3a_dateday03 "感觉很清新自然。"
        m 3b_dateday03 "没有另外两件那么夸张。"
        
        m 3a_dateday03 "这种日常风格..."
        m 3j_dateday03 "可能更适合平时的我。"
        m 3j_dateday03 "不会让人觉得太刻意。"
    else:
        m 3j_dateday03 "又穿上这套休闲装了呢~"
        if persistent.Dateday_casual_worn == 2:
            m 3b_dateday03 "第二次穿感觉更自在了。"
            m 3k_dateday03 "就像穿自己的衣服一样自然。"
        else:
            m 3b_dateday03 "已经穿这么多次了，就像量身定制一样。"
            m 3j_dateday03 "也许这就是最适合我的风格？"
    
    menu:
        m 5a_dateday03 "你觉得怎么样？{fast}"
        "很清新，很适合你":
            m 5b_dateday03 "谢谢..."
            if persistent.Dateday_casual_worn == 1:
                m 5b_dateday03 "这种日常风格确实让我比较放松。"
            else:
                m 5b_dateday03 "看来我们都喜欢这种自然的风格。"
            m 5b_dateday03 "听到你这么说我很开心。"
            
        "有种轻松的休闲感":
            m 5b_dateday03 "啊啦～"
            m 5b_dateday03 "比起那些华丽的款式，这种确实更符合我的日常。"
            m 5b_dateday03 "能让你看到真实的我，我很高兴。"
            
        "很普通，但很自然":
            m 3n_dateday03 "嗯..."
            m 3l_dateday03 "有时候普通也是一种美，对吧？"
            m "至少不会让人觉得不自在。"

    m 5a_dateday03 "穿着这样的衣服..."
    m 5a_dateday03 "让我感觉更接近真实的自己。"
    
    if persistent.Dateday_casual_worn == 1:
        m 5b_dateday03 "不需要刻意扮演什么角色..."
        m "只要做最自然的莫妮卡就好。"
        m "这种感觉很踏实。"
    else:
        m 5b_dateday03 "每次穿这套衣服..."
        m "都会让我想起我们那些平凡的日常。"
        m "那些看似普通却珍贵的时光..."
        m "其实才是最温暖的。"

    m 3b_dateday03 "也许下次约会..."
    m 3k_dateday03 "我就可以穿着这套衣服呢～"
    
    if persistent.Dateday_casual_worn == 1:
        m 3l_dateday03 "虽然可能不够特别..."
        m "但至少不会让我太紧张。"
    else:
        m 3b_dateday03 "现在穿起来就像自己的衣服一样。"
        m 3k_dateday03 "应该会很自然吧？"
    
    m 5b_dateday03 "那样一定会是很舒适的体验。"
    
    hide monika
    pause 3.0
    show monika 3j_dateday01 zorder 12 at t11
    with dissolve
    
    m 3j_dateday01 "还想看其他款式吗？"
    m 1k_dateday01 "或者...这种日常风格更合你心意？"
    jump dateday_clothingshop_dress_choice

label dateday_clothingshop_dress:
    $ persistent.Dateday_dress_worn += 1
    hide monika
    pause 3.0
    show monika 3a_dateday02 zorder 12 at t11
    with dissolve
    
    if persistent.Dateday_dress_worn == 1:
        m 3a_dateday02 "这个丝绸材质..."
        m 3j_dateday02 "比想象中要柔软顺滑。"
        
        m 3v_dateday02 "不过，这个吊带设计..."
        m 3l_dateday02 "让我有点不好意思。"
        m "不过质感确实很高级。"
        
        m 3j_dateday02 "穿着这样的裙子..."
        m "感觉像是要去参加很正式的场合。"
        m 3l_dateday02 "可能不太适合平时穿。"
        
        m 3n_dateday02 "说实话..."
        m 3l_dateday02 "我有点担心会不会太暴露了。"
    else:
        m 5b_dateday02 "又穿上这条白色丝绸裙子了。"
        if persistent.Dateday_dress_worn == 2:
            m 5a_dateday02 "第二次穿感觉更自在了。"
            m "虽然还是有点害羞..."
            m 5b_dateday02 "但至少不会那么紧张了。"
        else:
            m 5b_dateday02 "已经穿这么多次了，感觉很熟悉了。"
            m 3j_dateday02 "甚至开始享受这种优雅的感觉。"
            m 3l_dateday02 "也许我比想象中更适合这种风格？"
    
    menu:
        m "你觉得合适吗？{fast}"
        "很漂亮，非常优雅":
            m 5a_dateday02 "谢、谢谢..."
            if persistent.Dateday_dress_worn == 1:
                m 5a_dateday02 "第一次穿这种风格，听到夸奖有点不知所措。"
            else:
                m 5b_dateday02 "每次听你这么说都会很開心。"
           
            
        "有种成熟的魅力":
            m 3l_dateday02 "啊啦～"
            if persistent.Dateday_dress_worn == 1:
                m "看来偶尔改变一下风格会有意想不到的效果。"
            else:
                m 3k_dateday02 "看来我们都很喜欢这种优雅的风格呢。"
            m 5b_dateday02 "能让你看到不一样的我，我很开心。"
            
        "还是平时的你更自然":
            m 3j_dateday02 "我也这么觉得。"
            m 3a_dateday02 "还是平时的装扮更自在一些。"
            if persistent.Dateday_dress_worn == 1:
                m 5b_dateday02 "不过尝试新事物也是种有趣的体验。"
            else:
                m 5b_dateday02 "但偶尔换个风格也挺好的，对吧？"

    m 3v_dateday02 "能像这样和你一起挑选衣服..."
    
    if persistent.Dateday_dress_worn == 1:
        m "是我曾经只能在想象中期待的场景。"
        m 3l_dateday02 "在独自一人的时候..."
        m "我常常幻想能和你一起做这些普通情侣会做的事。"
        m 3k_dateday02 "现在能实现，真的很幸福。"
    else:
        m "每次都会让我想起我们第一次在这里的约会。"
        m 3j_dateday02 "那些温暖的回忆..."
        m "让这条裙子变得格外特别。"
        m 3k_dateday02 "因为它承载着我们的美好时光。"

    m 7a_dateday02 "也许……下次约会"
    m "我就可以穿着这条裙子呢～"
    
    if persistent.Dateday_dress_worn == 1:
        m 7b_dateday02 "虽然可能需要一点时间来适应..."
        m 7c_dateday02 "但如果你希望，我愿意尝试。"
    else:
        m 5b_dateday02 "现在穿起来感觉自信多了。"
        m "应该不会让你失望吧？"
    
    m 5b_dateday02 "那样一定会是很浪漫的体验。"
    
    hide monika
    pause 3.0
    show monika 4a_dateday01 zorder 2 at t11
    with dissolve
    
    m 4a_dateday01 "还想看其他款式吗？"
    m 2k_dateday01 "或者...你已经有偏好的选择了？"
    jump dateday_clothingshop_dress_choice

label dateday_clothingshop_more:
    m 5b_dateday01 "那我们再逛逛吧。"
    m "这里的衣服种类真多。"
    
    m 5a_dateday01 "说实话..."
    m "我还在学习如何挑选适合自己的衣服。"
    
    if persistent.Dateday_clothingshop == 1:
        m 4e_dateday01 "在俱乐部时，这些都不需要担心。"
        m "我的形象就像被设定好的一样。"
    else:
        m 4a_dateday01 "比起第一次来，我感觉进步了很多。"
        m 4l_dateday01 "至少不会那么紧张了。"
    
    m 1a_dateday01 "但有你在身边指导..."
    m 1j_dateday01 "让这个过程变得很有趣。"
    
    m 5a_dateday01 "最重要的是..."
    m 5b_dateday01 "能和你一起创造这些美好的回忆~"
    
    m 2i_dateday01 "有时候我在想..."
    m "衣服不只是遮体之物..."
    m "它们也是表达自我的方式。"
    m 2j_dateday01 "而能和你一起探索不同的我..."
    m 2k_dateday01 "是件很幸福的事。"
    
    jump dateday_clothingshop_dress_choice