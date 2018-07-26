# -*- coding: UTF-8 -*-
import json
import numpy as np
class DateEncoder(json.JSONEncoder):
    def default(self, o):

        if isinstance(o,np.ndarray):

            return  o.tolist()
        return json.JSONEncoder.default(self,o)
