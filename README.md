# Chatbot architecture
<img src="img_src/chatbot_skillogs_archi.png" title="Chatbot architecture">

# RASA framework implementation research

### definitions
* `rasa` is the framework. It is comprised of two distinct parts:
  * `NLU` which processes natural language understanding tasks to generate a language model,
  * and `Core` which processes the expression.
  both are trained separately.
* `rasa x` is the interface that helps users manage, train and deploy their rasa model.

### setup
* get last `chatbot_skillogs` repo update, 
* from local scp repo to AWS instance at `/home/ubuntu/chatbot/`,
* from the `aws_instance/chatbot/chatbot_skillogs` folder, install necessary requirements and train:
```bash
bash ./deploy.sh
```

### run
* open 1st terminal on your computer and:
```bash
cd /home/ubuntu/chatbot/chatbot_skillogs
screen
conda activate rasa
rasa run actions
```
* open 2nd terminal on your computer and:
```bash
cd /home/ubuntu/chatbot/chatbot_skillogs
screen
conda activate rasa
rasa x
```
* you can close the terminals
* to reconnect to "screened" terminals open terminal and:
  * `screen -ls` lists terminals, get ids,
  * `screen -r { id }` returns to "screened" terminal

### connect to chatbot
* password provided in terminal to connect  
* go to `<aws_instance/password>:port`

### documentations
* [installation](https://rasa.com/docs/rasa/user-guide/installation/)
* [tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)
* [commands cheatsheet](https://rasa.com/docs/rasa/user-guide/command-line-interface/)
* [actions management](https://rasa.com/docs/rasa/core/actions/)
* [community forum](https://forum.rasa.com/)  
* [About Ubuntu Screen](https://doc.ubuntu-fr.org/screen)