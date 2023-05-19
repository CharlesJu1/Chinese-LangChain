import sys
import os

abspath = os.path.abspath(os.path.dirname(__file__))
par_dir = os.path.dirname(abspath)
sys.path.append(par_dir)

from clc.langchain_application import LangChainApplication
from config import LangChainCFG
from logging_util import loggingSetup

if __name__ == '__main__':
    loggingSetup("./logs/test_langchain_application.txt")
    config = LangChainCFG()
    application = LangChainApplication(config)
    # result = application.get_knowledge_based_answer('马保国是谁')
    # print(result)
    # application.source_service.add_document('/home/searchgpt/yq/Knowledge-ChatGLM/docs/added/马保国.txt')
    # result = application.get_knowledge_based_answer('马保国是谁')
    # print(result)
    result = application.get_llm_answer('马保国是谁')
    print(result)