# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

# Load dataset once for reuse
DATASET_PATH = '/content/test-project/Cleaned_Pet_Dataset_VetPal.xlsx'
data = pd.read_excel(DATASET_PATH)


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = (
            "I'm sorry, I didn't understand that. Can you please rephrase your question? "
            "I'm here to help with first-aid tips and advice for your pet."
        )
        dispatcher.utter_message(text=response)
        return []


class ActionCustomFallback(Action):
    def name(self):
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = (
            "I'm not sure I understood. Can you rephrase or clarify?"
            "I'm sorry, I didn't understand that. Can you please rephrase your question? "
        )
        dispatcher.utter_message(text=response)
        return []
