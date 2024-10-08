from dotenv import load_dotenv #To activate the environment variables
import pandas as pd  #to read the csv file
import os
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import instruction_str, new_prompt, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import india_engine


load_dotenv()

population_path= os.path.join("data", "Population.csv")
population_df= pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df= population_df, verbose= True, instruction_str = instruction_str)
# update the prompt, pass the python dictionary
population_query_engine.update_prompts({"pandas_prompt": new_prompt})


#population_query_engine.query("What is the population of India")
#print(population_df.head())

tools =[
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine, metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),


QueryEngineTool(query_engine= india_engine, metadata= ToolMetadata(
        name="india_data",
        description="this gives information about the country India"

    ),
    ),
]

llm= OpenAI(model="gpt-3.5-turbo-0613")
agent= ReActAgent.from_tools(tools, llm= llm, verbose= True, context=context)

while(prompt := input("Enter a prompt (q to quit)")) != "q":
    result= agent.query(prompt)
    print(result)