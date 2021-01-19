KV = """

ScreenManager:
    id: scr_mngr
    MenuScreen:
    SphereScreen:
    CylinderScreen: 
    CubeScreen:
    ConeScreen:
    PyramidScreen:


<MenuScreen>
    id: mns
    name: 'menu'

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 8
        title: "G - Calc"
        anchor_title: 'center'
        height: 35
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [['dots-vertical', lambda x: nav_drawer.set_state("open") ]]

    MDRaisedButton:
        text: 'Sphere'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size: 20, 20
        size_hint: None,None
        on_press: 
            root.manager.current = 'sphere'
            root.manager.transition.direction = 'left'

    MDRaisedButton:
        text: 'Cylinder'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size: 20, 20
        size_hint: None,None
        on_press: 
            root.manager.current = 'cylinder'
            root.manager.transition.direction = 'left'

    MDRaisedButton:
        text: 'Cube'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size: 20, 20
        size_hint: None,None
        on_press: 
            root.manager.current = 'cube'
            root.manager.transition.direction = 'left'

    MDRaisedButton:
        text: 'Cone'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size: 20, 20
        size_hint: None,None
        on_press: 
            root.manager.current = 'cone'
            root.manager.transition.direction = 'left'

    MDRaisedButton:
        text: 'Pyramid'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size: 20, 20
        size_hint: None,None
        on_press: 
            root.manager.current = 'pyramid'
            root.manager.transition.direction = 'left'




<SphereScreen>
    id: spscreen
    name: 'sphere'

    canvas.before:
        Color:
            rgba: 207/255, 206/255, 204/255, 1
        Rectangle:
            pos: self.pos
            size: self.size


    Image:
        source: 'sphere.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    MDTextField:
        id: tf_rad1
        text: ''
        on_focus: self.text = ""
        pos_hint: {"center_x": .4, "center_y": 0.63}
        hint_text: "Enter Radius"
        size_hint_x: None
        width: 200
        max_text_length: 8
        input_filter: 'float'


    MDTextField:
        id: tf_vol1
        text: ''
        on_focus: self.text = ""
        pos_hint: {"center_x": .4, "center_y": 0.54}
        hint_text: "Enter Volume"
        size_hint_x: None
        width: 200
        max_text_length: 8
        input_filter: 'float'

    MDLabel:
        id: l_rad_name1
        text: 'Radius  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .71, "center_y": 0.4}

    MDLabel:
        id: l_rad_out1
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .81, "center_y": 0.4}

    MDLabel:
        id: l_vol_name1
        text: 'Volume  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .7, "center_y": 0.32}

    MDLabel:
        id: l_vol_out1
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .8, "center_y": 0.32}

    MDLabel:
        id: l_dia_name1
        text: 'Diameter  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .67, "center_y": 0.24}


    MDLabel:
        id: l_dia_out1
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .81, "center_y": 0.24}


    MDLabel:
        id: l_are_name1
        text: 'Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .75, "center_y": 0.16}

    MDLabel:
        id: l_are_out1
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .81, "center_y": 0.16}

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .2, "center_y": 0.05}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.63}
        text_color: app.theme_cls.primary_color
        on_press: 
            radius1 = tf_rad1.text           
            l_rad_out1.text = f'          {radius1}'

            v1 = app.sp_vol(radius1)
            volume1 = tf_vol1.text
            l_vol_out1.text = f'           {v1}'

            d1 = app.sp_diameter(radius1)
            l_dia_out1.text = f'          {d1}'

            a1 = app.sp_area(radius1)
            l_are_out1.text = f'          {a1}'

    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.54}
        text_color: app.theme_cls.primary_color
        on_press: 
            volume1 = tf_vol1.text
            l_vol_out1.text = f'           {volume1}'

            r1 = app.sp_rad(volume1)
            radius1 = tf_rad1.text 
            l_rad_out1.text = f'          {r1}'

            d1 = app.sp_diameter(str(r1))
            l_dia_out1.text = f'          {d1}'

            a1 = app.sp_area(str(r1))
            l_are_out1.text = f'          {a1}'



<CylinderScreen>
    id: cyscreen
    name: 'cylinder'

    canvas.before:
        Color:
            rgba: 207/255, 206/255, 204/255, 1
        Rectangle:
            pos: self.pos
            size: self.size




    Image:
        source: 'cylinder.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    MDTextField:
        id: tf_rad2
        text: ''

        pos_hint: {"center_x": .4, "center_y": 0.63}
        hint_text: "Enter Radius"
        size_hint_x: None
        width: 200
        max_text_length: 8
        input_filter: 'float'


    MDTextField:
        id: tf_hei2
        text: ''

        pos_hint: {"center_x": .4, "center_y": 0.54}
        hint_text: "Enter Height"
        size_hint_x: None
        width: 200
        max_text_length: 8
        input_filter: 'float'


    MDLabel:
        id: l_rad_name2
        text: 'Radius  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .71, "center_y": 0.47}

    MDLabel:
        id: l_rad_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .81, "center_y": 0.47}

    MDLabel:
        id: l_hei_name2
        text: 'Height  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .71, "center_y": 0.41}

    MDLabel:
        id: l_hei_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .81, "center_y": 0.41}

    MDLabel:
        id: l_vol_name2
        text: 'Volume  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .70, "center_y": 0.35}

    MDLabel:
        id: l_vol_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .8, "center_y": 0.35}

    MDLabel:
        id: l_dia_name2
        text: 'Diameter  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .67, "center_y": 0.29}


    MDLabel:
        id: l_dia_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .82, "center_y": 0.29}


    MDLabel:
        id: l_sare_name2
        text: 'Surface Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .61, "center_y": 0.23}

    MDLabel:
        id: l_sare_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .78, "center_y": 0.23}

    MDLabel:
        id: l_bare_name2
        text: 'Base Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .66, "center_y": 0.17}

    MDLabel:
        id: l_bare_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .82, "center_y": 0.17}

    MDLabel:
        id: l_lesurf_name2
        text: 'Leteral Surface  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .57, "center_y": 0.11}

    MDLabel:
        id: l_lesurf_out2
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .82, "center_y": 0.11}


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .2, "center_y": 0.05}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.55}
        text_color: app.theme_cls.primary_color
        on_press: 

            radius2 = tf_rad2.text
            l_rad_out2.text = f'          {radius2}'

            height2 = tf_hei2.text
            l_hei_out2.text = f'          {height2}'


            v2 = app.cy_vol(radius2, height2)
            l_vol_out2.text= f'           {v2}'

            d2 = app.cy_diameter(height2, v2, radius2)
            l_dia_out2.text = f'         {str(d2)}'

            sa2 = app.cy_surfarea(radius2, height2)
            l_sare_out2.text = f'             {sa2}'

            ba2 = app.cy_basearea(radius2)
            l_bare_out2.text = f'         {ba2}'

            ls2 = app.cy_lateral_surface(radius2, height2)
            l_lesurf_out2.text = f'         {ls2}'

            tf_rad2.text = ''
            tf_hei2.text = ''


<CubeScreen>
    id: cuscreen
    name: 'cube'

    canvas.before:
        Color:
            rgba: 207/255, 206/255, 204/255, 1
        Rectangle:
            pos: self.pos
            size: self.size


    Image:
        source: 'cube.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    MDTextField:
        id: tf_edge3
        text: ''
        on_focus: self.text = ""
        pos_hint: {"center_x": .4, "center_y": 0.63}
        hint_text: "Enter Edge"
        size_hint_x: None
        width: 200
        max_text_length: 8
        input_filter: 'float'

    MDLabel:
        id: l_edge_name3
        text: 'Edge  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .77, "center_y": 0.4}

    MDLabel:
        id: l_edge_out3
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.4}

    MDLabel:
        id: l_spacediag_name3
        text: 'Space Diagonal  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .59, "center_y": 0.32}

    MDLabel:
        id: l_spacediag_out3
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.32}

    MDLabel:
        id: l_sarea_name3
        text: 'Surface Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .63, "center_y": 0.24}


    MDLabel:
        id: l_sarea_out3
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.24}


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .2, "center_y": 0.05}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.63}
        text_color: app.theme_cls.primary_color
        on_press: 

            edge3 = tf_edge3.text
            l_edge_out3.text = f'          {edge3}'


            sd3 = app.cu_space_diagonal(edge3)
            l_spacediag_out3.text = f'          {sd3}'

            sa3 = app.cu_surface_area(edge3)
            l_sarea_out3.text = f'          {sa3}'

<ConeScreen>
    id: coscreen
    name: 'cone'

    canvas.before:
        Color:
            rgba: 207/255, 206/255, 204/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'cone.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    MDTextField:
        id: tf_radius4
        text: ''

        pos_hint: {"center_x": .4, "center_y": 0.63}
        hint_text: "Enter Radius"
        size_hint_x: None
        width: 200
        max_text_length: 16
        input_filter: 'float'

    MDTextField:
        id: tf_height4
        text: ''

        pos_hint: {"center_x": .4, "center_y": 0.54}
        hint_text: "Enter Height"
        size_hint_x: None
        width: 200
        max_text_length: 16
        input_filter: 'float'

    MDLabel:
        id: l_rad_name4
        text: 'Radius  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .73, "center_y": 0.47}

    MDLabel:
        id: l_rad_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.47}

    MDLabel:
        id: l_height_name4
        text: 'Height  |'
        theme_text_color: "Custom"
        font_size:'11sp'
        text_color: 0/255, 133/255, 101/255, 1
        pos_hint: {"center_x": .73, "center_y": 0.41}

    MDLabel:
        id: l_height_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.41}

    MDLabel:
        id: l_volume_name4
        text: 'Volume  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .72, "center_y": 0.35}


    MDLabel:
        id: l_volume_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.35}

    MDLabel:
        id: l_barea_name4
        text: 'Base Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .67, "center_y": 0.29}


    MDLabel:
        id: l_barea_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.29}   


    MDLabel:
        id: l_sarea_name4
        text: 'Surface Area  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .63, "center_y": 0.23}


    MDLabel:
        id: l_sarea_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.23}   

    MDLabel:
        id: l_lesurf_name4
        text: 'Leteral Surface  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .59, "center_y": 0.17}

    MDLabel:
        id: l_lesurf_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.17}

    MDLabel:
        id: l_sheight_name4
        text: 'Slant Height  |'
        theme_text_color: "Custom"
        text_color: 0/255, 133/255, 101/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .64, "center_y": 0.11}

    MDLabel:
        id: l_sheight_out4
        text: ''
        theme_text_color: "Custom"
        text_color: 0/255, 10/255, 65/255, 1
        font_size:'11sp'
        pos_hint: {"center_x": .84, "center_y": 0.11}


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .2, "center_y": 0.05}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.63}
        text_color: app.theme_cls.primary_color
        on_press: 

            radius4 = tf_radius4.text
            height4 = tf_height4.text


            l_rad_out4.text = f'          {radius4}'
            l_height_out4.text = f'          {height4}'

            tf_radius4.text = ''
            tf_height4.text = ''


            vo4 = app.co_volume(radius4, height4)
            l_volume_out4.text = f'          {vo4}'

            ba4 = app.co_barea(radius4)
            l_barea_out4.text = f'          {ba4}'

            sa4 = app.co_sarea(radius4, height4)
            l_sarea_out4.text = f'          {sa4}'

            ls4 = app.co_lsurface(radius4, height4)
            l_lesurf_out4.text = f'          {ls4}'

            sh4 = app.co_shieght(radius4, height4)
            l_sheight_out4.text = f'          {sh4}'

<PyramidScreen>
    id: pyscreen
    name: 'pyramid'

    Image:
        source: 'cylinder.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.08}

        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_rad2
            text: ''
            helper_text: "radius"
            helper_text_mode: "persistent"
            size_hint: 1, None
            height: "30dp"
            max_text_length: 15
            input_filter: 'float'
            multiline: False


        MDTextField:
            id: tf_hei2
            text: ''
            helper_text: "height"
            helper_text_mode: "persistent"
            size_hint: 1, None
            height: "30dp"
            max_text_length: 15
            input_filter: 'float'
            multiline: False

    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"




        MDTextField:
            id: tf_vol2
            helper_text: "volume"
            align: "center"
            helper_text_mode: "persistent"
            size_hint: 1, None
            height: "30dp"
            max_text_length: 21
            input_filter: 'float'
            multiline: False


    MDIconButton:
        icon: "owl"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .85, "center_y": 0.49}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            radius2 = tf_rad2.text
            height2 = tf_hei2.text
            volume2 = tf_vol2.text

            l_out_rad2.text = f'{radius2}'
            l_out_hei2.text = f'{height2}'
            l_out_vol2.text = f'{volume2}'



    GridLayout:
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .25, "center_y": .4}
        spacing: 20
        padding: 10


        MDLabel:
            id: l_name_rad2
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1


        MDLabel: 
            id: l_out_rad2
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_hei2
            text: 'height  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_hei2
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_hei2
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_vol2
            text: '' 
            font_size: "11px"





"""
