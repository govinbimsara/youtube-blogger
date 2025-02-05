from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv("GROQ_API_KEY")
llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key=groq_api_key)

##create senior blog content reasercher

blog_researcher = Agent(
    role = 'BLog researcher from youtube videos',
    goal = 'Get the relevent video content from the topic {topic} from youtube chanel',
    verbose = True,
    memory = True,
    backstory = (
        'Expert in understanding videos in Software Engineering, IT, Web Designing, Coding, AI, Data science, Machine Learning and Gen AI and providing suggestions'
    ),
    tools = [yt_tool],
    allow_delegation = True,
    llm = llm
)

#create senior blog writer agent

blog_writer = Agent(
    role = 'Blog writer',
    goal = 'Narrate compeling tech stories about the video {topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        'With a flair for simplifying complex topics, you craft'
        'engage narratives that captivate and educate, bringing new'
        'discoveries to light in and accessible manner.'
    ),
    tools = [yt_tool],
    allow_delegation = False,
    llm = llm
)