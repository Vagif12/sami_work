fake_system_data_workout_and_skipping_assistant = {
    "goal":"Complete a half marathon in under 2 hours within 3 months",
    "user_data":"""
    Here's some sample data using the metrics mentioned, with distances converted to kilometers:
    ---
    Jane Doe, age 32, is an intermediate-level runner with a weekly mileage of 20-25 miles. She has a history of knee strain and prefers long-distance running and interval training

    - **Cadence**: 180 steps per minute (SPM)
    - **Stride Length**: 1.2 meters
    - **Distance covered per minute** = 180 SPM * 1.2 meters = 216 meters/minute
    - **Ground Contact Time**: 210 milliseconds (ms) 
    - **Vertical Oscillation**: 6.5 cm
    - **Vertical Ratio**: 5.4% (calculated as vertical oscillation / stride length)
    - **Heart Rate**: 
    - **Resting**: 55 BPM
    - **Average during run**: 150 BPM
    - **Maximum**: 180 BPM
    - **Power**: 250 Watts (W)
    - **Intensity Factor**: 0.85
    - **Efficiency Factor**: 1.7 (calculated as power / heart rate)
    - **Aerobic Decoupling (Pw:Hr)**: 3.5% (suggesting steady aerobic efficiency)
    - **Pace**: Average of 5 min/km
    - **Grade Adjusted Pace (GAP)**: 4:55 min/km (slight adjustment due to minor elevation)
    - **Elevation Gain**: 120 meters over the course of the run

    ---

    - **Ground Contact Time Balance**: Left 51%, Right 49% (slightly off balance but within acceptable range)
    - **Lactate Threshold**: 4:45 min/km (estimated threshold pace)
    - **Recovery Time**: 24 hours recommended post-run
    - **VO2 Max**: 52 mL/kg/min (high aerobic capacity)
    - **Trail VO2 Max**: 50 mL/kg/min (slightly lower due to trail conditions)
    - **3D Distance**: 10.5 km (distance accounting for elevation changes)
    - **Body Battery**: 80% (moderate energy levels pre-run)
    - **Fitness Age**: 29 (based on fitness level)
    - **Heart Rate Variability (HRV)**: 70 ms
    - **Stress Level**: 30 (low to moderate stress level)
    - **Intensity Minutes**: 90 minutes (time spent in moderate to high intensity zones)
    - **Sleep Score**: 85 (good recovery quality)
    - **Training Status**: Productive
    - **Training Load**: 550 (optimal range)
    - **Pulse Ox**: 95% (oxygen saturation)
    - **Steps**: 12,000 (total steps for the day)
    - **Performance Condition**: +2 (showing slight improvement over baseline)
    - **Training Readiness**: High
    - **GPS Modes**: Standard (high accuracy mode enabled)
    - **Pace Pro**: Following pace targets for race day simulation
    - **Climb Pro**: Used for tracking hill segments
    - **Race Predictor**: Predicted half-marathon time of 1:52:30
    - **Navigation**: On-route guidance enabled
    - **Stamina**: 75% at start of run
    - **Suggested Workouts**: Endurance run or tempo intervals
    - **Endurance Score**: 70 (high endurance capacity)
    - **Hill Score (Endurance and Strength)**: 68 (indicating good strength for hill running)

    ---
    """,
    "existing_plan":"""
    Monthly Running Plan:

    Week 1: Tempo Run

    Distance: 8 km
    Pace: 5:00 min/km
    Description: Warm up with 1 km at an easy pace, then run 6 km at a steady tempo pace (challenging but sustainable), followed by a 1 km cooldown. Focus on maintaining a consistent rhythm and keeping your form relaxed.
    Week 2: Interval Training

    Distance: 6 x 800 meters
    Pace: 4:30 min/km for intervals, 6:00 min/km for recovery jogs
    Description: Begin with a 1 km warm-up. Run 800 meters at a faster pace (4:30 min/km), then recover with 400 meters at a slow jog. Repeat six times. Finish with a 1 km cooldown. This workout builds speed and endurance.
    Week 3: Long Run

    Distance: 12 km
    Pace: 5:45-6:00 min/km
    Description: Run at an easy, conversational pace to improve endurance. Focus on steady breathing and maintaining good posture. The goal is to build stamina and get comfortable with longer distances.
    Week 4: Hill Repeats

    Distance: 5 x 400 meters uphill
    Pace: 5:15 min/km on uphills, recovery jog back down
    Description: Warm up with 1 km at an easy pace. Find a moderate hill (4-5% grade) and run up at a strong but controlled pace, focusing on form. Jog back down to recover. Repeat five times. Finish with a 1 km cooldown. This workout builds leg strength and improves efficiency on hills.
    """,    
}



fake_system_data_workout_plan_creation = {
    "user_data":"""
    Here's some sample data using the metrics mentioned, with distances converted to kilometers:
    ---
    Jane Doe, age 32, is an intermediate-level runner with a weekly mileage of 20-25 miles. She has a history of knee strain and prefers long-distance running and interval training

    - **Cadence**: 180 steps per minute (SPM)
    - **Stride Length**: 1.2 meters
    - **Distance covered per minute** = 180 SPM * 1.2 meters = 216 meters/minute
    - **Ground Contact Time**: 210 milliseconds (ms) 
    - **Vertical Oscillation**: 6.5 cm
    - **Vertical Ratio**: 5.4% (calculated as vertical oscillation / stride length)
    - **Heart Rate**: 
    - **Resting**: 55 BPM
    - **Average during run**: 150 BPM
    - **Maximum**: 180 BPM
    - **Power**: 250 Watts (W)
    - **Intensity Factor**: 0.85
    - **Efficiency Factor**: 1.7 (calculated as power / heart rate)
    - **Aerobic Decoupling (Pw:Hr)**: 3.5% (suggesting steady aerobic efficiency)
    - **Pace**: Average of 5 min/km
    - **Grade Adjusted Pace (GAP)**: 4:55 min/km (slight adjustment due to minor elevation)
    - **Elevation Gain**: 120 meters over the course of the run

    ---

    - **Ground Contact Time Balance**: Left 51%, Right 49% (slightly off balance but within acceptable range)
    - **Lactate Threshold**: 4:45 min/km (estimated threshold pace)
    - **Recovery Time**: 24 hours recommended post-run
    - **VO2 Max**: 52 mL/kg/min (high aerobic capacity)
    - **Trail VO2 Max**: 50 mL/kg/min (slightly lower due to trail conditions)
    - **3D Distance**: 10.5 km (distance accounting for elevation changes)
    - **Body Battery**: 80% (moderate energy levels pre-run)
    - **Fitness Age**: 29 (based on fitness level)
    - **Heart Rate Variability (HRV)**: 70 ms
    - **Stress Level**: 30 (low to moderate stress level)
    - **Intensity Minutes**: 90 minutes (time spent in moderate to high intensity zones)
    - **Sleep Score**: 85 (good recovery quality)
    - **Training Status**: Productive
    - **Training Load**: 550 (optimal range)
    - **Pulse Ox**: 95% (oxygen saturation)
    - **Steps**: 12,000 (total steps for the day)
    - **Performance Condition**: +2 (showing slight improvement over baseline)
    - **Training Readiness**: High
    - **GPS Modes**: Standard (high accuracy mode enabled)
    - **Pace Pro**: Following pace targets for race day simulation
    - **Climb Pro**: Used for tracking hill segments
    - **Race Predictor**: Predicted half-marathon time of 1:52:30
    - **Navigation**: On-route guidance enabled
    - **Stamina**: 75% at start of run
    - **Suggested Workouts**: Endurance run or tempo intervals
    - **Endurance Score**: 70 (high endurance capacity)
    - **Hill Score (Endurance and Strength)**: 68 (indicating good strength for hill running)

    ---
    """   
}