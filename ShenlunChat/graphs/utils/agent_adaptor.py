
from typing import Any, Dict, List, Tuple, Union, TypedDict, Callable

# from pydantic import BaseModel
from langchain_core.pydantic_v1 import BaseModel, Field

class AgentNodeWrapper():
    def __init__(self,
                 agent,
                 input_state,
                 output_state,
                 input_mappings:Dict[Tuple,Tuple],
                 output_mappings:Dict[Tuple,Tuple]) -> None:
        """在这个修饰器中，主要用于给一个agent创建一个agent node节点
        agent:  可以使用 invoke函数, llm或者agent
        input_state: 输入的状态, BaseModel 或者Typedict
        output_state: 输出的状态, BaseModel 或者Typedict
        output_model: 输出的模型, BaseModel 或者Typedict
        input_mappings: 输入的键值对. 例如: [("key_in_level1", "key_in_level2")]， 每一个tuple都定义了从 input_state 中取值的路径
        output_mappings: 输出的键值对. 例如: {("key_in_level1", "key_in_level2"),("key_in_level1","key_in_level2")}， 每一个tuple都定义了从 output_state 中取值的路径
        """
        self.agent = agent
        self.input_state = input_state
        self.output_state = output_state
        self.input_mappings = input_mappings
        self.output_mappings = output_mappings
        assert len(self.input_mappings) >0 and len(self.output_mappings) >0, "input_mappings and output_mappings must be a list"
        # 查看 input_mappings 和 output_mappings 是否在 input_state 和 output_state 中
        ## state可能是一个多层级的BaseModel
        ##TODO: 这里需要检查input_state和output_state是否是BaseModel或者TypedDict

    def __call__(self, state):
        """这个修饰器主要用于给一个agent创建一个agent, 
        输入类型是input_state, 
        输出类型是output_state,
        """
        print("=== In Agent node： Start ")
        agent_input = dict()
        for key,value in self.input_mappings.items():
            agent_input.update(self.build_dict_from_tuple(value, self.get_attr_from_tuple(state, key)))
        agent_output = self.agent.invoke(agent_input)

        output_dict = dict()
        if isinstance(agent_output,BaseModel):
            for key, value in self.output_mappings.items():
                output_dict.update(self.build_dict_from_tuple(value,self.get_attr_from_tuple(agent_output,key)))
        elif isinstance(agent_output,dict):
            for key, value in self.output_mappings.items():
                output_dict.update(self.build_dict_from_tuple(value,self.get_keys_from_tuple(agent_output,key)))
        else:
            raise ValueError("agent_output must be a dict or a BaseModel")
        print("=== In Agent node： End ")
        return output_dict

    def get_attr_from_tuple(self, state, keys:Tuple[str]):
        """从state中根据tuple的路径获取值
        """
        attr = state
        for key in keys:
            # print("checking key: {} in attr: {}".format(key, attr))
            assert hasattr(attr, key), f"{attr} has no attribute {key}"
            attr = getattr(attr, key)
        return attr

    def get_keys_from_tuple(self, state, keys:Tuple[str]):
        """从state中根据tuple的路径获取值, state是一个dict
        """
        attr = state
        for key in keys:
            assert key in attr, f"{attr} has no attribute {key}"
            attr = attr[key]
        return attr

    def build_dict_from_tuple(self, keys:Tuple[str], value:Any):
        """根据tuple和value 最终形成嵌套的dict
        """
        output_dict = {}
        current_dict = output_dict
        for key in keys[:-1]:
            current_dict[key] = {}
            current_dict = current_dict[key]
        current_dict[keys[-1]] = value
        return output_dict
    
    # def set_attr_from_tuple(self, state, keys:Tuple[str], value:Any):
    #     """从state中根据tuple的路径设置值
    #     """
    #     attr = state
    #     for key in keys[:-1]:
    #         assert hasattr(attr, key), f"{attr} has no attribute {key}"
    #         attr = getattr(attr, key)
    #     setattr(attr, keys[-1], value)
    #     return state