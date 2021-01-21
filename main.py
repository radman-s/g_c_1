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

class IstriangleScreen(Screen):
    pass

class SquareScreen(Screen):
    pass

class RectangleScreen(Screen):
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
sm.add_widget(IstriangleScreen(name='istriangle'))
sm.add_widget(SquareScreen(name='square'))
sm.add_widget(RectangleScreen(name='rectangle'))

class MainApp(MDApp):



    def build(self):

        self.pi = 3.1415926535898
        self.enter_r = str('enter radius')
        self.enter_h = str('enter height')
        self.enter_v = str('enter volume')
        self.enter_e = str('enter edge')
        self.enter_s = str('enter side')
        self.enter_vr = str('enter volume or radius')
        self.enter_sa = str('enter side a')
        self.enter_sb = str('enter side b')
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
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            cs = math.sqrt((float(a)**2) + (float(b)**2))
            return round(cs, 2)

    def rt_per(self,  a, b, c):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            pe = float(a) + float(b) + float(c)
            return round(pe, 2)

    def rt_sper(self,  a, b, c):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            pe = (float(a) + float(b) + float(c)) /2
            return round(pe, 2)

    def rt_are(self,  a, b):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            ar = (float(a) * float(b)) / 2
            return round(ar, 2)

    def rt_irad(self,  a, b, c):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            ar = (float(a) * float(b)) / (float(a) + float(b) + float(c))
            return round(ar, 2)

    def rt_crad(self,  a, b, c):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            cr = float(c)/ 2
            return cr

# eq-triangle

    def qt_sid(self,p, sp, ar, al, s):
        if len(str(p)) > 0:
            s = float(p)/3
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


    def qt_per(self, s, sp, ar, al, p):
        if len(str(s)) > 0:
            p = 3 * float(s)
            return round(p, 2)
        elif len(str(sp)) > 0:
            a = 2 * float(sp) /3
            p = 3 * float(a)
            return round(p, 2)
        elif len(str(ar)) > 0:
            a = 2 * math.sqrt(float(ar)/math.sqrt(3))
            p = 3 * a
            return round(p, 2)
        elif len(str(al)) > 0:
            a = (2/math.sqrt(3)* float(al))
            p = 3 * a
            return round(p, 2)
        else:
            return p

    def qt_sper(self, s, ar, al, p, sp):
        if len(str(s)) > 0:
            sp = 3 * float(s) / 2
            return round(sp, 2)
        elif len(str(ar)) > 0:
            a = 2 * math.sqrt(float(ar)/math.sqrt(3))
            sp = 3 * a / 2
            return round(sp, 2)
        elif len(str(al)) > 0:
            a = (2/math.sqrt(3) * float(al))
            sp = 3 * a / 2
            return round(sp, 2)
        elif len(str(p)) > 0:
            a = float(p) / 3
            sp = 3 *a / 2
            return round(sp, 2)
        else:
            return sp

    def qt_are(self, s, al, p, sp, ar):
        if len(str(s)) > 0:
            ar = (1/4) * math.sqrt(3) * float(s)**2
            return round(ar, 2)
        elif len(str(al)) > 0:
            a = (2/math.sqrt(3) * float(al))
            ar = (1/4) * math.sqrt(3) * a**2
            return round(ar, 2)
        elif len(str(p)) > 0:
            a = float(p)/3
            ar = (1 / 4) * math.sqrt(3) * a**2
            return round(ar, 2)
        elif len(str(sp)) > 0:
            a = 2 * float(sp) / 3
            ar = (1 / 4) * math.sqrt(3) * a**2
            return round(ar, 2)
        else:
            return ar

    def qt_alt(self, s, p, sp, ar, al):
        if len(str(s)) > 0:
            al = (1/2) * math.sqrt(3) * float(s)
            return round(al, 2)
        elif len(str(p)) > 0:
            a = float(p) / 3
            al = (1/2) * math.sqrt(3) * float(a)
            return round(al, 2)
        elif len(str(sp)) > 0:
            a = 2 * float(sp) / 3
            al = (1/2) * math.sqrt(3) * a
            return round(al, 2)
        elif len(str(ar)) > 0:
            a = 2 * math.sqrt(float(ar)/math.sqrt(3))
            al = (1/2) * math.sqrt(3) * a
            return round(al, 2)
        else:
            return al

# is-trianlge

    def it_side_c(self, a):
        if len(str(a)) <= 0:
            c = self.enter_sa
            return c
        else:
            c = float(a)
            return round(c, 2)

    def it_per(self, a, b):
        if len(str(a)) <= 0:
            p = self.enter_sa
            return p
        elif len(str(b)) <= 0:
            p = self.enter_sb
            return p
        else:
            p = 2 * float(a) + float(b)
            return round(p, 2)

    def it_sper(self, a, b):
        if len(str(a)) <= 0:
            sp = self.enter_sa
            return sp
        elif len(str(b)) <= 0:
            sp = self.enter_sb
            return sp
        else:
            sp = float(a) + (float(b) / 2)
            return round(sp, 2)

    def it_are(self, a, b):
        if len(str(a)) <= 0:
            ar = self.enter_sa
            return ar
        elif len(str(b)) <= 0:
            ar = self.enter_sb
            return ar
        else:
            ar = float(b)/4 * math.sqrt(4 * float(a)**2 - float(b)**2)
            return round(ar, 2)

    def it_alta(self, a ,b):
        if len(str(a)) <= 0:
            aa = self.enter_sa
            return aa
        elif len(str(b)) <= 0:
            aa = self.enter_sb
            return aa
        else:
            aa = float(b) / (2 * float(a)) * math.sqrt(4 * float(a) ** 2 - float(b) ** 2)
            return round(aa, 2)

    def it_altb(self, a, b):
        if len(str(a)) <= 0:
            ab = self.enter_sa
            return ab
        elif len(str(b)) <= 0:
            ab = self.enter_sb
            return ab
        else:
            ab = (1/2) * math.sqrt(4 * float(a)**2 - float(b)**2)
            return round(ab, 2)

# square

    def sq_per(self,di, s, ar, pe):
        if len(str(di)) > 0:
            a = float(di)/ math.sqrt(2)
            pe = float(a) * 4
            return round(pe, 2)


        elif len(str(s)) > 0:
            pe = float(s) * 4
            return round(pe, 2)
        elif len(str(ar)) > 0:
            pe = float(ar) * 4
            return round(pe, 2)
        else:
            return pe

    def sq_are(self,di, s, pe, ar):
        if len(str(di)) > 0:
            a = float(di) / math.sqrt(2)
            ar = float(a) ** 2
            return round(ar, 2)
        elif len(str(s)) > 0:
            ar = float(s) ** 2
            return ar
        elif len(str(pe)) > 0:
            ar = float(pe) ** 2
            return ar
        else:
            return ar

    def sq_dia(self,s , pe, ar, di):
        if len(str(s)) > 0:
            di = math.sqrt(2) * float(s)
            return round(di, 2)
        elif len(str(pe)) > 0:
            di = math.sqrt(2) * float(pe)
            return round(di, 2)
        elif len(str(ar)) > 0:
            di = math.sqrt(2) * float(ar)
            return round(di, 2)
        else:
            return di

    def sq_sid(self, ar, di, pe, s):
        if len(str(ar)) > 0:
            s = math.sqrt(float(ar))
            return round(s, 2)
        elif len(str(di)) > 0:
            s = float(di) / math.sqrt(2)
            return round(s, 2)
        elif len(str(pe)) > 0:
            s = float(pe) / 4
            return round(s, 2)
        else:
            return s
# rectangle

    def re_are(self, a, b):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            a = float(a) * float(b)
            return round(a, 2)

    def re_dia(self, a, b):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            d = math.sqrt(float(a)**2 + float(b)**2)
            return round(d, 2)

    def re_per(self, a, b):
        if len(str(a)) <= 0:
            a = self.enter_sa
            return a
        elif len(str(b)) <= 0:
            b = self.enter_sb
            return b
        else:
            p = 2 * float(a) + 2 * float(b)
            return p


if __name__=='__main__':
    MainApp().run()
