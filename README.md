## Table of Contents

- [Table of Contents](#table-of-contents)
- [RASA Framework](#rasa-framework)
- [Interactive Mode](#interactive-mode)
- [Rasa X](#rasa-x)
- [Worklog](#worklog)

---

## Chatting with the Bot

If you want to chat with the bot, first install the __virtual env__

```{bash}
virtualenv venv
source activate.sh
pip3 install -r requirements.txt
```

Then train the model with
```{bash}
rasa train
```
and then kickstart the `action server` with
```{bash}
rasa run action
```
Now you can open a new tab and chat with ANOVA-bot using
```{bash}
rasa shell --endpoints endpoints.yml
```

The bot is still in its infancy so be nice to it!

## RASA Framework

### Working with Rasa NLU

```{bash}
rasa train nlu
rasa shell nlu
```

To learn custom entities, you have to set `return_sequence` to true in the `config.yml`. This is because we need to return a dense vector to train on the unseen entities that we custom-made in `nlu.md`.

### Custom Actions

If you have custom actions, you'll need to specify an endpoint which will be called when a custom action is predicted.
```{bash}
rasa shell --endpoints endpoints.yml
```

### Chitchat

__Note:__ This functionality was removed for Rasa X deployment because it's not supported there yet.

Chitchat is specified in `nlu.md` with
```{markdown}
## intent:chitchat/<topic>
    - <examples>
    - <examples>
```
The responses are stored in `./data/responses.md`
```
## <topic>
* chitchat/<topic>
    - <utterance>
```
The `domain.yml` file needs to be adjusted to have
```
intents:
  - greet: {triggers: utter_greet}
  - chitchat: {triggers: respond_chitchat}
```

## Interactive Mode

The docs STRONGLY recommend you develop your stories on interactive mode, and they are not wrong.

Yes. Listen to the docs =)

```{bash}
rasa interactive -m models
```

Remember to run `rasa action` to ensure that all the action functions can be called.

```{bash}
python -m rasa_sdk --actions actions
```

You'll need to refresh both `rasa action` and `rasa train` everytime
 you change something.

When you export, Rasa will ask whether you want to export. So the best choice is to export the interactive mode constructed files to a `backup` dir, otherwise they will be read in when you run `rasa train`.

## Rasa X

To check the API token authentication
```{bash}
curl --request POST \
     --url https://<Rasa X server host>/api/projects/default/git_repositories?api_token=<your api token> \
     --header 'content-type: application/json' \
     --data-binary @repository.json
```

When I first loaded up the server, the training data from `nlu.md` did not load properly. I removed the regex and synonyms and the data loaded properly, but I have yet to confirm whether it's one or both of them.

__Restarting the container__

```{bash}
sudo docker-compose down
sudo docker-compose up -d
```

__Troubleshooting Rasa X Training Errors__

Long story short, you want to look at the `network and console` tab after opening up `inspect`.

Here is a concise [blog post](https://gstephens.org/rasa/chatbot/2019/08/12/rasa-x-troubleshooting.html) about this.

You can track the Github issue [here](https://github.com/RasaHQ/rasa/issues/4231).

__Don't forget to update `actions.py` on Rasa X manually!__

__Setting up a Custom Actions Server__


For your `endpoints.yml` file, you'll need to this.
```
models:
  url: ${RASA_MODEL_SERVER}
  token: ${RASA_X_TOKEN}
  wait_time_between_pulls: ${RASA_MODEL_PULL_INTERVAL}
tracker_store:
  type: sql
  dialect: "postgresql"
  url: ${DB_HOST}
  port: ${DB_PORT}
  username: ${DB_USER}
  password: ${DB_PASSWORD}
  db: ${DB_DATABASE}
  login_db: ${DB_LOGIN_DB}
lock_store:
  type: "redis"
  url: ${REDIS_HOST}
  port: ${REDIS_PORT}
  password: ${REDIS_PASSWORD}
  db: ${REDIS_DB}
event_broker:
  type: "pika"
  url: ${RABBITMQ_HOST}
  username: ${RABBITMQ_USERNAME}
  password: ${RABBITMQ_PASSWORD}
  queue: ${RABBITMQ_QUEUE}
action_endpoint:
  url: ${RASA_USER_APP}/webhook
  token:  ""
```

For class #9 of the Rasa Masterclass, `docker-compose.override.yml` was specified to be
```
version: '3.4'
services:
  app:
    image: 'rasa/rasa-sdk:latest'
    volumes:
      - './actions:/app/actions'
    ports:
      - '5055:5055'
    depends_on:
      - rasa-production
```

The `RASA_USER_APP` variable is
```{bash}
http://app:5055
```
__Bot description for test users__

ANOVA-bot is a smart kid that knows a little about data science. It can tell random facts, be a little cheeky, and give you some tips about what to do if you're a student looking to do data science.

---

## Worklog

- 16/01/20 | 0.0.10-rc - Adding custom actions server for Rasa X and testing.
- 15/01/20 | 0.0.09-rc - Removing chitchat component to debug why model training isn't working. The `chitchat` component is stored on `save_chitchat` branch.
- 13/01/20 | 0.0.08-rc - Debugging Rasa X server and preparing another story with languages and industry advice.
- 12/01/20 | 0.0.07-rc - Merge with Master branch for Rasa X deployment.
- 27/01/20 | 0.0.06-rc - Revamped nlu classes to support a more structured story flow. Added 3 forms, academic, industry and career choice. Removed `interest_level` intents and
- 26/01/20 | 0.0.05-rc - Building miscellaneous question path and one happy path. Made forms work and updated intents classes - we're no longer incorporating the interest level of the user. Added list of random facts.
- 26/01/20 | 0.0.04-rc - Incorporate `chitchat` into chatbot.
- 25/01/20 | 0.0.03-rc - Build basic 'happy path' story for a particular audience. Provide structure of `utters` vs. `actions` and `forms`.
- 25/01/20 | 0.0.02-rc - Added initial NLU training examples after designing  story flow and intents offline.
- 24/12/19 | 0.0.01-rc - Initial commit.

