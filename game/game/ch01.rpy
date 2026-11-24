# Chapter 1. Wrack. Staged from work/cut/ch01.md; the text is the approved text.

define c_wrack = Character("Wrack")
define c_sefa = Character("Sefa")
define c_oro = Character("Elder Oro")
define c_ione = Character("Ione")
define c_davin = Character("Davin")

define qd = Dissolve(0.2)

transform head_left:
    xalign 0.27 yalign 1.0 yoffset -80 zoom 0.8
transform head_right:
    xalign 0.73 yalign 1.0 yoffset -80 xzoom -0.8 yzoom 0.8
transform bother_corner:
    xalign 1.0 yalign 1.0 yoffset -20 xzoom -0.45 yzoom 0.45

label ch01:

    # c01.s01
    scene cg wake
    with fade
    "He woke on the seabed with a kelp frond across his face and no idea who he was."

    "That was the second thing he noticed. The first was that he was breathing."
    "Water went in and out of him, cold and easy, and some part of him that had no words was certain this should be killing him."

    "He lay still and looked up. He was at the bottom of a forest."

    scene bg kelp_forest
    with dissolve
    "The light that came down through them was green at the edges and gold in the middle, and it moved slowly across the sand. And the forest was making a sound."
    "Every stem was humming in the current, each on its own low note, and the notes ran together into a chord that had no beginning and did not seem to need an end."
    "He felt it in his teeth."

    show p bother_alert as bother at bother_corner
    with qd
    "Something bumped his ribs."

    "He turned his head and found a whiskered grey muzzle a hand's width from his nose. It belonged to an animal like a seal that had been built by someone fond of dogs."
    "It wore a collar of plaited cord. It snuffled his neck, sneezed a stream of bubbles into his face, and looked up, very pleased with itself, for someone to tell about it."

    hide bother
    show p sefa_wary as right at head_right
    with qd
    "A girl of about sixteen hung in the water above him. She was holding a harvesting hook the way you hold something you are prepared to use."

    show p wrack_bewildered as left at head_left
    show p sefa_wary as right at head_right
    with qd
    "\"Bother, leave it,\" she said. Then, to him: \"You're wearing shoes.\""

    "He looked. He was. Heavy surface boots, a torn grey jacket with a corporate crest half ripped away, and around both wrists the raw red marks of a cable tie."

    "\"What's your name?\""

    hide left
    hide right
    hide bother
    with qd
    "He opened his mouth and found nothing behind it. Not a name, not a mother, not a street."
    "Only a blank like a wiped slate, and under the blank, very far down, the feeling of having done something terrible."

    show p wrack_blank as left at head_left
    show p sefa_wary as right at head_right
    with qd
    "\"I don't know,\" he said. His voice came out strange in the water, slow and round, and he understood, distantly, that he had never spoken in water before."

    show p sefa_thoughtful as right at head_right
    show p bother_pleased as bother at bother_corner
    with qd
    "The girl studied him. The animal she had called Bother swam a tight circle round his boots and came back to report to her knee."

    hide bother
    with qd
    show p wrack_puzzled as left at head_left
    with qd
    "\"Then you're Wrack,\" she said."
    show p sefa_amused as right at head_right
    with qd
    c_sefa "It's what we call what the tide brings in. I'm Sefa. Can you swim, or do I tow you?"

    scene cg swim
    with dissolve
    "He could swim, it turned out, though not as she did. She went through the water without seeming to do anything, a flick of the feet now and then, like a person strolling."
    "He laboured after her in his boots. The hound went ahead and came back, ahead and back, to make sure that nobody was lost."

    scene bg kelp_forest
    with dissolve
    show p wrack_puzzled as left at head_left
    show p sefa_wary as right at head_right
    with qd
    c_sefa "Don't touch anything,"
    "Sefa said over her shoulder."
    c_sefa "And don't say you're from the islands until an elder asks you. Some of them will mind."

    # c01.s02
    scene bg terraces_dome
    with fade
    "The forest had been tended. He began to see it as they went."
    "The sand between was raked clean, and here and there a stem had been cut and bound with cord, as a branch is pruned."
    "Then the ground began to step upward in terraces, each one walled with fitted stone, and there were people on them."

    scene bg terrace_work
    with dissolve

    "They were cutting fronds with hooks and laying them in floating nets. A shoal of fat silver fish grazed along the foot of a wall under the eye of two more hounds."
    "Somebody was singing, and the others took it up without lifting their heads. It was a slow song with a long line, and it fitted itself to the chord of the forest."

    "They stopped singing when they saw his boots."

    show p wrack_puzzled as left at head_left
    show p sefa_proud as right at head_right
    with qd
    c_sefa "Silverbacks,"
    "Sefa said, as though nothing had happened, nodding at the fish."
    c_sefa "We herd them. That's the nursery terrace, and those are the drying racks, and that's home."

    hide left
    hide right
    hide bother
    with qd
    "At the top of the terraces stood a dome."

    scene bg dome_dark_half
    with dissolve

    "It was the size of a hill. He could see at once that it had not been built by the people on the terraces, or by anyone like them. It was very old, and very beautiful."
    "Light shone through it from inside, but only on one side."
    "The other half of the dome was dark, and against the dark panes somebody had hung long strings of a weed that glowed a faint yellow-green, like a candle seen through a leaf."

    show p wrack_bewildered as left at head_left
    show p sefa_proud as right at head_right
    with qd
    c_wrack "What is it?"

    c_sefa "Low Anthem. It's a hold."
    show p sefa_sharp as right at head_right
    with qd
    "She saw that the word meant nothing to him, and her look sharpened."
    c_sefa "A hold. Where people live. The Makers built them, before the Sinking. They built all of them, there's three hundred. We just keep them."
    show p sefa_proud as right at head_right
    with qd
    "She shrugged, with the pride of someone speaking of a poor relation."
    show p sefa_amused as right at head_right
    with qd
    c_sefa "We're one of the small ones. Four hundred of us. Half our lamps are out. They've been out since before my grandmother was born, so nobody minds."

    show p wrack_puzzled as left at head_left
    with qd
    c_wrack "Who were the Makers?"

    show p sefa_thoughtful as right at head_right
    with qd
    "Sefa looked at him for some time."

    show p sefa_amazed as right at head_right
    with qd
    c_sefa "You really don't know anything,"
    c_sefa "They were the people before. They could make things like that,"
    "and she pointed at the white ribs,"
    c_sefa "and like the lamps, and the air-hearts that make the dry rooms dry."
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "Then the sea came up, three thousand years ago, and they went, and nobody knows how to make anything now. We know how to clean it and how to sing to it."
    c_sefa "If a lamp goes out it stays out."
    "She said it as she might have said that people grow old."
    show p sefa_amused as right at head_right
    with qd
    c_sefa "Come on. In at the sea-door, and mind your head."

    scene cg sea_door
    with fade
    "The sea-door was a round pool in the floor of the dome, twenty paces across, with the sea on one side of its surface and air on the other."
    "He came up through it into warmth and lamplight and the smell of smoke and frying fish, and stood dripping on a stone floor."
    "Then, because his body had apparently always known how, he breathed out the water and breathed in the air. It hurt a little, like a first breath on a cold morning."

    scene bg sea_door
    with dissolve
    "A great many people were looking at him."

    # c01.s03
    scene bg dry_room
    with fade
    "They put him in a dry room and argued about him for three days."

    "He was not in the room when they argued, but Sefa was, when she could get in. She brought him the news with his meals. She had appointed herself his guard."
    show p bother_pleased as bother at bother_corner
    with qd
    "It seemed nobody had asked her to, and nobody had told her to stop. The hound came with her and lay across the doorway with his chin on Wrack's boot."

    hide bother
    with qd
    show p wrack_puzzled as left at head_left
    show p sefa_amused as right at head_right
    with qd
    c_sefa "He's a tide hound,"
    "she said, when he asked."
    c_sefa "Every hold has them. They herd the silverbacks and they watch the terraces at night, and if a child swims off they bring it back by the collar. He's not a very good one."
    c_sefa "He's nosy. He goes through people's baskets. That's why he's called Bother."
    show p bother_pleased as bother at bother_corner
    with qd
    "Bother thumped his tail-flipper on the floor at the sound of his name."
    hide bother
    with qd
    c_sefa "He found you. He's been insufferable about it."

    hide left
    hide right
    hide bother
    with qd
    "The meals were flat cakes of pressed kelp, smoked silverback, and a bowl of small green globes that burst salt on the tongue. He ate everything."
    "He did not know when he had last eaten, and that was the least of what he did not know."

    show p wrack_puzzled as left at head_left
    show p sefa_dry as right at head_right
    with qd

    "The argument, as Sefa reported it, went like this. He breathed water, so he was a mariner; that was what the people of the holds called themselves."
    "He wore the clothes of the islands and did not know a single song, so he was not."
    "He was an agravar, a land-dweller, one of the forty million who lived on the rocks up above and threw their filth down. But agravars drowned. Then he was a spy."
    "Or he was bait. The corporations that ruled the islands had thrown a man in to see who came to collect him."

    show p wrack_pained as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_wrack "What do you think I am?"
    "Wrack asked her."

    "Sefa considered it honestly."
    c_sefa "I think you're somebody who's had something awful happen to them,"
    show p sefa_amused as right at head_right
    with qd
    c_sefa "Eat your sea-grapes."

    show p wrack_blank as left at head_left
    show p oro_gentle as right at head_right
    with qd
    "It was Elder Oro who ended the argument. Wrack met him on the second evening. He was a very old man with a gentle, slightly amused way of looking at things."
    "He came in and sat on the bench and looked at Wrack's wrists for a while."

    show p wrack_blank as left at head_left
    show p oro_gentle as right at head_right
    with qd
    c_oro "I am the eldest here, so I speak last,"
    c_oro "It's a great advantage. By the time it's my turn everyone else has said all the foolish things, and I need only choose the least foolish."
    "He nodded at the marks."
    show p oro_thoughtful as right at head_right
    with qd
    c_oro "I told them the sea does not usually deliver spies with their hands tied. Does that seem fair to you?"

    show p wrack_pained as left at head_left
    with qd
    c_wrack "I don't know what I am,"

    show p oro_gentle as right at head_right
    with qd
    c_oro "No. Well. It'll come or it won't. In the meantime Ione will look at you."

    show p ione_calm as right at head_right
    with qd

    "Ione was Sefa's mother, and the hold's healer."
    "She was a broad calm woman with her sleeves rolled, and her forearms were ridged from wrist to elbow with old shiny scars, as though she had once put both arms into a fire."
    "She did not explain them."
    scene cg healing
    with dissolve
    "She filled a shallow bowl from the sea-door and set it on the floor between them."
    "Then she held her hands over it without touching it, and went very still."

    "Wrack felt the room change. It was the way a room changes when someone starts to sing quietly in the corner."

    scene bg dry_room
    with dissolve
    show p wrack_puzzled as left at head_left
    show p sefa_sharp as right at head_right
    with qd
    c_sefa "She's intending it,"
    "Sefa told him, low."
    c_sefa "Watch. This is the gift."

    show p wrack_bewildered as left at head_left
    with qd
    c_wrack "What gift?"

    show p sefa_proud as right at head_right
    with qd
    c_sefa "{i}The{/i} gift."
    show p sefa_thoughtful as right at head_right
    with qd
    "She seemed at a loss as to where to begin."
    c_sefa "The sea answers some of us. Not many, one in ten maybe. You ask it for something, and if you've asked properly, it does it. There are two ways of asking."
    c_sefa "Mother's way is to ask it to care about someone. That's intending, and the water you've asked is intended water. It mends things. Cuts, fevers, bones if you're good."
    show p sefa_wary as right at head_right
    with qd
    "She hesitated."
    c_sefa "I can do cuts. The other way is calling, when you ask it to move. I can't do that at all. Hold still. It doesn't hurt."

    scene cg healing
    with dissolve
    "Ione lifted the water out of the bowl in her two hands. It held its shape, a little, as water should not. She laid it on his head."

    "It was warm, and it went on being warm inside his skull. It moved gently from place to place, like someone walking through a house and trying the doors."

    "After a long time she took her hands away."

    scene bg dry_room
    with dissolve
    show p wrack_puzzled as left at head_left
    show p ione_calm as right at head_right
    with qd
    c_ione "There's nothing broken,"
    "she told Elder Oro."
    c_ione "No blow, no fever, no poison. The memory isn't damaged."
    show p ione_cautious as right at head_right
    show p wrack_pained as left at head_left
    with qd
    "She looked at Wrack with something he did not like to see in a healer's face, which was caution."
    c_ione "It's gone. Taken, clean, all in one piece. I've seen it once before, in a caller from Deep Chorus who reached too far in a storm."
    show p ione_grave as right at head_right
    with qd
    c_ione "She came back not knowing her own children."

    show p oro_grave as right at head_right
    with qd
    c_oro "The undertow,"

    show p ione_grave as right at head_right
    with qd
    c_ione "The undertow."
    "Ione dried her hands on her tunic. She spoke to Wrack now, plainly, as healers speak to the people they have bad news for."
    c_ione "The sea gives when it's asked. But if you ask for more than you can carry, or if you let go of yourself altogether, it takes something back."
    show p ione_cautious as right at head_right
    with qd
    c_ione "A sense, a year of your life, a piece of your mind. It takes it whole and it keeps it. That's been done to you. I can't undo it. I don't know anyone who can."
    "She paused."
    show p ione_gentle as right at head_right
    with qd
    c_ione "But I'll say this to the elders. The undertow only takes from people who have the gift. So whatever else he is, he isn't an agravar. No agravar has ever been answered."
    c_ione "And whatever he did out there, he did it with everything he had."

    hide left
    hide right
    hide bother
    with qd
    "That decided it, more or less. A mariner the sea had marked was the sea's business."
    "They gave him a tunic of the grey-green cloth, which was called sea-silk and weighed nothing."
    "They gave him a hammock in the long dry hall where the unmarried men slept, a hook, and a row of terrace to work."

    # c01.s04
    scene bg terrace_work
    with fade
    "He was bad at it."

    "He cut the fronds too low and bled the stems."
    show p bother_aggrieved as bother at bother_corner
    with qd
    "He let a whole net of silverbacks out through a gate because he could not tell which way it latched, and Bother had to round them up, with a great deal of noise and an air of personal grievance."
    hide bother
    with qd
    "A net-mender named Davin, a quiet, big-handed man with a slow smile, came and showed him the latch three times, and did not seem to mind showing him a fourth."
    show p wrack_tunic_troubled as left at head_left
    show p davin_patient as right at head_right
    with qd
    c_davin "Up and across,"
    show p davin_amused as right at head_right
    show p wrack_tunic_faint_smile as left at head_left
    with qd
    c_davin "Everything in this hold is up and across. The Makers were all left-handed, my wife says."
    show p hesper_stern as right at head_right
    with qd
    "His wife was called Hesper. Wrack had seen her only at a distance, a lean hard woman whom people made room for."
    "She was the hold's Tidecaller, Davin said, with a pride he did not try to hide."
    "She was the only one for two hundred kilometres who could ask the sea to move and have it do so."

    scene bg sea_door
    with dissolve

    "He learned the shape of the days. They were short, and the hold kept them by song."
    "A singer stood at the sea-door and sang the turn of each watch, and the terraces picked it up and passed it out into the forest, so that the hour travelled outward through the kelp like a ripple."
    "Work was done in the water. Eating, sleeping and argument were done in the dry halls, where a fire would burn and a voice did not carry to every ear in the hold."

    scene bg dome_dark_half
    with dissolve
    "In the evenings the lamps on the lit side of the dome dimmed of their own accord, slowly, as they had every evening for three thousand years."
    "The dark side had only its strings of glowing weed."

    show p wrack_tunic_lost as left at head_left
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "Lampweed,"
    c_sefa "It grows up north. You hang it where the lamps have failed."
    show p sefa_amused as right at head_right
    with qd
    c_sefa "The old people say you can tell how a hold is doing by counting its lampweed, and then they say we shouldn't count ours."
    "She was showing him how to strip a frond."
    show p sefa_thoughtful as right at head_right
    with qd
    c_sefa "Mother says in her mother's time there were six more lamps. One goes every ten years or so. They just don't come on one evening."
    c_sefa "Then everyone goes and stands under it for a bit, and somebody brings the weed."

    show p wrack_tunic_troubled as left at head_left
    with qd
    c_wrack "And nobody can mend them."

    show p sefa_wary as right at head_right
    with qd
    c_sefa "Jef could. He'd have to come, though, and he's only one, and there are three hundred holds."
    "She saw his face."
    show p sefa_amused as right at head_right
    show p wrack_tunic_lost as left at head_left
    with qd
    c_sefa "You don't know who Jef is either."

    hide left
    hide right
    hide bother
    with qd
    scene bg long_dry_hall
    with fade
    show p wrack_tunic_attentive as left at head_left
    with qd
    "He heard about Jef from the night crew, lying in his hammock in the dark hall with the others talking round him. He gathered it in pieces."
    "Jef lived at the top of the world. Jef was older than the oldest song. He had been alive at the Hold Wars, nine hundred years ago."
    "When an air-heart failed in some great hold and the dry halls began to go stale, they sent to Jef, and if they were lucky he came, a small old man with a bag of tools."
    "He laid his hands on the thing and it worked again. He was the only one in the world who could do it. Some of the night crew spoke of him as of a clever uncle."

    scene cg c1_night_crew
    with dissolve
    "More of them spoke of him as a god, and one old woman made a small sign with her fingers whenever his name was said."

    "\"He rides the Dragon,\" a boy said, from somewhere down the hall."

    "\"Everybody rides the Dragon who can get on it.\""

    "\"He tells it who to let in, though.\""

    scene bg long_dry_hall
    with dissolve
    show p wrack_tunic_attentive as left at head_left
    with qd
    "The Dragon, Wrack learned, went round the world from top to bottom and never stopped. It was a kilometre long, and it sang."
    show p davin_neutral as right at head_right
    with qd
    "It came by the nearest calling stone about once a season, if the almanac was right. Davin had seen it once, as a boy, from a long way off."
    "He said that it had looked like a river that had got loose from its bed, and that he had dreamed about it for a year."

    hide right
    show p wrack_tunic_thinking as left at head_left
    with qd

    "\"And the Threaded,\" said the boy. \"Tell him about the Threaded.\""

    "\"Jef's monks,\" someone said. \"He puts a thread in their heads and they can ride the old machines. They keep the islanders out of our water."
    "There's one keeps these waters, a woman. She came through when I was small. Went past the terrace like a thrown knife.\""

    "\"There's not enough of them,\" the old woman said. \"There never was, and there's fewer now.\""

    show p wrack_tunic_troubled as left at head_left
    with qd
    "\"And one went up,\" said the boy. \"My uncle says so. One of the Threaded went up to the islands, before anybody here was born, and never came down again.\""

    "\"Your uncle says a great deal,\" said the old woman. But she made the sign with her fingers a second time, and it was not for Jef."

    "They taught him the tending song, the slow one for work that is never finished. He got the words wrong and they laughed at him, not unkindly. He liked them."
    show p bother_pleased as bother at bother_corner
    with qd
    "He liked the chord of the forest and the green-gold light, and the salt burst of the sea-grapes, and the weight of Bother's chin on his foot."
    hide bother
    with qd
    "He lay at night with his hands folded on his chest and tried not to feel the thing under the blank."

    scene bg meeting_hall
    with fade
    "On the ninth day he walked through the meeting hall on his way to the terraces."

    scene cg lamp_seam
    with dissolve
    "It was the heart of the dome, a round high room where the whole hold could sit. At its centre stood a Maker lamp. It had been dark since Sefa's grandmother was a child."
    "People touched it as they passed, for luck, so that at shoulder height it was polished to a shine. It was dusted every morning and sung to at every festival."
    "A wreath of fresh weed hung on it. Nobody had the least idea how it worked."

    scene bg meeting_hall
    with dissolve
    show p wrack_tunic_lost as left at head_left
    with qd
    "His hands reached up on their own."

    scene cg lamp_seam
    with dissolve
    "He did not decide to. He was looking at the wreath, and thinking of nothing, and his fingers found a seam that no one had ever seen, and opened it."
    "Inside was a shape he could not have named. He knew that it was wrong, as you know a word is misspelled before you can say how. It was seated badly."
    "It was clogged, and tired. He moved three things. He closed the seam."

    scene cg lamp_on
    with dissolve
    "The lamp came on."

    "Light poured down the hall, white and steady. People stopped where they stood. A child shrieked."
    "Someone dropped a basket, and the shellfish rolled across the floor in the first clear light that room had seen in three generations."

    "Elder Oro had been crossing the hall with his stick. He stood looking up at the lamp. Then he sat down on the floor, quite slowly, and began to cry."

    scene bg meeting_hall_lit
    with dissolve
    show p wrack_tunic_lost as left at head_left
    show p sefa_amazed as right at head_right
    with qd
    c_sefa "How did you do that?"
    "Sefa whispered."

    show p wrack_tunic_frightened as left at head_left
    with qd
    c_wrack "I don't know,"
    hide left
    hide right
    hide bother
    with qd
    "It was the truth, and it frightened him more than the breathing had."

    "Nobody in Low Anthem had ever seen a Maker thing repaired. Nobody in any hold had, for six hundred years, except by one pair of hands."
    "Those hands belonged to an old man at the top of the world, and half the people in the hall believed he was a god."

    "Elder Oro wiped his face with the heel of his hand."

    show p wrack_tunic_troubled as left at head_left
    show p oro_weeping as right at head_right
    with qd
    c_oro "Somebody,"
    show p oro_grave as right at head_right
    with qd
    c_oro "had better send word north."

    jump ch02
