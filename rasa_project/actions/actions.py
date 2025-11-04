from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckPainInRange(Action):
    def name(self) -> Text:
        return "action_check_pain_in_range"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # hard-coded balance for tutorial purposes. in production this
        # would be retrieved from a database or an API
        pain = tracker.get_slot("patient_pain_intensity_scale")
        pain_in_range = 0<= pain <= 10
        return [SlotSet("pain_in_range", pain_in_range)]
