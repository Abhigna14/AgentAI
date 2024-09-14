#prompt is the text you give to AI to get a specific response
from llama_index.core import PromptTemplate as MyPromptTemplate


# instruction_str is telling the QueryEngine what to do with python data
instruction_str = """\
 1. Convert the query to executable python code using pandas
 2. The final line of code should be a python expression that can be called with the 'eval()' function
 3. The code should represent a solution to the query
 4. PRINT ONLY THE EXPRESSIONS
 5. Do not quote the expression."""
 
new_prompt = MyPromptTemplate(
    """\
    you are working with a pandas dataframe in python 
    The name of the dataframe is df
    This is the result of 'print(df.head())':
    {df_str}

    Follow these instructions"
    {instruction_str}
    Query: {query_str}
    Expression: """
)

context= """ Purpose: The primary role of this agent is to assist users by providing accurate information about world population statistics and details about a country."""
