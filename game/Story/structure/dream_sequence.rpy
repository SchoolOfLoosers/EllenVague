label dream_sequence:
    if not played_dream_gas_station_1_sequence:
        $played_dream_gas_station_1_sequence = True
        call dream_gas_station_1
    if not played_dream_nightmare_interview_1_sequence and completed_ec_patty_1 and not ec_sarah_1_said_no_to_sex and not ec_sarah_1_had_sex_with_sarah:
        $played_dream_nightmare_interview_1_sequence = True
        call dream_nightmare_interview_1


    return