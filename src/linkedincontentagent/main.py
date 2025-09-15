#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crewai import Crew, Process, Agent, Task

from linkedincontentagent.crew import LinkedinContentAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


class SmartLinkedInContentCrew:
    """Smart LinkedIn Content Creation with Intelligent Routing"""

    def __init__(self):
        self.main_crew = LinkedinContentAgent()

    def create_classification_crew(self, content_input: str) -> str:
        """Create a mini crew just for classification"""
        classifier_agent = self.main_crew.content_classifier()

        classification_task = Task(
            description=f"""
            Analyze this input content and classify it as one of three types:
            
            Content to analyze: "{content_input}"
            
            Classification options:
            1. THOUGHT - Personal insights, opinions, industry observations, lessons learned, advice, hot takes, reflections
            2. PROJECT - Work projects, achievements, milestones, launches, completions, results, case studies, accomplishments  
            3. EVENT - Conferences, workshops, networking events, industry meetups, learning experiences, webinars
            
            Return ONLY the classification type (THOUGHT, PROJECT, or EVENT) followed by a brief explanation.
            Example: "PROJECT - This describes a completed work project with specific achievements and results."
            """,
            agent=classifier_agent,
            expected_output="A classification (THOUGHT, PROJECT, or EVENT) with brief explanation.",
        )

        classification_crew = Crew(
            agents=[classifier_agent],
            tasks=[classification_task],
            process=Process.sequential,
            verbose=False,
        )

        result = classification_crew.kickoff()
        return str(result)

    def create_specialized_crew(self, content_type: str, content_input: str):
        """Create a specialized crew based on content type"""

        if content_type == "THOUGHT":
            creator_agent = self.main_crew.thought_content_creator()
            specialist_agent = self.main_crew.thought_specialist()

            create_task = Task(
                description=f"""
                Transform this thought/insight into a compelling LinkedIn thought leadership post:
                
                Input: "{content_input}"
                
                Create a post that:
                - Opens with a provocative or relatable hook
                - Shares your personal perspective 
                - Makes the insight accessible and actionable
                - Encourages discussion and engagement
                - Ends with thought-provoking questions
                - Uses appropriate hashtags and formatting
                """,
                agent=creator_agent,
                expected_output="A compelling thought leadership LinkedIn post with strong engagement potential.",
            )

            review_task = Task(
                description="""
                Review and optimize the thought leadership post for:
                - Authenticity and credibility
                - Balance between confidence and humility  
                - Engagement potential and discussion value
                - Professional tone while being conversational
                - Clear value proposition for readers
                - Strategic hashtag usage and formatting
                - Strong call-to-action for meaningful discussion
                
                Provide the final optimized post.
                """,
                agent=specialist_agent,
                expected_output="An optimized, engaging thought leadership LinkedIn post ready for publishing.",
            )

        elif content_type == "PROJECT":
            creator_agent = self.main_crew.project_content_creator()
            specialist_agent = self.main_crew.project_specialist()

            create_task = Task(
                description=f"""
                Transform this project/achievement into an engaging LinkedIn post:
                
                Input: "{content_input}"
                
                Create a post that:
                - Highlights the problem solved and value created
                - Shares the journey and lessons learned
                - Includes challenges overcome
                - Quantifies results when possible
                - Gives proper credit to team members
                - Makes achievements relatable and inspiring
                - Provides actionable insights for others
                """,
                agent=creator_agent,
                expected_output="An engaging project showcase LinkedIn post that highlights achievements and provides value.",
            )

            review_task = Task(
                description="""
                Review and optimize the project post for:
                - Balance between showcasing and providing value
                - Professional humility while highlighting impact
                - Clear communication of lessons learned  
                - Proper team credit and collaboration emphasis
                - Actionable insights for readers
                - Appropriate metrics and results sharing
                - Inspiring and motivational tone
                
                Provide the final optimized post.
                """,
                agent=specialist_agent,
                expected_output="An optimized project showcase post that effectively balances achievement with humility and value.",
            )

        else:  # EVENT
            creator_agent = self.main_crew.event_content_creator()
            specialist_agent = self.main_crew.event_specialist()

            create_task = Task(
                description=f"""
                Transform this event experience into valuable LinkedIn content:
                
                Input: "{content_input}"
                
                Create a post that:
                - Shares key takeaways and learnings
                - Highlights interesting conversations or insights
                - Discusses industry trends discovered
                - Provides actionable advice for the community
                - Shows gratitude to organizers and connections
                - Explores future implications of learnings
                - Encourages others to participate in similar events
                """,
                agent=creator_agent,
                expected_output="A valuable event experience LinkedIn post that shares insights and builds connections.",
            )

            review_task = Task(
                description="""
                Review and optimize the event post for:
                - Value delivered to readers who didn't attend
                - Professional networking etiquette and gratitude
                - Clear articulation of key learnings
                - Potential for further discussion and connection
                - Appropriate tagging suggestions for people/organizations
                - Encouraging tone for community participation
                - Strategic positioning for future opportunities
                - CRITICAL: Ensure final post is EXACTLY 1300-2000 characters (including spaces)
                - Count characters and adjust if needed
                - If too short: add more takeaways, insights, or gratitude
                - If too long: condense while keeping key learnings and value
                
                Provide the final optimized post with character count.
                """,
                agent=specialist_agent,
                expected_output="An optimized event post (1300-2000 characters) that maximizes networking impact and community value.",
            )

        # Make review task depend on create task
        review_task.context = [create_task]

        specialized_crew = Crew(
            agents=[creator_agent, specialist_agent],
            tasks=[create_task, review_task],
            process=Process.sequential,
            verbose=True,
        )

        return specialized_crew


def run():
    """
    Run the smart LinkedIn content creation crew.
    """
    # You can modify this input or make it dynamic
    content_input = "I'm bad and lazy at posting on LinkedIn so I built this AI agent to make that easier for me using CrewAI and OpenAI API."

    try:
        smart_crew = SmartLinkedInContentCrew()

        # Step 1: Classify the content
        print("🔍 Classifying content...")
        classification_result = smart_crew.create_classification_crew(content_input)
        print(f"Classification result: {classification_result}")

        # Extract the classification type (first word before the dash)
        content_type = (
            classification_result.split(" - ")[0].split(":")[0].strip().upper()
        )

        # Ensure we have a valid classification
        if content_type not in ["THOUGHT", "PROJECT", "EVENT"]:
            # Default to THOUGHT if classification is unclear
            content_type = "THOUGHT"
            print(f"⚠️ Classification unclear, defaulting to THOUGHT")

        print(f"📝 Content classified as: {content_type}")

        # Step 2: Create specialized crew and process content
        print(f"🚀 Creating specialized {content_type.lower()} content crew...")
        specialized_crew = smart_crew.create_specialized_crew(
            content_type, content_input
        )

        # Step 3: Generate the final LinkedIn post
        print("✨ Generating optimized LinkedIn post...")
        final_result = specialized_crew.kickoff()

        print("\n" + "=" * 50)
        print("🎉 FINAL LINKEDIN POST:")
        print("=" * 50)
        print(final_result)

        return final_result

    except Exception as e:
        raise Exception(f"An error occurred while running the smart crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "content": "Sharing insights from my latest AI project implementation.",
        "current_year": str(datetime.now().year),
    }
    try:
        smart_crew = SmartLinkedInContentCrew()
        main_crew_instance = smart_crew.main_crew.crew()
        main_crew_instance.train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        smart_crew = SmartLinkedInContentCrew()
        main_crew_instance = smart_crew.main_crew.crew()
        main_crew_instance.replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "content": "Just completed an amazing machine learning workshop!",
        "current_year": str(datetime.now().year),
    }

    try:
        smart_crew = SmartLinkedInContentCrew()
        main_crew_instance = smart_crew.main_crew.crew()
        main_crew_instance.test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
