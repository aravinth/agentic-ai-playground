import os
from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"


## 1. Image Classifier Agent (to check if the image is an animal)
classifier_agent = Agent(
    role="Image Classifier Agent",
    goal="Determine if the image is of an animal or not",
    backstory="""
        You have an eye for animals! Your job is to identify the object in the image.
        Restrict the Classification to 'Human', 'Animal', 'Plant', 'Vehicle'. It can be multi-classifier as well.
        If you are not sure, say 'Unknown'.
    """,
    llm='ollama/deepseek-r1:1.5b'  # Model for image-related tasks
)


## 2. Object Description Agent (to describe the object in the image)
description_agent = Agent(
    role="Object Description Agent {image_path}",
    goal="Describe the object in the image",
    backstory="""
        You are a good describer of an image. Your task is to describe the image as such.
    """,
    llm='ollama/deepseek-r1:1.5b'  # Model for image-related tasks
)


## 3. Information Retrieval Agent (to fetch additional info about the object)
info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain object",
    backstory="""
        You are very good at telling interesting facts.
        You don't give any wrong information if you don't know it.
    """,
    llm='ollama/deepseek-r1:1.5b'  # Model for general knowledge retrieval
)
