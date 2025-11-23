# -*- coding: utf-8 -*-
"""
Created on Tue Oct 01 13:11:08 2019

@author: pedro
"""

import numpy as np
# NOTA: 'import math' foi removido, usaremos np.exp()

def cstr_dyn_ss(x,V,F,caf,Tf,Tj):

    # ... (comentários do modelo) ...

    # parameters
    k0 = 9703.*3600.  # frequency factor (1/h)
    H_rxn = 5960.     # heat of reaction (kcal/kgmol)
    E_act = 11843.    # activation energy (kcal/kgmol)
    rhocp = 500.      # density*heat cap. (kcal/(m^3 K))
    UA = 150.         # heat trans coeff * area / vol (kcal/(m^3 K h))
    R = 1.987         # ideal gas constant (kcal / (kgmol K))
	
    # states
    ca     = x[0]
    Temp   = x[1]

    # ratios
    fov   = F/V
    UAoV  = UA/V

    # modeling equations:
    
    # --- CORREÇÃO AQUI ---
    # Trocado 'math.exp' por 'np.exp'
    rate = k0*np.exp(-E_act/(R*Temp))*ca
    # --- FIM DA CORREÇÃO ---

    erro = np.zeros((2,))
    erro[0] = fov*(caf - ca) - rate
    erro[1]  = fov*(Tf - Temp) + (H_rxn/rhocp)*rate - (UAoV/rhocp)*(Temp - Tj)

    return erro