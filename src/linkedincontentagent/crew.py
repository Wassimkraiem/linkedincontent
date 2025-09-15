from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class LinkedinContentAgent:
    """LinkedIn Content Agent Crew with Specialized Teams"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Content Creator Agents
    @agent
    def thought_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["thought_content_creator"],
            verbose=True,
        )

    @agent
    def project_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["project_content_creator"],
            verbose=True,
        )

    @agent
    def event_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["event_content_creator"],
            verbose=True,
        )

    # Specialist Review Agents
    @agent
    def thought_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["thought_specialist"],
            verbose=True,
        )

    @agent
    def project_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["project_specialist"],
            verbose=True,
        )

    @agent
    def event_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["event_specialist"],
            verbose=True,
        )

    # Content Classifier Agent
    @agent
    def content_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config["content_classifier"],
            verbose=True,
        )

    # Classification Task
    @task
    def classify_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["classify_content_task"],
        )

    # Thought Leadership Tasks
    @task
    def create_thought_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_thought_post_task"],
        )

    @task
    def review_thought_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_thought_post_task"],
        )

    # Project Achievement Tasks
    @task
    def create_project_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_project_post_task"],
        )

    @task
    def review_project_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_project_post_task"],
        )

    # Event Experience Tasks
    @task
    def create_event_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_event_post_task"],
        )

    @task
    def review_event_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_event_post_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LinkedIn Content Agent crew with intelligent routing"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
