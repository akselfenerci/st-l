
class CreateXSobject:
   def __init__(self,table,idx):
        import forallpeople
        forallpeople.environment('structural',top_level=True)

        # section height
        s = table['h']
        self.h = s[idx[0]]*mm

        # section width (mm)
        s = table['b']
        self.b = s[idx[0]]*mm

        # web thickness (mm)
        s = table['tw']
        self.tw = s[idx[0]]*mm

        # flange thickness (mm)
        s = table['tf']
        self.tf = s[idx[0]]*mm

        # rounding radius (mm)
        s = table['r']
        self.r = s[idx[0]]*mm

        # weight m (kg/m)
        s = table['m']
        self.m = s[idx[0]]*kg/m

        # area (mm2)
        s = table['A']
        self.A = s[idx[0]]*mm**2

        # Second moment of area - strong axis yy (mm4 *10^6)
        s = table['I_y']
        self.I_y = s[idx[0]]*1e6*mm**4

        # radius of gyration - i_y (mm)
        s = table['i_y']
        self.i_y = s[idx[0]]*mm

        # section modulus - elastic - W_el_y (mm3 * 10^3)
        s = table['W_el,y']
        self.i_y = s[idx[0]]*1e3*mm**3

        # section modulus - plastic - W_pl_y (mm3 * 10^3)
        s = table['W_pl,y']
        self.W_pl_y = s[idx[0]]*1e3*mm**3

        # Second moment of area - weak axis zz (mm4 *10^6)
        s = table['I_z']
        self.I_z = s[idx[0]]*1e6*mm**4

        # radius of gyration - i_z (mm)
        s = table['i_z']
        self.i_z = s[idx[0]]*mm

        # section modulus - elastic - W_el_z (mm3 * 10^3)
        s = table['W_el,z']
        self.i_z = s[idx[0]]*1e3*mm**3

        # section modulus - plastic - W_pl_z (mm3 * 10^3)
        s = table['W_pl,z']
        self.W_pl_z = s[idx[0]]*1e3*mm**3

        # torsion constant - It (mm4*10^3)
        s = table['I_T']
        self.I_t = s[idx[0]]*1e3*mm**4

        # warping constant - Iw (mm4*10^6)
        s = table['I_w']
        self.I_w = s[idx[0]]*1e6*mm**4

        # buckling curve - bending around strong axis
        s = table['bucklecurvey']
        self.b_curve_y = s[idx[0]]

        # buckling curve - bending around weak axis
        s = table['bucklecurvez']
        self.b_curve_z = s[idx[0]]

        # Cross-section class (web in pure bending, strong axis)
        s = table['cscbendy']
        self.ccsbendy = s[idx[0]]

        # Cross-section class (web in pure compression)
        s = table['csccomp']
        self.csccomp = s[idx[0]]

        # Cross-section class (flanges in unifrom compression (can be axial force or bending moment))
        s = table['cscnm']
        self.cscnm = s[idx[0]]


def get_xs_data(fname,kname,sect_name):
    import pandas as pd

    table = pd.read_hdf(fname,kname)  
    idx = table.index[table['tverrsnitt'] == sect_name].tolist()
    sect =CreateXSobject(table,idx)
    return sect