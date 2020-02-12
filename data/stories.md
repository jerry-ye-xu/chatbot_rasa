## student + quantitative degree + industry 1
  * greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
  * affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
  * request_job_advice
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "cs"}
      - form: academic_background_form
      - slot{"major_one": "cs"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "math"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"years_of_study": "2"}
      - form: academic_background_form
      - slot{"years_of_study": "2"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_industry_advice
      - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * ask_ds_tools
      - action_ds_tools
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
    - utter_goodbye

## student + quantitative degree + industry 2
  * greet
      - utter_purpose_of_existence
      - utter_greet
      - action_pause
      - utter_user_purpose
  * affirm
      - action_intro_ds
      - action_pause
      - utter_ask_me
  * request_job_advice{"discipline": "data scientist"}
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "stats"}
      - form: academic_background_form
      - slot{"major_one": "stats"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "math"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"num_years": "0"}
      - form: academic_background_form
      - slot{"years_of_study": "0"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_industry_advice
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
      - action_pause
  * ask_average_salary
      - action_salary_range
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
      - utter_goodbye

## student + non-quantitative degree + industry 1
  * greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
  * affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
  * ask_ds_tools
    - action_ds_tools
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * request_job_advice
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "other"}
      - form: academic_background_form
      - slot{"major_one": "cs"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "other"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"years_of_study": "2"}
      - form: academic_background_form
      - slot{"years_of_study": "2"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_industry_advice
      - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * ask_ds_tools
      - action_ds_tools
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
    - utter_goodbye

## student + non-quantitative degree + industry 2
  * greet
      - utter_purpose_of_existence
      - utter_greet
      - action_pause
      - utter_user_purpose
  * affirm
      - action_intro_ds
      - action_pause
      - utter_ask_me
  * ask_day_to_day
    - action_day_to_day
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * request_job_advice{"discipline": "data scientist"}
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "other"}
      - form: academic_background_form
      - slot{"major_one": "stats"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "none"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"num_years": "3"}
      - form: academic_background_form
      - slot{"years_of_study": "0"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_industry_advice
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
      - action_pause
  * ask_average_salary
      - action_salary_range
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
      - utter_goodbye

## student + study advice + concise 1
  * greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
  * affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
  * request_study_advice
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "has_studies"}
  * form: affirm
      - form: academic_background_form
      - slot{"has_studies": true}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "cs"}
      - form: academic_background_form
      - slot{"major_one": "cs"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "math"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"years_of_study": "2"}
      - form: academic_background_form
      - slot{"years_of_study": "2"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_degree_advice
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
    - utter_goodbye

## student + miscellaneous queries
  * greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
  * affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
  * ask_average_salary
    - action_salary_range
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * ask_day_to_day
    - action_day_to_day
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
<!--   * ask_job_scopes
    - action_career_options
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me -->
  * ask_ds_tools
    - action_ds_tools
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * goodbye
    - utter_goodbye

## student + miscellaneous queries + study advice
  * greet
    - utter_purpose_of_existence
    - utter_greet
    - action_pause
    - utter_user_purpose
  * affirm
    - action_intro_ds
    - action_pause
    - utter_ask_me
  * ask_average_salary
    - action_salary_range
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * ask_day_to_day
    - action_day_to_day
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
<!--   * ask_job_scopes
    - action_career_options
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me -->
  * ask_ds_tools
    - action_ds_tools
    - utter_did_that_help
  * affirm
    - utter_smile
    - utter_ask_me
  * request_study_advice
      - utter_please_fill_form
      - academic_background_form
      - form{"name": "academic_background_form"}
      - slot{"requested_slot": "has_studies"}
  * form: affirm
      - form: academic_background_form
      - slot{"has_studies": true}
      - slot{"requested_slot": "major_one"}
  * form: academic_background{"discipline": "cs"}
      - form: academic_background_form
      - slot{"major_one": "cs"}
      - slot{"requested_slot": "major_two"}
  * form: academic_background{"discipline": "math"}
      - form: academic_background_form
      - slot{"major_two": "math"}
      - slot{"requested_slot": "years_of_study"}
  * form: academic_background{"years_of_study": "2"}
      - form: academic_background_form
      - slot{"years_of_study": "2"}
      - form{"name": null}
      - slot{"requested_slot": null}
      - action_degree_advice
      - utter_did_that_help
  * affirm
      - utter_smile
      - utter_ask_me
  * goodbye
    - utter_goodbye

<!-- * affirm
* mood_great
  - utter_happy -->
<!--
  * affirm
  - utter_industry_or_academia? -->

<!-- ## student + non-quantitative degree + somewhat interested

## student + non-quantitative degree + not sure

## student + quantitative degree + very interested

## student + quantitative degree + somewhat interested

## student + quantitative degree + not sure -->

## student + deny
* greet
  - utter_purpose_of_existence
  - utter_greet
  - action_pause
  - utter_user_purpose
* deny
  - utter_sadface
  - action_pause
  - utter_ask_me

## chitchat
* chitchat
  - respond_chitchat
