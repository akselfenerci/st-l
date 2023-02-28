#IPE240
import pandas as pd
tverrsnittsdata = pd.read_csv('C:\\Users\\47406\\AAA Studass filer\\tverrsnittsprofildata.csv',sep = ';')
section = 'IPE240'
sectionlist = tverrsnittsdata['tverrsnitt']
sectiondata = []
for i in range( 0,len(sectionlist)-1 ):
    if str(section) == str(sectionlist[i]):
        sectiondata = tverrsnittsdata.iloc[i]
    else:
        sectiondata = sectiondata

def h ():
    h            = sectiondata['h']
    return h
def b ():
    b            = sectiondata['b']
    return b
def tw ():
    tw           = sectiondata['tw']
    return tw
def tf ():
    tf           = sectiondata['tf']
    return tf
def r ():
    r            = sectiondata['r']
    return r
def m ():
    m            = sectiondata['m']
    return m
def P ():
    P            = sectiondata['P']
    return P
def A ():
    A            = sectiondata['A']
    return A

    #crossectional properties
def A_vz ():
    A_vz         = sectiondata['A_v,z']         #shear area z
    return A_vz
def A_vy ():
    A_vy         = sectiondata['A_v,y']         #shear area y
    return A_vy
def I_y ():
    I_y          = sectiondata['I_y']    *10**6
    return I_y
def i_y ():
    i_y          = sectiondata['i_y']
    return i_y
def W_ely ():
    W_ely        = sectiondata['W_el,y'] *10**3
    return W_ely
def W_ply ():
    W_ply        = sectiondata['W_pl,y'] *10**3
    return W_ply
def I_z ():
    I_z          = sectiondata['I_z']    *10**6
    return I_z
def i_z ():
    i_z          = sectiondata['i_z']
    return i_z
def W_elz ():
    W_elz        = sectiondata['W_el,z'] *10**3
    return W_elz
def W_plz ():
    W_plz        = sectiondata['W_pl,z'] *10**3
    return W_plz

    #torsion and warping[
def I_T ():
    I_T          = sectiondata['I_T'] *10**3
    return I_T
def W_T ():
    W_T          = sectiondata['W_T'] *10**3 #torsion modulus
    return W_T
def I_w ():
    I_w          = sectiondata['I_w'] *10**6 #warping constant
    return I_w
def W_w ():
    W_w          = sectiondata['W_w'] *10**3 #warping modulus
    return W_w

    #elastic and plastic capacities
def N_plRd ():
    N_plRd       = sectiondata['N_pl,Rd']   *10**3 #konverted to N
    return N_plRd
def V_plRdz ():
    V_plRdz      = sectiondata['V_pl,Rd,z'] *10**3 #konverted to N
    return V_plRdz
def V_plRdy ():
    V_plRdy      = sectiondata['V_pl,Rd,y'] *10**3 #konverted to N
    return V_plRdy
def M_elRdy ():
    M_elRdy      = sectiondata['M_el,Rd,y'] *10**6 #konverted to Nmm
    return M_elRdy
def M_plRdy ():
    M_plRdy      = sectiondata['M_pl,Rd,y'] *10**6 #konverted to Nmm
    return M_plRdy
def M_elRdz ():
    M_elRdz      = sectiondata['M_el,Rd,z'] *10**6 #konverted to Nmm
    return M_elRdz
def M_plRdz ():
    M_plRdz      = sectiondata['M_pl,Rd,z'] *10**6 #konverted to Nmm
    return M_plRdz

    #buckling
def bucklecurvey ():
    bucklecurvey = sectiondata['bucklecurvey'] #buckling about major axis y-y
    return bucklecurvey
def bucklecurvez ():
    bucklecurvez = sectiondata['bucklecurvez'] #buckling about major axis y-y
    return bucklecurvez

    #section classification
def cscbendy ():
    cscbendy     = sectiondata['cscbendy'] #web in pure bending around y-y
    return cscbendy
def csccomp ():
    csccomp      = sectiondata['csccomp'] #web in pure uniform compression
    return csccomp
def cscnm ():
    cscnm        = sectiondata['cscnm'] #flanges in uniform complession due to axial force or bending moment
    return cscnm