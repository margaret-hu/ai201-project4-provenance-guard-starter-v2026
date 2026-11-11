"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Criteria 1, 2, 3 and 5 are covered below; criterion 4 is noted at the end.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # False-positive check: my own writing, plain and formal.
        "texts": [
            "My name is Margaret Hu. A few years ago, I graduated from CSU East Bay with a Bachelor's degree in computer science. I initially considered pursuing an art career, but later decided to pursue a STEM career. Since the recession, I have not been able to find an entry-level software development job.",
            "During my free time, I enjoy reading, playing video games, and watching movies. I often read adventure stories with fantasy and/or science fiction elements. I love games that involve puzzles, action-adventure, and exploration. As for films, I like the ones with exceptional storytelling and boundless imagination.",
            "Programmers need a quiet area to work in, so sitting in front of a computer at home or in an office seems like a good working environment. Also, since programming involves analyzing the computing problem, generating algorithmic code to solve the problem, verify that the code meets the fundamental requirements, test it, debug it, and implementing it (a process that can take from a few days to about a year), the job can be quite stressful at times. Programmers are therefore given a high salary as compensation for any anxiety they might experience and for their ability to refine a given idea and resolve arising issues while converting a program into code.",
            "As technology continues to progress forward, our society has entered a time commonly referred to as the Digital Age, where most electronic devices are interconnected throughout the World Wide Web. But as new products are being released and current devices are updated to the latest software systems, software and program code must be written or rewritten, maintained, debugged, and constantly tested. Therefore, computer programming continues to be a necessary skill as the Internet continues to expand and nearly every job field is becoming an information field through inter-networking.",
            "I believe having friends and family who support and care about me is the reason I am currently content. Also, whenever I come across struggles and hardships in my life, I can take comfort knowing that God is always watching over me.",
            "I recall that during my adolescent years, I was obsessed with perfection and constantly thought about my future. Consequently, it placed me under constant stress. Whenever I made a mistake or something does not go as planned, I would often get upset and sometimes have a mental breakdown. With prescribed medication to help increase my serotonin level, after about five to seven years I got tired of this anxiety building up inside. Now more focused on the present, ever since I began to relax a bit, I have experienced some moments of inner peace.",
            "I heard Martha and Scott are hosting a Christmas caroling party on December 22. There will be lots of food and hot drinks, so you don’t need to bring anything unless you have a dish or dessert you want to share. You’re welcome to bring games, friends, and family members as well. If you don’t know any Christmas songs, that’s fine! They'll print out some copies of the songs so you can follow along with the words.",
            "Whenever Emily felt lonely, she would draw. Sometimes she drew pictures from the stories she had read. Other times she drew everyday objects.",
            "The story begins in the home of Marshmallow the Rabbit. He exits the house with a gift for his pen pal Teddy, who just moved into the area. They planned to meet under the old oak, where Marshmallow intends to surprise him with it. On his way, he trips on a rock and drops his gift, which starts to roll away. He runs after it down the hill, past the lake, and is about to retrieve it when a bird swoops in and takes it away. With a heavy heart, he goes to the old oak and waits for his pal to arrive. Meanwhile, the bird with the gift flies towards its nest in the old oak. The bird drops it in the nest, only for it to bounce out and land right in front of Marshmallow. Overjoyed, he retrieves his gift just as Teddy comes into view. As the sun slowly sets, we see Marshmallow handing his gift over to his new neighbor and close pal.",
            "My father often told me that where you live matters for a child's development. To drive his point home, he once told me a story. A mother and her son once lived near a marketplace. Every day, when her son went out to play, he pretended to be a merchant, buying and selling wares while haggling over prices with his friends. The mother decided to move. They settled into a house next to a cemetery. Now when her son went out, he would burn incense sticks and offer prayers to the dead. The mother decided to move again. She found a home beside a school. Her son now spent his free time reading and studying. And so, the mother decided to stay there.",
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        # 12 meditation texts: first 6 AI, last 6 human.
        "texts": [
            "Beyond formal sessions on a quiet cushion, meditation's true power lies in integrating mindfulness into daily activities. Whether walking to work, eating a meal, or listening to a friend, anchoring your awareness in the present moment helps quiet the mind’s relentless chatter. This ongoing practice transforms mundane routines into opportunities for grounding, making peace an accessible state throughout the day rather than a distant goal. Over time, consistent practitioners notice that everyday frustrations elicit fewer impulsive reactions. Instead of immediately absorbing stress or resisting discomfort, they learn to meet challenges with a calm, observant pause. By continually returning to the breath during routine tasks, we gradually rewrite our habitual responses to tension and foster a deep, enduring sense of emotional balance.",
            "Physiologically, the simple act of controlled, conscious breathing directly engages the body's parasympathetic nervous system. When we intentionally slow down our inhalation and exhalation, markers of chronic stress—such as an elevated heart rate and excess cortisol production—begin to decrease significantly. This biological shift explains why even a brief daily practice can yield profound restorative effects on physical health and overall well-being. By signaling safety to the brain through rhythmic breathing, we actively dismantle the relentless fight-or-flight response that modern life so frequently triggers. Consequently, meditation provides a practical mechanism to soothe the nervous system, allowing the body to recover from strain and paving the way for sustained mental clarity.",
            "Ultimately, the ongoing journey of meditation is not about forcing the mind to be entirely silent, but rather fundamentally changing our relationship with our thoughts and emotions. Thoughts will inevitably arise like passing clouds in a vast sky, and the practice teaches us to observe them with curiosity rather than harsh judgment. By cultivating this compassionate inner perspective, we build robust emotional resilience that buffers against life's unpredictable storms and hardships. True happiness, therefore, emerges not from the absolute absence of pain or difficulty, but from the unwavering confidence that we possess an internal anchor. Through steady practice, we learn that peace is always accessible, empowering us to navigate life's inevitable challenges with grace, clarity, and quiet strength.",
            "Neuroscientists and psychologists point to regular meditation as an effective tool for structural brain plasticity, particularly within regions responsible for self-regulation and emotional processing. Long-term practice is associated with increased gray-matter density in the hippocampus, which plays a central role in learning and memory, alongside a reduction in cell volume in the amygdala, the brain's primary stress center. This structural remodeling means that an individual’s physiological baseline for stress drops over time, leading to greater mental agility and emotional stability during high-pressure situations. Furthermore, as the communication pathways between the prefrontal cortex and the amygdala strengthen, individuals become far more capable of evaluating complex, emotionally charged events objectively rather than reacting through automatic, stress-driven reflexes.",
            "In addition to cognitive gains, meditation offers profound benefits for interoceptive awareness—the body’s capacity to perceive and correctly interpret its own internal biological signals. Modern life often forces people to ignore physical symptoms of fatigue, muscular tension, or burnout until they manifest as acute illness or severe mental exhaustion. Through focused breathwork and body scanning techniques, practitioners cultivate a fine-tuned awareness of early physical cues, allowing them to address stress before it becomes overwhelming. By recognizing how emotions register physically within the body—such as tightness in the chest or shallow breathing—meditators can intentionally relax those areas, breaking the cyclical loop where physical discomfort fuels psychological distress and vice versa.",
            "Ultimately, establishing a lasting meditation practice requires abandoning the common misconception that success is measured by achieving a completely blank mind. Mind-wandering is an inherent function of human cognition, and the true essence of meditation occurs at the exact moment one notices the mind has drifted and gently brings focus back to the chosen object of awareness. Each instance of redirecting attention acts as a mental repetition, building focus and self-compassion while dissolving self-criticism. Over time, this non-judgmental approach transfers into daily existence, empowering individuals to navigate personal failures, unexpected delays, and interpersonal conflict with a sense of perspective, patience, and unshakeable inner peace.",
            "Happiness is a subject that has generated a great deal of debate since antiquity. Despite its numerous interpretations, it has universally been accepted as a positive state of mental and emotional well-being in our world today. Moreover, others have discovered that people with a positive mindset show signs of better performance than those who are neutral or negative. Further research has shown that happiness is actually the precursor of success, not the other way around. Shawn Achor, happiness researcher and author of The Happiness Advantage, illustrates that we enjoy more success in life if we are happy and have an optimistic outlook. In addition, Achor presents some compelling evidence that meditation can increase one's happiness baseline. This correlation between happiness and meditation presents some interesting ideas worth investigating.",
            "Meditation is beneficial both physiologically and psychologically. According to Shawn Achor, happiness researcher and author of The Happiness Advantage, neuroscientists have found that meditation increases brain activity in the left prefrontal cortex, which happens to be the part of the brain that correlates with happiness. However, it is not something that can immediately be accomplished, and since happiness is subjective and relative for each individual, it may not be the easiest task for some people. Meditation takes patience and practice, but years of sequestered, celibate silence is not required to receive its benefits. Though it may seem tedious in the beginning, studies have shown that meditation can induce feelings of serenity and contentment and heighten a person's level of awareness and empathy as well.",
            "Victor Davich, in the book entitled The Best Guide to Meditation, states that meditation stems from our desire to be happy. However, there are two barriers that make it difficult to obtain it: pain and suffering. Though both may seem to be the antithesis of happiness, experienced meditators have argued that we often experience happiness through pain. Pain is inevitable, a truth that cannot be denied but difficult to accept. Many wish to avoid or escape from pain, but any attempt to do so is impractical; therefore, to resist pain brings suffering. Only by accepting the pain can it be ameliorated. Additionally, meditation can also be used as a means of reducing stress. Just like pain, you must first be willing to accept the stress and confusion in both your mind and body. Then, by focusing and visualizing on the stress can meditation cause it to dissipate.",
            "There are actually more than one variations of meditation that has developed from its original form as people of different religions and ethnicities have both adopted and adapted it for their own spiritual purposes. One such form is called mindfulness meditation, a two-tiered process that brings an individual's focus of attention to the internal and external experiences presently occurring with an open mind. In the article entitled “The Meaning Connection Between Mindfulness and Happiness”, Zvi J. Bellin explains that attention and cognitive flexibility plays an important role between mindfulness meditation and happiness. Studies have shown that mindfulness meditation strengthens the awareness of one's metacognition, which in turn has a positive effect on the person's sense of responsibility, compassion, self-acceptance, and character. As a result, it contributes to a more coherent and healthy sense of self and identity.",
            "Another form meditation, developed Japan, is Zen meditation, known as zazen. It is considered the highest form of self-expression, for zazen aims to free us in both mind and body. In Zen Mind, Beginner's Mind, Shunryu Suzuki discusses that zazen requires us to let go of what we know in order to have a clear mind that will be able to focus on the actual experience of meditating. Additionally, he suggests that in order to obtain perfect calmness within your zazen, you should not be bothered by any thoughts that may pass your mind. If you just let them come and go, then you will have control. Moreover, Suzuki proposes that we need to cease our dualist way of thinking so that we may be able see things as they are. However, to do so does not mean to cease all thought. When practicing zazen, the mind should always concentrate on your breathing, for it reminds us that we are dependent on the world around us, on the very air we breathe; yet every breath we take is proof that we are alive and therefore independent.",
            "The subject of meditation presents interesting ideas regarding achieving happiness. It may not be suitable or easy for everyone, but studies show that people who meditate regularly have improved their physical, mental, and emotional well-being. All you need to meditate is a quiet place to sit, clear your mind, and focus on your breathing. However, just as the world possesses a multitude of cultures, meditation has branched into many different forms. Despite its variations, perhaps the hardest part is accepting the undeniable truth that pain is inevitable. Only by finding pleasure within pain can we find peace and contentment. It may not be the happiness we expected, but know that it is a happiness we can achieve.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Reachability of all three labels: 6 AI, 6 human, 4 borderline.
        "texts": [
            "Tea is widely celebrated for its rich blend of antioxidants and natural compounds that support both physical and mental well-being. Varieties like green, black, white, and oolong tea contain high levels of polyphenols and catechins, which help protect cells from oxidative stress and promote heart health by improving cholesterol levels and circulation. Additionally, tea offers a unique balance of mild caffeine and L-theanine, an amino acid that fosters alert relaxation without the jittery crash often associated with coffee. Whether enjoyed hot or iced, regular tea consumption can support digestion.",
            "Beyond formal sessions on a quiet cushion, meditation's true power lies in integrating mindfulness into daily activities. Whether walking to work, eating a meal, or listening to a friend, anchoring your awareness in the present moment helps quiet the mind’s relentless chatter. This ongoing practice transforms mundane routines into opportunities for grounding, making peace an accessible state throughout the day rather than a distant goal. Over time, consistent practitioners notice that everyday frustrations elicit fewer impulsive reactions. Instead of immediately absorbing stress or resisting discomfort, they learn to meet challenges with a calm, observant pause. By continually returning to the breath during routine tasks, we gradually rewrite our habitual responses to tension and foster a deep, enduring sense of emotional balance.",
            "Physiologically, the simple act of controlled, conscious breathing directly engages the body's parasympathetic nervous system. When we intentionally slow down our inhalation and exhalation, markers of chronic stress—such as an elevated heart rate and excess cortisol production—begin to decrease significantly. This biological shift explains why even a brief daily practice can yield profound restorative effects on physical health and overall well-being. By signaling safety to the brain through rhythmic breathing, we actively dismantle the relentless fight-or-flight response that modern life so frequently triggers. Consequently, meditation provides a practical mechanism to soothe the nervous system, allowing the body to recover from strain and paving the way for sustained mental clarity.",
            "Ultimately, the ongoing journey of meditation is not about forcing the mind to be entirely silent, but rather fundamentally changing our relationship with our thoughts and emotions. Thoughts will inevitably arise like passing clouds in a vast sky, and the practice teaches us to observe them with curiosity rather than harsh judgment. By cultivating this compassionate inner perspective, we build robust emotional resilience that buffers against life's unpredictable storms and hardships. True happiness, therefore, emerges not from the absolute absence of pain or difficulty, but from the unwavering confidence that we possess an internal anchor. Through steady practice, we learn that peace is always accessible, empowering us to navigate life's inevitable challenges with grace, clarity, and quiet strength.",
            "Neuroscientists and psychologists point to regular meditation as an effective tool for structural brain plasticity, particularly within regions responsible for self-regulation and emotional processing. Long-term practice is associated with increased gray-matter density in the hippocampus, which plays a central role in learning and memory, alongside a reduction in cell volume in the amygdala, the brain's primary stress center. This structural remodeling means that an individual’s physiological baseline for stress drops over time, leading to greater mental agility and emotional stability during high-pressure situations. Furthermore, as the communication pathways between the prefrontal cortex and the amygdala strengthen, individuals become far more capable of evaluating complex, emotionally charged events objectively rather than reacting through automatic, stress-driven reflexes.",
            "In addition to cognitive gains, meditation offers profound benefits for interoceptive awareness—the body’s capacity to perceive and correctly interpret its own internal biological signals. Modern life often forces people to ignore physical symptoms of fatigue, muscular tension, or burnout until they manifest as acute illness or severe mental exhaustion. Through focused breathwork and body scanning techniques, practitioners cultivate a fine-tuned awareness of early physical cues, allowing them to address stress before it becomes overwhelming. By recognizing how emotions register physically within the body—such as tightness in the chest or shallow breathing—meditators can intentionally relax those areas, breaking the cyclical loop where physical discomfort fuels psychological distress and vice versa.",
            "My name is Margaret Hu. A few years ago, I graduated from CSU East Bay with a Bachelor's degree in computer science. I initially considered pursuing an art career, but later decided to pursue a STEM career. Since the recession, I have not been able to find an entry-level software development job.",
            "During my free time, I enjoy reading, playing video games, and watching movies. I often read adventure stories with fantasy and/or science fiction elements. I love games that involve puzzles, action-adventure, and exploration. As for films, I like the ones with exceptional storytelling and boundless imagination.",
            "I believe having friends and family who support and care about me is the reason I am currently content. Also, whenever I come across struggles and hardships in my life, I can take comfort knowing that God is always watching over me.",
            "I recall that during my adolescent years, I was obsessed with perfection and constantly thought about my future. Consequently, it placed me under constant stress. Whenever I made a mistake or something does not go as planned, I would often get upset and sometimes have a mental breakdown. With prescribed medication to help increase my serotonin level, after about five to seven years I got tired of this anxiety building up inside. Now more focused on the present, ever since I began to relax a bit, I have experienced some moments of inner peace.",
            "I heard Martha and Scott are hosting a Christmas caroling party on December 22. There will be lots of food and hot drinks, so you don’t need to bring anything unless you have a dish or dessert you want to share. You’re welcome to bring games, friends, and family members as well. If you don’t know any Christmas songs, that’s fine! They'll print out some copies of the songs so you can follow along with the words.",
            "The story begins in the home of Marshmallow the Rabbit. He exits the house with a gift for his pen pal Teddy, who just moved into the area. They planned to meet under the old oak, where Marshmallow intends to surprise him with it. On his way, he trips on a rock and drops his gift, which starts to roll away. He runs after it down the hill, past the lake, and is about to retrieve it when a bird swoops in and takes it away. With a heavy heart, he goes to the old oak and waits for his pal to arrive. Meanwhile, the bird with the gift flies towards its nest in the old oak. The bird drops it in the nest, only for it to bounce out and land right in front of Marshmallow. Overjoyed, he retrieves his gift just as Teddy comes into view. As the sun slowly sets, we see Marshmallow handing his gift over to his new neighbor and close pal.",
            "Programmers need a quiet area to work in, so sitting in front of a computer at home or in an office seems like a good working environment. Also, since programming involves analyzing the computing problem, generating algorithmic code to solve the problem, verify that the code meets the fundamental requirements, test it, debug it, and implementing it (a process that can take from a few days to about a year), the job can be quite stressful at times. Programmers are therefore given a high salary as compensation for any anxiety they might experience and for their ability to refine a given idea and resolve arising issues while converting a program into code.",
            "As technology continues to progress forward, our society has entered a time commonly referred to as the Digital Age, where most electronic devices are interconnected throughout the World Wide Web. But as new products are being released and current devices are updated to the latest software systems, software and program code must be written or rewritten, maintained, debugged, and constantly tested. Therefore, computer programming continues to be a necessary skill as the Internet continues to expand and nearly every job field is becoming an information field through inter-networking.",
            "The subject of meditation presents interesting ideas regarding achieving happiness. It may not be suitable or easy for everyone, but studies show that people who meditate regularly have improved their physical, mental, and emotional well-being. All you need to meditate is a quiet place to sit, clear your mind, and focus on your breathing. However, just as the world possesses a multitude of cultures, meditation has branched into many different forms. Despite its variations, perhaps the hardest part is accepting the undeniable truth that pain is inevitable. Only by finding pleasure within pain can we find peace and contentment. It may not be the happiness we expected, but know that it is a happiness we can achieve.",
            "Plato's “Allegory of the Cave” illustrates the idea that we should not always take what we are told to be fact; for what may seem to be true may only be in part real or not at all factual. Just as the prisoners believe the shadows to be reality, those who believe that empirical evidence ensures knowledge are only seeing a shadow of it. Knowledge does not simply arise in an individual. In order to learn and understand what is real, one must actively pursue that knowledge themselves through study and education. Unfortunately, most people would rather live in a comfortable situation than to face against life's challenges and hardships, even if that life were as real as the shadows upon the wall. Thus it is essential, as Plato reveals in his allegory, to keep an open yet skeptical mind to change, for to believe what is taught without question will only lead to self imposed ignorance.",
        ],
    },

    # Criterion 5: every one of these must return a 4xx with a JSON `error` and
    # `message`. Raw request bodies, sent exactly as written.
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing_text"},                # no text field at all
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "A normal sentence with no creator id attached."},  # no creator_id
            # 10,005 characters, just over the 10,000 cap in criterion 5.
            {"text": "word " * 2001, "creator_id": "eval_bad_over_cap"},
        ],
    },

    # Not expressible here (run separately, and say so in the write-up):
    #   - criterion 5, JSON list body and "valid /submit still works after each
    #     rejection": check_bad_input.py (validate() requires dict bodies).
    #   - criterion 4, appeals: needs a content_id from /submit first, and
    #     run_eval.py only posts to /submit. Run check_appeal.py.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
