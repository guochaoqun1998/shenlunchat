from ShenlunChat.utils.prompt_decorator import get_docstring
from ShenlunChat.agents.prompts.demonstration import DemonstrationBase, ExampleBase

class SplitPointsExamples(ExampleBase):
    @get_docstring
    def example1(self):
        """
        输入: 1.发展数字化政务服务。搭建政务服务网“用户空间”，推出“在线导办”“引导式办事指南”，提供智能化、精准化、个性化的政务服务。2.探索智慧居家养老服务。配备智能设备，开发手机APP，发起“一键呼”项目，在全国100个城市建立养老信息综合平台，便利老人生活，方便子女尽孝，促进科学决策。3开展“同车不同温”试点。改造空调系统，定期关注温度数据，为空调温度调控提供数据支持，提高乘客舒适度，提升地铁服务质量。
        输出: { 'check_point'=["1.发展数字化政务服务。搭建政务服务网“用户空间”，推出“在线导办”“引导式办事指南”，提供智能化、精准化、个性化的政务服务。","2.探索智慧居家养老服务。配备智能设备，开发手机APP，发起“一键呼”项目，在全国100个城市建立养老信息综合平台，便利老人生活，方便子女尽孝，促进科学决策。","3开展“同车不同温”试点。改造空调系统，定期关注温度数据，为空调温度调控提供数据支持，提高乘客舒适度，提升地铁服务质量。"] }
        """
        pass

    @get_docstring
    def example2(self):
        """
        输入: 发展数字化政务服务。搭建政务服务网“用户空间”，推出“在线导办”“引导式办事指南”，提供智能化、精准化、个性化的政务服务。探索智慧居家养老服务。配备智能设备，开发手机APP，发起“一键呼”项目，在全国100个城市建立养老信息综合平台，便利老人生活，方便子女尽孝，促进科学决策。开展“同车不同温”试点。改造空调系统，定期关注温度数据，为空调温度调控提供数据支持，提高乘客舒适度，提升地铁服务质量。
        输出: { 'check_point'=["发展数字化政务服务。搭建政务服务网“用户空间”，推出“在线导办”“引导式办事指南”，提供智能化、精准化、个性化的政务服务。探索智慧居家养老服务。配备智能设备，开发手机APP，发起“一键呼”项目，在全国100个城市建立养老信息综合平台，便利老人生活，方便子女尽孝，促进科学决策。开展“同车不同温”试点。改造空调系统，定期关注温度数据，为空调温度调控提供数据支持，提高乘客舒适度，提升地铁服务质量。"] }
        """
        pass

    @get_docstring
    def example3(self):
        """
        输入: 发展数字化政务服务；探索智慧居家养老服务；开展“同车不同温”试点
        输出: { 'check_point'=["发展数字化政务服务","探索智慧居家养老服务","开展“同车不同温”试点"] }
        """
        pass

class SplitPointsDemonstration(DemonstrationBase):
    example_cls = SplitPointsExamples

    def get_prompt(self) -> str:
        config = self.version1()
        return self._get_prompt(**config)
    
    def version1(self):
        return {"all":True}


if __name__ == "__main__":
    split_points_demonstration = SplitPointsDemonstration()
    print(split_points_demonstration.get_prompt())