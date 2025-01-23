from ShenlunChat.utils.prompt_decorator import get_docstring
from ShenlunChat.agents.prompts.demonstration import DemonstrationBase, ExampleBase

class SplitSmallPointsExamples(ExampleBase):
    @get_docstring
    def example1(self):
        """
        输入: 发展数字化政务服务。搭建政务服务网“用户空间”，推出“在线导办”“引导式办事指南”，提供智能化、精准化、个性化的政务服务。
        输出: {"points": ["发展数字化政务服务","搭建政务服务网“用户空间”","推出“在线导办”“引导式办事指南”","提供智能化、精准化、个性化的政务服务"]}
        """
        pass

class SplitSmallPointsDemonstration(DemonstrationBase):
    example_cls = SplitSmallPointsExamples

    def get_prompt(self) -> str:
        config = self.version1()
        return self._get_prompt(**config)
    
    def version1(self):
        return {"all":True}


if __name__ == "__main__":
    split_points_demonstration = SplitSmallPointsDemonstration()
    print(split_points_demonstration.get_prompt())