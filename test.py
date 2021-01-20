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


def sq_are(self, s, di, pe, ar):
    if len(str(s)) > 0 or len(str(di)) > 0 or len(str(pe)) > 0:
        ar = float(s) ** 2
        return round(ar, 2)
    else:
        return ar


def sq_dia(self, s, pe, ar, di):
    if len(str(s)) > 0 or len(str(pe)) > 0 or len(str(ar)) > 0:
        di = float(s) * math.sqrt(2)
        return round(di, 2)
    else:
        return di


def sq_per(self, s, ar, di, pe):
    if len(str(s)) > 0 or len(str(ar)) > 0 or len(str(di)) > 0:
        pe = 4 * float(s)
        return round(pe, 2)
    else:
        return pe

"""
            sid11 = tf_sid11.text
            dia11 = tf_dia11.text
            per11 = tf_per11.text
            are11 = tf_are11.text
            
            si11 = app.sq_sid(are11, dia11, per11, sid11)
            di11 = app.sq_dia(sid11, per11, are11, dia11)
            pe11 = app.sq_per(sid11, are11, dia11, per11)
            
            ar11 = app.sq_are(sid11, dia11, per11, are11)
            
            l_out_sid11.text = f'{si11}'
            l_out_dia11.text = f'{di11}'
            l_out_per11.text = f'{pe11}'
            l_out_are11.text = f'{ar11}'
"""