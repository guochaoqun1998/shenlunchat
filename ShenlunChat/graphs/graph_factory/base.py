#@Author: guochaoqun  
#@Date: 2024-08-04 14:32:52  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 14:32:52 

from typing import Dict, Union, Callable
from langgraph.graph import StateGraph, START, END

from ShenlunChat.graphs.agent_nodes.factory import AgentNodeFactory
from ShenlunChat.graphs.agent_nodes.base import  AgentNodeConfig
from ShenlunChat.graphs.tool_nodes.base import ToolNodeConfig

class GraphConfig():
    graph = None
    agent_node_dict = None
    tool_node_dict = None
    build_config = None
    build_method = None
    input_cls = None
    output_cls = None
    schema_cls = None

class GraphBuilder():
    """这是graph的创建基类"""
    @staticmethod
    def get_graph(agentnode_config_dict:Dict,
                  tool_node_dict:Dict[str,ToolNodeConfig], 
                  build_config:Dict,
                  build_method:Union[None,Callable])->GraphConfig:
        """创造一个graph"""
        config = GraphConfig()

        config.tool_node_dict = tool_node_dict
        config.build_config = build_config
        config.build_method = build_method

        agent_node_dict = GraphBuilder.get_agent_nodes(agentnode_config_dict)
        graph = GraphBuilder.build(agent_node_dict, tool_node_dict, build_config, build_method)

        config.agent_node_dict = agent_node_dict
        config.input_cls = graph.input
        config.output_cls = graph.output
        config.schema_cls = graph.schema

        graph = graph.compile()
        config.graph = graph

        return config

    @staticmethod
    def get_agent_nodes(agentnode_config_dict) -> Dict[str, AgentNodeConfig]:
        agent_node_dict = {}
        for agentnode_name, config in agentnode_config_dict.items():
            agent_node_dict[agentnode_name] = AgentNodeFactory.create_agent_node(**config)
        return agent_node_dict

    @staticmethod
    def build(agent_node_dict: Dict[str, AgentNodeConfig], 
              tool_node_dict, 
              build_config=None, 
              build_method=None)->StateGraph:
        assert build_config is None or build_method is None, "build_config and build_method could only choose one, rather than both"
        assert build_config is not None or build_method is not None, "build_config and build_method could not be both None"
        # 自定义构建函数
        if build_method is not None:
            return build_method(agent_node_dict, tool_node_dict)
        
        def split_type_and_name(node_name):
            node_type, name=  node_name.split(":")
            assert node_type in ["agent", "tool"], f"node_type {node_type} is not in ['agent', 'tool']"
            return node_type, name

        # 默认构建函数
        ## 规则: config包含有以下信息：
        ### 1. config["agent_nodes"]: 一个list，包含了agent node的名字
        ### 2. config["tool_nodes"]: 一个list，包含了tool node的名字
        ### 3. config["edges"]: List[Tuple[str, str]]，包含了node之间的直接连接。 （对于直接连接：只能用于一对一）
        ### 另外， 这里可以有 END， START
        ### 4. config["conditional_edge"]: List[Tuple[str, callable, Dict{str:str}]]，包含了node之间的条件连接。 （对于条件连接：可以用于一对多）
        ### 第一个str 表示起始的node， 第二个 route， 第三个dcit表示mapping.
        ### 5. config["state"]: 会规定  state_schema， input, output 用到的是谁到input_state / output_state.
        ### 格式为： "state_schema": (agent:name, 'input_state' or 'output_state')

        # 1. 获取 input_state, output_state, state_schema
        state_config = dict()
        for key in ["input", "output", "state_schema"]:
            if build_config["state"].get(key) is not None:
                state_name = build_config["state"][key][1]
                type_name, name = split_type_and_name(build_config["state"][key][0])
                if type_name == "agent":
                    config = agent_node_dict[name]
                elif type_name == "tool":
                    config = tool_node_dict[name]
                state_config[key] = getattr(config, state_name) 
        assert len(state_config)>0, "state_config is empty"

        # 2. 创建graph 
        graph = StateGraph(**state_config)
        
        # 3. 添加agent node
        for agent_node_name in build_config["agent_nodes"]:
            agent_config = agent_node_dict[agent_node_name]
            graph.add_node(agent_node_name,agent_config.agent_node)

        # 4. 添加tool node
        if build_config.get("tool_nodes", None) is not None:
            for tool_node_name in build_config["tool_nodes"]:
                tool_config = tool_node_dict[tool_node_name]
                graph.add_node(tool_node_name,tool_config.tool_node)
        
        # 5. 添加边
        for edge in build_config["edges"]:
            start, end = edge
            assert start == START or start in agent_node_dict or start in tool_node_dict, f"start node {start} not in agent_node_dict or tool_node_dict"
            assert end == END or end in agent_node_dict or end in tool_node_dict, f"end node {end} not in agent_node_dict or tool_node_dict"
            graph.add_edge(start, end)

        # 6. 添加条件边
        if build_config.get("conditional_edge",None) is not None:
            for edge in build_config["conditional_edge"]:
                start, route, mapping_dict = edge
                assert start == START or start in agent_node_dict or start in tool_node_dict, f"start node {start} not in agent_node_dict or tool_node_dict"
                if isinstance(mapping_dict,dict):
                    for end in mapping_dict.values():
                        assert end == END or end in agent_node_dict or end in tool_node_dict, f"end node {end} not in agent_node_dict or tool_node_dict"
                elif isinstance(mapping_dict, list):
                    for end in mapping_dict:
                        assert end == END or end in agent_node_dict or end in tool_node_dict, f"end node {end} not in agent_node_dict or tool_node_dict"
                graph.add_conditional_edges(start, route, mapping_dict)
            
        # # 7. 编译
        # graph = graph.compile()
        return graph

class GraphBase():
    agentnode_config_dict = None
    tool_node_dict = None
    build_config = None
    build_method = None

    def create_graph(self):
        # print("config： ", self.build_config)
        config = GraphBuilder.get_graph(self.agentnode_config_dict, 
                                     self.tool_node_dict,
                                     self.build_config, 
                                     self.build_method)
        return config