# Stream-Data

This repo projects an example of publicly deployment of data presentation and data visualization by using streamlit.io (https://docs.streamlit.io/) The scope of the project can expand to data analysis and execute one or couple machine learning algorithms.

# Requirements 

Python 3.10.x
Streamlit 1.12.0
Pandas==1.4.3
Pillow==9.2.0

and so on. See requirements.txt please.

# Execute & Deploy

My demo:
https://callmecelebi-stream-data-streamthedata-y1iwpc.streamlitapp.com/

For you:
1. Using the requirements create a virtual env. (Pipenv, Conda Env, Virtualenv, It does not matter, whatever suits you. I'm using virtualenv)
  > virtualenv streamdataenv
  > pip install requirements.txt (While in root dir)
2. Clone the repository.
3. Cd to main, root. (Stream-data)
4. Execute in your terminal:
  > streamlit run "c:/Users/path/to/Stream Data in local/streamthedata.py"                                                                              
5. The address is in your local:
   http://localhost:8501/
   Every change and save updates this page dynamically. When you stage, commit and finally push all changes to Github repo, It will update your public streamlit app link page which I shared of an example link as well. Tip: Do the changes mostly in your local, then push it. It will save you tons of time.
6. Then go to https://share.streamlit.io/. Deploy your own Stream-data folder from local or Github repository.
7. The address is generated by streamlit automatically, when you deploy app to the streamlit cloud it will be generated automatically.
   https://{githubusername}-{repositoryname with dash}-{pyfilenamewithoutextension}-{randomkeyfromstreamlit}.streamlitapp.com
   
