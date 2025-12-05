# -------------------------------
# Gardening Advice Program
# -------------------------------

# Function to get user inputs
def get_user_inputs():
    """
    Ask the user for the current season and plant type.
    Returns both values as lowercase strings.
    """
    season = input("Enter the current season (summer, winter, spring, autumn): ").lower()
    plant_type = input("Enter the plant type (flower, vegetable, herb): ").lower()
    return season, plant_type


# Function containing advice based on season
def get_season_advice(season):
    """
    Provide gardening advice depending on the season.
    """
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
        "spring": "A great time to plant new seedlings.\n",
        "autumn": "Prepare your garden for colder weather.\n"
    }
    return season_advice.get(season, "No advice for this season.\n")


# Function containing advice based on plant type
def get_plant_advice(plant_type):
    """
    Provide advice depending on the plant type.
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest leaves regularly to promote growth."
    }
    return plant_advice.get(plant_type, "No advice for this type of plant.")


# Function to recommend plants based on the season
def recommend_plants(season):
    """
    Suggest plants suitable for the selected season
    """
    recommendations = {
        "summer": ["Sunflowers", "Tomatoes", "Basil"],
        "winter": ["Kale", "Winter cabbage", "Pansies"],
        "spring": ["Lavender", "Strawberries", "Mint"],
        "autumn": ["Broccoli", "Cauliflower", "Marigolds"]
    }
    plants = recommendations.get(season, [])
    if plants:
        return "Recommended plants for this season: " + ", ".join(plants)
    return "No plant recommendations available."


# -------------------------------
# Main Program
# -------------------------------

# Get inputs from the user
season, plant_type = get_user_inputs()

# Generate advice
advice = get_season_advice(season)
advice += get_plant_advice(plant_type)
advice += "\n" + recommend_plants(season)

# Display final advice
print("\n--- Gardening Advice ---")
print(advice)

