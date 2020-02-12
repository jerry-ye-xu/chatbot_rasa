
## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm

## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm
    - action_default_ask_affirmation
* affirm
    - utter_ask_me
* career_paths{"discipline": "data science"}
    - exp_and_background_form
    - form{"name": "exp_and_background_form"}
    - slot{"requested_slot": "academic_background"}
* form: strong_idea{"discipline": "math"}

## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm
    - exp_and_background_form
    - form{"name": "exp_and_background_form"}
    - slot{"requested_slot": "major_one"}
* form: academic_background{"discipline": "math"}
    - form: exp_and_background_form
    - slot{"major_one": "math"}
    - slot{"requested_slot": "major_two"}
* form: academic_background{"discipline": "comp sci"}
    - form: exp_and_background_form
    - slot{"major_two": "comp sci"}
    - slot{"requested_slot": "years_of_exp"}
* form: industry

## interactive_story_2
* want_random_fact
    - utter_random_fact
* want_random_fact
    - utter_random_fact
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* want_random_fact
    - utter_random_fact

## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
* career_paths{"discipline": "data science"}
    - exp_and_background_form
    - form{"name": "exp_and_background_form"}
    - slot{"requested_slot": "major_one"}
* form: academic_background{"discipline": "cs"}
    - form: exp_and_background_form
    - slot{"major_one": "cs"}
    - slot{"requested_slot": "major_two"}
* form: academic_background{"discipline": "math"}
    - form: exp_and_background_form
    - slot{"major_two": "math"}
    - slot{"requested_slot": "years_of_exp"}
* years_of_exp
    - respond_chitchat

## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
* career_paths
    - exp_and_background_form
    - form{"name": "exp_and_background_form"}
    - slot{"requested_slot": "major_one"}
* form: academic_background{"discipline": "cs"}
    - form: exp_and_background_form
    - slot{"major_one": "cs"}
    - slot{"requested_slot": "major_two"}
* form: academic_background{"discipline": "math"}
    - form: exp_and_background_form
    - slot{"major_two": "math"}
    - slot{"requested_slot": "years_of_exp"}
* form: work_exp{"num_work_years": "2"}
    - form: exp_and_background_form
    - slot{"years_of_exp": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
* average_salary{"discipline": "data scientist"}
    - action_salary_range
* average_salary{"discipline": "data scientist"}
    - action_salary_range
    - utter_did_that_help
* affirm
    - utter_ask_me
* industry

## interactive_story_1
* greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
* affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
* average_salary
    - action_salary_range
    - utter_did_that_help
* affirm
    - utter_smile
    - utter_ask_me
* industry{"discipline": "data scientist"}
    - action_industry_advice
* industry
    - action_industry_advice
    - utter_did_that_help
    - utter_ask_me
* career_paths{"discipline": "data scientist"}
    - exp_and_background_form
    - form{"name": "exp_and_background_form"}
    - slot{"requested_slot": "major_one"}
* form: academic_background{"discipline": "stats"}
    - form: exp_and_background_form
    - slot{"major_one": "stats"}
    - slot{"requested_slot": "major_two"}
* form: academic_background{"discipline": "math"}
    - form: exp_and_background_form
    - slot{"major_two": "math"}
    - slot{"requested_slot": "years_of_exp"}
* form: work_exp{"num_work_years": "2"}
    - form: exp_and_background_form
    - slot{"years_of_exp": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
* average_salary
* average_salary{"discipline": "data scientist"}
    - action_salary_range
    - utter_did_that_help
* affirm
    - utter_smile
    - utter_ask_me
    - action_pause
* goodbye
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* request_study_advice{"discipline": "data science"}
    - utter_please_fill_form
    - academic_background_form
    - form{"name": "academic_background_form"}
    - slot{"requested_slot": "has_studies"}
* form: academic_background
    - form: academic_background_form
* form: affirm
    - form: academic_background_form
    - slot{"has_studies": true}
    - slot{"requested_slot": "major_one"}
* form: academic_background{"discipline": "cs"}
    - form: academic_background_form
    - slot{"major_one": "cs"}
    - slot{"requested_slot": "major_two"}
* form: academic_background{"discipline": "stats"}
    - form: academic_background_form
    - slot{"major_two": "stats"}
    - slot{"requested_slot": "years_of_study"}
* form: num_years{"num_years": "3"}
    - form: academic_background_form
    - slot{"years_of_study": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_pause
    - action_degree_advice
    - utter_did_that_help
* appreciation
    - utter_your_welcome
* ask_average_salary{"discipline": "data scientists"}
    - action_salary_range
    - utter_did_that_help
* deny
    - utter_sadface
    - utter_ask_me
* goodbye
    - utter_goodbye
<!-- * ask_job_scopes
    - action_career_options
    - utter_did_that_help
* affirm
    - utter_smile
    - utter_ask_me -->
