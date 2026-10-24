
import streamlit as st

# ── Page configuration ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="Workout Planner",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Personal Workout Planner")
st.caption("Build a personalized workout based on your goals, fitness level, and equipment.")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 1 — st.slider
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("1. Workout Duration")

duration = st.slider(
    "How long do you want to work out?",
    min_value=10,
    max_value=120,
    value=30,
    step=5
)

st.metric("Workout Duration", f"{duration} minutes")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 2 — st.selectbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("2. Workout Type")

workout_type = st.selectbox(
    "What type of workout do you want?",
    ["Strength Training", "Cardio", "HIIT", "Yoga"]
)

workout_tips = {
    "Strength Training": "Focus on controlled movements and proper form.",
    "Cardio": "Maintain a steady pace and monitor your breathing.",
    "HIIT": "Alternate intense exercise with short recovery periods.",
    "Yoga": "Focus on flexibility, breathing, and controlled movement."
}

st.info(workout_tips[workout_type])

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 3 — st.radio
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("3. Fitness Level")

fitness_level = st.radio(
    "What is your current fitness level?",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

if fitness_level == "Beginner":
    st.info("Start with lighter exercises and longer rest periods.")

elif fitness_level == "Intermediate":
    st.info("Increase intensity and challenge yourself progressively.")

else:
    st.info("Focus on advanced movements and higher intensity.")


st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 4 — st.multiselect
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("4. Available Equipment")

equipment = st.multiselect(
    "What equipment do you have available?",
    [
        "Dumbbells",
        "Resistance Bands",
        "Kettlebells",
        "Yoga Mat",
        "Jump Rope",
        "Pull-up Bar"
    ],
    default=["Yoga Mat"]
)

if equipment:
    st.write("Your available equipment:")

    for item in equipment:
        st.write(f"✓ {item}")

else:
    st.warning("No equipment selected. Bodyweight exercises are still an option!")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 5 — st.text_input
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("5. Personal Workout Goal")

workout_goal = st.text_input(
    "What is your main fitness goal?",
    placeholder="Example: Build muscle, lose weight, improve endurance"
)

if workout_goal:
    st.success(f"Your goal: {workout_goal}")

    st.write("Here are some ideas to help you get started:")

    st.write(f"1. Create a weekly plan focused on {workout_goal}.")
    st.write(f"2. Track your progress toward {workout_goal}.")
    st.write(f"3. Adjust your training as you improve in {workout_goal}.")

else:
    st.info("Enter a goal to receive workout suggestions.")
st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 6 — st.checkbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("6. Your Personalized Workout Plan")

show_summary = st.checkbox(
    "Show my personalized workout plan",
    value=True
)

if show_summary:

    st.success("Your Workout Plan Is Ready!")

    st.write(f"**Workout Type:** {workout_type}")
    st.write(f"**Duration:** {duration} minutes")
    st.write(f"**Fitness Level:** {fitness_level}")
    st.write(f"**Equipment:** {', '.join(equipment) if equipment else 'Bodyweight only'}")
    st.write(f"**Personal Goal:** {workout_goal if workout_goal else 'General fitness'}")

    st.subheader("Estimated Calories Burned")

    calories_per_minute = {
        "Strength Training": 5,
        "Cardio": 8,
        "HIIT": 10,
        "Yoga": 3
    }

    intensity_multiplier = {
        "Beginner": 0.8,
        "Intermediate": 1.0,
        "Advanced": 1.2
    }

    estimated_calories = (
        duration
        * calories_per_minute[workout_type]
        * intensity_multiplier[fitness_level]
    )

    st.metric(
        "Estimated Calories",
        f"{estimated_calories:.0f} kcal"
    )

    progress = duration / 120

    st.progress(progress)

    st.caption("Workout duration relative to the 120-minute maximum.")
    st.caption("Calories are rough illustrative estimates, not personalized measurements.")
