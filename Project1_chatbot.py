import json
import random
import datetime

# -------------------------------------------------------------
# 1. ROUTE DATABASE (Supports Dynamic Additions)
# -------------------------------------------------------------
route_database = {
    "1": {
        "title": "Shakargarh ➔ University Campus",
        "fare": "Rs. 250 per student",
        "driver": "Ali Raza (CS Dept)",
        "rating": "4.9 ⭐ (54 Rides)",
        "safety": "Verified ID, Live GPS, SOS Ready",
        "pickup_stops": "Railway Station, Circular Road",
        "timing": "07:30 AM"
    },
    "2": {
        "title": "Narowal City ➔ University Campus",
        "fare": "Rs. 120 per student",
        "driver": "Usman Ahmad (SE Dept)",
        "rating": "4.8 ⭐ (38 Rides)",
        "safety": "Verified Staff Driver, Dashcam Enabled",
        "pickup_stops": "Kachery Road, Saddar Bazaar",
        "timing": "07:45 AM"
    },
    "3": {
        "title": "Zafarwal ➔ University Campus",
        "fare": "Rs. 200 per student",
        "driver": "Hamza Tariq (EE Dept)",
        "rating": "4.7 ⭐ (29 Rides)",
        "safety": "Verified Driver, Live GPS Active",
        "pickup_stops": "Main Highway Stop, Bypass Chowk",
        "timing": "07:15 AM"
    },
    "4": {
        "title": "Local Hostels Express",
        "fare": "Rs. 80 per student",
        "driver": "Bilal Hassan (Physics Dept)",
        "rating": "4.9 ⭐ (82 Rides)",
        "safety": "Campus Guard Verified Driver",
        "pickup_stops": "Housing Colony 1 & 2",
        "timing": "08:00 AM"
    }
}

intents_data = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "salam", "start"],
        "responses": [
            "Salam! Welcome to CampusRide Narowal. Type 'routes' to book, 'offer' to post a ride, or ask about safety/fares!",
            "Hello! I am your Student Carpool Assistant. Do you want to book a ride or offer a ride today?"
        ]
    },
    "safety_policy": {
        "keywords": ["safe", "safety", "darr", "fear", "security", "verify", "driver", "sos", "gps"],
        "responses": [
            "🛡️ 100% Safe & Secure!\n  1. Student Verification mandatory.\n  2. Live GPS Ride tracking.\n  3. In-app SOS button."
        ]
    }
}

def log_conversation(user_input, bot_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("carpool_chat_history.log", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] User: {user_input}\n")
        file.write(f"[{timestamp}] Bot: {bot_response}\n\n")

# -------------------------------------------------------------
# 2. OFFER A RIDE FORM (Adds new ride to database dynamically)
# -------------------------------------------------------------
def handle_offer_ride():
    print("\n--- 🚗 OFFER A RIDE (DRIVER REGISTRATION FORM) ---")
    name = input("Enter your Full Name: ").strip()
    student_id = input("Enter your Student Roll No / Department: ").strip()
    phone = input("Enter your Contact / WhatsApp Number: ").strip()
    vehicle = input("Enter Vehicle Details (e.g. Honda CD70 / Alto LEB-123): ").strip()
    
    start_loc = input("Pickup Area (e.g. Shakargarh / Saddar Bazaar): ").strip()
    dest_loc = input("Destination (e.g. University Main Campus): ").strip()
    fare = input("Enter Demanded Fare per Seat (e.g. Rs. 150): ").strip()
    timing = input("Enter Departure Time (e.g. 07:30 AM): ").strip()

    # Create new option key (e.g., '5')
    next_index = str(len(route_database) + 1)
    route_title = f"{start_loc} ➔ {dest_loc}"

    # Add dynamically to Database
    route_database[next_index] = {
        "title": route_title,
        "fare": f"{fare} per student",
        "driver": f"{name} ({student_id})",
        "rating": "5.0 ⭐ (New Verified Driver)",
        "safety": f"Verified Student ID, Contact: {phone}, Vehicle: {vehicle}",
        "pickup_stops": start_loc,
        "timing": timing
    }

    success_msg = (
        f"\n🎉 CONGRATULATIONS {name.upper()}! YOUR RIDE IS NOW LIVE!\n"
        f"---------------------------------------------------\n"
        f" Assigned Route Option ID: #{next_index}\n"
        f" Route: {route_title}\n"
        f" Fare: {fare} per student\n"
        f" Departure Time: {timing}\n"
        f"---------------------------------------------------\n"
        f"Other students can now view and book your ride via 'routes' menu!"
    )
    print(success_msg)
    log_conversation("OFFER RIDE SUBMITTED", success_msg)

# -------------------------------------------------------------
# 3. PASSENGER BOOKING FORM
# -------------------------------------------------------------
def handle_registration(pre_selected_route=None):
    print("\n--- 📝 STUDENT RIDE BOOKING FORM ---")
    name = input("Enter your Full Name: ").strip()
    student_id = input("Enter your Student Roll No / ID: ").strip()
    
    if pre_selected_route and pre_selected_route in route_database:
        route_info = route_database[pre_selected_route]
        selected_route_name = route_info["title"]
        estimated_fare = route_info["fare"]
    else:
        choice = input("Enter Route Number: ").strip()
        route_info = route_database.get(choice, route_database["1"])
        selected_route_name = route_info["title"]
        estimated_fare = route_info["fare"]

    pickup_spot = input("Enter exact Pickup Location: ").strip()
    timing = input("Enter Preferred Pick-up Time: ").strip()

    confirmation = (
        f"\n✅ RIDE BOOKED SUCCESSFULLY!\n"
        f"-----------------------------------\n"
        f" Passenger Name: {name} ({student_id})\n"
        f" Selected Route: {selected_route_name}\n"
        f" Total Fare: {estimated_fare}\n"
        f" Assigned Driver: {route_info['driver']}\n"
        f" Pickup Location: {pickup_spot} @ {timing}\n"
        f"-----------------------------------\n"
    )
    print(confirmation)
    log_conversation("BOOKING SUBMITTED", confirmation)

# -------------------------------------------------------------
# 4. MAIN ENGINE
# -------------------------------------------------------------
def run_carpool_bot():
    print("=====================================================")
    print("   🚘 CAMPUS-RIDE ASSISTANT (Narowal & Shakargarh) 🚘   ")
    print("=====================================================")
    print("Type 'routes' to see/book rides | Type 'offer' to list your ride | Type 'exit' to quit.\n")

    bot_state = "NORMAL"
    last_viewed_route = None

    while True:
        raw_input = input("Student: ")
        clean_input = raw_input.lower().strip()

        if clean_input in ["exit", "bye", "quit"]:
            print("Bot: Goodbye! Safe journey!")
            break

        if not clean_input:
            continue

        # Route Detail Viewing State
        if bot_state == "AWAITING_ROUTE_CHOICE" and clean_input in route_database.keys():
            selected = route_database[clean_input]
            last_viewed_route = clean_input
            
            response = (
                f"\n📍 ROUTE DETAILS: {selected['title']}\n"
                f"---------------------------------------------------\n"
                f"💰 Fare: {selected['fare']}\n"
                f"👨‍✈️ Offered By / Driver: {selected['driver']}\n"
                f"⭐ Rating: {selected['rating']}\n"
                f"🛡️ Safety Info: {selected['safety']}\n"
                f"🚏 Pickup Spot: {selected['pickup_stops']}\n"
                f"⏰ Timing: {selected['timing']}\n"
                f"---------------------------------------------------\n"
                f"Do you want to book a seat in this ride? (Type 'yes' or 'no')"
            )
            print(f"Bot: {response}\n")
            log_conversation(raw_input, response)
            bot_state = "CONFIRM_BOOKING"
            continue

        # Confirmation State
        if bot_state == "CONFIRM_BOOKING":
            if clean_input in ["yes", "y", "haan", "ha", "sure", "book"]:
                handle_registration(pre_selected_route=last_viewed_route)
                bot_state = "NORMAL"
                print()
                continue
            else:
                print("Bot: Okay! Type 'routes' to check other options.\n")
                bot_state = "NORMAL"
                continue

        # Offer Ride Trigger
        if any(kw in clean_input for kw in ["offer", "drive", "give ride", "my car", "my bike"]):
            handle_offer_ride()
            bot_state = "NORMAL"
            print()
            continue

        # Display Available Routes
        if any(kw in clean_input for kw in ["route", "routes", "location", "available"]):
            print("📍 Currently Available Campus Rides:")
            for key, data in route_database.items():
                print(f"  {key}. {data['title']} (by {data['driver'].split('(')[0].strip()})")
            
            print("\n👉 Type/Press any Route Number (e.g. 1, 2, 3...) to view details & book!")
            bot_state = "AWAITING_ROUTE_CHOICE"
            continue

        # General Passenger Registration Trigger
        if clean_input in ["register", "book"]:
            handle_registration()
            bot_state = "NORMAL"
            print()
            continue

        # Default Keyword Fallback
        matched = False
        for intent, data in intents_data.items():
            for keyword in data["keywords"]:
                if keyword in clean_input:
                    bot_response = random.choice(data["responses"])
                    print(f"Bot: {bot_response}\n")
                    matched = True
                    break
            if matched: break
        
        if not matched:
            print("Bot: Type 'routes' to view/book rides, or type 'offer' to list your own ride!\n")

if __name__ == "__main__":
    run_carpool_bot()
