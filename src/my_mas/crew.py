from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

# Uncomment the following line to use an example of a custom tool
# from my_mas.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class MyMas():
	"""MyMas crew for product comparison analysis"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Optional hook to be executed before the crew starts
		# You can modify inputs dynamically if needed
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Optional hook to be executed after the crew has finished
		print(f"Results: {output}")
		return output

	@agent
	def analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['analyst'],
			verbose=True
		)

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)

	@agent
	def summary_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_specialist'],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyst_task'],
		)

	@task
	def researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['researcher_task'],
		)

	@task
	def summary_specialist_task(self) -> Task:
		return Task(
			config=self.tasks_config['summary_specialist_task'],
		)

	@task
	def reporting_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_analyst_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MyMas crew"""
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
			tasks=self.tasks,    # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
