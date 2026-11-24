# Chapter 16. The Long Way Round. Staged from work/cut/ch16.md; the text is the approved text.

define c_kelder = Character("Speaker of Kelder")
define c_lockkeeper = Character("Senior Lockkeeper")
define c_noodle = Character("Noodle-stall old man")

label ch16:

    # c16.s01
    scene bg c16_kelder_day
    with fade
    "He began at the bottom of the hill."
    show p wrack_thread_troubled as left at head_left
    with qd
    "It was two hundred paces from the refinery school to the tin roofs, and it took him half the morning. Sefa walked on one side of him and the man in Meridian grey on the other. The dockers of the Waterline watched him pass."
    "Some of them took their caps off. Some did not."
    "The tanks stood behind the sea-wall in rows. Electric lamps hung over them on wires, hard and white, and they did not flicker. That had been in the paper."
    "{i}Lamps that do not fail.{/i} The people of four holds sat in the water in lines, as they had been put. Each wore a brass tag on a cord at the wrist, stamped with a number."
    show p wrack_strong_attentive as left at head_left
    with qd
    "Nobody had locked the sheds. There had been no need. There was nowhere to go."
    "Somebody had been at the sluices, all the same. The iron gates at the seaward end of every row hung open, sawn through at the hinge. A big grey-bearded man was sitting on the wall beside the last of them with a hacksaw across his knees."
    "A woman sat against his shoulder, and two girls."

    show p corin_weary as right at head_right
    with qd
    c_corin "Three days,"
    "He did not get up."
    show p corin_grief as right at head_right
    with qd
    c_corin "The dockers lent me the saws. They'd heard the sirens, same as these did. Nobody came to open a door for any of them."
    "He looked at the blade."
    c_corin "He'll have reckoned the cost of that. He'll have had a figure for it."

    show p wrack_thread_pleading as left at head_left
    with qd
    c_ilan "I need them,"
    c_ilan "I've come to ask."

    show p corin_earnest as right at head_right
    with qd
    c_corin "Then ask them. Not me. I'm nobody's pilot."

    hide left
    hide right
    with qd
    "The speaker of Kelder was an old man with a mild, defeated face. He listened, standing in the trough with the white light on his head. Ilan told him what was being done to the sea."
    "He told him about the ring, and the city under it, and what he thought could be done."
    "He said that he could do none of it himself. He was asking for every caller and every healer the four holds had, to go to the edge of dead water and risk the undertow, for a place that none of them had seen."

    show p kelder_mild as right at head_right
    with qd
    c_kelder "We marked a paper,"
    c_kelder "Twenty years. I marked it for all of us. Our lamps were out."

    show p wrack_thread_troubled as left at head_left
    with qd
    c_ilan "I can't unmark it. I can tell you that the man who holds it is drying the sea you came from."

    c_kelder "And if we come out of these tanks, where do we go after? Kelder's dark."

    c_ilan "I don't know. I think I know. I can't promise it."

    hide left
    hide right
    with qd
    "The old man considered him."

    show p kelder_considering as right at head_right
    with qd
    c_kelder "You're the first of them who's said so,"
    "He turned, and spoke to the nearest of his people, and they spoke to the next. Ilan watched it go down the rows. It was a Moot, he saw. It was a small one, held in a trough. It took two hours, and nobody raised a voice."

    hide right
    with qd

    scene cg c16_kelder_exit
    with dissolve
    "Then the callers of Kelder got up out of the orphan water. They went down through the open sluice into the harbour, which was clean, and could hear. He saw their faces as it touched them."

    scene cg c15_harbour_clear
    with dissolve
    "By evening the tanks were empty. Eleven thousand mariners hung in Port Halcyon harbour under the eyes of the Stacks. On the quay a docker's wife was handing bread rolls down over the edge, one at a time, to children who had never seen bread."

    scene bg c16_kelder_evening
    with dissolve
    show p okonta_grave as right at head_right
    with qd
    "Okonta had watched it all from the wall. Corin came and stood in front of her. He had the hacksaw still in his hand, and seemed not to know it."

    show p corin_earnest as right at head_right
    with qd
    c_corin "I know where his twenty-two fly,"
    c_corin "I know their watches, and who's tired of it. I'd fly for you. If you'd have me."

    show p okonta_flat as right at head_right
    with qd
    c_okonta "I'm not him,"
    c_okonta "I can't make you anything."

    show p corin_earnest as right at head_right
    with qd
    c_corin "No."

    show p okonta_flat as right at head_right
    with qd
    "She was silent."

    c_okonta "Say it, then."

    show p corin_earnest as right at head_right
    with qd
    "He said it. He was fifty-eight years old, and his voice shook like a boy's. {i}Keep the water. Own nothing you can't carry. Come when you're called.{/i}"

    show p okonta_grave as right at head_right
    with qd
    c_okonta "To whom?"

    show p corin_earnest as right at head_right
    with qd
    c_corin "To you. You're alive."

    hide right
    with qd

    scene cg c16_okonta_corin
    with dissolve
    "She nodded once. She had still not smiled. But she put her hand on his forearm, as an old man had gripped hers in the gallery of the Dragon, and held it there."

    # c16.s02
    scene bg c16_kelder_evening
    with fade
    "He could not call. He could ride."
    show p wrack_thread_dejected as left at head_left
    with qd
    "The Thread was not the gift, and being ebbed did not touch it. He lay along the needle with Sefa behind him and thought, with some bitterness, that it was the one thing Jef had given him that he could not spoil."
    "Okonta flew on one side, and Corin on the other. They ran west."

    scene bg c16_saltgate_stacks
    with dissolve
    "Saltgate stood on its black pillars with its feet out of the water."
    "He had never seen the bottoms of the stacks. Nobody had. The lowest stilts of the city stood on them in the open air like the legs of a wading bird."

    scene bg c16_market_dry
    with dissolve
    "The canals were ditches. The stallholders sat on the boards with their goods around them and nobody to sell to. The mariners had gone out with the water."

    scene bg c16_sluice_dry
    with dissolve
    "On the Sluice the noodle stall was open. The old man with the bucket looked at him twice, as he had before."

    show p noodle_kindly as right at head_right
    with qd
    c_noodle "You're Tomas Voss's boy,"
    c_noodle "I said so to my wife, the last time. She said he was drowned."

    hide right
    with qd
    "He ladled a bowl, and would not be paid."

    show p noodle_puzzled as right at head_right
    with qd
    c_noodle "Your mother used to come down for broth. She never took the noodles. I always wondered."

    hide right
    with qd
    "Ilan ate it standing on the towpath, under the fourth-floor window. The canal below him was a bed of black mud with a bicycle in it."

    scene bg c16_lock_box
    with dissolve
    "The Lockkeepers kept their senior box at the north gate. He climbed to it by an iron ladder, slowly, stopping at every landing. The woman inside was seventy. She had a brass badge worn smooth, and a kettle, and a logbook the size of a paving stone."

    show p lockkeeper_stern as right at head_right
    with qd
    c_lockkeeper "We don't take sides,"
    "she said, before he had his breath."
    c_lockkeeper "I'll tell you that at once, and save you the stairs next time. Four hundred years. Halcyon's asked, and Kessler's asked, and your mother's people have asked. We keep the gates."

    show p wrack_strong_attentive as left at head_left
    with qd
    c_ilan "I'm not asking you to take a side. I'm asking you to read me a measurement."

    hide left
    hide right
    with qd
    "She looked at him over her cup. Then she opened the book."

    show p lockkeeper_stern as right at head_right
    with qd
    c_lockkeeper "Down two metres and forty since the ninth of the month,"
    c_lockkeeper "And falling a hand a day. There's four centuries of soundings in this book. The most it ever moved before was the width of that hand."
    "She shut it."
    c_lockkeeper "My grandfather kept this box. He used to say that the only thing a Lockkeeper has to know is that the sea comes in and the sea goes out. He never said what we did if it only went out."

    show p wrack_thread_troubled as left at head_left
    with qd
    c_ilan "If it doesn't come back, there are no gates."

    show p lockkeeper_resolved as right at head_right
    with qd
    c_lockkeeper "I can count, young man."
    "She drank her tea."
    c_lockkeeper "No sea, no gates. No gates, no Lockkeepers, and no Saltgate. That isn't a side. That's arithmetic."
    show p wrack_strong_attentive as left at head_left
    with qd
    "She reached up and took hold of a brass handle over her head, polished by generations of hands."
    c_lockkeeper "What is it you want carried, and where to?"

    show p wrack_strong_resolved as left at head_left
    with qd
    c_ilan "People. To the edge of it."

    hide left
    hide right
    with qd
    "She pulled. A horn sounded over the north gate, deep and long. Another answered from the east, and a third. He had lived in that city for sixteen years and had never heard them. Nobody had. They were for the day the gates were shut."

    show p lockkeeper_resolved as right at head_right
    with qd
    c_lockkeeper "Every gate barge we have,"
    c_lockkeeper "And I'll have the figures read from every box on the hour, for anyone who'll listen. I don't say they'll believe a Lockkeeper. But we've never yet told them anything that wasn't so."

    scene bg c16_barges_lantern
    with dissolve
    "Garran's dockers loaded the barges that night, in the mud, by lantern."

    # c16.s03
    scene bg dc_high_hall
    with fade
    "He went north, because there was one hold he could not ask by messenger."
    "They received him in the high hall, under the vault of clear glass. He had been told what the hall did. He stood on the inlaid wave in the middle of the floor and spoke to seven elders, and knew that twelve thousand people were hearing him twice."

    show p wrack_thread_troubled as left at head_left
    with qd
    c_ilan "I've come to tell you three things, and then to ask for one,"
    c_ilan "The first is that two of your hearts can't be mended. Elder Vey has told you that. They want making, and nobody alive can make. The second is that there's dead water coming up from the south. Your choirs have heard it. It will be here in forty days."
    c_ilan "The third is that I can do nothing about either. I'm ebbed. I can't call a cupful. And when I wasn't ebbed, I gave the sea an order, and killed ten kilometres of it. You know that too."

    hide left
    with qd
    "The canyon gave it back to him, from below, and from above."

    show p wrack_thread_pleading as left at head_left
    with qd
    c_ilan "There's a city under the Girdle. I think it can be raised. I think that if it is, the thing that's killing the water stops, and there's room in it for every dark hold there is. I can't raise it."
    c_ilan "It would take every caller you have, and every healer, at the edge of deaf water, passing strength hand to hand through a man who has gone under once already. Some of them may not come back whole. I've nothing to offer for it. I'm only asking."

    hide left
    with qd
    "Elder Vey sat very straight. It was some time before she spoke."

    show p vey_tight as right at head_right
    with qd
    c_vey "You ask,"
    c_vey "You have not told us what you will do for us."

    show p wrack_strong_calm as left at head_left
    with qd
    c_ilan "No."

    show p vey_shaken as right at head_right
    with qd
    c_vey "He never asked us for anything. The old man. Not in nine hundred years. He came, and mended, and complained of his knees, and went away."
    "Her hands were folded in her lap."
    c_vey "I have wondered, since, whether that was why we let him carry it. It is very easy to be grateful. It asks nothing of one."

    hide left
    hide right
    with qd
    "She did not put it to the elders. She lifted her head, and spoke to the vault."

    show p vey_tight as right at head_right
    with qd
    c_vey "The hold has heard him,"
    c_vey "Let the choirs answer."

    hide right
    with qd

    scene cg c16_choirs_answer
    with dissolve
    "For a moment there was nothing. Then, far down in the canyon, a single choirmaster sang a phrase. It was four notes, rising. Another took it up across the gulf, and another above."
    "It climbed the walls tier by tier, forty choirs one after the other, until the whole canyon was ringing with it, and the glass over his head hummed."

    scene bg dc_high_hall
    with dissolve
    show p vey_tight as right at head_right
    with qd
    c_vey "That is yes,"
    c_vey "You'll want Aurel. He has already packed."

    hide right
    with qd

    scene bg dc_sea_door
    with dissolve
    "At the sea-door on the rim a huge young man in sealskin was sitting on a bale."

    show p brask_wry as right at head_right
    with qd
    c_brask "Rime's sent forty,"
    c_brask "And a sledge of cod. Southerners never bring enough to eat."

    hide right
    with qd
    "He looked Ilan over, from the feet up, as he had at Greywatch Stone."

    show p brask_wry as right at head_right
    with qd
    c_brask "You're less than you were. You look better for it."

    hide right
    with qd

    # c16.s04
    scene bg c16_girdle_fleet
    with fade
    "The Eyes had begun to drift."
    "Dace said so, when the needles found her. The calm places of the Belt had moved on a pattern since before there were charts. Now they were sliding, all of them, toward one point in the open Girdle, like crumbs toward a hole in a cloth."
    "Lashing had gone with its Eye. It lay now on a flat grey sea, under a ring of sky, at the edge of the dead water."
    "He came to it on the twentieth day, and did not know the place."

    scene cg c16_fleet_gathered
    with dissolve
    "There were boats to the horizon. Lashing's six thousand hulls were the middle of it. Round them lay the gate barges of Saltgate, and tugs out of Keelhaven, and the fishing smacks of the Stubborns."
    "He saw the boats of Old Tolla, with the first fish of the catch nailed to their bows. There was a white Brightwater hospital ship. Her captain had turned her round at sea, he heard, on the day he learned how Dr Marsh had died."
    "Agravars stood at every rail."
    "And in the water were the mariners. Two hundred holds had sent everyone who could travel. Odile had the Moot there, with her lists. They hung in the warm cloudy sea in their thousands, long-limbed and dark-eyed, looking up."

    scene bg c16_girdle_fleet
    with dissolve
    "He saw the brass tags of Kelder, still on their cords. Somebody had told them they might take the tags off, and they had said that they would do it afterwards."
    "It was the first time in three thousand years that the two peoples had been within arm's reach, in such numbers, with nothing in anyone's hands. Nobody was speaking. Forty thousand people were looking at each other across a metre of air and water."
    "They were finding out that the other was real."

    scene cg c16_grey_wall
    with dissolve
    "To the west, where the sea should have gone on, there was a wall."
    "It was forty kilometres off, and it filled a quarter of the horizon. It stood a little higher than the sea in front of it, like the edge of a table. As he watched, the whole length of it shivered, and stepped toward him, and was still again."

    scene bg c16_girdle_fleet
    with dissolve
    "He could not feel the water under the boat. Nor could anyone. The deaf sea began two kilometres to the west, at a line as sharp as a shoreline, and the callers of two hundred holds had drawn up along it like people at the lip of a cliff."

    # c16.s05
    scene cg c16_maelis_arrives
    with fade
    "The rays came on the twenty-second day."
    "They had never before come into the Girdle. They rose round the rafts in a slow wheel, hundreds of them, pale wings turning under the grey water, and on every deck the agravars went silent. Some knelt."
    "The old one with the notched wing came alongside Dace's boat. A tall woman in a patched coat stepped off its back and over the gunwale, as one steps off a ferry."

    scene bg c16_boat_stern
    with dissolve
    "Her hair had begun to grow. She looked at Ilan, wrapped in his blanket in the stern. She looked for longer at the girl beside him."

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "Show me your hands,"

    show p maelis_cropped_impassive as right at head_right
    with qd
    "Sefa held them out. Maelis took them in her own and turned them over. She pressed the palms with her thumbs, as Jef had pressed Ilan's fingers under a lamp."

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "They told me,"
    c_maelis "They've had it since Fallow. They wouldn't let me come until I'd sat nine days with the water."

    hide right
    with qd
    "She took a small clay bottle from her pocket, stopped with wax, and set it on the thwart between them."

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "I ask everyone the same question. I asked him. What will you do with the life you get back?"

    show p sefa_lip as right at head_right
    with qd
    "Sefa looked at the bottle. Her mouth worked."

    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "I thought I knew,"
    c_sefa "I had it all ready, in case you ever came. I was going to say I'd go and look at that tank with the lid off, and then find every other one like it."
    "She drew a breath."

    show p sefa_shaken as right at head_right
    with qd
    c_sefa "It's not that, though. It's that I thought it was mine. I thought I was good at it. I was {i}proud{/i}. And then it went, and I was still there. I could still set a bone. I could still tell when somebody meant a thing."
    "She looked up."

    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "If I had it back, I'd know I was only where it went through. I think I'd be better at it. I don't know what I'd do. I'd just stop thinking it was me."

    hide right
    with qd
    "Maelis was silent for some time."

    show p maelis_cropped_amused as right at head_right
    with qd
    c_maelis "He took thirty-eight years to find that out,"
    "she said, with a glance at Ilan."
    c_maelis "And had to be drowned twice."

    hide right
    with qd
    "She put the bottle into Sefa's hand, and closed the fingers on it."

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "Drink it in the sea. Not in a boat."

    hide right
    with qd
    "Sefa went over the side. Bother went after her. Ilan could not see what happened under the water. He saw the hound come up alone, and bark, once, at nothing."

    scene cg c16_sefa_handful
    with dissolve
    "Then she surfaced beside the boat. She was holding a double handful of sea up in front of her face, and she was laughing and crying together. It held its shape a little, as water should not. It was warm."
    "He could see the warmth, like the air over a stove."

    scene bg c16_boat_stern
    with dissolve
    show p maelis_cropped_amused as right at head_right
    with qd
    c_maelis "That is the first thing I have enjoyed in half a year,"
    "She sat down on the thwart."
    c_maelis "Now. They've told me something else. In fifty-five years they have never once told me what they want. I've asked. They thought it was funny."

    show p maelis_cropped_level as right at head_right
    with qd
    "She looked out at the turning wings."

    show p maelis_cropped_grave as right at head_right
    with qd
    c_maelis "They're tired, Ilan. They have remembered everything, for everybody, since before the Makers. Every drowned child. Every war. All that the undertow ever took. Nobody has ever taken any of it off them. They've carried it by themselves."

    hide right
    with qd
    "She folded her hands."

    show p maelis_cropped_grave as right at head_right
    with qd
    c_maelis "There are walls in that city which remember. They want them lit. They want, for once, to put something down."

    show p wrack_strong_attentive as left at head_left
    with qd
    c_ilan "And you?"

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "I'm coming in with you. I knew him when he was fourteen and couldn't speak. He taught me a game with stones."

    hide left
    with qd
    show p maelis_cropped_grave as right at head_right
    with qd
    "Her face was quite calm."

    show p maelis_cropped_level as right at head_right
    with qd
    c_maelis "I should like him to see mine."

    hide right
    with qd

    # c16.s06
    scene bg c16_boat_stern_evening
    with fade
    "Hesper came last, on the evening before."
    "He was in the stern, watching Odile and forty choirmasters sort eleven thousand callers into rings. He had nothing to do with it. Odo of Lashing was doing the same for the boats, through his brass trumpet."
    "Teodora Raske stood on the deck of a tug with her three hundred and eleven, checking the seals on one another's hard suits. Adler Crane was among them, in a borrowed helmet, holding a lamp for Hanne."
    "They looked like people about to sit an examination."
    show p wrack_strong_calm as left at head_left
    with qd
    "He had been somebody that people could not do without. He was watching it stop. He found, to his surprise, that it was like setting down a sled rope."
    "\"You've got thin,\" somebody said, in the water."
    show p hesper_tired as right at head_right
    with qd
    "Hesper had her arms folded on the gunwale. She looked ten years older than at Low Anthem. The cord was gone from her wrist."

    show p hesper_stern as right at head_right
    with qd
    c_hesper "I went back,"
    c_hesper "To where we built it, off the Crown. And then I went to Fallow. I wanted to see it properly. I'd only seen that it worked."
    show p hesper_raw as right at head_right
    with qd
    "She was not looking at him."
    c_hesper "There's nothing. No weed. No fish. I put my hand in, and it was like putting it into a dead mouth. I did one of those. I stood in front of two million people and told the sea to stand, and it never spoke again."
    "Her jaw was tight."
    c_hesper "Davin would have known. He'd not have needed to go and look."

    show p wrack_thread_ashamed as left at head_left
    with qd
    c_ilan "I needed to go and look. I never did. For fifteen years."

    show p hesper_stern as right at head_right
    with qd
    c_hesper "I know. It's why I can stand to talk to you."

    hide left
    hide right
    with qd

    scene cg c16_sefa_asleep
    with dissolve
    "She glanced along the boat. Sefa was asleep in the bows with her hand trailing in the water. Even from the stern he could see that the sea round her fingers was faintly gold."

    scene bg c16_boat_stern_evening
    with dissolve
    show p hesper_stern as right at head_right
    with qd
    "Hesper looked at that for a long moment. Something went out of her shoulders."

    show p hesper_eased as right at head_right
    with qd
    c_hesper "Then it wasn't the wrong one,"
    c_hesper "It was only lent."

    show p wrack_strong_attentive as left at head_left
    with qd
    c_ilan "You said you'd stop me yourself, if I did it again without learning."

    show p hesper_eased as right at head_right
    with qd
    c_hesper "I did. I'll hold to it."
    "She almost smiled."
    c_hesper "You're not to try lifting that city, Wrack. I can see you thinking about it. You'd die of it, and it'd come up crooked."
    show p hesper_teacher as right at head_right
    with qd
    c_hesper "You showed three hundred of us a thing at Tidehall that had never been done, and then you went off to do everything by yourself, as usual. You can't. {i}We{/i} can. You've only to be the place it goes through."
    "She pushed off from the gunwale."
    c_hesper "I've twelve who know how a great weight is built. And how it isn't. Odile's put us in the first ring."

    hide left
    hide right
    with qd

    scene bg c16_rafts_night
    with dissolve
    "Later, when the lanterns were lit, a big man came picking his way across the rafts with a child asleep on his shoulder."

    scene cg c16_garran_west
    with dissolve
    "Garran stood on the planking and looked west. Now and then it shivered."

    scene bg c16_rafts_night
    with dissolve
    show p garran_pensive as right at head_right
    with qd
    c_garran "Is that it?"
    c_garran "The other field?"

    show p wrack_strong_calm as left at head_left
    with qd
    c_ilan "It's under that."

    hide left
    with qd
    show p garran_pensive as right at head_right
    with qd
    "The porter studied it for a while, as he might have studied a crate too heavy for one."

    show p garran_accepting as right at head_right
    with qd
    c_garran "Then we'd best go and fetch it,"

    hide right
    with qd
    jump ch17
