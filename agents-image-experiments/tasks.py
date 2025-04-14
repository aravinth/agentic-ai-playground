from crewai import Task
from agents import classifier_agent,description_agent,info_agent

# Task 1: Check if the image is an animal
task1 = Task(
                description="Classify the image ({image_path}) and tell me if it's an animal.",
                expected_output="If it's an animal, say 'animal'; otherwise, say 'not an animal'.",
                agent=classifier_agent
)
# Task 2: If it's an animal, describe it
task2 = Task(
                description="Describe the animal in the image.({image_path})",
                expected_output="Give a detailed description of the animal.",
                agent=description_agent
)
# Task 3: Provide more information about the animal
task3 = Task(
                description="Give additional information about the described animal.",
                expected_output="Provide at least 5 interesting facts or information about the animal.",
                agent=info_agent    
)
