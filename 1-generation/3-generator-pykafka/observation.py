#!/usr/bin/env python
import random
import numpy as np

from datetime import datetime
from datetime import timedelta

# random lab function
def oru():

    CMP = {
        'components':{
        'sodium': {'value':int(),'unit':'mmol/L'},
        'potassium':{'value':int(),'unit':'mmol/L'},
        'chloride':{'value':int(),'unit':'mmol/L'},
        'bicarb':{'value':int(),'unit':'mmol/L'},
        'bun':{'value':int(),'unit':'mg/dL'},
        'creatinine':{'value':int(),'unit':'mg/dL'},
        'glucose':{'value':int(),'unit':'mg/dL'},
        },
        'method':str(),
        'service_id':str()

    }

    CBC = {
        'components':{
        'hemoglobin':{'value':int(),'unit':'g/dL'},
        'hematocrit':{'value':int(),'unit':'%'},
        'wbc':{'value':int(),'unit':'x1000/uL'},
        'platelet':{'value':int(), 'unit':'x1000/uL'},
        },
        'method':str(),
        'service_id':str()
    }
    
    BABESIA = {
        'components':{
        'count':{'value':int(),'unit':''},
        'result':{'value':str(),'unit':''}
        },
        'method':str(),
        'service_id':str()
    }

    x = random.randint(0, 3)
    
    if x == 0:
        CMP['components']['sodium']['value'] = np.random.normal(139.59, 4.47)
        CMP['components']['potassium']['value'] = np.random.normal(4.19, 0.57)
        CMP['components']['chloride']['value'] = np.random.normal(101.04, 5.43)
        CMP['components']['bicarb']['value'] = np.random.normal(22.65, 4.02)
        CMP['components']['bun']['value'] = np.random.normal(23.64, 19.78)
        CMP['components']['creatinine']['value'] = np.random.normal(1.34, 1.55)
        CMP['components']['glucose']['value'] = np.random.normal(129.26, 60.48)

        CMP['service_id'] = 'COMPREHENSIVE METABOLIC PANEL'
        CMP['method'] = 'YH DPP RS1'

        return CMP
    
    elif x == 1:
        CBC['components']['hemoglobin']['value'] = np.random.normal(13, 1.5)
        CBC['components']['hematocrit']['value'] = np.random.normal(40, 5)
        CBC['components']['wbc']['value'] = np.random.normal(8, 2)
        CBC['components']['platelet']['value'] = np.random.normal(250, 100)

        CBC['service_id'] = 'COMPLETE BLOOD COUNT'
        CBC['method'] = 'SYSMEX'
        
        return CBC
    else:
        r = random.randint(0, 1)
        if r == 0:
            BABESIA['components']['count']['value'] = np.random.normal(1, 15)
            BABESIA['components']['result']['value'] = 'positive'
        else:
            BABESIA['components']['count']['value'] = 0
            BABESIA['components']['result']['value'] = 'negative'

        BABESIA['service_id'] = 'BABESIA'
        BABESIA['method'] = 'MANUAL SMEAR REVIEW'
        
        return BABESIA


# result object
class Observation:

    def __init__(self):
        self.oru  = oru()
        self.universal_service_id = self.oru['service_id']
        self.method = self.oru['method']

        # time objects
        self.msh_time = datetime.now()
        

        self.obx_time = (self.msh_time - timedelta(minutes=np.random.normal(1, 0.5)))
        
        if self.method == 'SYSMEX':
        	self.obs_end_time = (self.obx_time - timedelta(minutes=np.random.normal(25, 5)))
        else:
        	self.obs_end_time = (self.obx_time - timedelta(minutes=np.random.normal(15, 3)))        

        self.req_time = (self.obs_end_time - timedelta(minutes=np.random.normal(20, 5)))
           
        # result status
        self.result_status = 'Verified'