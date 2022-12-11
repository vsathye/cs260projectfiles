The model and the ability to run/retrain it can be found in project_code.ipynb

To run the code simply upload everything to google colab, or another way of connecting to a gpu, and run all the cells in order. To add prompts edit the list of possible prompts in the cell titled #RUN THIS CELL TO GENERATE THE FILES FOR AB TESTING and then run it to generate new ab testing files. Then run website.py to gather new information To then retrain the model with the better image by running the cell entitled #RUN THIS CELL TO TAKE THE RESULTS OF AB TESTING AND RETRAIN THE MODEL


the model to get semantically similar future prompts can be found in semantic_similarity.ipynb
The mock webapp can eb found running website.py
The mock server (went unimplimented in final version) can be found in server.py