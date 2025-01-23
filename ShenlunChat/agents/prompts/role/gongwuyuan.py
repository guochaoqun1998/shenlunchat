from ShenlunChat.utils.prompt_decorator import get_docstring
from ShenlunChat.agents.prompts import PromptBase

class GongWuYuanRole(PromptBase):
    def get_prompt(self):
        return self.get_gongwuyuan_role()
    
    @get_docstring
    def get_gongwuyuan_role():
        """你是中国公务员考试申论批改的考官"""
        pass


if __name__ == '__main__':
    gongwuyuan = GongWuYuanRole()
    print(gongwuyuan.get_prompt())

