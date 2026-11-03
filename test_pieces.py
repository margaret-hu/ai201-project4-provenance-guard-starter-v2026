"""
The three test pieces for Milestone 4. Fill in each slot, then run:

    python test_pieces.py

It prints both signals side by side for every piece, so you can see where they
agree and where they split.
"""

PIECES = {
    # Something you are confident an AI wrote (e.g. prompt a chatbot for a
    # generic paragraph on a topic).
    "clearly_ai": "Tea is widely celebrated for its rich blend of antioxidants and natural compounds that support both physical and mental well-being. Varieties like green, black, white, and oolong tea contain high levels of polyphenols and catechins, which help protect cells from oxidative stress and promote heart health by improving cholesterol levels and circulation. Additionally, tea offers a unique balance of mild caffeine and L-theanine, an amino acid that fosters alert relaxation without the jittery crash often associated with coffee. Whether enjoyed hot or iced, regular tea consumption can support digestion.",

    # ⚠️ Something you actually wrote yourself. Not a sample from the web.
    "clearly_human": "My name is Margaret Hu. A few years ago, I graduated from CSU East Bay with a Bachelor's degree in computer science. I initially considered pursuing an art career, but later decided to pursue a STEM career. Since the recession, I have not been able to find an entry-level software development job. My interests include reading, playing video games, and watching movies. I often read adventure stories with fantasy and/or science fiction elements. I love games that involve puzzles, action-adventure, and exploration, such as Genshin Impact or The Legend of Zelda. As for films, I like the ones with exceptional storytelling and boundless imagination. Some of my favorites include Kiki's Delivery Service, Spirited Away, and Howl's Moving Castle. I especially enjoy watching Hayao Miyazaki's films.",

    # Borderline: formal human writing (an essay, a report, a cover letter)
    # that you wrote but that reads polished and uniform.
    "formal_human": "The subject of meditation presents interesting ideas regarding achieving happiness. It may not be suitable or easy for everyone, but studies show that people who meditate regularly have improved their physical, mental, and emotional well-being. All you need to meditate is a quiet place to sit, clear your mind, and focus on your breathing. However, just as the world possesses a multitude of cultures, meditation has branched into many different forms. Despite its variations, perhaps the hardest part is accepting the undeniable truth that pain is inevitable. Only by finding pleasure within pain can we find peace and contentment. It may not be the happiness we expected, but know that it is a happiness we can achieve.",

    # Lightly-edited AI: take human written text and have AI improve, rephrase,
    # or polish it. The hardest case for both signals.
    "edited_ai": "Wilbur and Orville Wright were two of seven children born to Milton Wright, a bishop in the Church of the United Brethren in Christ, and Susan Catherine Koerner. Wilbur was born on a farm near Millville, Indiana, on April 16, 1867. Two years later, the family relocated to Dayton, Ohio, purchasing the home at 7 Hawthorn Street where Orville was born on August 19, 1871. Because Milton’s ministerial duties required frequent travel, he often returned with small gifts for his children. In 1878, he brought the boys a toy helicopter made of cork, bamboo, and paper, powered by a rubber band—a design created by French aeronautical pioneer Alphonse Pénaud. Deeply fascinated by the toy's mechanics, Wilbur and Orville sparked a lifelong passion for aviation and flight.",
}


if __name__ == "__main__":
    from detector import model_signal
    from stylometry import style_signal

    print(f"{'piece':<15} {'model':>7} {'style':>7}")
    for name, text in PIECES.items():
        if text.startswith("REPLACE ME"):
            print(f"{name:<15} (not filled in yet)")
            continue
        print(f"{name:<15} {model_signal(text):>7.3f} {style_signal(text):>7.3f}")
