import streamlit as st
import json
import datetime
import random

# Load wardrobe
def load_wardrobe():
    with open('wardrobe.json', 'r') as f:
        return json.load(f)

# Choose today's outfit
def pick_outfit(wardrobe):
    today = datetime.date.today()
    unused_items = [item for item in wardrobe if item['last_worn'] != str(today)]
    outfit = random.sample(unused_items, k=min(2, len(unused_items)))  # 1 top + 1 bottom
    return outfit

# Save updated wardrobe
def update_last_worn(wardrobe, chosen_outfit):
    today = str(datetime.date.today())
    for item in wardrobe:
        if item in chosen_outfit:
            item['last_worn'] = today
    with open('wardrobe.json', 'w') as f:
        json.dump(wardrobe, f, indent=2)

# UI
def main():
    st.title("👕 Daily Wardrobe Picker")

    wardrobe = load_wardrobe()
    outfit = pick_outfit(wardrobe)

    st.subheader("Today's Outfit")
    for item in outfit:
        st.image(item["image"], width=150)
        st.write(f"{item['type'].title()}: {item['name']}")

    if st.button("Confirm Today's Outfit"):
        update_last_worn(wardrobe, outfit)
        st.success("Outfit saved!")

if __name__ == "__main__":
    main()
