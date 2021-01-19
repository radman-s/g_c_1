from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from helpers import KV
from kivy.core.window import Window
import math
from datetime import date


Window.clearcolor = (0, 1, 0, 1)
Window.size = (300, 500)



class MenuScreen(Screen):
    pass

class CylinderScreen(Screen):
    pass

class SphereScreen(Screen):
    pass

class CubeScreen(Screen):
    pass

class ConeScreen(Screen):
    pass

class PyramidScreen(Screen):
    pass

class CapsuleScreen(Screen):
    pass

class CircleScreen(Screen):
    pass

class RtriangleScreen(Screen):
    pass

class EqtriangleScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(CubeScreen(name='cube'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='sphere'))
sm.add_widget(CylinderScreen(name='cylinder'))
sm.add_widget(ConeScreen(name='cone'))
sm.add_widget(PyramidScreen(name='pyramid'))
sm.add_widget(CapsuleScreen(name='capsule'))
sm.add_widget(CircleScreen(name='circle'))
sm.add_widget(RtriangleScreen(name='rtriangle'))
sm.add_widget(EqtriangleScreen(name='eqtriangle'))

class MainApp(MDApp):



    def build(self):

        self.pi = 3.1415926535898
        self.enter_r = str('Enter radius')
        self.enter_h = str('Enter height')
        self.enter_v = str('Enter volume')
        self.enter_e = str('Enter edge')
        self.enter_s = str('Enter side')
        self.enter_vr = str('enter volume or radius')
        self.theme_cls.primary_palette = "Gray"  # "Purple", "Red"
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.accent_hue = '700'
        # self.theme_cls.theme_style = 'Dark'

        self.screen = Builder.load_string(KV)
        return self.screen

# sphere
    def sp_rad(self,v, r):

        if len(str(v)) > 0:
            sq = (1 / 3)
            vo = (3 * float(v)) / (4 * self.pi)
            rad = vo ** sq
            return round(rad,2)
        else:
            return r

    def sp_vol(self, r, v):

        if len(str(r)) > 0:
            vol = 4 / 3 * self.pi * float(r) ** 3
            return round(vol, 2)
        else:
            return v


    def sp_diameter(self, r):

        if len(str(r)) > 0:
            d = float(r) * 2
            return d
        else:
            r = self.enter_vr
            return r

    def sp_area(self, r):

        if len(str(r)) > 0:
            a = 4 * self.pi * float(r) ** 2
            return round(a,2)
        else:
            r = self.enter_vr
            return r
# cylinder

    def cy_rad(self, v, h):
        if len(v) <= 0:
            v = self.enter_v
            return v
        elif len(h) <= 0 :
            h = self.enter_h
            return h
        else:
            r = math.sqrt(float(v) / (self.pi * float(h)))
            return round(r, 2)


    def cy_dia(self, v, h):

        if len(v) <= 0:
            v = self.enter_v
            return v
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            top = float(v) / (3.14 * float(h))
            but = math.sqrt(top) * 2
            return round(but, 2)


    def cy_bar(self, r):
       if type(r) == str:
           return r
       else:
           ba = self.pi * (float(r)) ** 2
           return round(ba, 2)


    def cy_sar(self, r, h):
        if type(r) == str:
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            a = 2 * self.pi * float(r) * float(h) + 2 * self.pi * float(r) ** 2
            return round(a, 2)


    def cy_lsu(self, r, h):
        if type(r) == str:
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            ls = 2 * self.pi * float(r) * float(h)
            return round(ls, 2)

# cube

    def cu_space_diagonal(self, e):
        if len(e) <= 0:
            e = self.enter_e
            return e
        else:
            sd = math.sqrt(3 * float(e))
            return round(sd, 2)

    def cu_surface_area(self, e):
        if len(e) <= 0:
            e = self.enter_e
            return e
        else:
            a = 6 * (float(e))**2
            return round(a, 2)

# cone

    def co_vol(self, r, h):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h

        else:
            v = self.pi * float(r) ** 2 * (float(h)/3)
            return round(v, 2)


    def co_barea(self, r):
        if len(r) <= 0:
            r = self.enter_r
            return r
        else:
            a = self.pi * float(r) ** 2
            return round(a, 2)

    def co_sarea(self, r, h):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            a = self.pi * float(r) *(float(r) + math.sqrt(float(h)**2 + float(r)**2))
            return round(a, 2)

    def co_lsurf(self, r, h):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            a = self.pi * float(r) * (math.sqrt(float(h)**2 + float(r)**2))
            return round(a, 2)

    def co_shei(self, r, h):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            l = math.sqrt(float(r)** 2 + float(h) ** 2)
            return round(l, 2)

# pyramid

    def py_vol(self, s, h):
        if len(s) <= 0:
            s = self.enter_s
            return s
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            v = (1 / 3) * ((float(s)) ** 2) * float(h)
            return round(v, 2)


    def py_shei(self, s, h):
        if len(s) <= 0:
            s = self.enter_s
            return s
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            sh = math.sqrt(float(h) ** 2 + (1 / 4) * float(s) ** 2)
            return round(sh, 2)


    def py_lsa(self, s, h):
        if len(s) <= 0:
            s = self.enter_s
            return s
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            ls = float(s) * math.sqrt(float(s) ** 2 + 4 * float(h) ** 2)
            return round(ls, 2)


    def py_bsa(self, s):
        if len(s) <= 0:
            s = self.enter_s
            return s
        else:
            bs = float(s) **2
            return round(bs, 2)


    def py_tsa(self, s, h):
        if len(s) <= 0:
            s = self.enter_s
            return s
        elif len(h) <= 0:
            h = self.enter_h
            return h
        else:
            ta = float(s) * (float(s) + math.sqrt(float(s) ** 2 + 4 * float(h) ** 2))
            return round(ta, 2)
# capsule

    def ca_vol(self, r, s):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(s) <= 0:
            s = self.enter_s
            return s
        else:
            v = self.pi * (float(r) ** 2) * ((4 / 3) * float(r) + float(s))
            return round(v, 2)

    def ca_sar(self, r, s):
        if len(r) <= 0:
            r = self.enter_r
            return r
        elif len(s) <= 0:
            s = self.enter_s
            return s
        else:
            sa = 2 * self.pi * float(r) * (2 * float(r) + float(s))
            return round(sa, 2)

    def ca_cir(self, r):
        if len(r) <= 0:
            r = self.enter_r
            return r
        else:
            c = 2 * self.pi * float(r)
            return round(c, 2)

# cirlce

    def ci_rad(self, d, c, a, r):
        if len(str(d)) > 0:
            r = float(d)/2
            return round(r, 2)
        elif len(str(c)) > 0:
            r = float(c)/(self.pi * 2)
            return round(r, 2)
        elif len(str(a)) > 0:
            r = math.sqrt(float(a)/self.pi)
            return round(r,2)
        else:
            return r


    def ci_dia(self, r, c, a, d):
        if len(str(r)) > 0:
            d = 2 * float(r)
            return round(d, 2)
        elif len(str(c)) > 0:
            d = float(c)/self.pi
            return round(d, 2)
        elif len(str(a)) > 0:
            d = 2 * math.sqrt(float(a) / self.pi)
            return round(d, 2)
        else:
            return d


    def ci_cir(self, r, a, d, c):
        if len(str(r)) > 0:
            c = 2 * self.pi * float(r)
            return round(c, 2)
        elif len(str(a)) > 0:
            c = 2 * self.pi * math.sqrt(float(a) / self.pi)
            return round(c, 2)
        elif len(str(d)) > 0:
            c =  self.pi * float(d)
            return round(c, 2)
        else:
            return c


    def ci_are(self, r, d, c, a):
        if len(str(r)) > 0:
            a = self.pi * float(r) ** 2
            return round(a, 2)
        elif len(str(d)) > 0:
            a = (self.pi * float(d) ** 2) / 4
            return round(a, 2)
        elif len(str(c)) > 0:
            a = (float(c) ** 2) / (4 * self.pi)
            return round(a, 2)
        else:
            return a

# r-triangle

    def rt_sic(self, a, b):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            cs = math.sqrt((float(a)**2) + (float(b)**2))
            return round(cs, 2)

    def rt_per(self,  a, b, c):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            pe = float(a) + float(b) + float(c)
            return round(pe, 2)

    def rt_sper(self,  a, b, c):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            pe = (float(a) + float(b) + float(c)) /2
            return round(pe, 2)

    def rt_are(self,  a, b):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            ar = (float(a) * float(b)) / 2
            return round(ar, 2)

    def rt_irad(self,  a, b, c):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            ar = (float(a) * float(b)) / (float(a) + float(b) + float(c))
            return round(ar, 2)

    def rt_crad(self,  a, b, c):
        if len(str(a)) <= 0:
            a = 'enter side a'
            return a
        elif len(str(b)) <= 0:
            b = 'enter side b'
            return b
        else:
            cr = float(c)/ 2
            return cr

# eq-triangle

    def qt_side(self,p, sp, ar, al, s):
        if len(str(p)) > 0:
            s = 3 * float(p)/3 /2
            return round(s, 2)
        elif len(str(sp)) > 0:
            s = 2 * float(sp) / 3
            return round(s, 2)
        elif len(str(ar)) > 0:
            s = 2 * math.sqrt(float(ar)/math.sqrt(3))
            return round(s, 2)
        elif len(str(al)) > 0:
            s = (2 / math.sqrt(3) * float(al))
            return round(s, 2)
        else:
            return s






if __name__=='__main__':
    MainApp().run()
