https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/

`mkdir llamaindex-ollama-agent`

`cd llamaindex-ollama-agent`

`conda create --name llamaindex-basic-agent python=3.12` instead of poetry

`conda activate llamaindex-basic-agent`

`pip install llama-index python-dotenv`

`conda list`

`conda info --envs`

`echo $OPENAI_API_KEY` https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety 

`chmod +x ./ollama-darwin`

`./ollama-darwin list`

`./ollama-darwin serve`

`python main.py`