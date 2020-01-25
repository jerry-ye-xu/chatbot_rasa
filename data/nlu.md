<!--
    INTENT: SMALL TALK
-->

## intent:greet
- hey
- hey there
- hello
- sup
- wassup
- what's up?
- hi
- gday
- good morning
- good afternoon
- good evening
- how's life?


## intent:goodbye
- cya
- bye
- bye bye
- goodbye
- I gotta go
- g2g
- going now
- gotta run
- see ya
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- right
- yea I agree
- for sure
- cool
- alright

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- I'm not sure

## intent:appreciation
- Thanks
- Thank you
- Thanks alot!
- That was really helpful.
- Good advice.
- I see, that was insightful!
- Oh really that's really cool!

## intent:name
- What's your name?
- What are you called?
- What do I call you?
- Do you have a name?
- Your name is...?

<!--
    INTENT: LEVEL OF INTEREST
-->

## intent:no_idea
- Is [programming](coding) useful?
- Is [coding](coding) hard?
- I don't know what I want to do...
- Not sure if I'm interested.
- how do I get into [data science](discipline)?
- what degree is best for [data science](discipline)?
- how do I get into [AI](discipline)?
- How much [math](discipline) do I need for [data science](discipline)?
- What is [data science](discipline)?
- What's [data science](discipline) like?
- Do jobs in [data science](discipline) pay well?

## intent:some_idea
- What's good for [data science](discipline)?
- I just like [math](discipline). What kind of career paths are there?
- I think [data science](discipline) sounds cool
- I think [data science](discipline) is interesting
- Tell me more about [data science](discipline)
- What is good about [data science](discipline)?
- what are the best courses in [data science](discipline)?
- I think both [data science](discipline) and [programming](discipline) are fun
- I did an online course and I think [data science](discipline) is pretty cool.

## intent:strong_idea
- Building models is fun!
- I'm looking for [data science](discipline) [graduate jobs](job)
- I wanna get a role in [analytics](job)
- I want to work in [data science](discipline)
- I enjoy [predictive modelling](ml_sub_discipline)
- I'm currently studying [computer science] and [statistics](stats_subjects)
- I'm into [deep learning](discipline)
- I'm interested in [machine learning](discipline)

<!--
    INTENT: ASK QUESTIONS
-->

## intent:average_salary
- how much does a [data scientist](discipline) make?
- what is the average salary of someone doing [data science](discipline)?
- does [data science](discipline) make alot of money?
- how good is [data science](discipline) for making money?
- is it easy to make alot of money in [data science](discipline)?
- what is the top salary for a [data scientist](discipline)?

## intent:career_paths
- what are some common career paths for [data scientists](discipline)?
- what does a [data scientists](discipline) do?
- what jobs are there in [data science](discipline)?
- what are some jobs in [data science](discipline)?
- how much career progression do you have?
- how do you get promoted?

## intent:unsure_degree
- I'm not sure what I should study?
- What [degree](undergrad_studies) is best for me?
- What should I study?
- what should I study at uni?
- what should I study at university?
- Should I do [computer science](discipline)?
- Should I do a [data science](discipline) [degree](undergrad_studies)?
- What kind of academic background should I have?
- Will math be useful for [data science](discipline)?
- Is [software engineering](discipline) helpful for [data science](discipline)?
- Will [computer science](discipline) be useful for [data science](discipline)?
- Is [statistics](discipline) good for [data science](discipline)?

<!--
    INTENT: CAREER PATH
-->

## intent:research
- I want to do a [PhD](phd_studies)
- I want to do [honours](postgrad_studies)
- I'm thinking about doing a [PhD](phd_studies)
- I'm thinking about doing [honours](postgrad_studies)
- I'm considering further studies
- I'm considering [postgraduate studies](postgrad_studies)
- I'm considering [postgrad](postgrad_studies)
- I want to do [research](phd_studies) in [machine learning](discipline)
- I want to do [research](phd_studies) in [NLP](ml_sub_discipline)
- I want to do [research](phd_studies) in [natural language processing](ml_sub_discipline)
- I want to do [research](phd_studies) in [CV](ml_sub_discipline)
- I want to do [research](phd_studies) in [computer vision](ml_sub_discipline)

## intent:industry
- I want to do [software engineering](job) after [graduating](milestone)
- I want to work in [SWE](job) after [graduating](milestone)
- I want to be a [data scientist](job)
- I just want to get a job
- Probably want to just work
- I don't mind doing [engineering](job)
- I want to do [analytics](job)
- I want to work as a [machine learning engineer](job)
- I just want to do [ML engineering](job)
- Thinking about becoming a [dev](job)
- My goal is to be a [machine learning](discipline) practitioner
- I want to do research in [machine learning](discipline)
- I want to work on [NLP](ml_sub_discipline) problems in industry
- I want to do research in [natural language processing](ml_sub_discipline)
- I want to do research in [CV](ml_sub_discipline)
- I want to do research in [computer vision](ml_sub_discipline)

<!--
    INTENT: HAVING SOME FUN
-->

## intent:bot_challenge
- are you an [AI](chatbot)?
- how did someone build an [AGI](chatbot) like you?
- are you a [bot]((chatbot)?
- are you a human?
- am I talking to a [bot](chatbot)?
- am I talking to a human?
- do you exist?
- what are you?
- are you the new [super AI](chatbot)?
- how come [chatbots](chatbot) are so smart?

<!-- ## intent:out_of_scope
- Are you trolling me?
- Is time travel possible?
- Who is batman?
- Is it true that Australian's animals are all trying to kill you?
- Are Australian snakes dangerous?
- Do spiders bite where you live?
- How's the weather?
- What's the weather like where you are?
- Is it hot over there?
- Do you live in a cold area?
- Does Australia rain often?
- What is the meaning of life?
- Why are we here?
- Do humans really exist?
- Why are we building robots? -->

## intent:chitchat/meaning_of_life
- What is the meaning of life?
- Why are we here?
- Do humans really exist?
- Why are we building robots?

## intent:chitchat/ask_weather
- How's the weather?
- What's the weather like where you are?
- Is it hot over there?
- Do you live in a cold area?
- Does Australia rain often?

## intent:chitchat/ask_aussie_animals
- Is it true that Australian's animals are all trying to kill you?
- Are Australian snakes dangerous?
- Do spiders bite where you live?

## intent:chitchat/am_I_trolling
- Are you trolling me?
- Is time travel possible?
- Who is batman?

<!--
    REGEX EXPRESSSIONS
-->

## regex:math_subjects
- [Mm]{1}[Aa]{1}[Tt]{1}[Hh]{1}[0-9]{3-4}

## regex:compsci_subjects
- [Cc]{1}[Oo]{1}[Mm]{1}[Pp]{1}[0-9]{3-4}

## regex:stats_subjects
- [Ss]{1}[Tt]{1}[Aa]{1}[Tt]{1}[0-9]{3-4}

## regex:datasci_subjects
- [Dd]{1}[Aa]{1}[Tt]{1}[Aa]{1}[0-9]{3-4}

## regex:swe_subjects
- [Ss]{1}[Oo]{1}[Ff]{1}[Tt]{1}[0-9]{3-4}

<!--
    SYNONYMS
-->

## synonym:coding
- programming
- engineering
- scripting
- building


## synonym:data_science

## synonym:phd_studies
- PhD studies

## synonym:milestone
- finish uni
- finish university

## synonym:chatbot
- AI
- AGI
- bot
- robot
- super AI
- new AI
- chat application