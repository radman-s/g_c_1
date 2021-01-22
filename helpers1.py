KV = """

ScreenManager:
    id: scr_mngr
    MenuScreen:
    SphereScreen:
    CylinderScreen: 
    CubeScreen:
    ConeScreen:
    PyramidScreen:
    CapsuleScreen:
    CircleScreen:
    RtriangleScreen:
    EqtriangleScreen:
    IstriangleScreen:
    SquareScreen:
    RectangleScreen:

<MenuScreen>
    id: mns
    name: 'menu'
    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size


    Image:
        source: 'main.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1


        BoxLayout:
            pos_hint: {'center_x': 0.5, "center_y": 0.6}
            spacing: "10dp"



            MDRaisedButton:
                text: 'Sphere'
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'sphere'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Cylinder'
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'cylinder'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Cube'
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'cube'
                    root.manager.transition.direction = 'left'
        BoxLayout:
            pos_hint: {"center_y": .5}
            spacing: "10dp" 

            MDRaisedButton:
                text: 'Cone'
                pos_hint: {'center_x': 0.5, 'center_y': 1.7}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'cone'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Pyramid'
                pos_hint: {'center_x': 0.5, 'center_y': 1.7}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'pyramid'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Capsule'
                pos_hint: {'center_x': 0.5, 'center_y': 1.7}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'capsule'
                    root.manager.transition.direction = 'left'


        BoxLayout:
            pos_hint: {"center_y": .5}
            spacing: "10dp"


            MDRaisedButton:
                text: 'Circle'
                pos_hint: {'center_x': 0.5, 'center_y': 1.4}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'circle'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'R-Triangle'
                pos_hint: {'center_x': 0.5, 'center_y': 1.4}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'rtriangle'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Eq-Triangle'
                pos_hint: {'center_x': 0.5, 'center_y': 1.4}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'eqtriangle'
                    root.manager.transition.direction = 'left'

        BoxLayout:
            pos_hint: {"center_y": .5}     
            spacing: "10dp"  

            MDRaisedButton:
                text: 'Is-Triangle'
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'istriangle'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Square'
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'square'
                    root.manager.transition.direction = 'left'

            MDRaisedButton:
                text: 'Rectangle'
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size: 20, 20
                size_hint: None,None
                on_press: 
                    root.manager.current = 'rectangle'
                    root.manager.transition.direction = 'left'

<SphereScreen>
    id: spscreen
    name: 'sphere'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'sphere.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.14}

        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_vol1
            helper_text: "volume"

            on_focus: self.text = ""
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


        MDTextField:
            id: tf_rad1
            text: ''
            helper_text: "radius"
            on_focus: self.text = ""
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.5}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:


            l_out_vol1.text = ''
            l_out_rad1.text = ''
            l_out_dia1.text = ''
            l_out_are1.text = ''



    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color

        pos_hint: {"center_x": .92, "center_y": 0.6}

        user_font_size: "23sp"

        on_press:

            volume1 = tf_vol1.text
            radius1 = tf_rad1.text

            r1 = app.sp_rad(volume1,radius1)
            v1 = app.sp_vol(radius1, volume1)
            d1 = app.sp_diameter(r1)
            a1 = app.sp_area(r1)

            l_out_rad1.text = f'{r1}'
            l_out_vol1.text = f'{v1}'
            l_out_dia1.text = f'{d1}'
            l_out_are1.text = f'{a1}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.4}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'


    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .5}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_vol1
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_vol1
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_rad1
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_rad1
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_dia1
            text: 'diameter  |'
            halign: 'right'
            font_size: "11px"


        MDLabel: 
            id: l_out_dia1
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_are1
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are1
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<CylinderScreen>
    id: cyscreen
    name: 'cylinder'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'cylinder.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.145}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_vol2
            helper_text: "volume"
            align: "center"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


        MDTextField:
            id: tf_hei2
            text: ''
            helper_text: "height"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.5}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            tf_hei2.text = ''
            tf_vol2.text = ''
            l_out_vol2.text = ''
            l_out_hei2.text = ''
            l_out_rad2.text = ''
            l_out_dia2.text = ''
            l_out_bar2.text = ''
            l_out_sar2.text = ''
            l_out_lsu2.text = ''

    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.6}
        user_font_size: "23sp"
        on_press:

            volume2 = tf_vol2.text
            height2 = tf_hei2.text
            radius2 = app.cy_rad(volume2, height2)
            diameter2 = app.cy_dia(volume2, height2)

            bare2 = app.cy_bar(radius2)
            sare2 = app.cy_sar(radius2,height2)
            lsur2 = app.cy_lsu(radius2, height2)

            l_out_vol2.text = f'{volume2}'
            l_out_hei2.text = f'{height2}'
            l_out_rad2.text = f'{radius2}'
            l_out_dia2.text = f'{diameter2}'
            l_out_bar2.text = f'{bare2}'
            l_out_sar2.text = f'{sare2}'
            l_out_lsu2.text = f'{lsur2}'


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.4}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'


    GridLayout:
        id: cyvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .4}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            id: l_name_vol2
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_vol2
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_hei2
            text: 'height  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_hei2
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_rad2
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_rad2
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_dia2
            text: 'diameter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_dia2
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_bar2
            text: 'base area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_bar2
            text: '' 
            font_size: "11px"          

        MDLabel:
            id: l_name_sar2
            text: 'surface area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sar2
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_lsu2
            text: 'lateral surface  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_lsu2
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'


<CubeScreen>
    id: cuscreen
    name: 'cube'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'cube.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y":  1.145}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_edg3
            helper_text: "edge"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.515}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            tf_edg3.text = ''
            l_out_edg3.text = ''
            l_out_spd3.text = ''
            l_out_sua3.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.615}
        user_font_size: "23sp"   
        on_press:
            edge3 = tf_edg3.text
            sp3 = app.cu_space_diagonal(edge3)
            su3 = app.cu_surface_area(edge3)
            l_out_edg3.text = f'{edge3}'
            l_out_spd3.text = f'{sp3}'
            l_out_sua3.text = f'{su3}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.415}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'


    GridLayout:
        id: cuvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .55}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_edg3
            text: 'edge  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_edg3
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_spd3
            text: 'space diagonal  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_spd3
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_sua3
            text: 'surface area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sua3
            text: '' 
            font_size: "11px"
            multiline: False

    MDToolbar:
        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'


<ConeScreen>
    id: coscreen
    name: 'cone'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'cone.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_rad4
            helper_text: "radius"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_hei4
            helper_text: "height"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"

    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.52}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            tf_rad4.text = ''
            tf_hei4.text = ''
            l_out_rad4.text = ''
            l_out_hei4.text = ''
            l_out_vol4.text = ''
            l_out_bar4.text = ''
            l_out_sar4.text = ''
            l_out_lsu4.text = ''
            l_out_she4.text = ''

    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.62}
        user_font_size: "23sp"   
        on_press:

            radius4 = tf_rad4.text
            height4 = tf_hei4.text

            vl4 = app.co_vol(radius4,height4)
            ba4 = app.co_barea(radius4)
            sa4 = app.co_sarea(radius4,height4)
            ls4 = app.co_lsurf(radius4, height4)
            sh4 = app.co_shei(radius4, height4)

            l_out_rad4.text = f'{radius4}'
            l_out_hei4.text = f'{height4}'
            l_out_vol4.text = f'{vl4}' 
            l_out_bar4.text = f"{ba4}"
            l_out_sar4.text = f'{sa4}'
            l_out_lsu4.text = f'{ls4}'
            l_out_she4.text = f'{sh4}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.42}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'            

    GridLayout:
        id: cuvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .42}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_rad4
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_rad4
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_hei4
            text: 'height  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_hei4
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_vol4
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_vol4
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_bar4
            text: 'base area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_bar4
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_sar4
            text: 'surface area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sar4
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_lsu4
            text: 'lateral surface  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_lsu4
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_she4
            text: 'slant height  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_she4
            text: '' 
            font_size: "11px"
            multiline: False

    MDToolbar:
        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'


<PyramidScreen>
    id: pyscreen
    name: 'pyramid'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'pyramid.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}

        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_sid5
            helper_text: "side"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


        MDTextField:
            id: tf_hei5
            helper_text: "height"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.52}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:
            l_out_sid5.text = ''
            l_out_hei5.text = ''
            l_out_vol5.text = ''
            l_out_she5.text = ''
            l_out_lsa5.text = ''
            l_out_bsa5.text = ''
            l_out_tsa5.text = ''
            tf_sid5.text = ''
            tf_hei5.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.62}
        user_font_size: "23sp"   
        on_press:
            side5 = tf_sid5.text
            height5 = tf_hei5.text

            vol5 = app.py_vol(side5, height5)
            she5 = app.py_shei(side5, height5)
            lsa5 = app.py_lsa(side5, height5)
            bsa5 = app.py_bsa(side5)
            tsa5 = app.py_tsa(side5, height5)

            l_out_sid5.text = f'{side5}'
            l_out_hei5.text = f'{height5}'
            l_out_vol5.text = f'{vol5}'
            l_out_she5.text = f'{she5}'
            l_out_lsa5.text = f'{lsa5}'
            l_out_bsa5.text = f'{bsa5}'
            l_out_tsa5.text = f'{tsa5}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.42}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'


    GridLayout:
        id: cuvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .37, "center_y": .45}
        spacing: 30
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_sid5
            text: 'side length |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sid5
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_hei5
            text: 'height  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_hei5
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_vol5
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_vol5
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_she5
            text: 'slant height  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_she5
            text: '' 
            font_size: "11px"
            multiline: False


        MDLabel:
            id: l_name_lsa5
            text: 'lateral sur. area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_lsa5
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_bsa5
            text: 'base sur. area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_bsa5
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_tsa5
            text: 'total sur. area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_tsa5
            text: '' 
            font_size: "11px"
            multiline: False


    MDToolbar:
        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<CapsuleScreen>
    id: cascreen
    name: 'capsule'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'capsule.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.14}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_rad6
            helper_text: "radius"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


        MDTextField:
            id: tf_sid6
            helper_text: "side"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.52}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.62}
        user_font_size: "23sp"
        on_press:

            radius6 = tf_rad6.text
            side6 = tf_sid6.text

            vo6 = app.ca_vol(radius6, side6)
            su6 = app.ca_sar(radius6, side6)
            ci6 = app.ca_cir(radius6)

            l_out_rad6.text = f'{radius6}'
            l_out_sid6.text = f'{side6}'

            l_out_vol6.text = f'{vo6}'
            l_out_cir6.text = f'{ci6}'
            l_out_sar6.text = f'{su6}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.42}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'       

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .49}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_rad6
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_rad6
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sid6
            text: 'side  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sid6
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_vol6
            text: 'volume  |'
            halign: 'right'
            font_size: "11px"


        MDLabel: 
            id: l_out_vol6
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_sar6
            text: 'surface area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sar6
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_cir6
            text: 'circumference  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_cir6
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<CircleScreen>
    id: ciscreen
    name: 'circle'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'circle.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_rad7
            helper_text: "radius"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_dia7
            helper_text: "diameter"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

    BoxLayout:
        pos_hint: {"center_y": 1.07}
        padding: "10dp"
        spacing: "10dp"

        MDTextField:

            id: tf_cir7
            helper_text: "circumference"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False       

        MDTextField:
            id: tf_are7
            helper_text: "area"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False   


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.44}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:
            l_out_rad7.text = ''
            l_out_dia7.text = ''
            l_out_cir7.text = ''
            l_out_are7.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.54}
        user_font_size: "23sp"
        on_press:

            radius7 = tf_rad7.text
            diameter7 = tf_dia7.text
            circum7 = tf_cir7.text
            area7 = tf_are7.text

            ra7 = app.ci_rad(diameter7, circum7, area7, radius7)
            di7 = app.ci_dia(radius7, circum7, area7, diameter7)
            ci7 = app.ci_cir(radius7, area7, diameter7, circum7)
            ar7 = app.ci_are(radius7, diameter7, circum7, area7)

            l_out_rad7.text = f'{ra7}'
            l_out_dia7.text = f'{di7}'
            l_out_cir7.text = f'{ci7}'
            l_out_are7.text = f'{ar7}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.34}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'


    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .44}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_rad7
            text: 'radius  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_rad7
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_dia7
            text: 'diameter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_dia7
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_cir7
            text: 'circumference  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_cir7
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_are7
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are7
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<RtriangleScreen>
    id: rtscreen
    name: 'rtriangle'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'r_triangle.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_side_a8
            helper_text: "side a"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_side_b8
            helper_text: "side b"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1}
        padding: "10dp"


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.51}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            tf_side_a8.text = ''
            tf_side_b8.text = ''           
            l_out_sa8.text = ''
            l_out_sb8.text = ''
            l_out_sc8.text = ''
            l_out_per8.text = ''
            l_out_sper8.text = ''
            l_out_arer8.text = ''
            l_out_irad8.text =''
            l_out_crad8.text = ''



    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.61}
        user_font_size: "23sp"
        on_press:

            side_a8 = tf_side_a8.text
            side_b8 = tf_side_b8.text

            sc8 = app.rt_sic(side_a8, side_b8)
            pe8 = app.rt_per(side_a8, side_b8, sc8)
            sp8 = app.rt_sper(side_a8, side_b8, sc8)
            ar8 = app.rt_are(side_a8, side_b8)
            irad8 =  app.rt_irad(side_a8, side_b8, sc8)
            crad8 = app.rt_crad(side_a8, side_b8, sc8)


            l_out_sa8.text = f'{side_a8}'
            l_out_sb8.text = f'{side_b8}'
            l_out_sc8.text = f'{sc8}'
            l_out_per8.text = f'{pe8}'
            l_out_sper8.text = f'{sp8}'
            l_out_arer8.text = f'{ar8}'
            l_out_irad8.text = f'{irad8}'
            l_out_crad8.text = f'{crad8}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.41}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .375}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_sa8
            text: 'side a  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sa8
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sb8
            text: 'side b  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sb8
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sc8
            text: 'side c  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sc8
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_per8
            text: 'perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_per8
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_sper8
            text: 'semi perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sper8
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_are8
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_arer8
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_irad8
            text: 'inradius  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_irad8
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_crad8
            text: 'circumradius  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_crad8
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<EqtriangleScreen>
    id: eqtscreen
    name: 'eqtriangle'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'eq_triangle.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.13}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_sid9
            helper_text: "side"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_per9
            helper_text: "perimeter"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": 1.05}
        padding: "10dp"
        spacing: "10dp" 

        MDTextField:
            id: tf_sper9
            helper_text: "semiperimeter"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_are9
            helper_text: "area"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    BoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y": .97}
        padding: "10dp"
        spacing: "10dp" 


        MDTextField:
            id: tf_alt9
            helper_text: "altitude"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.34}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:
            l_out_sid9.text = ''
            l_out_per9.text = ''
            l_out_sper9.text = ''
            l_out_are9.text = ''
            l_out_alt9.text = ''



    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.44}
        user_font_size: "23sp"
        on_press:

            sid9 = tf_sid9.text
            per9 = tf_per9.text
            sper9 = tf_sper9.text
            are9 = tf_are9.text
            alt9 = tf_alt9.text

            si9 = app.qt_sid(per9, sper9, are9, alt9, sid9)
            pe9 = app.qt_per(sid9, sper9, are9, alt9, per9)
            sp9 = app.qt_sper(sid9, are9, alt9, per9, sper9)
            ar9 = app.qt_are(sid9, alt9, per9, sper9, are9)
            al9 = app.qt_alt(sid9, per9, sper9, are9, alt9)

            l_out_sid9.text = f'{si9}'
            l_out_per9.text = f'{pe9}'
            l_out_sper9.text = f'{sp9}'
            l_out_are9.text = f'{ar9}'
            l_out_alt9.text = f'{al9}'


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.24}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .31}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            id: l_name_sid9
            text: 'side  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sid9
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_per9
            text: 'perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_per9
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_sper9
            text: 'semiperimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sper9
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_are9
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are9
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_alt9
            text: 'altitude  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_alt9
            text: '' 
            font_size: "11px"

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<IstriangleScreen>
    id: istscreen
    name: 'istriangle'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'is_triangle.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.14}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_sida10
            helper_text: "side a"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_sidb10
            helper_text: "side b"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.515}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:
            tf_sida10.text = ''
            tf_sidb10.text = ''
            l_out_sida10.text = ''
            l_out_sidb10.text = ''
            l_out_sidc10.text = ''
            l_out_per10.text = ''
            l_out_sper10.text = ''
            l_out_are10.text = ''
            l_out_alta10.text = ''
            l_out_altb10.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.615}
        user_font_size: "23sp"
        on_press:

            sida10 = tf_sida10.text
            sidb10 = tf_sidb10.text

            si10 = app.it_side_c(sida10)
            pe10 = app.it_per(sida10, sidb10)
            sp10 = app.it_sper(sida10, sidb10)
            ar10 = app.it_are(sida10, sidb10)
            aa10 = app.it_alta(sida10, sidb10)
            ab10 = app.it_altb(sida10, sidb10)


            l_out_sida10.text = f'{sida10}'
            l_out_sidb10.text = f'{sidb10}'
            l_out_sidc10.text = f'{si10}'
            l_out_per10.text = f'{pe10}'
            l_out_sper10.text = f'{sp10}'
            l_out_are10.text = f'{ar10}'
            l_out_alta10.text = f'{aa10}'
            l_out_altb10.text = f'{ab10}'


    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.415}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .38}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            id: l_name_sida10
            text: 'side a |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sida10
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sidb10
            text: 'side b  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sidb10
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sidc10
            text: 'side c  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sidc10
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_per10
            text: 'perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_per10
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_sper10
            text: 'semiperimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sper10
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_are10
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are10
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_alta10
            text: 'altitude a & c |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_alta10
            text: '' 
            font_size: "11px"    

        MDLabel:
            id: l_name_altb10
            text: 'altitude b |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_altb10
            text: '' 
            font_size: "11px"    

    MDToolbar:

        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<SquareScreen>
    id: sqtscreen
    name: 'square'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'square.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_sid11
            helper_text: "side"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_dia11
            helper_text: "diagonal"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

    BoxLayout:
        pos_hint: {"center_y": 1.07}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_per11
            helper_text: "perimeter"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_are11
            helper_text: "area"
            helper_text_mode: "persistent"
            on_focus: self.text = ""
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.44}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:
            l_out_are11.text = ''
            l_out_per11.text = ''
            l_out_dia11.text = ''
            l_out_sid11.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.54}
        user_font_size: "23sp"
        on_press:

            sid11 = tf_sid11.text
            dia11 = tf_dia11.text
            per11 = tf_per11.text
            are11 = tf_are11.text

            ar11 = app.sq_are(dia11, sid11, per11, are11)
            pe11 = app.sq_per(dia11, sid11, are11, per11)
            di11 = app.sq_dia(sid11, per11, are11, dia11)
            si11 = app.sq_sid(are11, dia11, per11, sid11)

            l_out_are11.text = f'{ar11}'
            l_out_per11.text = f'{pe11}'
            l_out_dia11.text = f'{di11}'
            l_out_sid11.text = f'{si11}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.34}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .44}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_sid11
            text: 'side |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_sid11
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_dia11
            text: 'diagonal  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_dia11
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_per11
            text: 'perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_per11
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_are11
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are11
            text: '' 
            font_size: "11px"


    MDToolbar:
        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



<RectangleScreen>
    id: rectscreen
    name: 'rectangle'

    canvas.before:
        Color:
            rgba: 217/255, 217/234, 217/225, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'rectangle.png'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        allow_stretch:True
        opacity: 1

    BoxLayout:
        pos_hint: {"center_y": 1.15}
        padding: "10dp"
        spacing: "10dp"  

        MDTextField:
            id: tf_sida12
            helper_text: "side a"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False

        MDTextField:
            id: tf_sidb12
            helper_text: "side b"
            helper_text_mode: "persistent"
            line_color_focus: 0, 0, 1, 1
            size_hint: 1, None
            height: "30dp"
            input_filter: 'float'
            multiline: False


    MDIconButton:
        icon: "delete"
        theme_text_color: "ContrastParentBackground"
        pos_hint: {"center_x": .92, "center_y": 0.51}
        text_color: app.theme_cls.primary_color
        user_font_size: "23sp"
        on_press:

            tf_sida12.text = ''
            tf_sidb12.text = ''

            l_out_sida12.text = ''
            l_out_sidb12.text = ''

            l_out_dia12.text = ''
            l_out_per12.text = ''
            l_out_are12.text = ''


    MDIconButton:
        icon: "owl"
        theme_text_color: "Custom"
        text_color: app.theme_cls.accent_color
        pos_hint: {"center_x": .92, "center_y": 0.61}
        user_font_size: "23sp"
        on_press:

            sida12 = tf_sida12.text
            sidb12 = tf_sidb12.text

            ar12 = app.re_are(sida12, sidb12)
            pe12 = app.re_per(sida12, sidb12)
            di12 = app.re_dia(sida12, sidb12)

            l_out_sida12.text = f'{sida12}'
            l_out_sidb12.text = f'{sidb12}'

            l_out_dia12.text = f'{di12}'
            l_out_per12.text = f'{pe12}'
            l_out_are12.text = f'{ar12}'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Hint"
        pos_hint: {"center_x": .92, "center_y": 0.41}
        text_color: app.theme_cls.primary_color
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'

    GridLayout:
        id: spvalues
        cols: 2
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .36, "center_y": .48}
        spacing: 34
        padding: 10
        canvas.before:
            Color:
                rgba: 179/255, 179/234, 179/225, 1
            Rectangle:
                pos: self.pos
                size: self.size


        MDLabel:
            id: l_name_sida12
            text: 'side a |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sida12
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_sidb12
            text: 'side b  |'
            halign: 'right'
            font_size: "11px"
            color: 0, 0, 1, 1

        MDLabel: 
            id: l_out_sidb12
            text: '' 
            font_size: "11px"
            color: 1, 0, 0, 1

        MDLabel:
            id: l_name_dia12
            text: 'diagonal  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_dia12
            text: '' 
            font_size: "11px"
            multiline: False

        MDLabel:
            id: l_name_per12
            text: 'perimeter  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_per12
            text: '' 
            font_size: "11px"

        MDLabel:
            id: l_name_are12
            text: 'area  |'
            halign: 'right'
            font_size: "11px"

        MDLabel: 
            id: l_out_are12
            text: '' 
            font_size: "11px"

    MDToolbar:
        type: 'bottom'       
        mode: 'free-end'
        elevation: 10
        height: '25px'



"""
