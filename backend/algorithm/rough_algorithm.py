class Algorithm(Request):

    dictionary = 
    {
    'Education Navigation (REN)' : 'OPC',
    'Education support (RES)' : 'OQC',
    'Employment Navigation (RENA)' : 'OPC',
    'Employment Support (RESA)' : 'OQC'
    'Health care Navigation (RHN)' : 'OPC',
    'Health care Support (RHS)' : 'OQC',
    'Local  Navigation (RLN)' : 'OPC',
    'Local support (RLS)' : 'OQC',
    'Wellbeing/leisure (RWL)' : 'OQC',
    'Pick up and delivery (RPUD)' : 'OQE',
    'Pick up and drop off (RPUO)' : 'OQE',
    'Homemaking supports (RHMS)' : 'OQE'
    }

    def unpack_request(Request):
        opc_score = 0
        oqc_score = 0
        oqe_score = 0

        scores = [] 

        if Request.education_navigation == True:
            opc_score += 1
        if Request.education_support == True:
            oqc_score += 1
        if Request.employment_navigation == True:
            opc_score += 1 
        if Request.employment_support == True:
            oqc_score += 1
        if Request.health_care_navigation == True:
            opc_score += 1
        if Request.health_care_support == True:
            oqc_score += 1
        if Request.local_navigation == True:
            opc_score += 1
        if Request.local_support == True:
            oqc_score += 1
        if Request.wellbeing_leisure == True:
            oqc_score += 1
        if Request.pickup_delivery == True:
            oqe_score += 1
        if pickup_dropoff == True:
            oqe_score += 1
        if homemaking_supports == True:
            oqe_score += 1 

        scores.append(opc_score)
        scores.append(oqc_score)
        scores.append(oqe_score)

        return scores

    def compare_against_user(scores, user):

        matching_score = 0

        if user.chat_call == True:
            matching_score += scores[0] 
        if user.connect == True:
            matching_score += scores[1] 
        if user.errand_task == True:
            matching_score += scores[2]

        return (user.username, matching_score) 

        # username may be replaced with gmail or any other suitable field 