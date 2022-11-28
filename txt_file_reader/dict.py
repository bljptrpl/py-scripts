# create a dictionary library
import pandas as pd
dict = [{ 'C1_CALC_GRP_L' : ['CALC_GRP_CD','CalculationGroupLanguageInfo', 'CalculationGroupCd']},
{ 'C1_CALC_GRP_L' : ['DESCR100','CalculationGroupLanguageInfo', 'Description100']},
{ 'C1_CALC_GRP_L' : ['DESCRLONG','CalculationGroupLanguageInfo', 'DetailedDescription']},
{ 'C1_CALC_GRP_L' : ['LANGUAGE_CD','CalculationGroupLanguageInfo', 'LanguageCd']},
{ 'C1_CALC_GRP_L' : ['VERSION','CalculationGroupLanguageInfo', 'VersionNum']},
{ 'C1_CALC_RULE' : ['BF_CD','CalculationRuleInfo', 'BillFactorCd']},
{ 'C1_CALC_RULE' : ['BO_DATA_AREA','CalculationRuleInfo', 'BusinessObjectDataArea']},
{ 'C1_CALC_RULE' : ['BUS_OBJ_CD','CalculationRuleInfo', 'BusinessObjectCd']},
{ 'C1_CALC_RULE' : ['CALC_GRP_CD','CalculationRuleInfo', 'CalculationGroupCd']},
{ 'C1_CALC_RULE' : ['CALC_RULE_CD', 'CalculationRuleInfo', 'CalculationRuleCd']}
] 

d2 = {'C1_CALC_GRP_L' : ['CALC_GRP_CD','CalculationGroupLanguageInfo', 'CalculationGroupCd'],
'C1_CALC_GRP_L' : ['DESCR100','CalculationGroupLanguageInfo', 'Description100'], 
'C1_CALC_GRP_L' : ['DESCRLONG','CalculationGroupLanguageInfo', 'DetailedDescription'],
'C1_CALC_RULE' : ['CALC_RULE_CD', 'CalculationRuleInfo', 'CalculationRuleCd']
}

# d3 = {
#      'C1_CALC_GRP_L', 'CALC_GRP_CD': ['CalculationGroupLanguageInfo', 'CalculationGroupCd'],
#  'C1_CALC_GRP_L', 'DESCR100': ['CalculationGroupLanguageInfo', 'Description100'],
#  'C1_CALC_GRP_L', 'DESCRLONG': ['CalculationGroupLanguageInfo', 'DetailedDescription'],
#  'C1_CALC_GRP_L', 'LANGUAGE_CD': ['CalculationGroupLanguageInfo', 'LanguageCd'],
#  'C1_CALC_GRP_L', 'VERSION': ['CalculationGroupLanguageInfo', 'VersionNum'],
#  'C1_CALC_RULE', 'BF_CD': ['CalculationRuleInfo', 'BillFactorCd'],
#  'C1_CALC_RULE', 'BO_DATA_AREA': ['CalculationRuleInfo', 'BusinessObjectDataArea'],
#  'C1_CALC_RULE', 'BUS_OBJ_CD': ['CalculationRuleInfo', 'BusinessObjectCd'],
#  'C1_CALC_RULE', 'CALC_GRP_CD': ['CalculationRuleInfo', 'CalculationGroupCd'],
#  'C1_CALC_RULE', 'CALC_RULE_CD': ['CalculationRuleInfo', 'CalculationRuleCd'],
#  'C1_CALC_RULE', 'CALC_RULE_STEP_ALG_CD': ['CalculationRuleInfo', 'StepMultiplierAlgorithm'],
#  'C1_CALC_RULE', 'CALC_RULE_VAL_ALG_CD': ['CalculationRuleInfo', 'CalcRuleValueAlgorithm'],
#  'C1_CALC_RULE', 'CR_EXEC_SEQ': ['CalculationRuleInfo', 'CrExecSequenceNum'],
#  'C1_CALC_RULE', 'DST_ID': ['CalculationRuleInfo', 'DistributionId'],
#  'C1_CALC_RULE', 'ITEM_TYPE_CD': ['CalculationRuleInfo', 'ItemTypeCd'],
#  'C1_CALC_RULE', 'REF_CALC_GRP_CD': ['CalculationRuleInfo', 'RefCalculationGroupCd'],
# }
d = {}

d['CI_CALC_RULE'] = ['id', 'personName']

d3 = {
     'C1_CALC_GRP_L': {'CALC_GRP_CD': ['CalculationGroupLanguageInfo', 'CalculationGroupCd'], 
     'DESCR100': ['CalculationGroupLanguageInfo', 'Description100'],
    'DESCRLONG': ['CalculationGroupLanguageInfo', 'DetailedDescription'],
    'LANGUAGE_CD': ['CalculationGroupLanguageInfo', 'LanguageCd'],
    'VERSION': ['CalculationGroupLanguageInfo', 'VersionNum']},
'C1_CALC_RULE': {'BF_CD': ['CalculationRuleInfo', 'BillFactorCd'],
    'BO_DATA_AREA': ['CalculationRuleInfo', 'BusinessObjectDataArea'],
    'BUS_OBJ_CD': ['CalculationRuleInfo', 'BusinessObjectCd'],
    'CALC_GRP_CD': ['CalculationRuleInfo', 'CalculationGroupCd'],
    'CALC_RULE_CD': ['CalculationRuleInfo', 'CalculationRuleCd'],
    'CALC_RULE_STEP_ALG_CD': ['CalculationRuleInfo', 'StepMultiplierAlgorithm'],
    'CALC_RULE_VAL_ALG_CD': ['CalculationRuleInfo', 'CalcRuleValueAlgorithm'],
    'CR_EXEC_SEQ': ['CalculationRuleInfo', 'CrExecSequenceNum'],
    'DST_ID': ['CalculationRuleInfo', 'DistributionId'],
    'ITEM_TYPE_CD': ['CalculationRuleInfo', 'ItemTypeCd'],
    'REF_CALC_GRP_CD': ['CalculationRuleInfo', 'RefCalculationGroupCd']}
}


for i in range(8):
    #print(d['CI_CALC_RULE'])
    #print(d2['C1_CALC_GRP_L'])
    print(d3['C1_CALC_GRP_L']['DESCR100'])