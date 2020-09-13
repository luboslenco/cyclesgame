from arm.logicnode.arm_nodes import *

class GetScaleNode(ArmLogicTreeNode):
    """Get scale node"""
    bl_idname = 'LNGetScaleNode'
    bl_label = 'Get Scale'

    def init(self, context):
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('NodeSocketVector', 'Scale')

add_node(GetScaleNode, category=PKG_AS_CATEGORY, section='scale')