from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Linkedincontentagent():
    """LinkedIn Content Agent Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_content_creator'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def growth_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_growth_strategist'],  # type: ignore[index]
            verbose=True
        )

    @task
    def create_post_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_post_task'],  # type: ignore[index]
        )

    @task
    def optimize_post_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_post_task'],  # type: ignore[index]
            output_file='linkedin_post.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LinkedIn Content Agent crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
