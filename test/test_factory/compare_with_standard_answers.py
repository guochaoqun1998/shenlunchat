from ShenlunChat.agents.agent_factory.factory import AgentFactory

if __name__=="__main__":
    model_info = {"chat_name":"openai","model_name":"gpt-4o","model_config":{}}
    task_info = {"task_name":"compare_with_standard_answers","prompt_type":"prompt"}
    tool_info = []
    config = AgentFactory.create_agent(model_info,task_info,tool_info,llm=True)
    print("create agent success")
    point = "树立品牌标杆"
    this_point = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
    standard_points = ["设立品牌标杆。强化品牌建设，发挥质量奖示范作用，推广先进经验，将质量文化、品牌理念向全产业链延伸",
                       "创建区域品牌。打造龙头企业，成立行业联盟，制定产业全链条标准，提升全行业质量。",
                       "提供商标品牌服务，设立指导站，提供一站式公共服务平台，开展专题培训。",
                       "打造社会服务平台。开展品牌论坛，发起活动，建设品牌专业组织，为企业提供人才、品牌服务。",
                       "举办高端品牌会议。大力宣传，推动企业竞争从要素向品牌转变。"]
    student_answer = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
    # input = config.input_model(point=point,this_point=this_point,standard_points=standard_points)
    result = config.agent.invoke(dict(point=point,this_point=this_point,standard_points=standard_points))
    print(result)