- [RASA Framework](#rasa-framework)
- [Application](#application)
- [Worklog](#worklog)

---

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


## Interactive Mode

The docs STRONGLY recommend you develop your stories on interactive mode, and they are not wrong =D

Yes. Listen to the docs =)

```{bash}
rasa interactive -m models
```

Remember to run `rasa action` to ensure that all the action functions can be called.

You'll need to refresh both `rasa action` and `rasa train` everytime
 you change something.

When you export, Rasa will ask whether you want to export. So the best choice is to export the interactive mode constructed files to a `backup` dir, otherwise they will be read in when you run `rasa train`.

## Application



## Worklog
- 12/01/20 | 0.0.7-rc - Merge with Master branch for Rasa X deployment.  
- 27/01/20 | 0.0.6-rc - Revamped nlu classes to support a more structured story flow. Added 3 forms, academic, industry and career choice. Removed `interest_level` intents and
- 26/01/20 | 0.0.5-rc - Building miscellaneous question path and one happy path. Made forms work and updated intents classes - we're no longer incorporating the interest level of the user. Added list of random facts.
- 26/01/20 | 0.0.4-rc - Incorporate `chitchat` into chatbot.
- 25/01/20 | 0.0.3-rc - Build basic 'happy path' story for a particular audience. Provide structure of `utters` vs. `actions` and `forms`.
- 25/01/20 | 0.0.2-rc - Added initial NLU training examples after designing  story flow and intents offline.
- 24/12/19 | 0.0.1-rc - Initial commit.

