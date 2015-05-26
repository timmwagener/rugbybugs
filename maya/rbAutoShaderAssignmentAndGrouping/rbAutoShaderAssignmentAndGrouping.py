




#rbAutoShaderAssignmentAndGrouping Module
#----------------------------------------------------

'''
Description:
Module to automatically group and assign shaders to animation assets

ToDo:
-

'''



#Import
#----------------------------------------------------
import pymel.core as pm






#RbAutoShaderAssignmentAndGrouping Class
#----------------------------------------------------

class RbAutoShaderAssignmentAndGrouping():
	
	
	
	#Constructor
	def __init__(self):
		
		#Instance Vars
		#----------------------------------------------------
		
		#Debug
		self.verbose = True
		self.chrystalGroupsCount = 51
		
		
		
		
		#Shader Assignment Dict
		#----------------------------------------------------
		
		self.genericAssetAssignmentDict = {'material_mt' : 'pCube1', 'material2_mt': ['pCube2', 'pCube3'], 'material3_mt' : 'pCube4'}
		
		
		#rugbybug
		#----------------------------------------------------
		
		self.rugbybugAssignmentDict = { 'Bug_WingsUpper_Main_Mt': ['left_wing_upper', 'right_wing_upper', 'carapace_3', 'carapace_2', 'left_carapace_1', 'right_carapace_1'], 
		'Bug_LowerBody_Main_Mt' : 'inner_body_back',
		'Bug_Wings_Main_Mt' : ['left_wing_lower', 'right_wing_lower'],
		'Bug_Eye_Main_Mt' : ['left_eye', 'right_eye'],
		'Bug_BodyInner_Guts_Main_Mt' : 'Bug_Inner_Guts',
		'Bug_Legs_Main_Mt' : ['left_front_foot_2', 'left_front_foot_1', 'left_front_leg_3', 'left_front_leg_2', 'left_front_leg_1', 'left_middle_foot_4', 'left_middle_foot_5', 'left_middle_toe_1', 'left_middle_toe_2', 'left_middle_toe_3', 'left_end_leg_1', 'left_end_leg_2', 'left_end_leg_3', 'left_end_foot_1', 'left_end_foot_2', 'left_end_foot_3', 'left_end_foot_4', 'left_end_foot_5', 'right_nipper', 'left_antenna_head_base', 'left_antenna_head_tip', 'right_antenna_head_base', 'right_antenna_head_tip', 'left_antenna_mouth_base', 'left_antenna_mouth_tip', 'right_antenna_mouth_base', 'right_antenna_mouth_tip', 'left_mouth', 'right_mouth', 'right_end_leg_1', 'right_end_leg_2', 'right_end_leg_3', 'right_end_foot_1', 'right_end_foot_2', 'right_end_foot_3', 'right_end_foot_4', 'right_end_foot_5', 'right_end_toe_1', 'right_end_toe_2', 'right_end_toe_3', 'left_nipper', 'right_front_toe_2', 'right_front_toe_3', 'right_middle_leg_1', 'right_middle_leg_2', 'right_middle_leg_3', 'right_middle_foot_1', 'right_middle_foot_2', 'right_middle_foot_3', 'right_middle_foot_4', 'right_middle_foot_5', 'right_middle_toe_1', 'right_middle_toe_2', 'right_middle_toe_3', 'left_front_foot_3', 'left_front_foot_4', 'left_front_foot_5', 'left_front_toe_1', 'left_front_toe_2', 'left_front_toe_3', 'left_middle_leg_1', 'left_middle_leg_2', 'left_middle_leg_3', 'left_middle_foot_1', 'left_middle_foot_2', 'left_middle_foot_3', 'head', 'bottom_plate_front', 'bottom_plate_back', 'inner_body_front', 'left_end_toe_1', 'left_end_toe_2', 'left_end_toe_3', 'right_front_leg_1', 'right_front_leg_2', 'right_front_leg_3', 'right_front_foot_1', 'right_front_foot_2', 'right_front_foot_3', 'right_front_foot_4', 'right_front_foot_5', 'right_front_toe_1']}
		
		
		#ant
		#----------------------------------------------------
		
		self.antAssignmentDict = {'antMiddle02_main_mt' : 'middle_body_middle',
		'antHead_main_mt' : ['left_mouth', 'right_mouth', 'head'],
		'antMiddle01_main_mt' : 'middle_body_tip',
		'antMiddle03_main_mt' : ['left_middle_foot_1', 'left_front_foot_1', 'left_tooth_10', 'right_tooth_1', 'right_tooth_2', 'right_tooth_3', 'right_tooth_4', 'right_tooth_5', 'right_tooth_6', 'right_tooth_7', 'right_tooth_8', 'right_tooth_9', 'right_tooth_10', 'middle_body_base', 'left_tooth_1', 'left_tooth_2', 'left_tooth_3', 'left_tooth_4', 'left_tooth_5', 'left_tooth_6', 'left_tooth_7', 'left_tooth_8', 'left_tooth_9', 'right_end_foot_1', 'right_front_foot_1', 'right_middle_foot_1', 'left_end_foot_1'],
		'antLegs_main_mt' : ['left_middle_leg_3', 'left_middle_leg_2', 'right_front_leg_2', 'left_front_leg_3', 'left_front_leg_2', 'right_end_leg_2', 'right_end_leg_3', 'right_front_leg_3', 'right_middle_leg_2', 'right_middle_leg_3', 'left_end_leg_3', 'left_end_leg_2'],
		'antLegsAtt_main_mt' : ['left_middle_leg_1', 'right_front_leg_1', 'left_front_leg_1', 'right_end_leg_1', 'right_middle_leg_1', 'left_end_leg_1'],
		'antBack_main_mt' : ['left_end_foot_4', 'left_end_foot_5', 'left_end_foot_3', 'left_middle_foot_5', 'left_middle_foot_4', 'left_middle_foot_3', 'left_middle_foot_2', 'left_front_foot_9', 'left_front_foot_8', 'left_end_foot_6', 'left_end_foot_7', 'left_end_foot_8', 'left_end_foot_9', 'left_front_foot_7', 'left_front_foot_6', 'left_front_foot_5', 'left_front_foot_4', 'left_front_foot_3', 'left_front_foot_2', 'booty', 'booty_bridge', 'right_middle_foot_6', 'right_middle_foot_7', 'right_middle_foot_8', 'right_middle_foot_9', 'right_end_foot_2', 'right_end_foot_6', 'right_end_foot_3', 'right_end_foot_4', 'right_end_foot_5', 'right_front_foot_2', 'right_front_foot_5', 'right_front_foot_3', 'right_front_foot_4', 'right_front_foot_6', 'right_front_foot_7', 'right_front_foot_8', 'right_front_foot_9', 'right_middle_foot_2', 'right_middle_foot_3', 'right_middle_foot_4', 'right_middle_foot_5', 'left_end_foot_2', 'left_middle_foot_8', 'left_middle_foot_9', 'left_middle_foot_7', 'left_middle_foot_6', 'right_antenna_head_tip_4', 'right_antenna_head_tip_5', 'right_antenna_head_tip_6', 'right_antenna_head_tip_7', 'right_antenna_head_tip_8', 'right_antenna_head_tip_9', 'right_antenna_head_tip_10', 'right_antenna_head_tip_11', 'right_antenna_head_tip_12', 'right_antenna_head_tip_13', 'right_antenna_head_tip_14', 'left_antenna_head_tip_9', 'left_antenna_head_tip_10', 'left_antenna_head_tip_11', 'left_antenna_head_tip_12', 'left_antenna_head_tip_13', 'left_antenna_head_tip_14', 'right_antenna_head_base', 'right_antenna_head_tip_1', 'right_antenna_head_tip_2', 'right_antenna_head_tip_3', 'right_end_foot_7', 'right_end_foot_8', 'right_end_foot_9', 'left_antenna_head_base', 'left_antenna_head_tip_1', 'left_antenna_head_tip_2', 'left_antenna_head_tip_3', 'left_antenna_head_tip_4', 'left_antenna_head_tip_5', 'left_antenna_head_tip_6', 'left_antenna_head_tip_7', 'left_antenna_head_tip_8'],
		'eyes_main_mt' : ['left_eye', 'right_eye'],
		'antenna_tip_main_mt' : ['right_antenna_head_tip_16', 'right_antenna_head_tip_17', 'right_antenna_head_tip_15', 'left_antenna_head_tip_15', 'left_antenna_head_tip_16', 'left_antenna_head_tip_17']
		}
		
		
		#frog
		#----------------------------------------------------
		
		self.frogAssignmentDict = {'Frog_Main_Mt' : 'body',
		'Frog_MouthInner_Main_Mt' : 'inner_mouth',
		'Frog_Eyelids_Main_Mt' : ['left_eyelid', 'right_eyelid'],
		'Frog_Eyes_Main_Mt' : ['left_eye', 'right_eye'],
		'Frog_Tongue_Main_Mt' : 'tongue'
		}
		
		
		
		
		
		
		
		
		
		#Group Lists
		#----------------------------------------------------
		
		
		#rugbybug
		#----------------------------------------------------
		
		self.rugbybug_carapace_grp_list = ['left_carapace_1', 'right_carapace_1', 'carapace_2', 'carapace_3']
		self.rugbybug_wings_grp_list = ['left_wing_lower', 'left_wing_upper', 'right_wing_lower', 'right_wing_upper']
		
		
		self.rugbybug_left_front_leg_grp_list = ['left_front_leg_2', 'left_front_leg_3', 'left_front_leg_1', 'left_front_toe_1', 'left_front_toe_2', 'left_front_toe_3', 'left_front_foot_1', 'left_front_foot_2', 'left_front_foot_3', 'left_front_foot_4', 'left_front_foot_5']
		self.rugbybug_left_middle_leg_grp_list = ['left_middle_leg_1', 'left_middle_leg_2', 'left_middle_leg_3', 'left_middle_foot_1', 'left_middle_foot_2', 'left_middle_foot_3', 'left_middle_foot_4', 'left_middle_foot_5', 'left_middle_toe_1', 'left_middle_toe_2', 'left_middle_toe_3']
		self.rugbybug_left_end_leg_grp_list = ['left_end_leg_1', 'left_end_leg_2', 'left_end_leg_3', 'left_end_toe_1', 'left_end_toe_2', 'left_end_toe_3', 'left_end_foot_1', 'left_end_foot_2', 'left_end_foot_3', 'left_end_foot_4', 'left_end_foot_5']
		
		self.rugbybug_left_front_arm_grp_list = ['left_front_arm_1', 'left_front_arm_2', 'left_front_arm_3', 'left_front_hand_1', 'left_front_hand_2', 'left_front_hand_3', 'left_front_hand_4', 'left_front_hand_5', 'left_front_finger_1', 'left_front_finger_2', 'left_front_finger_3']
		
		
		self.rugbybug_right_front_leg_grp_list = ['right_front_leg_1', 'right_front_leg_2', 'right_front_leg_3', 'right_front_toe_1', 'right_front_toe_2', 'right_front_toe_3', 'right_front_foot_1', 'right_front_foot_2', 'right_front_foot_3', 'right_front_foot_4', 'right_front_foot_5']
		self.rugbybug_right_middle_leg_grp_list = ['right_middle_leg_1', 'right_middle_leg_2', 'right_middle_leg_3', 'right_middle_toe_1', 'right_middle_toe_2', 'right_middle_toe_3', 'right_middle_foot_1', 'right_middle_foot_2', 'right_middle_foot_3', 'right_middle_foot_4', 'right_middle_foot_5']
		self.rugbybug_right_end_leg_grp_list = ['right_end_leg_1', 'right_end_leg_2', 'right_end_leg_3', 'right_end_foot_1', 'right_end_foot_2', 'right_end_foot_3', 'right_end_foot_4', 'right_end_foot_5', 'right_end_toe_1', 'right_end_toe_2', 'right_end_toe_3']
		
		self.rugbybug_right_front_arm_grp_list = ['right_front_arm_1', 'right_front_arm_2', 'right_front_arm_3', 'right_front_hand_1', 'right_front_hand_2', 'right_front_hand_3', 'right_front_hand_4', 'right_front_hand_5', 'right_front_finger_1', 'right_front_finger_2', 'right_front_finger_3']
		
		self.rugbybug_body_lower_grp_list = ['bottom_plate_back', 'bottom_plate_front', 'inner_body_back', 'inner_body_front']
		self.rugbybug_head_grp_list = ['left_eye', 'right_eye', 'left_mouth', 'right_mouth', 'head', 'left_antenna_head_tip', 'left_antenna_head_base', 'right_antenna_head_base', 'right_antenna_head_tip', 'left_antenna_mouth_base', 'left_antenna_mouth_tip', 'right_antenna_mouth_base', 'right_antenna_mouth_tip', 'right_nipper', 'left_nipper']
		
		
		
		
		#ant
		#----------------------------------------------------
		
		self.ant_left_front_arm_grp_list = ['left_front_arm_1', 'left_front_arm_2', 'left_front_arm_3', 'left_front_hand_1', 'left_front_hand_2', 'left_front_hand_3', 'left_front_hand_4', 'left_front_hand_5', 'left_front_hand_6', 'left_front_hand_7', 'left_front_hand_8', 'left_front_hand_9']
		self.ant_left_middle_arm_grp_list = ['left_middle_arm_1', 'left_middle_arm_2', 'left_middle_arm_3', 'left_middle_hand_1', 'left_middle_hand_2', 'left_middle_hand_3', 'left_middle_hand_4', 'left_middle_hand_5', 'left_middle_hand_6', 'left_middle_hand_7', 'left_middle_hand_8', 'left_middle_hand_9']
		
		self.ant_right_front_arm_grp_list = ['right_front_arm_1', 'right_front_arm_2', 'right_front_arm_3', 'right_front_hand_1', 'right_front_hand_2', 'right_front_hand_3', 'right_front_hand_4', 'right_front_hand_5', 'right_front_hand_6', 'right_front_hand_7', 'right_front_hand_8', 'right_front_hand_9']
		self.ant_right_middle_arm_grp_list = ['right_middle_arm_1', 'right_middle_arm_2', 'right_middle_arm_3', 'right_middle_hand_1', 'right_middle_hand_2', 'right_middle_hand_3', 'right_middle_hand_4', 'right_middle_hand_5', 'right_middle_hand_6', 'right_middle_hand_7', 'right_middle_hand_8', 'right_middle_hand_9']
		
		
		self.ant_left_front_leg_grp_list = ['left_front_leg_1', 'left_front_leg_2', 'left_front_leg_3', 'left_front_foot_1', 'left_front_foot_2', 'left_front_foot_3', 'left_front_foot_4', 'left_front_foot_5', 'left_front_foot_6', 'left_front_foot_7', 'left_front_foot_8', 'left_front_foot_9']
		self.ant_left_middle_leg_grp_list = ['left_middle_leg_1', 'left_middle_leg_2', 'left_middle_leg_3', 'left_middle_foot_1', 'left_middle_foot_2', 'left_middle_foot_3', 'left_middle_foot_4', 'left_middle_foot_5', 'left_middle_foot_6', 'left_middle_foot_7', 'left_middle_foot_8', 'left_middle_foot_9']
		self.ant_left_end_leg_grp_list = ['left_end_leg_1', 'left_end_leg_2', 'left_end_leg_3', 'left_end_foot_1', 'left_end_foot_2', 'left_end_foot_3', 'left_end_foot_4', 'left_end_foot_5', 'left_end_foot_6', 'left_end_foot_7', 'left_end_foot_8', 'left_end_foot_9']
		
		self.ant_right_front_leg_grp_list = ['right_front_leg_1', 'right_front_leg_2', 'right_front_leg_3', 'right_front_foot_1', 'right_front_foot_2', 'right_front_foot_3', 'right_front_foot_4', 'right_front_foot_5', 'right_front_foot_6', 'right_front_foot_7', 'right_front_foot_8', 'right_front_foot_9']
		self.ant_right_middle_leg_grp_list = ['right_middle_leg_1', 'right_middle_leg_2', 'right_middle_leg_3', 'right_middle_foot_1', 'right_middle_foot_2', 'right_middle_foot_3', 'right_middle_foot_4', 'right_middle_foot_5', 'right_middle_foot_6', 'right_middle_foot_7', 'right_middle_foot_8', 'right_middle_foot_9']
		self.ant_right_end_leg_grp_list = ['right_end_leg_1', 'right_end_leg_2', 'right_end_leg_3', 'right_end_foot_1', 'right_end_foot_2', 'right_end_foot_3', 'right_end_foot_4', 'right_end_foot_5', 'right_end_foot_6', 'right_end_foot_7', 'right_end_foot_8', 'right_end_foot_9']
		
		
		self.ant_head_grp_list = ['left_eye', 'right_eye', 'left_mouth', 'right_mouth', 'head']
		self.ant_antenna_head_grp_list = ['left_antenna_head_base', 'left_antenna_head_tip_1', 'left_antenna_head_tip_2', 'left_antenna_head_tip_3', 'left_antenna_head_tip_4', 'left_antenna_head_tip_5', 'left_antenna_head_tip_6', 'left_antenna_head_tip_7', 'left_antenna_head_tip_8', 'left_antenna_head_tip_9', 'left_antenna_head_tip_10', 'left_antenna_head_tip_11', 'left_antenna_head_tip_12', 'left_antenna_head_tip_13', 'left_antenna_head_tip_14', 'left_antenna_head_tip_15', 'left_antenna_head_tip_16', 'left_antenna_head_tip_17', 'right_antenna_head_base', 'right_antenna_head_tip_1', 'right_antenna_head_tip_2', 'right_antenna_head_tip_3', 'right_antenna_head_tip_4', 'right_antenna_head_tip_5', 'right_antenna_head_tip_6', 'right_antenna_head_tip_7', 'right_antenna_head_tip_8', 'right_antenna_head_tip_9', 'right_antenna_head_tip_10', 'right_antenna_head_tip_11', 'right_antenna_head_tip_12', 'right_antenna_head_tip_13', 'right_antenna_head_tip_14', 'right_antenna_head_tip_15', 'right_antenna_head_tip_16', 'right_antenna_head_tip_17']
		self.ant_left_tooth_grp_list = ['left_tooth_1', 'left_tooth_2', 'left_tooth_3', 'left_tooth_4', 'left_tooth_5', 'left_tooth_6', 'left_tooth_7', 'left_tooth_8', 'left_tooth_9', 'left_tooth_10']
		self.ant_right_tooth_grp_list = ['right_tooth_1', 'right_tooth_2', 'right_tooth_3', 'right_tooth_4', 'right_tooth_5', 'right_tooth_6', 'right_tooth_7', 'right_tooth_8', 'right_tooth_9', 'right_tooth_10']
		
		
		self.ant_middle_body_grp_list = ['middle_body_base', 'middle_body_middle', 'middle_body_tip']
		self.ant_booty_grp_list = ['booty', 'booty_bridge']
		
		
		
		
		#frog
		#----------------------------------------------------
		
		self.frog_grp_list = ['left_eye', 'right_eye', 'left_eyelid', 'right_eyelid', 'tongue', 'body', 'inner_mouth']
		
		
		
		
		#chrystal
		#----------------------------------------------------
		
		#chrystal lights and inner parts
		self.inner_chrystal_grp_list = ['inner_chrystal', 'inner_chrystal_logo']
		self.inner_chrystal_rockremainder_grp_list = ['inner_chrystal_rockremainder_0', 'inner_chrystal_rockremainder_1', 'inner_chrystal_rockremainder_2']
		self.inner_chrystal_lights_grp_list = ['inner_chrystal_light_center', 'inner_chrystal_light_a_1', 'inner_chrystal_light_a_2', 'inner_chrystal_light_b_1', 'inner_chrystal_light_b_2']
		self.chrystal_intermediary_lights_grp_list = ['chrystal_intermediary_light_center', 'chrystal_intermediary_light_a_1', 'chrystal_intermediary_light_a_2', 'chrystal_intermediary_light_b_1', 'chrystal_intermediary_light_b_2']
		
		#innerHull
		self.piece_0_innerHull_grp_list = ['piece_0_innerHull']
		self.piece_1_innerHull_grp_list = ['piece_1_innerHull']
		self.piece_2_innerHull_grp_list = ['piece_2_innerHull']
		self.piece_3_innerHull_grp_list = ['piece_3_innerHull']
		self.piece_4_innerHull_grp_list = ['piece_4_innerHull']
		self.piece_5_innerHull_grp_list = ['piece_5_innerHull']
		self.piece_6_innerHull_grp_list = ['piece_6_innerHull']
		self.piece_7_innerHull_grp_list = ['piece_7_innerHull']
		self.piece_8_innerHull_grp_list = ['piece_8_innerHull']
		self.piece_9_innerHull_grp_list = ['piece_9_innerHull']
		
		self.piece_10_innerHull_grp_list = ['piece_10_innerHull']
		self.piece_11_innerHull_grp_list = ['piece_11_innerHull']
		self.piece_12_innerHull_grp_list = ['piece_12_innerHull']
		self.piece_13_innerHull_grp_list = ['piece_13_innerHull']
		self.piece_14_innerHull_grp_list = ['piece_14_innerHull']
		self.piece_15_innerHull_grp_list = ['piece_15_innerHull']
		self.piece_16_innerHull_grp_list = ['piece_16_innerHull']
		self.piece_17_innerHull_grp_list = ['piece_17_innerHull']
		self.piece_18_innerHull_grp_list = ['piece_18_innerHull']
		self.piece_19_innerHull_grp_list = ['piece_19_innerHull']
		
		self.piece_20_innerHull_grp_list = ['piece_20_innerHull']
		self.piece_21_innerHull_grp_list = ['piece_21_innerHull']
		self.piece_22_innerHull_grp_list = ['piece_22_innerHull']
		self.piece_23_innerHull_grp_list = ['piece_23_innerHull']
		self.piece_24_innerHull_grp_list = ['piece_24_innerHull']
		self.piece_25_innerHull_grp_list = ['piece_25_innerHull']
		self.piece_26_innerHull_grp_list = ['piece_26_innerHull']
		self.piece_27_innerHull_grp_list = ['piece_27_innerHull']
		self.piece_28_innerHull_grp_list = ['piece_28_innerHull']
		self.piece_29_innerHull_grp_list = ['piece_29_innerHull']
		
		self.piece_30_innerHull_grp_list = ['piece_30_innerHull']
		self.piece_31_innerHull_grp_list = ['piece_31_innerHull']
		self.piece_32_innerHull_grp_list = ['piece_32_innerHull']
		self.piece_33_innerHull_grp_list = ['piece_33_innerHull']
		self.piece_34_innerHull_grp_list = ['piece_34_innerHull']
		self.piece_35_innerHull_grp_list = ['piece_35_innerHull']
		self.piece_36_innerHull_grp_list = ['piece_36_innerHull']
		self.piece_37_innerHull_grp_list = ['piece_37_innerHull']
		self.piece_38_innerHull_grp_list = ['piece_38_innerHull']
		self.piece_39_innerHull_grp_list = ['piece_39_innerHull']
		
		self.piece_40_innerHull_grp_list = ['piece_40_innerHull']
		self.piece_41_innerHull_grp_list = ['piece_41_innerHull']
		self.piece_42_innerHull_grp_list = ['piece_42_innerHull']
		self.piece_43_innerHull_grp_list = ['piece_43_innerHull']
		self.piece_44_innerHull_grp_list = ['piece_44_innerHull']
		self.piece_45_innerHull_grp_list = ['piece_45_innerHull']
		self.piece_46_innerHull_grp_list = ['piece_46_innerHull']
		self.piece_47_innerHull_grp_list = ['piece_47_innerHull']
		self.piece_48_innerHull_grp_list = ['piece_48_innerHull']
		self.piece_49_innerHull_grp_list = ['piece_49_innerHull']
		
		self.piece_50_innerHull_grp_list = ['piece_50_innerHull']
		
		
		#outerHull
		self.piece_0_outerHull_grp_list = ['piece_0_outerHull']
		self.piece_1_outerHull_grp_list = ['piece_1_outerHull']
		self.piece_2_outerHull_grp_list = ['piece_2_outerHull']
		self.piece_3_outerHull_grp_list = ['piece_3_outerHull']
		self.piece_4_outerHull_grp_list = ['piece_4_outerHull']
		self.piece_5_outerHull_grp_list = ['piece_5_outerHull']
		self.piece_6_outerHull_grp_list = ['piece_6_outerHull']
		self.piece_7_outerHull_grp_list = ['piece_7_outerHull']
		self.piece_8_outerHull_grp_list = ['piece_8_outerHull']
		self.piece_9_outerHull_grp_list = ['piece_9_outerHull']
		
		self.piece_10_outerHull_grp_list = ['piece_10_outerHull']
		self.piece_11_outerHull_grp_list = ['piece_11_outerHull']
		self.piece_12_outerHull_grp_list = ['piece_12_outerHull']
		self.piece_13_outerHull_grp_list = ['piece_13_outerHull']
		self.piece_14_outerHull_grp_list = ['piece_14_outerHull']
		self.piece_15_outerHull_grp_list = ['piece_15_outerHull']
		self.piece_16_outerHull_grp_list = ['piece_16_outerHull']
		self.piece_17_outerHull_grp_list = ['piece_17_outerHull']
		self.piece_18_outerHull_grp_list = ['piece_18_outerHull']
		self.piece_19_outerHull_grp_list = ['piece_19_outerHull']
		
		self.piece_20_outerHull_grp_list = ['piece_20_outerHull']
		self.piece_21_outerHull_grp_list = ['piece_21_outerHull']
		self.piece_22_outerHull_grp_list = ['piece_22_outerHull']
		self.piece_23_outerHull_grp_list = ['piece_23_outerHull']
		self.piece_24_outerHull_grp_list = ['piece_24_outerHull']
		self.piece_25_outerHull_grp_list = ['piece_25_outerHull']
		self.piece_26_outerHull_grp_list = ['piece_26_outerHull']
		self.piece_27_outerHull_grp_list = ['piece_27_outerHull']
		self.piece_28_outerHull_grp_list = ['piece_28_outerHull']
		self.piece_29_outerHull_grp_list = ['piece_29_outerHull']
		
		self.piece_30_outerHull_grp_list = ['piece_30_outerHull']
		self.piece_31_outerHull_grp_list = ['piece_31_outerHull']
		self.piece_32_outerHull_grp_list = ['piece_32_outerHull']
		self.piece_33_outerHull_grp_list = ['piece_33_outerHull']
		self.piece_34_outerHull_grp_list = ['piece_34_outerHull']
		self.piece_35_outerHull_grp_list = ['piece_35_outerHull']
		self.piece_36_outerHull_grp_list = ['piece_36_outerHull']
		self.piece_37_outerHull_grp_list = ['piece_37_outerHull']
		self.piece_38_outerHull_grp_list = ['piece_38_outerHull']
		self.piece_39_outerHull_grp_list = ['piece_39_outerHull']
		
		self.piece_40_outerHull_grp_list = ['piece_40_outerHull']
		self.piece_41_outerHull_grp_list = ['piece_41_outerHull']
		self.piece_42_outerHull_grp_list = ['piece_42_outerHull']
		self.piece_43_outerHull_grp_list = ['piece_43_outerHull']
		self.piece_44_outerHull_grp_list = ['piece_44_outerHull']
		self.piece_45_outerHull_grp_list = ['piece_45_outerHull']
		self.piece_46_outerHull_grp_list = ['piece_46_outerHull']
		self.piece_47_outerHull_grp_list = ['piece_47_outerHull']
		self.piece_48_outerHull_grp_list = ['piece_48_outerHull']
		self.piece_49_outerHull_grp_list = ['piece_49_outerHull']
		
		self.piece_50_outerHull_grp_list = ['piece_50_outerHull']
		
		
		#intermediary
		self.piece_0_intermediary_grp_list = ['piece_0_intermediary_0', 'piece_0_intermediary_1']
		self.piece_1_intermediary_grp_list = ['piece_1_intermediary_0']
		self.piece_2_intermediary_grp_list = ['piece_2_intermediary_0']
		self.piece_3_intermediary_grp_list = ['piece_3_intermediary_0']
		self.piece_4_intermediary_grp_list = ['piece_4_intermediary_0']
		self.piece_5_intermediary_grp_list = ['piece_5_intermediary_0']
		self.piece_6_intermediary_grp_list = ['piece_6_intermediary_0']
		self.piece_7_intermediary_grp_list = ['piece_7_intermediary_0']
		self.piece_8_intermediary_grp_list = ['piece_8_intermediary_0']
		self.piece_9_intermediary_grp_list = ['piece_9_intermediary_0', 'piece_9_intermediary_1']
		
		self.piece_10_intermediary_grp_list = ['piece_10_intermediary_0', 'piece_10_intermediary_1']
		self.piece_11_intermediary_grp_list = ['piece_11_intermediary_0', 'piece_11_intermediary_1']
		self.piece_12_intermediary_grp_list = ['piece_12_intermediary_0', 'piece_12_intermediary_1']
		self.piece_13_intermediary_grp_list = ['piece_13_intermediary_0', 'piece_13_intermediary_1']
		self.piece_14_intermediary_grp_list = ['piece_14_intermediary_0', 'piece_14_intermediary_1']
		self.piece_15_intermediary_grp_list = ['piece_15_intermediary_0']
		self.piece_16_intermediary_grp_list = ['piece_16_intermediary_0']
		self.piece_17_intermediary_grp_list = ['piece_17_intermediary_0']
		self.piece_18_intermediary_grp_list = ['piece_18_intermediary_0']
		self.piece_19_intermediary_grp_list = ['piece_19_intermediary_0']
		
		self.piece_20_intermediary_grp_list = ['piece_20_intermediary_0']
		self.piece_21_intermediary_grp_list = ['piece_21_intermediary_0']
		self.piece_22_intermediary_grp_list = ['piece_22_intermediary_0']
		self.piece_23_intermediary_grp_list = ['piece_23_intermediary_0', 'piece_23_intermediary_1', 'piece_23_intermediary_2']
		self.piece_24_intermediary_grp_list = ['piece_24_intermediary_0', 'piece_24_intermediary_1']
		self.piece_25_intermediary_grp_list = ['piece_25_intermediary_0', 'piece_25_intermediary_1']
		self.piece_26_intermediary_grp_list = ['piece_26_intermediary_0', 'piece_26_intermediary_1']
		self.piece_27_intermediary_grp_list = ['piece_27_intermediary_0', 'piece_27_intermediary_1']
		self.piece_28_intermediary_grp_list = ['piece_28_intermediary_0', 'piece_28_intermediary_1']
		self.piece_29_intermediary_grp_list = ['piece_29_intermediary_0', 'piece_29_intermediary_1']
		
		self.piece_30_intermediary_grp_list = ['piece_30_intermediary_0', 'piece_30_intermediary_1']
		self.piece_31_intermediary_grp_list = ['piece_31_intermediary_0', 'piece_31_intermediary_1']
		self.piece_32_intermediary_grp_list = ['piece_32_intermediary_0']
		self.piece_33_intermediary_grp_list = ['piece_33_intermediary_0']
		self.piece_34_intermediary_grp_list = ['piece_34_intermediary_0']
		self.piece_35_intermediary_grp_list = ['piece_35_intermediary_0']
		self.piece_36_intermediary_grp_list = ['piece_36_intermediary_0']
		self.piece_37_intermediary_grp_list = ['piece_37_intermediary_0']
		self.piece_38_intermediary_grp_list = ['piece_38_intermediary_0', 'piece_38_intermediary_1']
		self.piece_39_intermediary_grp_list = ['piece_39_intermediary_0', 'piece_39_intermediary_1']
		
		self.piece_40_intermediary_grp_list = ['piece_40_intermediary_0', 'piece_40_intermediary_1']
		self.piece_41_intermediary_grp_list = ['piece_41_intermediary_0', 'piece_41_intermediary_1']
		self.piece_42_intermediary_grp_list = ['piece_42_intermediary_0', 'piece_42_intermediary_1']
		self.piece_43_intermediary_grp_list = ['piece_43_intermediary_0', 'piece_43_intermediary_1']
		self.piece_44_intermediary_grp_list = ['piece_44_intermediary_0', 'piece_44_intermediary_1']
		self.piece_45_intermediary_grp_list = ['piece_45_intermediary_0', 'piece_45_intermediary_1']
		self.piece_46_intermediary_grp_list = ['piece_46_intermediary_0', 'piece_46_intermediary_1']
		self.piece_47_intermediary_grp_list = ['piece_47_intermediary_0', 'piece_47_intermediary_1']
		self.piece_48_intermediary_grp_list = ['piece_48_intermediary_0', 'piece_48_intermediary_1']
		self.piece_49_intermediary_grp_list = ['piece_49_intermediary_0', 'piece_49_intermediary_1']
		
		self.piece_50_intermediary_grp_list = ['piece_50_intermediary_0', 'piece_50_intermediary_1']
	
	
	
	
	
	
	
	
	#Toplevel Methods
	#----------------------------------------------------
	
	
	
	#Shader Assignment
	#----------------------------------------------------
	
	
	#assignMaterials
	def assignMaterials(self, assignmentDict):
		
		#get active selection
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if selectionList empty
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select geometry to assign shaders.')
			return None
			
		
		#build materialList and objectList
		
		materialList = []
		objectList = []
		
		for key in assignmentDict:
			
			#append materialList
			materialList.append(key)
			
			#append objectList
			#if value of key is a list iterate it and append each value to objectlist
			if(type(assignmentDict[key]) is list):
				for value in assignmentDict[key]:
					objectList.append(value)
			#else just append value
			else: objectList.append(assignmentDict[key])
			
		
		#print built material and object lists if verbose = True
		if(self.verbose):
			print('\n')
			print('Material List:\n--------------------')
			print(materialList)
			print('\n')
			print('Object List:\n--------------------')
			print(objectList)
			print('\n')
		
		
		#get missing materials list
		missingMaterialsList = self.getMissingMaterials(materialList)
	
		
		#check if all materials exists in scene
		if(missingMaterialsList):
			if(self.verbose): 
				print('Not all shaders needed to assign are present in the scene.\nThe following materials are missing:')
				for material in missingMaterialsList:
					print(material)
			return None
			
		
		
		
		
		
		#Iterate selectionList and assign shader
		for object in selectionList:
			
			#get objectName without namespaces
			objectNameNoNamespace = self.removeNamespace(object.name())
			
			
			#check if object is in objectList
			if not(objectNameNoNamespace in objectList):
				if(self.verbose): print(objectNameNoNamespace +' not in dictionary for shader assignment. Skipping object')
				continue
			
			
			
			#materialToAssign
			materialToAssign = None
			
			#iterate through assignmentDict and find shader for object
			for key in assignmentDict:
			
			
				#if value of key is a list iterate it and check if value is object to be assigned
				if(type(assignmentDict[key]) is list):
					for value in assignmentDict[key]:
						if(value == objectNameNoNamespace): 
							materialToAssign = key
							break
				#else just append value
				else: 
					if(assignmentDict[key] == objectNameNoNamespace): 
						materialToAssign = key
						break
						
			
			#Get shadinggroup pynode from material
			material, shadingGroup = self.getShadingEngineForMaterial(materialToAssign)


			#Assign material to object
			pm.sets(shadingGroup, edit=1, forceElement = object)
			
			#print log
			if(self.verbose): print(object.name() +' --> ' +material.name())
		
		
		#Success Msg
		if(self.verbose): print('Successfully assigned shaders')
	
	
	
	
	
	
	
	
	
	#Grouping
	#----------------------------------------------------
	
	
	#groupRugbybug
	def groupRugbybug(self):
		
		
		
		#get active selection
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if selectionList empty
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select geometry to assign shaders.')
			return None
		
		
		
		
		
		#Create groups
		#----------------------------------------------------
		
		pm.select(cl = True)
		carapace_grp = pm.group(n = 'carapace_grp')
		pm.select(cl = True)
		wings_grp = pm.group(n = 'wings_grp')
		
		pm.select(cl = True)
		left_front_leg_grp = pm.group(n = 'left_front_leg_grp')
		pm.select(cl = True)
		left_middle_leg_grp = pm.group(n = 'left_middle_leg_grp')
		pm.select(cl = True)
		left_end_leg_grp = pm.group(n = 'left_end_leg_grp')
		
		pm.select(cl = True)
		left_front_arm_grp = pm.group(n = 'left_front_arm_grp')
		
		pm.select(cl = True)
		right_front_leg_grp = pm.group(n = 'right_front_leg_grp')
		pm.select(cl = True)
		right_middle_leg_grp = pm.group(n = 'right_middle_leg_grp')
		pm.select(cl = True)		
		right_end_leg_grp =  pm.group(n = 'right_end_leg_grp')
		
		pm.select(cl = True)
		right_front_arm_grp = pm.group(n = 'right_front_arm_grp')
		
		pm.select(cl = True)
		body_lower_grp =  pm.group(n = 'body_lower_grp')
		pm.select(cl = True)
		head_grp = pm.group(n = 'head_grp')
		
		
		pm.select(cl = True)
		legs_grp = pm.group(n = 'legs_grp')
		
		pm.select(cl = True)
		arms_grp = pm.group(n = 'arms_grp')
		
		pm.select(cl = True)
		rugbybug_grp = pm.group(n = 'rugbybug_grp')
		
		
		
		
		
		#Parent groups
		#----------------------------------------------------
		
		pm.select(cl = True)
		pm.parent(left_front_leg_grp, left_middle_leg_grp, left_end_leg_grp, right_front_leg_grp, right_middle_leg_grp, right_end_leg_grp, legs_grp)
		
		pm.select(cl = True)
		pm.parent(left_front_arm_grp, right_front_arm_grp, arms_grp)
		
		pm.select(cl = True)
		pm.parent(carapace_grp, wings_grp, legs_grp, arms_grp, body_lower_grp, head_grp, rugbybug_grp)
		pm.select(cl = True)
		
		
		
		
		
		
		#Sort Selectionlist in groups
		#----------------------------------------------------
		
		for object in selectionList:
			
			#get objectName without namespaces
			objectNameNoNamespaces = self.removeNamespace(object.name())
			
			
			#Test for existence in all lists, if found parent and continue
			
			if(objectNameNoNamespaces in self.rugbybug_carapace_grp_list):
				pm.select(cl = True)
				pm.parent(object, carapace_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.rugbybug_wings_grp_list):
				pm.select(cl = True)
				pm.parent(object, wings_grp)
				pm.select(cl = True)
				continue
				
			

			#left legs
			
			if(objectNameNoNamespaces in self.rugbybug_left_front_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_front_leg_grp)
				pm.select(cl = True)
				continue
			
			if(objectNameNoNamespaces in self.rugbybug_left_middle_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_middle_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.rugbybug_left_end_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_end_leg_grp)
				pm.select(cl = True)
				continue
			

			#left arm
			
			if(objectNameNoNamespaces in self.rugbybug_left_front_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_front_arm_grp)
				pm.select(cl = True)
				continue
				
			
			#right legs
			
			if(objectNameNoNamespaces in self.rugbybug_right_front_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_front_leg_grp)
				pm.select(cl = True)
				continue
			
			if(objectNameNoNamespaces in self.rugbybug_right_middle_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_middle_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.rugbybug_right_end_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_end_leg_grp)
				pm.select(cl = True)
				continue
			
			#right arm
			
			if(objectNameNoNamespaces in self.rugbybug_right_front_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_front_arm_grp)
				pm.select(cl = True)
				continue
				
			
			#body lower
			
			if(objectNameNoNamespaces in self.rugbybug_body_lower_grp_list):
				pm.select(cl = True)
				pm.parent(object, body_lower_grp)
				pm.select(cl = True)
				continue
				
				
			#head
			
			if(objectNameNoNamespaces in self.rugbybug_head_grp_list):
				pm.select(cl = True)
				pm.parent(object, head_grp)
				pm.select(cl = True)
				continue
	
	
	
	
	
	
	
	
	
	
	#groupAnt
	def groupAnt(self):
		
		
		
		#get active selection
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if selectionList empty
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select geometry to assign shaders.')
			return None
		
		
		
		
		
		#Create groups
		#----------------------------------------------------
		
		
		pm.select(cl = True)
		left_front_arm_grp = pm.group(n = 'left_front_arm_grp')
		pm.select(cl = True)
		left_middle_arm_grp = pm.group(n = 'left_middle_arm_grp')
		
		pm.select(cl = True)
		right_front_arm_grp = pm.group(n = 'right_front_arm_grp')
		pm.select(cl = True)
		right_middle_arm_grp = pm.group(n = 'right_middle_arm_grp')
		
		
		pm.select(cl = True)
		left_front_leg_grp = pm.group(n = 'left_front_leg_grp')
		pm.select(cl = True)
		left_middle_leg_grp = pm.group(n = 'left_middle_leg_grp')
		pm.select(cl = True)
		left_end_leg_grp = pm.group(n = 'left_end_leg_grp')
		
		
		pm.select(cl = True)
		right_front_leg_grp = pm.group(n = 'right_front_leg_grp')
		pm.select(cl = True)
		right_middle_leg_grp = pm.group(n = 'right_middle_leg_grp')
		pm.select(cl = True)
		right_end_leg_grp = pm.group(n = 'right_end_leg_grp')
		
		
		pm.select(cl = True)
		head_grp = pm.group(n = 'head_grp')
		pm.select(cl = True)
		antenna_head_grp = pm.group(n = 'antenna_head_grp')
		pm.select(cl = True)
		left_tooth_grp = pm.group(n = 'left_tooth_grp')
		pm.select(cl = True)
		right_tooth_grp = pm.group(n = 'right_tooth_grp')
		
		
		pm.select(cl = True)
		middle_body_grp = pm.group(n = 'middle_body_grp')
		pm.select(cl = True)
		booty_grp = pm.group(n = 'booty_grp')
		
		
		pm.select(cl = True)
		arms_grp = pm.group(n = 'arms_grp')
		
		pm.select(cl = True)
		legs_grp = pm.group(n = 'legs_grp')
		
		pm.select(cl = True)
		ant_grp = pm.group(n = 'ant_grp')
		
		
		
		
		
		#Parent groups
		#----------------------------------------------------
	
		pm.select(cl = True)
		pm.parent(left_front_arm_grp, left_middle_arm_grp, right_front_arm_grp, right_middle_arm_grp, arms_grp)
		
		pm.select(cl = True)
		pm.parent(left_front_leg_grp, left_middle_leg_grp, left_end_leg_grp, right_front_leg_grp, right_middle_leg_grp, right_end_leg_grp ,legs_grp)
		
		pm.select(cl = True)
		pm.parent(antenna_head_grp,left_tooth_grp, right_tooth_grp , head_grp)
		
		pm.select(cl = True)
		pm.parent(booty_grp, middle_body_grp, head_grp, arms_grp, legs_grp, ant_grp)
		pm.select(cl = True)
		
		
		
		
		#Sort Selectionlist in groups
		#----------------------------------------------------
	
		for object in selectionList:
			
			#get objectName without namespaces
			objectNameNoNamespaces = self.removeNamespace(object.name())
			
			
			#Test for existence in all lists, if found parent and continue
			
			
			#arms
			
			if(objectNameNoNamespaces in self.ant_left_front_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_front_arm_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_left_middle_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_middle_arm_grp)
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.ant_right_front_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_front_arm_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_right_middle_arm_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_middle_arm_grp)
				pm.select(cl = True)
				continue
				
				
				
			#legs
			
			if(objectNameNoNamespaces in self.ant_left_front_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_front_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_left_middle_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_middle_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_left_end_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_end_leg_grp)
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.ant_right_front_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_front_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_right_middle_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_middle_leg_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_right_end_leg_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_end_leg_grp)
				pm.select(cl = True)
				continue
				
				
			
			#head
			
			if(objectNameNoNamespaces in self.ant_head_grp_list):
				pm.select(cl = True)
				pm.parent(object, head_grp)
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.ant_antenna_head_grp_list):
				pm.select(cl = True)
				pm.parent(object, antenna_head_grp)
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.ant_left_tooth_grp_list):
				pm.select(cl = True)
				pm.parent(object, left_tooth_grp)
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.ant_right_tooth_grp_list):
				pm.select(cl = True)
				pm.parent(object, right_tooth_grp)
				pm.select(cl = True)
				continue
				
				
			#body
			
			if(objectNameNoNamespaces in self.ant_middle_body_grp_list):
				pm.select(cl = True)
				pm.parent(object, middle_body_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.ant_booty_grp_list):
				pm.select(cl = True)
				pm.parent(object, booty_grp)
				pm.select(cl = True)
				continue
			
	
	
	
	
	
	
	#groupFrog
	def groupFrog(self):
		
		
		
		#get active selection
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if selectionList empty
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select geometry to assign shaders.')
			return None
		
		
		
		
		
		#Create groups
		#----------------------------------------------------
		
		pm.select(cl = True)
		frog_grp = pm.group(n = 'frog_grp')
		pm.select(cl = True)
		
		
		
		
		
		
		#Sort Selectionlist in groups
		#----------------------------------------------------
	
		for object in selectionList:
			
			#get objectName without namespaces
			objectNameNoNamespaces = self.removeNamespace(object.name())
			
			
			#Test for existence in all lists, if found parent and continue
			
				
			if(objectNameNoNamespaces in self.frog_grp_list):
				pm.select(cl = True)
				pm.parent(object, frog_grp)
				pm.select(cl = True)
				continue
	
	
	
	
	
	
	
	#groupChrystal
	def groupChrystal(self):
		
		
		
		#get active selection
		selectionList = pm.ls(sl = True, fl = True, type = 'transform')
		pm.select(cl = True)
		
		#check if selectionList empty
		if not(selectionList):
			if(self.verbose): print('No objects selected, please select geometry to do grouping.')
			return None
		
		
		
		
		
		#Create groups
		#----------------------------------------------------
		
		pm.select(cl = True)
		chrystal_grp = pm.group(n = 'chrystal_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		innerHull_grp = pm.group(n = 'innerHull_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		outerHull_grp = pm.group(n = 'outerHull_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		intermediary_grp = pm.group(n = 'intermediary_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		innerChrystal_grp = pm.group(n = 'innerChrystal_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		chrystal_meshlights_grp = pm.group(n = 'chrystal_meshlights_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		inner_chrystal_lights_grp = pm.group(n = 'inner_chrystal_lights_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		chrystal_intermediary_lights_grp = pm.group(n = 'chrystal_intermediary_lights_grp')
		pm.select(cl = True)
		
		pm.select(cl = True)
		inner_chrystal_rockremainder_grp = pm.group(n = 'inner_chrystal_rockremainder_grp')
		pm.select(cl = True)
		
		
		#innerHull_piece_groups_list
		innerHull_piece_groups_list = []
		for index in range(self.chrystalGroupsCount):
			pm.select(cl = True)
			innerHull_piece_groups_list.append(pm.group(n = 'piece_' +str(index) +'_innerHull_grp'))
			pm.select(cl = True)
			
		#outerHull_piece_groups_list
		outerHull_piece_groups_list = []
		for index in range(self.chrystalGroupsCount):
			pm.select(cl = True)
			outerHull_piece_groups_list.append(pm.group(n = 'piece_' +str(index) +'_outerHull_grp'))
			pm.select(cl = True)
			
		#intermediary_piece_groups_list
		intermediary_piece_groups_list = []
		for index in range(self.chrystalGroupsCount):
			pm.select(cl = True)
			intermediary_piece_groups_list.append(pm.group(n = 'piece_' +str(index) +'_intermediary_grp'))
			pm.select(cl = True)
	
	
	
		
		
		
		
		#Parent groups
		#----------------------------------------------------
	
		pm.select(cl = True)
		pm.parent(innerHull_grp, outerHull_grp, intermediary_grp, innerChrystal_grp, chrystal_meshlights_grp, inner_chrystal_rockremainder_grp, chrystal_grp)
		
		pm.select(cl = True)
		pm.parent(inner_chrystal_lights_grp, chrystal_intermediary_lights_grp, chrystal_meshlights_grp)
		
		pm.select(cl = True)
		pm.parent(innerHull_piece_groups_list, innerHull_grp)
		
		pm.select(cl = True)
		pm.parent(outerHull_piece_groups_list, outerHull_grp)
		
		pm.select(cl = True)
		pm.parent(intermediary_piece_groups_list, intermediary_grp)
		pm.select(cl = True)
		
		
		
		
		
		#Sort Selectionlist in groups
		#----------------------------------------------------
	
		for object in selectionList:
			
			#get objectName without namespaces
			objectNameNoNamespaces = self.removeNamespace(object.name())
			
			
			#Test for existence in all lists, if found parent and continue
			
				
			if(objectNameNoNamespaces in self.inner_chrystal_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerChrystal_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.inner_chrystal_rockremainder_grp_list):
				pm.select(cl = True)
				pm.parent(object, inner_chrystal_rockremainder_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.inner_chrystal_lights_grp_list):
				pm.select(cl = True)
				pm.parent(object, inner_chrystal_lights_grp)
				pm.select(cl = True)
				continue
				
			if(objectNameNoNamespaces in self.chrystal_intermediary_lights_grp_list):
				pm.select(cl = True)
				pm.parent(object, chrystal_intermediary_lights_grp)
				pm.select(cl = True)
				continue
				
				
				
			
			#innerHull
			if(objectNameNoNamespaces in self.piece_0_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[0])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_1_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[1])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_2_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[2])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_3_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[3])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_4_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[4])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_5_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[5])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_6_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[6])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_7_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[7])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_8_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[8])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_9_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[9])
				pm.select(cl = True)
				continue
				
				
				
			if(objectNameNoNamespaces in self.piece_10_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[10])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_11_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[11])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_12_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[12])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_13_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[13])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_14_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[14])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_15_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[15])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_16_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[16])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_17_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[17])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_18_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[18])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_19_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[19])
				pm.select(cl = True)
				continue
				
				
			
			
			if(objectNameNoNamespaces in self.piece_20_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[20])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_21_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[21])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_22_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[22])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_23_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[23])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_24_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[24])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_25_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[25])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_26_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[26])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_27_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[27])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_28_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[28])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_29_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[29])
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.piece_30_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[30])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_31_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[31])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_32_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[32])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_33_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[33])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_34_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[34])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_35_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[35])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_36_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[36])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_37_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[37])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_38_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[38])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_39_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[39])
				pm.select(cl = True)
				continue
				
				
			
			if(objectNameNoNamespaces in self.piece_40_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[40])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_41_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[41])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_42_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[42])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_43_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[43])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_44_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[44])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_45_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[45])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_46_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[46])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_47_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[47])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_48_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[48])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_49_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[49])
				pm.select(cl = True)
				continue
				
			
			if(objectNameNoNamespaces in self.piece_50_innerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, innerHull_piece_groups_list[50])
				pm.select(cl = True)
				continue
				
				
				
				
				
				
				
				
			#outerHull
			if(objectNameNoNamespaces in self.piece_0_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[0])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_1_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[1])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_2_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[2])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_3_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[3])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_4_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[4])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_5_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[5])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_6_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[6])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_7_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[7])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_8_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[8])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_9_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[9])
				pm.select(cl = True)
				continue
				
				
				
			if(objectNameNoNamespaces in self.piece_10_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[10])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_11_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[11])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_12_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[12])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_13_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[13])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_14_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[14])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_15_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[15])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_16_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[16])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_17_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[17])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_18_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[18])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_19_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[19])
				pm.select(cl = True)
				continue
				
				
			
			
			if(objectNameNoNamespaces in self.piece_20_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[20])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_21_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[21])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_22_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[22])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_23_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[23])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_24_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[24])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_25_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[25])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_26_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[26])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_27_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[27])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_28_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[28])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_29_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[29])
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.piece_30_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[30])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_31_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[31])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_32_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[32])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_33_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[33])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_34_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[34])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_35_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[35])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_36_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[36])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_37_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[37])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_38_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[38])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_39_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[39])
				pm.select(cl = True)
				continue
				
				
			
			if(objectNameNoNamespaces in self.piece_40_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[40])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_41_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[41])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_42_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[42])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_43_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[43])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_44_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[44])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_45_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[45])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_46_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[46])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_47_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[47])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_48_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[48])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_49_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[49])
				pm.select(cl = True)
				continue
				
			
			if(objectNameNoNamespaces in self.piece_50_outerHull_grp_list):
				pm.select(cl = True)
				pm.parent(object, outerHull_piece_groups_list[50])
				pm.select(cl = True)
				continue
				
				
				
				
				
				
			#intermediary
			if(objectNameNoNamespaces in self.piece_0_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[0])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_1_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[1])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_2_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[2])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_3_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[3])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_4_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[4])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_5_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[5])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_6_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[6])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_7_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[7])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_8_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[8])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_9_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[9])
				pm.select(cl = True)
				continue
				
				
				
			if(objectNameNoNamespaces in self.piece_10_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[10])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_11_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[11])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_12_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[12])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_13_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[13])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_14_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[14])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_15_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[15])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_16_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[16])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_17_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[17])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_18_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[18])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_19_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[19])
				pm.select(cl = True)
				continue
				
				
			
			
			if(objectNameNoNamespaces in self.piece_20_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[20])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_21_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[21])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_22_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[22])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_23_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[23])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_24_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[24])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_25_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[25])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_26_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[26])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_27_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[27])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_28_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[28])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_29_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[29])
				pm.select(cl = True)
				continue
				
				
			if(objectNameNoNamespaces in self.piece_30_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[30])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_31_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[31])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_32_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[32])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_33_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[33])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_34_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[34])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_35_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[35])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_36_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[36])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_37_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[37])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_38_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[38])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_39_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[39])
				pm.select(cl = True)
				continue
				
				
			
			if(objectNameNoNamespaces in self.piece_40_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[40])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_41_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[41])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_42_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[42])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_43_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[43])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_44_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[44])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_45_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[45])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_46_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[46])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_47_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[47])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_48_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[48])
				pm.select(cl = True)
				continue
			if(objectNameNoNamespaces in self.piece_49_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[49])
				pm.select(cl = True)
				continue
				
			
			if(objectNameNoNamespaces in self.piece_50_intermediary_grp_list):
				pm.select(cl = True)
				pm.parent(object, intermediary_piece_groups_list[50])
				pm.select(cl = True)
				continue
		
		
		
		
		pm.select(cl = True)
		
		
		
		
	
	
	
	#Methods
	#----------------------------------------------------
	
	
	#getMissingMaterials
	def getMissingMaterials(self, materialList):
		
		#get all sceneMaterials
		sceneMaterialsList = pm.ls(fl = True, mat = True)
		
		
		#existingMaterialsList
		existingMaterialsList = []
		
		#Iterate sceneMaterialsLIst and append to existingMaterialsList when name is in materialList
		for material in sceneMaterialsList:
			if(self.removeNamespace(material.name()) in materialList): existingMaterialsList.append(self.removeNamespace(material.name()))
		
		
		#missingMaterialsList
		missingMaterialsList = []
		
		#Iterate materialsList and append to missingMaterialsLIst when material not in existingMaterialsList
		for material in materialList:
			if(material not in existingMaterialsList): missingMaterialsList.append(material)
		
		return missingMaterialsList
		
		
	
	#getShadingEngineForMaterial
	def getShadingEngineForMaterial(self, materialName):
		
		#get all sceneMaterials
		sceneMaterialsList = pm.ls(fl = True, mat = True)
		
		#materialToGetShadingEngine for
		materialToGetShadingEngineFor = None
		
		#Iterate sceneMaterialsLIst get pynode of material to get shading engine for
		for material in sceneMaterialsList:
			if(self.removeNamespace(material.name()) == materialName): 
				materialToGetShadingEngineFor = material
				break
			
			
		
		#return materialShadingEngine
		return [materialToGetShadingEngineFor , pm.listFuture(materialToGetShadingEngineFor, type = 'shadingEngine')[0]]
	
	
	
	
	
	
	#Shared Methods
	#----------------------------------------------------
	
	
	
	
	#removeNamespace
	def removeNamespace(self, name):
		
		return name.split(':')[-1]
	
	
	
		
	
	
		
#Execute Temp
#----------------------------------------------------

'''
from rugbyBugs.maya.rbAutoShaderAssignmentAndGrouping import rbAutoShaderAssignmentAndGrouping

#Reload if true
doReload = True
if(doReload): reload(rbAutoShaderAssignmentAndGrouping)

#Create Instance if it doesnt exist
rbAutoShaderAssignmentAndGroupingInstance = rbAutoShaderAssignmentAndGrouping.RbAutoShaderAssignmentAndGrouping()

#assign Ant
#rbAutoShaderAssignmentAndGroupingInstance.assignMaterials(rbAutoShaderAssignmentAndGroupingInstance.antAssignmentDict)

#groupAnt
rbAutoShaderAssignmentAndGroupingInstance.groupAnt()
'''


	
	
	