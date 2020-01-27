# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import requests
import time

from bs4 import BeautifulSoup

from typing import Any, Text, Dict, List, Union

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
        return "action_salary_range"

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

class ActionIndustryAdvice(Action):
    def name(self) -> Text:
        return "action_industry_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Working in industry requires a slightly different set of skills compared to working in academia.\nThe emphasis becomes providing business (often monetary) value.\nState-of-the-art models may not be needed, and sometimes explainability is more important.\nSoftware engineering skills often are more important than understanding the complexities of advanced algorithms."
        )
        return []

class AcademicBackgroundForm(FormAction):
    def name(self) -> Text:
        return "academic_background_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot('has_studies') == False:
            return ["has_studies"]
        else:
            return [
                "has_studies", "major_one", "major_two", "years_of_study"
            ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "has_studies":[
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
            "major_one": [
                self.from_entity(
                    entity="discipline",
                    not_intent="chitchat"
                )
            ],
            "major_two": [
                self.from_entity(
                    entity="discipline",
                    not_intent="chitchat"
                )
            ],
            "years_of_study": [
                self.from_entity(
                    entity="num_years",
                    intent=[
                        "academic_background",
                        "num_years"
                    ],
                    not_intent=[
                        "work_background"
                    ]
                )
            ]
        }


    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_years_of_study(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"years_of_study": value}
        else:
            dispatcher.utter_message(template="utter_not_int")
            # validation failed, set slot to None
            return {"years_of_study": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks")
        return []

class WorkExpForm(FormAction):
    arr_languages = [
        "python", "r", "sql", "scala", "julia", "matlab",
        "vba", "sas", "go", "Gglang", "java", "c++", "c",
        "rust", "haskell", "clojure", "javascript", "other"
    ]

    def name(self) -> Text:
        return "work_exp_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "lang_one", "lang_two", "lang_three", "years_of_work"
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "lang_one": [
                self.from_entity(
                    entity="language",
                    not_intent="chitchat"
                )
            ],
            "lang_two": [
                self.from_entity(
                    entity="language",
                    not_intent="chitchat"
                )
            ],
            "lang_two": [
                self.from_entity(
                    entity="language",
                    not_intent="chitchat"
                )
            ],
            "years_of_work": [
                self.from_entity(
                    entity="num_years",
                    intent=[
                        "work_background",
                        "num_years"
                    ],
                    not_intent=[
                        "academic_background"
                    ]
                )
            ]
        }


    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_lang_one(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:

        if value not in arr_languages:
            return {"lang_one": "none"}
        else:
            return {"lang_one": value}

    def validate_lang_two(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:

        if value.lower() not in arr_languages:
            return {"lang_two": "none"}
        else:
            return {"lang_two": value}

    def validate_lang_three(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:

        if value not in arr_languages:
            return {"lang_three": "none"}
        else:
            return {"lang_three": value}

    def validate_years_of_work(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"years_of_work": value}
        else:
            dispatcher.utter_message(template="utter_not_int")
            # validation failed, set slot to None
            return {"years_of_work": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks")
        return []

class IndustryOrAcademiaForm(FormAction):
    def name(self) -> Text:
        return "industry_or_academia_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "work_in_research"
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "work_in_research":[
                self.from_intent(intent="research", value=True),
                self.from_intent(intent="industry", value=False),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks")
        return []
