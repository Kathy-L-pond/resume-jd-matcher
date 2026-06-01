from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from resume_jd_matcher.tools.custom_tool import MyCustomTool   # 如果后面要加工具再用

@CrewBase
class ResumeJdMatcher:
    """AI 简历优化 & JD匹配 Agent 团队"""

    # ==================== Agents ====================
    @agent
    def jd_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['jd_parser'],
            verbose=True
        )

    @agent
    def resume_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_analyzer'],
            verbose=True
        )

    @agent
    def matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['matcher'],
            verbose=True
        )

    @agent
    def resume_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_optimizer'],
            verbose=True
        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_letter_writer'],
            verbose=True
        )

    # ==================== Tasks ====================
    @task
    def parse_jd_task(self) -> Task:
        return Task(
            config=self.tasks_config['parse_jd_task']
        )

    @task
    def analyze_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_resume_task']
        )

    @task
    def match_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_task']
        )

    @task
    def optimize_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_resume_task']
        )

    @task
    def cover_letter_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_task']
        )

    # ==================== Crew ====================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,   # 顺序执行
            verbose=True
        )