# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import requests
import time

from bs4 import BeautifulSoup

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionPause(Action):
    def name(self) -> Text:
        return "action_pause"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time.sleep(0.75)
        return []

class ActionIntroDataScience(Action):
    def name(self) -> Text:
        return "action_intro_ds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Data science is a field that combines ideas from statistics and computer science.\nIt involves building data pipelines, data analysis, building models and applying these models for prediction or inference."
        )
        return []

class ActionSalaryRange(Action):
    def name(self) -> Text:
        return "action_intro_ds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="According to GlassDoor, the average data science salary in Australia is A$110k, last checked on 25/01/2020.\nThe top salary that I have heard is A$250k package, and senior data scientists are often hitting the A$160-200k mark.\nSo the earning potential is pretty good!"
        )
        return []

class ActionCareerPaths(Action):
    def name(self) -> Text:
        return "action_career_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Data science careers are broad and are often a mixture of business problem solving, programming and statistical analysis.\nDifferent roles include data engineering and machine learning engineering with a bigger focus on productionising data pipelines and/or software.\n To succeed, you have to draw quantifiable insights from data and build infrastructure around the models you create."
        )
        return []

class ExpAndBackgroundForm(FormAction):
    def name(self) -> Text:
        return "exp_and_background_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "academic_background", "research"
        ]