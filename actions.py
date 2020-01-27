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


#############################

####   GENERAL ACTIONS   ####

#############################

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

class ActionDataScienceTools(Action):
    def name(self) -> Text:
        return "action_ds_tools"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Python, R and SQL are the most used languages in the profession. Typically you would be required to learn one of either R or Python.\nIn the real world, you may need to incorporate your models into a web application, and be able to deploy and maintain it.\nThis would require a huge range of skills, including knowledge of web languages such as Javascript, CI/CD tools such as Jenkins and containerisation tools such as Docker."
        )
        return []

class ActionDayToDay(Action):
    def name(self) -> Text:
        return "action_day_to_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Data scientist is a very broad term, and the job description can vary greatly depending on industry and seniority.\nAt the junior level, you would be expected to clean and analysis data, build and test models.\nIf you are required to interface with the business-side, you may need to prepare presentations, dashboards and other communication materials.\nOverall, your day-to-day could be non-stop coding, engaging with stakeholders or even catching up on the most recent work in research!"
        )
        return []

#############################

####   SPECIFIC ADVICE   ####

#############################

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

class ActionDegreeAdvice(Action):
    def name(self) -> Text:
        return "action_degree_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if not tracker.get_slot("has_studies"):
            dispatcher.utter_message(
                text="I strongly recommend taking a combination of subjects in statistics, computer science and mathematics. This is because data science is fusion of multiple disciplines, and there are important concepts in each field you should understand.\nThe gains once you dive deeper in each field is marginal so just choose what you like after you cover the basics.\nIf you are interested in a different field, taking some electives would benefit you greatly.\nIn statistics, you should take some subjects linear models, statistical inference, probability theory and time series/stohastic processes.\nIn math, linear algebra and vector calculus are essential. Taking a course in optimisation would be useful too. Eventually taking measure theory would be helpful for more advanced probability theory.\nData structures and algorithms in computer science are fundamental. Distributed systems and operating systems would be very useful if you have enough space to take them.\nThese are just suggestions!"
            )

        else:
            msg_combined = []
            major_one = tracker.get_slot("major_one")
            major_two = tracker.get_slot("major_two")
            major_arr = [major_one, major_two]

            if major_one == "other" and (major_two == "other" or major_two == "none"):
                no_stem_major = "Pursuing your field of interest is very important. You should not force yourself to study something you are not interested in.\nThat being said, if you want to learn some data science, taking some of the electives mentioned below would benefit you greatly.\nThese are just suggestions!"
                msg_combined.append(no_stem_major_msg)

            if "cs" not in major_arr:
                do_cs_msg = "Programming skills are very important for both academia and research. I would recommend taking some fundamental CS subjects.\nData structures and algorithms in computer science are fundamental.\nDistributed systems and operating systems would be very useful if you have enough space to take them."
                msg_combined.append(do_cs_msg)
            else:
                cs_msg = "Nice to see that you are doing computer science!"
                msg_combined.append(cs_msg)

            if "math" not in major_arr:
                do_math_msg = "Math is the core of data science. It may not seem directly applicable, but a strong foundation will allow you to learn things more quickly later down the track.\nConsidering that data science is evolving at such a rapid pace, building a skillset to self-teach is important.\nLinear algebra and vector calculus are essential. Measure theory would be helpful for probability theory.\nOptimisation is also really helpful, but likely requires substantial prerequisites.\n"
                msg_combined.append(do_math_msg)
            else:
                math_msg = "Math is really good for building a strong foundation in data science, so it's good that you are taking it."
                msg_combined.append(math_msg)

            if "stats" not in major_arr:
                do_stats_msg = "Statistics is super useful. Taking some courses in probability theory would be helpful. An advanced course in linear models is important, as it's one of the fundamental models in machine learning. Statistical inference and Bayesian statistics are also valuable courses."
                msg_combined.append(do_stats_msg)
            else:
                stats_msg = "Statistics is often seen as the \"pre\"data science discipline but the truth is much of the field is directly relevant. ANOVA-bot is a stats major too!"
                msg_combined.append(stats_msg)

            degree_advice_msg = "\n".join(msg_combined)
            dispatcher.utter_message(
            text=f"{degree_advice_msg}"
            )

        return []


##########################

####   FORM ACTIONS   ####

##########################

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
                self.from_intent(intent="academic_background", value=True)
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
