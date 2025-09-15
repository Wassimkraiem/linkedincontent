# Linkedincontentagent Crew

Welcome to the Linkedincontentagent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/linkedincontentagent/config/agents.yaml` to define your agents
- Modify `src/linkedincontentagent/config/tasks.yaml` to define your tasks
- Modify `src/linkedincontentagent/crew.py` to add your own logic, tools and specific args
- Modify `src/linkedincontentagent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the linkedinContentAgent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research o# Linkedincontentagent Crew

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
