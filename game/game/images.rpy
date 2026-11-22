# Chapter 1 art. Backgrounds are 1920x1088 on disk; scaled to the 1920x1080 screen.
# Portraits are transparent head-and-shoulders, 1024x1024, drawn facing the viewer's
# right. ch01.rpy puts Wrack on the left as drawn and flips the other speaker.

image bg dry_room = Transform("bg/dry_room.png", size=(1920, 1080))
image bg kelp_forest = At(Transform("bg/kelp_forest.png", size=(1920, 1080)), water)
image bg meeting_hall = Transform("bg/meeting_hall.png", size=(1920, 1080))
image bg terraces_dome = At(Transform("bg/terraces_dome.png", size=(1920, 1080)), water)
image bg sea_door = At(Transform("bg/sea_door.png", size=(1920, 1080)), water_soft)
image bg terrace_work = At(Transform("bg/terrace_work.png", size=(1920, 1080)), water)
image bg long_dry_hall = Transform("bg/long_dry_hall.png", size=(1920, 1080))

image p wrack_bewildered = "p_wrack_bewildered.png"
image p wrack_blank = "p_wrack_blank.png"
image p wrack_pained = "p_wrack_pained.png"
image p wrack_puzzled = "p_wrack_puzzled.png"
image p wrack_tunic_troubled = "p_wrack_tunic_troubled.png"
image p wrack_tunic_lost = "p_wrack_tunic_lost.png"
image p wrack_tunic_frightened = "p_wrack_tunic_frightened.png"
image p wrack_tunic_faint_smile = "p_wrack_tunic_faint_smile.png"
image p sefa_wary = "p_sefa_wary.png"
image p sefa_sharp = "p_sefa_sharp.png"
image p sefa_proud = "p_sefa_proud.png"
image p sefa_thoughtful = "p_sefa_thoughtful.png"
image p sefa_amazed = "p_sefa_amazed.png"
image p sefa_amused = "p_sefa_amused.png"
image p oro_gentle = "p_oro_gentle.png"
image p oro_grave = "p_oro_grave.png"
image p oro_weeping = "p_oro_weeping.png"
image p oro_thoughtful = "p_oro_thoughtful.png"
image p ione_calm = "p_ione_calm.png"
image p ione_grave = "p_ione_grave.png"
image p ione_concentrating = "p_ione_concentrating.png"
image p ione_cautious = "p_ione_cautious.png"
image p ione_gentle = "p_ione_gentle.png"
image p davin_smile = "p_davin_smile.png"
image p davin_neutral = "p_davin_neutral.png"
image p davin_patient = "p_davin_patient.png"
image p davin_amused = "p_davin_amused.png"
image p bother_pleased = "p_bother_pleased.png"
image p bother_alert = "p_bother_alert.png"
image p bother_aggrieved = "p_bother_aggrieved.png"
