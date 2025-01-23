from ShenlunChat.utils.prompt_decorator import get_docstring
from ShenlunChat.agents.prompts.demonstration import DemonstrationBase, ExampleBase

class CompareWithStandardAnswersExamples(ExampleBase):
    @get_docstring
    def example1(self):
        pass

class CompareWithStandardAnswersDemonstration(DemonstrationBase):
    example_cls = CompareWithStandardAnswersExamples

    def get_prompt(self) -> str:
        config = self.non_example()
        return self._get_prompt(**config)
    
    def non_example(self):
        return {"example_list":[],"all":False}

    def version1(self):
        return {"all":True}


if __name__ == "__main__":
    compare_with_standard_answers_demonstration = CompareWithStandardAnswersDemonstration()
    print(compare_with_standard_answers_demonstration.get_prompt())