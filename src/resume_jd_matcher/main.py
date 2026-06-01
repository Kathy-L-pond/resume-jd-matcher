#!/usr/bin/env python
from resume_jd_matcher.crew import ResumeJdMatcher
from datetime import datetime

def run():
    # 这里是测试用的JD和简历（你可以后面自己改）
    inputs = {
        "user_jd": """我们正在招聘AI产品经理实习生。
要求：熟悉LLM、Agent、RAG；有产品思维；本科211或以上，硕士优先。
地点：香港/深圳。""",
        
        "user_resume": """Yingxuan Luo
211软件工程本科，港大IDT硕士
熟练C++/C，略懂Python
参加过AI相关课程，了解CrewAI概念
目标：AI产品经理暑期实习"""
    }
    
    print("🚀 开始运行 AI 简历优化 & JD匹配 Agent...")
    result = ResumeJdMatcher().crew().kickoff(inputs=inputs)
    print("\n✅ 运行完成！下面是Agent的完整输出：\n")
    print(result.raw)

if __name__ == "__main__":
    run()