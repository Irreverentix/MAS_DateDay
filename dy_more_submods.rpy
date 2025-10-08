init 11000:
    screen mas_extramenu_area():
        zorder 52
        
        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")
        
        frame:
            area (0, 0, 1280, 720)
            background Solid("#0000007F")
            
            # 关闭按钮
            textbutton _("Close"):
                area (60, 596, 120, 35)
                style "hkb_button"
                action Jump("mas_extra_menu_close")
           
            frame:
                area (195, 450, 80, 255)
                style "mas_extra_menu_frame"
                vbox:
                    spacing 2
                    label "Zoom":
                        text_style "mas_extra_menu_label_text"
                        xalign 0.5
                    
                    textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)
                    
                    bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                        style "mas_adjust_vbar"
                        xalign 0.5
                    $ store.mas_sprites.adjust_zoom()
            
            # 动态按钮网格系统
            vbox:
                xpos 310
                ypos 439
                spacing 20
                
                # 定义所有可能的模组按钮
                $ all_mod_buttons = [
                    # 格式: (模组名称, 按钮显示文本, 跳转标签)
                    ("Date day", "约会日", "Dateday_entry"),
                    ("Open World", "Open World", "view_OW"),
                    ("BonkAMon", "敲敲莫妮卡", "view_bonkmenu"),
                    # 在这里可以添加更多模组...
                ]
                
                # 筛选已安装的模组
                $ installed_buttons = []
                for mod_name, button_text, jump_label in all_mod_buttons:
                    if store.mas_submod_utils.isSubmodInstalled(mod_name):
                        $ installed_buttons.append((button_text, jump_label))
                
                # 如果没有安装任何模组，显示提示
                if len(installed_buttons) == 0:
                    frame:
                        xsize 202
                        ysize 65
                        style "mas_extra_menu_frame"
                        textbutton ("无可用模组"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()
                
                else:
                    # 将按钮按每行3个分组
                    $ button_rows = []
                    $ current_row = []
                    
                    for i, (button_text, jump_label) in enumerate(installed_buttons):
                        $ current_row.append((button_text, jump_label))
                        
                        # 每3个按钮换一行，或者是最后一个按钮
                        if len(current_row) >= 3 or i == len(installed_buttons) - 1:
                            $ button_rows.append(current_row)
                            $ current_row = []
                    
                    # 渲染按钮行
                    for row in button_rows:
                        hbox:
                            spacing 20
                            for button_text, jump_label in row:
                                frame:
                                    xsize 202
                                    ysize 65
                                    style "mas_extra_menu_frame"
                                    if persistent._mas_in_idle_mode:
                                        textbutton (button_text):
                                            xalign 0.5
                                            yalign 0.5
                                            action NullAction()
                                    else:
                                        textbutton (button_text):
                                            xalign 0.5
                                            yalign 0.5
                                            action [Hide("mas_extramenu_area"), Jump(jump_label)]
                                            hover_sound gui.hover_sound