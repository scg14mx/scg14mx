Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
 source .\\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
rn -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rn -f frontend.zip
deactivate