sudo apt-get update && sudo apt-get -y upgrade
mkdir -p /home/ubuntu/chatbot/chatbot_skillogs/download
cd download
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
eval "$(/home/ubuntu/miniconda/bin/conda shell.bash hook)"
conda init
conda create -n rasa python=3.6.8 -y
conda activate rasa
cd ..
sudo apt-get install gcc -y
pip install -r requirements.txt
pip install python-dateutil==2.8
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
python -m spacy download en
python -m spacy download fr
rasa train