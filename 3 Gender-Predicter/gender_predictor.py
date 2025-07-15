import requests

def predict_gender(name):
    url = f"https://api.genderize.io?name={name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("\n[Error] Could not connect to the API. Check your internet connection.")
        return None

def display_result(data):
    name = data.get("name")
    gender = data.get("gender")
    probability = data.get("probability")

    print("\n" + "=" * 35)
    print("       GENDER PREDICTION RESULT")
    print("=" * 35)
    print(f"  Name        : {name.capitalize()}")
    if gender is None:
        print("  Gender      : Could not predict")
        print("  Probability : N/A")
    else:
        print(f"  Gender      : {gender.capitalize()}")
        print(f"  Probability : {probability * 100:.1f}%")
    print("=" * 35)



while True:
    name = input("\nEnter a name (or type 'exit' to quit): ").strip()

    if name.lower() == "exit":
        print("\nGoodbye!\n")
        break

    if not name.isalpha():
        print("\n[Error] Invalid input. Please enter a valid name (letters only).")
        continue

    data = predict_gender(name)

    if data is not None:
        display_result(data)

