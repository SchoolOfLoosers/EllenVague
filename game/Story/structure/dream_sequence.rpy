label dream_sequence:
    if not played_dream_gas_station_1_sequence:
        $played_dream_gas_station_1_sequence = True
        call dream_gas_station_1
    if not played_dream_nightmare_interview_1_sequence and completed_ec_patty_1:
        $played_dream_nightmare_interview_1_sequence = True
        call dream_nightmare_interview_1