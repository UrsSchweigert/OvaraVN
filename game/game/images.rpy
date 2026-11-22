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

image p wrack_bewildered = At("p_wrack_bewildered.png", lit_portrait)
image p wrack_blank = At("p_wrack_blank.png", lit_portrait)
image p wrack_pained = At("p_wrack_pained.png", lit_portrait)
image p wrack_puzzled = At("p_wrack_puzzled.png", lit_portrait)
image p wrack_tunic_troubled = At("p_wrack_tunic_troubled.png", lit_portrait)
image p wrack_tunic_lost = At("p_wrack_tunic_lost.png", lit_portrait)
image p wrack_tunic_frightened = At("p_wrack_tunic_frightened.png", lit_portrait)
image p wrack_tunic_faint_smile = At("p_wrack_tunic_faint_smile.png", lit_portrait)
image p sefa_wary = At("p_sefa_wary.png", lit_portrait)
image p sefa_sharp = At("p_sefa_sharp.png", lit_portrait)
image p sefa_proud = At("p_sefa_proud.png", lit_portrait)
image p sefa_thoughtful = At("p_sefa_thoughtful.png", lit_portrait)
image p sefa_amazed = At("p_sefa_amazed.png", lit_portrait)
image p sefa_amused = At("p_sefa_amused.png", lit_portrait)
image p oro_gentle = At("p_oro_gentle.png", lit_portrait)
image p oro_grave = At("p_oro_grave.png", lit_portrait)
image p oro_weeping = At("p_oro_weeping.png", lit_portrait)
image p oro_thoughtful = At("p_oro_thoughtful.png", lit_portrait)
image p ione_calm = At("p_ione_calm.png", lit_portrait)
image p ione_grave = At("p_ione_grave.png", lit_portrait)
image p ione_concentrating = At("p_ione_concentrating.png", lit_portrait)
image p ione_cautious = At("p_ione_cautious.png", lit_portrait)
image p ione_gentle = At("p_ione_gentle.png", lit_portrait)
image p davin_smile = At("p_davin_smile.png", lit_portrait)
image p davin_neutral = At("p_davin_neutral.png", lit_portrait)
image p davin_patient = At("p_davin_patient.png", lit_portrait)
image p davin_amused = At("p_davin_amused.png", lit_portrait)
image p bother_pleased = At("p_bother_pleased.png", lit_portrait)
image p bother_alert = At("p_bother_alert.png", lit_portrait)
image p bother_aggrieved = At("p_bother_aggrieved.png", lit_portrait)

# Full-screen illustrations (1920x1080) for narrated passages.
image cg wake = "cg/wake.png"
image cg swim = "cg/swim.png"
image cg sea_door = "cg/sea_door.png"
image cg healing = "cg/healing.png"
image cg lamp_seam = "cg/lamp_seam.png"
image cg lamp_on = "cg/lamp_on.png"
