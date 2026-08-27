import requests
import json
import os


# ============================================================
#              COUNTRY INFORMATION CLI APP
# ============================================================

BASE_URL = "https://countries.dev"
HISTORY_FILE = "search_history.json"


# ============================================================
# LOAD SEARCH HISTORY
# ============================================================

def load_history():
    """
    Load previous country searches from search_history.json.

    Returns:
        list: Previous searches
    """

    # Check if history file exists
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        # Open JSON file
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:

            history = json.load(file)

        # Make sure history is a list
        if isinstance(history, list):
            return history

        return []

    except json.JSONDecodeError:

        print("⚠️ History file contains invalid JSON.")
        return []

    except OSError:

        print("⚠️ Could not read search history.")
        return []


# ============================================================
# SAVE SEARCH HISTORY
# ============================================================

def save_history(history):
    """
    Save country search history into search_history.json.
    """

    try:

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    except OSError:

        print("❌ Could not save search history.")


# ============================================================
# SHOW SEARCH HISTORY
# ============================================================

def show_history(history):
    """
    Display all previously searched countries.
    """

    print("\n" + "=" * 60)
    print("                  📜 SEARCH HISTORY")
    print("=" * 60)

    # If history is empty
    if not history:

        print("📭 No search history found.")

    else:

        for number, country in enumerate(
            history,
            start=1
        ):

            print(f"{number}. {country}")

    print("=" * 60)


# ============================================================
# DISPLAY COUNTRY INFORMATION
# ============================================================

def display_country(country):
    """
    Display country information in a clean format.
    """

    # --------------------------------------------------------
    # Country name
    # --------------------------------------------------------

    name = country.get(
        "name",
        "N/A"
    )

    # --------------------------------------------------------
    # Official name
    # --------------------------------------------------------

    official_name = country.get(
        "nativeName",
        "N/A"
    )

    # --------------------------------------------------------
    # Capital
    # --------------------------------------------------------

    capital = country.get(
        "capital",
        "N/A"
    )

    # --------------------------------------------------------
    # Population
    # --------------------------------------------------------

    population = country.get(
        "population",
        "N/A"
    )

    # --------------------------------------------------------
    # Region
    # --------------------------------------------------------

    region = country.get(
        "region",
        "N/A"
    )

    # --------------------------------------------------------
    # Flag
    # --------------------------------------------------------

    flag = country.get(
        "flag",
        "🏳️"
    )

    # --------------------------------------------------------
    # Currency
    # --------------------------------------------------------

    currencies = country.get(
        "currencies",
        []
    )

    currency_list = []

    for currency in currencies:

        code = currency.get(
            "code",
            "N/A"
        )

        currency_name = currency.get(
            "name",
            "Unknown"
        )

        currency_symbol = currency.get(
            "symbol",
            ""
        )

        if currency_symbol:

            currency_text = (
                f"{currency_name} "
                f"({code}) "
                f"{currency_symbol}"
            )

        else:

            currency_text = (
                f"{currency_name} "
                f"({code})"
            )

        currency_list.append(
            currency_text
        )

    if currency_list:

        currency = ", ".join(
            currency_list
        )

    else:

        currency = "N/A"

    # --------------------------------------------------------
    # Languages
    # --------------------------------------------------------

    languages = country.get(
        "languages",
        []
    )

    language_list = []

    for language in languages:

        language_name = language.get(
            "name",
            "Unknown"
        )

        language_list.append(
            language_name
        )

    if language_list:

        language_text = ", ".join(
            language_list
        )

    else:

        language_text = "N/A"

    # ========================================================
    # PRINT INFORMATION
    # ========================================================

    print("\n" + "=" * 60)
    print("                🌍 COUNTRY INFORMATION")
    print("=" * 60)

    print(f"\n{flag}  {name}\n")

    print(f"Official Name : {official_name}")
    print(f"Capital       : {capital}")

    # Format population with commas
    if isinstance(population, int):

        print(
            f"Population    : {population:,}"
        )

    else:

        print(
            f"Population    : {population}"
        )

    print(f"Region        : {region}")
    print(f"Currency      : {currency}")
    print(f"Languages     : {language_text}")

    print("=" * 60)


# ============================================================
# SEARCH COUNTRY
# ============================================================

def search_country(country_name, history):
    """
    Search a country using countries.dev API.

    Handles:
        - ConnectionError
        - Timeout
        - HTTPError
        - JSON errors
        - Unexpected errors
    """

    # --------------------------------------------------------
    # Build API URL
    # --------------------------------------------------------

    url = f"{BASE_URL}/name/{country_name}"

    try:

        print(
            f"\n🔎 Searching for '{country_name}'..."
        )

        # ----------------------------------------------------
        # API REQUEST
        # ----------------------------------------------------

        response = requests.get(
            url,
            timeout=10
        )

        # ----------------------------------------------------
        # CHECK 404
        # ----------------------------------------------------

        if response.status_code == 404:

            print("\n❌ Country not found.")

            print(
                "Please check the spelling "
                "and try again."
            )

            return

        # ----------------------------------------------------
        # CHECK OTHER HTTP ERRORS
        # ----------------------------------------------------

        response.raise_for_status()

        # ----------------------------------------------------
        # CONVERT RESPONSE TO JSON
        # ----------------------------------------------------

        data = response.json()

        # ----------------------------------------------------
        # DEBUG / STRUCTURE CHECK
        # ----------------------------------------------------

        if not isinstance(data, list):

            print(
                "\n❌ Unexpected API response."
            )

            print(
                "The API did not return a list."
            )

            return

        # ----------------------------------------------------
        # CHECK EMPTY RESPONSE
        # ----------------------------------------------------

        if len(data) == 0:

            print(
                "\n❌ No country information found."
            )

            return

        # ----------------------------------------------------
        # FIRST COUNTRY
        # ----------------------------------------------------

        country = data[0]

        # ----------------------------------------------------
        # DISPLAY INFORMATION
        # ----------------------------------------------------

        display_country(country)

        # ----------------------------------------------------
        # SAVE SEARCH HISTORY
        # ----------------------------------------------------

        history.append(country_name)

        save_history(history)

        print(
            "\n✅ Search saved to history."
        )

    # ========================================================
    # CONNECTION ERROR
    # ========================================================

    except requests.exceptions.ConnectionError:

        print(
            "\n❌ Connection Error."
        )

        print(
            "Please check your internet connection."
        )

    # ========================================================
    # TIMEOUT ERROR
    # ========================================================

    except requests.exceptions.Timeout:

        print(
            "\n❌ Timeout Error."
        )

        print(
            "The API took too long to respond."
        )

    # ========================================================
    # HTTP ERROR
    # ========================================================

    except requests.exceptions.HTTPError as error:

        print(
            "\n❌ HTTP Error."
        )

        print(
            f"Details: {error}"
        )

    # ========================================================
    # JSON ERROR
    # ========================================================

    except requests.exceptions.JSONDecodeError:

        print(
            "\n❌ JSON Error."
        )

        print(
            "The API returned invalid JSON."
        )

    # ========================================================
    # UNEXPECTED ERROR
    # ========================================================

    except Exception as error:

        print(
            "\n❌ Unexpected Error."
        )

        print(
            f"Type   : {type(error).__name__}"
        )

        print(
            f"Details: {error}"
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    # --------------------------------------------------------
    # Load history
    # --------------------------------------------------------

    search_history = load_history()

    # --------------------------------------------------------
    # Welcome
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("              🌍 COUNTRY INFORMATION APP")
    print("=" * 60)

    print(
        "Powered by countries.dev"
    )

    print("=" * 60)

    # ========================================================
    # MAIN LOOP
    # ========================================================

    while True:

        # ----------------------------------------------------
        # MENU
        # ----------------------------------------------------

        print("\nPlease choose an option:")

        print(
            "1. 🌍 Search Country"
        )

        print(
            "2. 📜 View Search History"
        )

        print(
            "3. 🚪 Quit"
        )

        # ----------------------------------------------------
        # GET USER CHOICE
        # ----------------------------------------------------

        choice = input(
            "\nEnter your choice (1-3): "
        ).strip()

        # ====================================================
        # OPTION 1
        # ====================================================

        if choice == "1":

            country_name = input(
                "\nEnter a country name: "
            ).strip()

            # Check empty input
            if not country_name:

                print(
                    "\n❌ Country name cannot be empty."
                )

                continue

            # Search country
            search_country(
                country_name,
                search_history
            )

        # ====================================================
        # OPTION 2
        # ====================================================

        elif choice == "2":

            show_history(
                search_history
            )

        # ====================================================
        # OPTION 3
        # ====================================================

        elif choice == "3":

            print("\n" + "=" * 60)

            print(
                "👋 Thank you for using "
                "Country Information App!"
            )

            print(
                "Goodbye! 🚪"
            )

            print("=" * 60)

            break

        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "\n❌ Invalid choice."
            )

            print(
                "Please enter 1, 2, or 3."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()