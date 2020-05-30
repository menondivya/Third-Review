import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def getCost(val1,val2,val3):
# 	Flame sensor- 0 or 1
# 	difficulty sensor - 0 or 1
# 	Distance - 0 to 150cm
# 	conditionerature - 0 to 50degree
	difficulty=ctrl.Antecedent(np.arange(0,100,1),'difficulty')
	distance=ctrl.Antecedent(np.arange(0,500,10),'distance')
	condition=ctrl.Antecedent(np.arange(0,100,1),'condition')
	cost=ctrl.Consequent(np.arange(0,10,1),'cost')


	difficulty['low']=fuzz.trapmf(difficulty.universe,[-2.2,-1.1,0,50])
	difficulty['medium']=fuzz.trimf(difficulty.universe,[0,50,100])
	difficulty['high']=fuzz.trapmf(difficulty.universe,[50,100,100.1,100.2])

	distance['low']=fuzz.trapmf(distance.universe,[-0.9,-0.8,0,250])
	distance['medium']=fuzz.trimf(distance.universe,[0,250,500])
	distance['high']=fuzz.trapmf(distance.universe,[250,500,500.1,500.2])

	condition['low']=fuzz.trapmf(condition.universe,[-2,-1,0,50])
	condition['medium']=fuzz.trimf(condition.universe,[0,50,100])
	condition['high']=fuzz.trapmf(condition.universe,[20,100,100.1,100.2])

	cost['low']=fuzz.trapmf(cost.universe,[-0.2,-0.1,0,3])
	cost['medium']=fuzz.trimf(cost.universe,[3,5,7])
	cost['high']=fuzz.trapmf(cost.universe,[7,10,10.1,10.2])

	rule1 = ctrl.Rule(distance['high'] & difficulty['high'] & condition['high'] , cost['low'])
	rule2 = ctrl.Rule(distance['high'] & difficulty['high'] & condition['medium'] , cost['low'])
	rule3 = ctrl.Rule(distance['high'] & difficulty['high'] & condition['low'] , cost['medium'])
	rule4 = ctrl.Rule(distance['high'] & difficulty['medium'] & condition['high'] , cost['medium'])
	rule5 = ctrl.Rule(distance['high'] & difficulty['medium'] & condition['medium'] , cost['medium'])
	rule6 = ctrl.Rule(distance['high'] & difficulty['medium'] & condition['low'] , cost['medium'])
	rule7 = ctrl.Rule(distance['high'] & difficulty['low'] & condition['high'] , cost['medium'])
	rule8 = ctrl.Rule(distance['high'] & difficulty['low'] & condition['medium'] , cost['medium'])
	rule9 = ctrl.Rule(distance['high'] & difficulty['low'] & condition['low'] , cost['medium'])
	rule10 = ctrl.Rule(distance['medium'] & difficulty['high'] & condition['high'] , cost['low'])
	rule11 = ctrl.Rule(distance['medium'] & difficulty['high'] & condition['medium'] , cost['high'])
	rule12 = ctrl.Rule(distance['medium'] & difficulty['high'] & condition['low'] , cost['medium'])
	rule13 = ctrl.Rule(distance['medium'] & difficulty['medium'] & condition['high'] , cost['medium'])
	rule14 = ctrl.Rule(distance['medium'] & difficulty['medium'] & condition['medium'] , cost['medium'])
	rule15 = ctrl.Rule(distance['medium'] & difficulty['medium'] & condition['low'] , cost['medium'])
	rule16 = ctrl.Rule(distance['medium'] & difficulty['low'] & condition['high'] , cost['medium'])
	rule17 = ctrl.Rule(distance['medium'] & difficulty['low'] & condition['medium'] , cost['low'])
	rule18 = ctrl.Rule(distance['medium'] & difficulty['low'] & condition['low'] , cost['low'])
	rule19 = ctrl.Rule(distance['low'] & difficulty['high'] & condition['high'] , cost['high'])
	rule20 = ctrl.Rule(distance['low'] & difficulty['high'] & condition['medium'] , cost['medium'])
	rule21 = ctrl.Rule(distance['low'] & difficulty['high'] & condition['low'] , cost['medium'])
	rule22 = ctrl.Rule(distance['low'] & difficulty['medium'] & condition['high'] , cost['medium'])
	rule23 = ctrl.Rule(distance['low'] & difficulty['medium'] & condition['medium'] , cost['low'])
	rule24 = ctrl.Rule(distance['low'] & difficulty['medium'] & condition['low'] , cost['medium'])
	rule25 = ctrl.Rule(distance['low'] & difficulty['low'] & condition['high'] , cost['medium'])
	rule26 = ctrl.Rule(distance['low'] & difficulty['low'] & condition['medium'] , cost['high'])
	rule27 = ctrl.Rule(distance['low'] & difficulty['low'] & condition['low'] , cost['high'])

	
	cost_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
	cost = ctrl.ControlSystemSimulation(cost_ctrl)
	cost.input['distance'] = val1
	cost.input['difficulty'] = val2
	cost.input['condition'] = val3
	cost.compute()
	return(round(cost.output['cost']))
