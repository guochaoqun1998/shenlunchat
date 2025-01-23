#@Author: guochaoqun  
#@Date: 2024-08-04 15:36:28  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 15:36:28 

from ShenlunChat.graphs.graph_factory.split_points_graph import SplitPointsGraph
from ShenlunChat.graphs.graph_factory.split_small_points_graph import SplitSmallPointsGraph
from ShenlunChat.graphs.graph_factory.compare_with_standard_answers_graph import CompareWithStandardAnswersGraph
from ShenlunChat.graphs.graph_factory.base import GraphConfig

class GraphFactory():
    """这是graph的工厂类"""
    @staticmethod
    def create_graph(graph_name)->GraphConfig:
        """创建一个graph"""
        if graph_name == "split_points":
            return SplitPointsGraph().create_graph()
        elif graph_name == "split_small_points":
            return SplitSmallPointsGraph().create_graph()
        elif graph_name == "compare_with_standard_answers":
            return CompareWithStandardAnswersGraph().create_graph()
        else:
            raise ValueError("graph_name is not supported")
        