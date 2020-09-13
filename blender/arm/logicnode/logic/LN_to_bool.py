from arm.logicnode.arm_nodes import *

class ToBoolNode(ArmLogicTreeNode):
    """To Bool Node"""
    bl_idname = 'LNToBoolNode'
    bl_label = 'To Bool'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('NodeSocketBool', 'Bool')

add_node(ToBoolNode, category=PKG_AS_CATEGORY)