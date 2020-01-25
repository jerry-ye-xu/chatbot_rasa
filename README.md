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

## Application

## Worklog

- 26/12/19 | 0.0.4-rc - Incorporate `chitchat` into chatbot.
- 25/12/19 | 0.0.3-rc - Build basic 'happy path' story for a particular audience. Provide structure of `utters` vs. `actions` and `forms`.
- 25/12/19 | 0.0.2-rc - Added initial NLU training examples after designing  story flow and intents offline.
- 24/12/19 | 0.0.1-rc - Initial commit.

