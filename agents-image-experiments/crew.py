from crewai import Crew
from crewai.project import crew
from agents import classifier_agent,description_agent,info_agent
from tasks import task1,task2,task3


crew = Crew(
    agents=[classifier_agent, description_agent, info_agent],
    tasks=[task1, task2, task3],
    verbose=True # Enable verbose output for better debugging
)

# Execute the tasks with the provided image path
result = crew.kickoff(inputs={'image_path': 'input.jpg'})
print(result)
