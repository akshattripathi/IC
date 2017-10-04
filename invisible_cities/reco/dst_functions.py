import pandas as pd
import tables as tb
import numpy  as np

from .  corrections import Correction
from .  corrections import LifetimeXYCorrection
from .. io.dst_io   import load_dst


def load_z_corrections(filename):
    dst = load_dst(filename, "Corrections", "Zcorrections")
    return Correction((dst.z.values,), dst.factor.values, dst.uncertainty.values)


def load_xy_corrections(filename, **kwargs):
    dst  = load_dst(filename, "Corrections", "XYcorrections")
    x, y = np.unique(dst.x.values), np.unique(dst.y.values)
    f, u = dst.factor.values, dst.uncertainty.values

    return Correction((x, y),
                      f.reshape(x.size, y.size),
                      u.reshape(x.size, y.size),
                      **kwargs)


def load_lifetime_xy_corrections(filename, interp_strategy="nearest"):
    dst  = load_dst(filename, "Corrections", "LifetimeXY")
    x, y = np.unique(dst.x.values), np.unique(dst.y.values)
    f, u = dst.factor.values, dst.uncertainty.values

    return LifetimeXYCorrection(f.reshape(x.size, y.size),
                                u.reshape(x.size, y.size),
                                x, y)
