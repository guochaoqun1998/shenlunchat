<!-- /*
 * @Author: guochaoqun 
 * @Date: 2024-07-25 22:39:15 
 * @Last Modified by: guochaoqun
 * @Last Modified time: 2024-07-25 22:40:07
 * @Description:  在这个文件中用于说明ShenlunChat的用法
 */ -->

# ShenlunChat 项目结构

## 核心架构

1. 所有的大任务都被拆解为小任务，每一个小任务都是由Graph来完成。
2. 每一个Graph 由 Node, InputState, OutputState, edge 组成。但实际上每一个graph都是线性的实现，不是图的实现流程，可以直接由LCEL来完成。其中Node由AgentNode 或者 ToolNode 来实现。
3. ToolNode 定制化相对较强。
4. AgentNode 由 Node, InputState, OutputState, InputMapping, OutputMapping 组成。Node是Agent，是核心，是LCEL的实现。由LLM, Prompt, Tool 组成。 这里的Tool都是None.

以上实现存在的问题：
1. Agents 和 tools 都是线性调用，实际上没有用到graph。使用Graph结构增加了复杂度。
2. 工厂类创建过多，但是代码复用性较差。没有使用config来创建子类。有共用的函数调用结构，但是抽象类和子类没有很好的区分。
3. 没有完善的config来创建子类。
4. 最好按照task进行分类，方便每一个task需要分散在不同的文件中。
5. 之后改用pydantic V2, Model 可以复用。
6. 模块化方面的问题。代码中有多个init_.py文件是空的，这可能意味着模块划分不够清晰，或者某些模块没有正确导出内容，导致导入时不够直观。例如，agents/prompts/factory/init.py是空的，可能需要显式导出相关类，方便外部引用。
7. 类型提示和文档方面，部分方法的参数和返回值缺乏明确的类型提示，例如create_agent方法的参数没有类型注释，可能影响代码的可读性和IDE的支持。此外，某些方法的文档字符串不够详细，导致使用者难以理解其用途和参数要求。