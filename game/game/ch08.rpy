# Chapter 8. Saltgate. Staged from work/cut/ch08.md; the text is the approved text.

define c_dace = Character("Dace")
define c_yeva = Character("Yeva")
define c_pell = Character("Pell")
define c_marsh = Character("Linnea Marsh")
define c_garran = Character("Garran")

label ch08:

    # c08.s01
    scene bg c8_belt_under
    with fade
    "They rode the Dragon north for a day, as far as the edge of the Bright Shelves, and left it there on the needles. Sefa rode behind Ilan with her arms round his waist."
    "She did not speak to him for the first two hundred kilometres. In the third hundred she said that he leaned too hard into his turns, and he took it for the beginning of a peace."

    "He was Ilan now. It sat on him like a coat he had not worn for years, familiar and the wrong size. Sefa and Okonta went on calling him Wrack, out of habit or on purpose, and he found that he was glad of it."

    "The water grew warm and thick. The white sand was left behind. On the fourth day the surface above them began to heave, and a grey twilight came down through it, and Okonta slowed."

    show p wrack_thread_attentive as left at head_left
    show p okonta_grave as right at head_right
    with qd
    c_okonta "The Belt,"
    c_okonta "That's the south edge of the storms. From here to the far side it's three hundred kilometres of weather, and every island on Ovara is somewhere in it. I can take a needle under."
    c_okonta "You can't take a girl who's never seen an agravar into Saltgate on one, and walk her up out of a canal in a Threaded's wake. You'd have every wrecker in the port on you by noon."
    "She looked up."
    c_okonta "There should be a boat. The rays said a boat."

    hide left
    hide right
    with qd
    scene bg c8_belt_rain
    with dissolve
    "There was a boat."

    scene cg c8_dace_boat
    with dissolve
    "It was painted four different colours, in patches, and it sat on the swell like a duck. When they came up beside it a long weather-beaten face looked over the side. It belonged to a woman of fifty or so, with a pipe in her teeth and a hat tied on with string."

    scene bg c8_belt_rain
    with dissolve
    show p wrack_thread_calm as left at head_left
    show p dace_cheerful as right at head_right
    with qd
    c_dace "You'll be the party,"
    c_dace "I'm Dace. I'm Driftfolk, out of Lashing. A stingray the size of a customs cutter came up alongside my raft nine days ago and put a picture in my head, and I've not been right since."
    "She took the pipe out."
    c_dace "I intend to dine out on it for the rest of my life. Which of you's the one that's worth four years' scrip?"

    show p wrack_thread_wry as left at head_left
    with qd
    c_ilan "I am,"

    show p dace_dry as right at head_right
    with qd
    c_dace "Thought so. You've the look of a man who's been to an office."
    "She put down a rope ladder."
    show p dace_cheerful as right at head_right
    with qd
    c_dace "There's a face like yours on every wall from here to the Crown, with a reward under it. So you'll want a hat. I've brought a hat."

    hide left
    hide right
    with qd
    "Okonta would not come aboard. She took the second needle in tow behind her own and said that she would be under the keel all the way, and under the city after that, and that if Ilan wanted her he had only to think so loudly. Then she was gone, without a ripple."

    "The boat was named {i}Patience{/i} on the bow, {i}Second Wife{/i} on the stern, and something else again on her papers. She was eleven metres of patched timber with a deckhouse and a mast and an engine that Dace addressed as an equal."
    "Ilan knew her kind. Every harbour on the Girdle had a hundred. They belonged to the people with no corporation, the ones who lived on the water because every scrap of land was owned."
    "They were called the Driftfolk, and they had no island. They had rafts, lashed together in floating towns, which followed the calm places through the storms. They carried what the corporations would not carry, to people the corporations did not serve, and asked no questions of anyone."
    "Halcyon's security manuals classed them as a nuisance. He had signed off on those manuals."

    "Sefa had never been above the surface for more than a few minutes. She sat in the bows with her feet trailing in the sea, at Dace's order, and stared at the sky. Rain came across the water in walls."

    show p wrack_thread_calm as left at head_left
    show p sefa_amazed as right at head_right
    with qd
    c_sefa "It's so loud,"
    c_sefa "How does anyone think?"

    show p dace_cheerful as right at head_right
    with qd
    c_dace "Most don't,"
    "said Dace cheerfully."
    c_dace "Hold on to something. Here's where it stops being pretty."

    hide left
    hide right
    with qd

    # c08.s02
    scene bg c8_boat_storm
    with fade
    "They crossed the storms by the Eyes."

    "Ilan had done it a hundred times on company ships, behind glass, with a drink. He had never done it in an open boat. You ran flat out through wind and black rain toward a patch of calm that you could not yet see."
    "The calm drifted. There were dozens of them, scattered through the Belt, and they moved on a pattern that took years to learn. The big ships had instruments. The Driftfolk had it by heart, handed down like a song."
    "You reached your Eye, and the wind dropped as though a door had shut. You sat in flat water under a ring of blue sky, with the storm standing all round you like a wall, and you waited for the next Eye to come within reach."
    "If you misjudged it, you were caught between two with nowhere to go. Ships were lost that way every season."

    "Gale skates went over them in thousands. They threw themselves out of the wave-tops and glided on the wind for a kilometre at a time. Dace read them like a newspaper."
    "When they flew high, she said, the Eye was near. When they turned all together, like a shaken cloth, the wind was about to change."
    "Grey fins followed the boat, six or eight of them. They were belt sharks, Dace said. They followed anything that floated, for the scraps and the dumping."
    show p bother_alert as bother at bother_corner
    with qd
    "Bother stood with his front flippers on the gunwale and barked at them until he was hoarse."
    hide bother
    with qd

    "Sefa lay in the bottom of the boat and was sick. She held Bother's collar, and said that a sea you had to stay on top of was no sea at all."

    scene bg c8_eye_boat
    with dissolve
    "In the Eyes there was time to talk. It was in the second one, with the boat turning slowly on water like green glass, that she asked him."

    show p wrack_thread_attentive as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "Tell me about them. The islanders. I want to know what I'm going to see."
    c_sefa "Not what Mother says. What they're actually like."

    hide left
    hide right
    with qd
    "He thought about how to begin."

    show p wrack_thread_thinking as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_ilan "There are forty million of them, and there's no room,"
    c_ilan "Start there. Every island on Ovara put together would fit inside the Anthem Waters twenty times over. So every bit of ground is owned. You can't be born without being born on somebody's land."
    c_ilan "Two hundred years ago the trading houses bought out the island governments, one after another, and now there are five that matter. Each one's a company, and it's also a country."
    c_ilan "If you're born on a Halcyon island, you're Halcyon's. It houses you and schools you, and pays you in its own money. Scrip. You can only spend it in the company's shops. If there's a war, it puts you in a uniform."

    show p sefa_puzzled as right at head_right
    with qd
    c_sefa "What are they at war about?"

    show p wrack_thread_troubled as left at head_left
    with qd
    c_ilan "Land. Each other's. There isn't any left that's spare."
    "He looked at the wall of cloud."
    c_ilan "Halcyon digs. Ore, fuel, anything under the sea bed. Kessler-Vane builds ships and guns for all of them. Brightwater sells food and water and medicine, and it's the one everybody likes. Meridian lends the money and insures the ships. Orrin owns the screens and decides what people hear."
    "He rubbed his wrists; it had become a habit."
    c_ilan "They're not wicked, Sefa. Most of them. They work twelve hours and go home to two rooms. They like music and fried food, and they love their children. They've been told all their lives that there's nothing down here but fish and a fairy tale. And so what they throw away, they throw in the sea."

    show p sefa_hard as right at head_right
    with qd
    c_sefa "And you told them where."

    show p wrack_thread_ashamed as left at head_left
    with qd
    c_ilan "I told them where."

    hide left
    hide right
    with qd
    "She was silent for a while. Dace, at the tiller, was carefully watching the skates."

    show p wrack_thread_ashamed as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "Did you like it?"
    c_sefa "Being one of them?"

    hide left
    hide right
    with qd
    "It was not a question he had expected."

    show p wrack_thread_thinking as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_ilan "I liked being good at something,"
    c_ilan "I liked that there was always a next thing to get. I had a flat with a bluewood table. Do you know what bluewood is? It's the last real tree. The table cost more than my father earned in his life."
    "He shook his head."
    c_ilan "I don't think I liked anything, particularly. I think I was very busy."

    show p sefa_sick as right at head_right
    with qd
    c_sefa "That's the saddest thing I ever heard,"
    "Sefa said, and was sick again."

    hide left
    hide right
    with qd

    # c08.s03
    scene bg c8_saltgate
    with fade
    "Saltgate came up out of the rain on the fifth evening."

    "Ilan had forgotten it, and then remembered it. Now he saw it for the first time, all at once."

    "A hundred sea-stacks stood in the gap between two corporate waters. On every one of them people had built. They had built up, and then out."
    "They built across from stack to stack on stilts and girders and cables, tier on tier, until the city hung over the water like a mass of nests in a dead tree. And every surface of it flashed and crawled with coloured light."
    "Signs forty metres high sold noodles, loans, cigarettes, and a singer with silver eyelids. He smelled smoke and frying oil. He heard ten thousand engines, and music from a hundred doors, and over all of it the horns of ships."

    "Sefa had her mouth open."

    show p wrack_hat_guarded as left at head_left
    show p sefa_amazed as right at head_right
    with qd
    c_sefa "Where's the dark?"
    c_sefa "Where do they put the {i}dark{/i}?"

    show p dace_dry as right at head_right
    with qd
    c_dace "They don't keep any,"

    hide left
    hide right
    with qd
    scene bg c8_lock
    with dissolve
    "Under everything the canals ran between the pilings, and at the mouth of each stood a lock. Men in oilskins and brass badges sat in glass boxes above them, drinking tea."

    show p wrack_hat_guarded as left at head_left
    show p dace_dry as right at head_right
    with qd
    c_dace "Lockkeepers,"
    c_dace "They're the only law there is here. They own the gates, and they take a toll off everyone who comes through. Halcyon, Driftfolk, your people, all the same rate."
    c_dace "They won't take a side for any money. That's why it's a free port. If the Lockkeepers shut the gates, the whole city starves in a week, so nobody's ever cared to annoy them."
    "She raised two fingers to the nearest box. A badge raised two fingers back."
    c_dace "Your folk come in by the locks, love. Right into the middle of town. It's the only place in the world they can."

    hide left
    hide right
    with qd
    "She looked at Sefa."

    show p wrack_hat_guarded as left at head_left
    show p dace_dry as right at head_right
    with qd
    c_dace "Now you listen. You stay wet. Canals and the Wet Market, no higher. I've a tub in the deckhouse for when we're tied up. A day in the dry up there and you'll be on your back, and two days you'll be in a box."

    show p sefa_dry as right at head_right
    with qd
    c_sefa "I know that."

    show p dace_dry as right at head_right
    with qd
    c_dace "She knows that,"
    "Dace said to Ilan."
    c_dace "They all know that. I've carried three out on a plank."

    hide left
    hide right
    with qd
    scene bg c8_poster_canal
    with dissolve
    "His own face looked down at him from a wall at the first landing. CHIEF SURVEYOR ILAN VOSS. LOST AT SEA. THE COMPANY MOURNS. A REWARD IS OFFERED FOR INFORMATION."

    "Sefa looked at the wall, and then at him."

    show p wrack_hat_guarded as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "You had a different mouth,"

    hide left
    hide right
    with qd
    "He pulled the hat down."

    # c08.s04
    scene bg c8_wet_market
    with fade
    "The Wet Market lay in the heart of the city, where six canals met."

    "It was a basin a hundred metres across, roofed over, high above, by the floors of buildings. The stalls stood round it on three tiers of planking. The top tier was dry. The middle one was awash at high tide."
    "The lowest was a metre under water, and the stallholders there sat in the sea up to their chests, or were mariners and sat in it altogether. The water was full of light and legs."

    "Everything was sold here. Agravars in plastic capes sold steel knives and needles and coils of wire, and glass beads, and small cheap radios sealed in wax."
    "Mariners from holds along the Shoulder sold sea-silk by the bolt, and pearls, and smoked silverback. Driftfolk sold whatever they had found. There was shouting in three languages."
    "A mariner woman was arguing over the price of a hatchet with a man who had his trousers rolled to the thigh. She kept sinking to her chin between offers, to breathe."

    show p bother_aggrieved as bother at bother_corner
    with qd
    "Sefa swam through it with her eyes going from side to side, and Bother swam at her shoulder, appalled."
    hide bother
    with qd

    show p wrack_hat_calm as left at head_left
    show p sefa_amazed as right at head_right
    with qd
    c_sefa "They're just {i}talking{/i} to each other,"
    "she said, surfacing beside the boat."
    c_sefa "They're cheating each other over fish. That one called that one a thief, and then they both laughed."
    "She pushed her wet hair back."
    c_sefa "Nobody told me there was anywhere it was like this."

    show p wrack_hat_melancholy as left at head_left
    with qd
    c_ilan "There isn't anywhere else,"
    c_ilan "My mother came up through that lock there, when she was nineteen. To see the lights."

    hide left
    hide right
    with qd
    scene bg c8_sluice
    with dissolve
    "He had not meant to go to the Sluice. His feet took him, that night, as his hands had once gone to a lamp."

    "It was a back canal in the poor quarter, narrow and dim. He knew every door. He knew the noodle stall on the corner, and the smell of it. The tenement was still standing. There was a light in the fourth-floor window, and somebody else's curtain."

    "He stood on the towpath in the rain and looked up. She had sat at that window with her feet in a basin, humming. She had put her hands on either side of his face when he was seven."
    "He had thought that he was ashamed of where he came from. It had been easier than knowing that he was afraid of what he was."

    "An old man came out of the noodle stall with a bucket and looked at him twice. Ilan went away again."

    # c08.s05
    scene bg c8_noodle_window
    with fade
    show p wrack_hat_guarded as left at head_left
    show p pell_nervous as right at head_right
    with qd
    c_ilan "The twenty-second floor doesn't have a button,"

    hide left
    hide right
    with qd
    "They were in a noodle shop across the canal from the tower. Dace was eating. Sefa was in the water under the window with her chin on the sill and a bowl balanced in front of her."
    "A thin, nervous young man named Pell sat with them. He was a filing clerk at the port office, and he had not touched his food. Dace had introduced him as a friend with clean hands."

    show p wrack_hat_guarded as left at head_left
    show p dace_dry as right at head_right
    with qd
    c_dace "The Clean Hands,"
    c_dace "It's a sort of club. Clerks, mostly, and stokers. A few doctors. People who see the tonnage sheets and can't sleep. They jam a valve here and lose a manifest there, and they send word down to the holds when a barge is due."
    "She had patted the young man's shoulder."
    c_dace "They've no leader and no meetings. It's the only reason any of them are alive."

    hide left
    hide right
    with qd
    scene bg c8_brightwater_ext
    with dissolve
    "Across the water the Brightwater Wellness Centre rose thirty storeys, white-tiled, softly lit. Its sign was a blue drop and a smiling sun."

    "Brightwater was the corporation people liked. It sold bread, and bottled water, and the pills that every agravar child took for the lungs. Its shops were clean and its staff were kind. Its advertisements showed grandmothers."
    "Ilan had dealt with its board for ten years, and they were the only people on Ovara who had ever frightened him. Its chief was a physician named Linnea Marsh."
    "She had begun in a dockside dispensary, and still kept a stethoscope in her desk. She had once explained to him, kindly, over tea, why a medicine that cured in a single dose was a poor product."

    scene bg c8_noodle_window
    with dissolve
    show p wrack_hat_guarded as left at head_left
    show p pell_nervous as right at head_right
    with qd
    c_ilan "It's listed as plant,"
    c_ilan "I signed a requisition for that floor once, as a favour between companies. Sixty thousand litres a week of filtered seawater, trucked up in sealed tanks. I thought it was for a pool."

    c_pell "It's a woman,"
    "He spoke almost too low to hear."
    c_pell "They've had her eight months. One of ours cleans on twenty-one. She hears the pumps."

    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "A Wellwalker,"
    "She said the word as someone else might say {i}saint{/i}."

    hide left
    hide right
    with qd
    "Ilan had heard of them only as a line in a security briefing. Sefa told him the rest, there at the window, in a low fierce voice."
    "The healers of the two great hospitals did not all stay at the bottom of the Wells. Some took a turn at walking the world. They went alone, with nothing. They went from hold to hold, and into the ports, and up onto the beaches of the islands."
    "They healed whoever they met, mariner or agravar, and asked for nothing. They never stayed. To meet one was the luck of a lifetime. Children in Low Anthem played at being one. Ione had met one, once, when she was a girl, and it was why she had become a healer."

    show p wrack_hat_guarded as left at head_left
    show p sefa_hard as right at head_right
    with qd
    c_sefa "And they caught one,"
    c_sefa "And put her in a pot."

    c_ilan "They're trying to find out why intended water stops working,"
    c_ilan "It fades in a few days. If they could make it keep, they could bottle it. It would be worth more than everything else they sell."

    c_sefa "It stops because she stops minding it. Any child knows that."

    c_ilan "They don't believe that. It isn't a thing you can put on an invoice."
    "He turned his cup."
    c_ilan "There's no sea in that building. Nothing that's joined to it. It'll be orphan water, all of it, in pipes and tanks. Whatever I can do in there will be weak, and it won't last."

    show p dace_dry as right at head_right
    with qd
    c_dace "Then how do we get in?"

    hide left
    hide right
    with qd
    "He took off the hat."

    scene bg c8_lobby
    with dissolve
    "It was the most frightening thing he had done since he woke up, and the easiest. He walked into the white lobby in a suit that Dace had procured without explanation. There was soft music, and a smell of lemons."
    "He gave his name and his grade and an eleven-digit authority code that his mouth knew better than he did. Then he watched a receptionist's face do what the lieutenant's had done at Greywatch Stone."

    "Chief Surveyor Voss was not dead. He had been on a confidential assignment."
    "He was here to inspect the plant on twenty-two, on behalf of a partner corporation that was, he let it be understood, extremely displeased. He would not be signing in."

    "Nobody stops a man of that grade in a building like that. Agravars had built their whole world on it. He heard his own voice, cool and bored and faintly threatening. He knew it well. He had used it for fifteen years."

    scene bg c8_tank_room
    with dissolve
    "She was in a tank."

    scene cg c8_yeva_tank
    with dissolve
    "The woman in it had been tall once. She floated curled, with tubes in her arms, and her eyes were open. The water round her was orphan water. It had been cut off from the sea and filtered until it was dead."

    scene bg c8_tank_room
    with dissolve
    "He could feel that she had not been answered in eight months. He could feel that she had gone on asking every day."

    "He put his hand on the glass. Her eyes moved to it, and then to his face. He saw her register what he was. She saw the gift in him, standing in a place like this, in a suit."

    show p wrack_suit_sorrowful as left at head_left
    show p yeva_tired as right at head_right
    with qd
    c_ilan "I'm sorry,"
    c_ilan "For all of it. Can you swim?"

    hide left
    hide right
    with qd
    "The alarm went when he broke the seals. After that it was not elegant."

    "There were four guards in the corridor and nothing to call on. He stood with a dying woman in his arms and asked, and there was no one there. Then he thought of the sprinklers."
    "A grid of pipes ran through every ceiling in the tower, full of stale standing water. He asked again. It answered faintly, like a voice down a bad line."
    scene bg c8_stair_flooded
    with dissolve
    "But there was a great deal of it. It was enough to fill a corridor to the knee and take the feet from under four men. It held for a few seconds as a slope of water down thirty flights of the emergency stair."
    "It was already fading as they rode it down. He carried the Wellwalker against his chest, and she weighed nothing at all."

    scene bg c8_loading_dock
    with dissolve
    "They went into the canal from a loading dock as the last of it gave out. Dace's boat was there. Sefa was in the water with her arms up."

    # c08.s06
    scene bg c8_under_market
    with fade
    "Her name was Yeva."

    "She had been walking the world for thirty years when they took her. They had found her on a beach in the Green Terraces, setting a fisherman's leg."
    "She lay for two days in the shadows under the Wet Market, where the sea came in clean on the tide, and let it come back to her. Sefa did not leave her. She fed her broth from a spoon and held her up in the water, and looked at her as Elder Oro had looked at the lamp."

    "On the third day Yeva opened her eyes properly. She had a long worn face and a dry manner. She looked at Sefa, and at the band on her arm."

    show p wrack_thread_calm as left at head_left
    show p yeva_dry as right at head_right
    with qd
    c_yeva "Who gave you that?"

    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "My hold. On the road. There wasn't anyone else."

    show p yeva_dry as right at head_right
    with qd
    c_yeva "Hm. You've good hands. You grip too hard."
    "She turned her head and looked at Ilan."
    c_yeva "And you call like a man shifting furniture."

    show p wrack_thread_wry as left at head_left
    with qd
    c_ilan "I've been told."

    show p yeva_stern as right at head_right
    with qd
    c_yeva "I felt you, in that corridor. You went through the pipes like a bailiff."
    "She sat up, slowly, against a piling."
    c_yeva "Give me your hand. No, in the water."

    hide left
    hide right
    with qd
    "A market porter had dropped a crate on Dace's foot that morning, and the foot was the size of a melon. Dace sat on the edge of the planking with it hanging in the canal, smoking, and said she did not mind being practised on."

    show p wrack_thread_attentive as left at head_left
    show p yeva_dry as right at head_right
    with qd
    c_yeva "You know how to ask the sea to move,"
    c_yeva "Now you'll ask it to care. It's the same asking. You're simply not allowed to want anything for yourself while you do it. Not even to be good at it. Go on."

    hide left
    hide right
    with qd
    scene cg c8_cupful
    with dissolve
    "He stood waist deep in the canal with a cupful of water between his palms. For an hour he failed."

    scene bg c8_under_market
    with dissolve
    "He knew why. He wanted very badly to be a man who healed instead of a man who burned. He wanted it so much that the water could feel nothing else in him."
    "Yeva watched him fail without comment. Sefa, behind her, was trying not to tell him what he was doing wrong, and nearly bursting with it."

    scene cg c8_cupful
    with dissolve
    "Then Dace shifted, and swore at her foot, in real pain. He stopped thinking about himself and thought about the foot. He thought about the small crushed bones in it, and how it must throb."

    "The water went warm in his hands."

    scene bg c8_under_market
    with dissolve
    show p wrack_thread_calm as left at head_left
    show p yeva_dry as right at head_right
    with qd
    c_yeva "There,"
    c_yeva "That's all it is. That's all it ever is. You'll spend the rest of your life trying to get out of your own way."

    hide left
    hide right
    with qd
    "He learned to mend, to purge and to ease. Yeva taught him the three of them in the nine days she could spare. She taught Sefa at the same time, and Sefa learned twice as fast."
    "She said frankly that he would never be delicate. She said also that she had not felt strength like it outside the Wells."

    show p wrack_thread_straining as left at head_left
    show p yeva_dry as right at head_right
    with qd
    c_yeva "Purging is your one,"
    "They were working on a stoker's lungs, black from twenty years of refinery smoke. Ilan had his hands on the man's back, and the foulness was coming up out of him into the water like ink."
    c_yeva "Poison, rot, filth. You've a feeling for where it sits. I'd wonder why, if I didn't already know who you were."

    hide left
    hide right
    with qd
    "He looked up."

    show p wrack_thread_ashamed as left at head_left
    show p yeva_stern as right at head_right
    with qd
    c_yeva "The sea tells me things too,"
    c_yeva "It told me in that tank who'd signed for the water."
    "She let that land."
    c_yeva "I'm not going to forgive you. It isn't mine to do. But I'll tell you what I tell every healer, and you'll remember it. You can't mend anything you won't look at."

    hide left
    hide right
    with qd

    # c08.s07
    scene bg c8_market_low
    with fade
    "The clinic was Sefa's idea."

    "She said that if agravars thought mariners were a story, somebody had better show them otherwise. She said that she had not come all this way to hide under a market."
    "And she said, when Dace objected, that Brightwater had kept a Wellwalker in a jar for eight months to find out how to sell what she did. The quickest way to spoil that was to give it away under their noses."

    show p yeva_tired as right at head_right
    with qd
    "Yeva looked at her for some time."
    c_yeva "I've been thirty years on the road,"
    c_yeva "and I never thought of sitting still in one place and letting them come to me. Help me up."

    hide right
    with qd
    "They set it up on the lowest tier of the Wet Market, where the stalls stand half in the water and half out. It was a plank table and two basins and a girl of sixteen."
    "Behind her stood a Wellwalker out of a legend. She had been starved for eight months, and she was upright through pure obstinacy."

    "For the first morning nobody came. People looked, and walked on."

    scene cg c8_porter_child
    with dissolve
    "In the afternoon a dock porter came down the steps with a child in his arms. He was a big slow man with a broken nose. The child was four or five, and limp, and her breath rattled."
    "The company clinic had priced the fever at three months' scrip. He did not have three months' scrip. He stood at the edge of the planking and did not seem to know how to ask."

    "Sefa held out her arms. He looked at her wet hair and her dark eyes for a long moment, and then he put his daughter into them."

    scene bg c8_market_low
    with dissolve
    "She laid the child in the basin and put her hands in the water. The market went quiet around them. It took about as long as boiling an egg. The child sat up, and looked at the lamps, and asked for noodles."

    "By nightfall the queue went round the lock and up the stair."

    "They healed anyone. They asked nothing. They said, to everyone who asked, that it could not be bottled or sold and would not keep, and that anybody claiming otherwise was a thief."
    "Ilan worked at the second basin with his hat on. He purged lungs and blood and old infections. In nine days he saw more of what the refineries did to people than he had seen in fifteen years of sitting above them."
    "The porter came back every day. His name was Garran, and the child's was Pim. He appointed himself to keep the queue in order, and nobody argued with him."

    "Brightwater's security came on the fourth day. There were twelve of them, in white, with batons. They found three hundred dock families standing between them and the table."
    "Garran was in front with his arms folded. Above them, in a glass box, a Lockkeeper was drinking his tea with great attention. The men in white went away again."

    "She came on the sixth night, alone, after the market lamps were dimmed."

    "Ilan knew her walk before he saw her face. She came down the steps to the lowest tier in a plain raincoat, with no guard, and stood at the edge of the planking where Garran had stood."
    "She looked at the two basins. She looked at Yeva for a long time."

    show p wrack_hat_guarded as left at head_left
    show p marsh_flat as right at head_right
    with qd
    c_marsh "I had you in a tank for eight months,"
    c_marsh "I signed for it. I told myself it was research."

    show p yeva_stern as right at head_right
    with qd
    c_yeva "I know what you told yourself,"
    c_yeva "I could hear it through the glass."

    show p marsh_flat as right at head_right
    with qd
    c_marsh "Yes. I expect you could."
    "She did not flinch. Her eyes moved to Ilan, under his hat, and rested there without surprise."
    c_marsh "Mr Voss. I thought it must be. Nobody else knew which floor."
    "She turned back."
    c_marsh "I've watched this table for three days from a window. I saw that child's lungs. I trained eleven years to do less than that girl did in four minutes."
    c_marsh "I've spent thirty more working out what people will pay not to watch their children die."
    "She said it flatly, like a diagnosis."
    c_marsh "I have forty hospitals. There are beds in them empty tonight, because the people who need them have no scrip."
    c_marsh "I want to open the wards. To you, and to any healer of yours who'll come. No charge at the door."

    hide left
    hide right
    with qd
    "Sefa had stopped with a cloth in her hand."

    show p wrack_hat_guarded as left at head_left
    show p yeva_stern as right at head_right
    with qd
    c_yeva "Why?"

    show p marsh_humble as right at head_right
    with qd
    c_marsh "Because I was a doctor before I was a board. I'd like to be one again before I die. I haven't a better reason."

    show p yeva_stern as right at head_right
    with qd
    c_yeva "I'll not go into one of your buildings again,"
    c_yeva "The girl might. That's hers to say."

    show p sefa_hard as right at head_right
    with qd
    c_sefa "I'd want to see the tank first,"
    c_sefa "Empty. With the lid off."

    show p marsh_flat as right at head_right
    with qd
    c_marsh "You shall."

    show p wrack_hat_calm as left at head_left
    with qd
    c_ilan "Can you do it?"
    c_ilan "It isn't only yours to open."

    hide left
    hide right
    with qd
    "For the first time Marsh hesitated."

    show p wrack_hat_calm as left at head_left
    show p marsh_hesitant as right at head_right
    with qd
    c_marsh "No,"
    c_marsh "Brightwater's notes are held at the Exchange, like everybody's. I can't give away a bandage without the chairman's leave. I've asked to see him."
    "She turned her collar up against the drip from the planking overhead."
    c_marsh "He's always been very civil to me. He remembers my children's names."

    hide left
    hide right
    with qd
    "Ilan said nothing. He knew whose leave she meant. He knew how that civility felt, from the inside."

    "She went back up the steps. Sefa watched her go."

    show p wrack_hat_melancholy as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "She meant it,"
    c_sefa "I could feel her meaning it. Is that allowed? For one of them just to stop?"

    c_ilan "I don't know,"
    c_ilan "I've never seen anyone try."

    hide left
    hide right
    with qd
    "On the ninth day Yeva went back to her road. She kissed Sefa on the forehead, which made Sefa cry. To Ilan she said only,"

    show p wrack_hat_melancholy as left at head_left
    show p yeva_dry as right at head_right
    with qd
    c_yeva "Look at it. All of it. Every day."

    hide left
    hide right
    with qd
    "A week later there was a mariner healer at the waterline in Clearwell, under Brightwater's own white terraces. After that came another in the Stubborns, and one at the Crown. Pell came to the boat with the figures, shaking with joy."
    "Within the month, Brightwater's medical division had lost a third of its custom. In Clearwell the workers' towns had stopped buying at the company pharmacy. The board was in emergency session, and the smiling sun had been taken off three buildings by persons unknown."

    scene bg c8_poster_canal
    with dissolve
    "On the last evening Garran stopped by the canal where Ilan was sitting. He had Pim on his shoulders. He had been watching Ilan for days."

    show p wrack_hat_melancholy as left at head_left
    show p garran_wary as right at head_right
    with qd
    c_garran "You're not one of them,"
    c_garran "Not quite. You're one of us, and you're not that either. You talk like the Sluice."
    "He scratched his broken nose."
    c_garran "Who are you?"

    hide left
    hide right
    with qd
    "He could have said {i}Wrack{/i}. It was a good name. A kind girl had given it to him, and he had been a better man under it."

    show p wrack_hat_melancholy as left at head_left
    show p garran_wary as right at head_right
    with qd
    c_ilan "Ilan Voss,"
    c_ilan "I was born four streets from here."

    hide left
    hide right
    with qd
    "Garran looked at the poster on the wall across the canal. He looked back."

    show p wrack_hat_melancholy as left at head_left
    show p garran_accepting as right at head_right
    with qd
    c_garran "Thought you were drowned,"

    show p wrack_hat_calm as left at head_left
    with qd
    c_ilan "I was. It didn't take."

    hide left
    hide right
    with qd
    "The big man considered this. Then he nodded, slowly. He seemed to be putting it away to think about later. He went off up the stair with his daughter, who was waving."

    jump ch09
