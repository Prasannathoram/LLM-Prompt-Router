from classifier import classify_intent
from router import route_and_respond
from logger import log_route


def run():

    while True:

        message = input("\nEnter message: ")

        if message.lower() == "exit":
            break

        intent_data = classify_intent(message)

        response = route_and_respond(message, intent_data)

        log_route(intent_data, message, response)

        print("\nDetected Intent:", intent_data["intent"])
        print("Confidence:", intent_data["confidence"])

        print("\nResponse:\n")
        print(response)


if __name__ == "__main__":
    run()