import json
from datetime import datetime

def log_route(intent_data, message, final_response):

    log_entry = {
        "intent": intent_data["intent"],
        "confidence": intent_data["confidence"],
        "user_message": message,
        "final_response": final_response,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("route_log.jsonl","a+") as f:
        f.write(json.dumps(log_entry) + "\n")