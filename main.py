import json

def load_bus_data(file_path):
    with open('bus.json', 'r') as file:
        data = json.load(file)
    return data

def get_bus_timings(question, data):
    question = question.lower().strip()
    for item in data["questions"]:
        keywords = item["keywords"]
        if any(keyword.lower() in question for keyword in keywords):
            return item["answer"]
    return "Sorry, I don't have information about that."

def main():
    file_path = "bus.json"  # Path to your JSON file
    bus_data = load_bus_data('bus.json')

    while True:
        user_question = input("What do you want to know about bus timings? (Type 'quit' to exit)\n")
        if user_question.lower().strip() == 'quit':
            print("Exiting...")
            break
        else:
            response = get_bus_timings(user_question, bus_data)
            print(response)

if __name__ == "__main__":
    main()
