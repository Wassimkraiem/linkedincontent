# Linkedincontentagent Crew

Welcome to the Linkedincontentagent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

# How to Run the App

Follow these steps to generate LinkedIn posts using the AI agents:

1. **Install Dependencies**

   - Make sure you have Python >=3.10 <3.14 installed.
   - Install dependencies using [UV](https://docs.astral.sh/uv/):
     ```bash
     pip install uv
     crewai install
     ```

2. **Add Your OpenAI API Key**

   - Copy your OpenAI API key into the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

3. **Update Your Content Input**

   - Open [`src/linkedincontentagent/main.py`](src/linkedincontentagent/main.py).
   - Find the `content_input` variable in the `run()` function:
     ```python
     content_input = "I'm bad and lazy at posting on LinkedIn so I built this AI agent to make that easier for me using CrewAI and OpenAI API."
     ```
   - Replace the value with your own thought, project, or event description.

4. **Run the App**
   - From your project root, run:
     ```bash
     crewai run
     ```
   - The app will classify your input, generate a draft post, optimize it, and print the final LinkedIn post.

For advanced usage, see the rest of the README and the docstrings

## How to Use the AI Agents

This project leverages multiple specialized AI agents to automate and optimize LinkedIn content creation. Here’s how you can use them:

1. **Content Classification**

   - The system first analyzes your input and classifies it as a THOUGHT, PROJECT, or EVENT using a dedicated classifier agent.

2. **Specialized Content Creation**

   - Based on the classification, the appropriate content creator agent transforms your input into a draft LinkedIn post tailored for that category.

3. **Expert Review and Optimization**

   - A specialist agent reviews and refines the draft post to maximize engagement, authenticity, and professional impact.

4. **Running the Workflow**

   - To generate a LinkedIn post, run the following command from your project root:
     ```bash
     crewai run
     ```
   - The system will process your input, classify it, create a draft, and optimize the final post.

5. **Customizing Inputs**

   - You can modify the input content in [`src/linkedincontentagent/main.py`](src/linkedincontentagent/main.py) by changing the `content_input` variable.
   - For advanced usage, you can define agents and tasks in [`src/linkedincontentagent/config/agents.yaml`](src/linkedincontentagent/config/agents.yaml) and [`src/linkedincontentagent/config/tasks.yaml`](src/linkedincontentagent/config/tasks.yaml).

6. **Training, Testing, and Replay**
   - Use the following commands for additional functionality:
     - Train:
       ```bash
       crewai train <iterations> <output_file>
       ```
     - Test:
       ```bash
       crewai test <iterations> <eval_llm>
       ```
     - Replay:
       ```bash
       crewai replay <task_id>
       ```

For more details, see the docstrings and logic in [`src/linkedincontentagent/main.py`](src/linkedincontentagent/main.py).

...existingn LLMs in the root folder.

## Understanding Your Crew

The linkedinContentAgent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
