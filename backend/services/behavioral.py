def analyze(tx):
    score = 0

    try:
        # Handle missing or invalid input
        if not tx.user_history.usual_time or "-" not in tx.user_history.usual_time:
            return 0

        # Split safely
        start_str, end_str = tx.user_history.usual_time.split("-")

        # Normalize
        start_str = start_str.strip().lower()
        end_str = end_str.strip().lower()

        def parse_hour(time_str):
            time_str = time_str.strip()

            # Handle AM/PM
            if "pm" in time_str:
                val = int(time_str.replace("pm", "").strip())
                return val + 12 if val != 12 else 12

            if "am" in time_str:
                val = int(time_str.replace("am", "").strip())
                return 0 if val == 12 else val

            # Handle HH:MM
            if ":" in time_str:
                return int(time_str.split(":")[0])

            # Fallback
            return int(time_str)

        usual_start = parse_hour(start_str)
        usual_end = parse_hour(end_str)

        current_hour = int(tx.time.split(":")[0])

        # Behavioral anomaly check
        if current_hour < usual_start or current_hour > usual_end:
            score += 20

    except Exception as e:
        print(" Behavioral Error:", e)
        return 0

    return score