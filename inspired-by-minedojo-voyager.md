Directory structure:
└── minedojo-voyager/
    ├── README.md
    ├── FAQ.md
    ├── LICENSE
    ├── requirements.txt
    ├── setup.py
    ├── installation/
    │   ├── fabric_mods_install.md
    │   └── minecraft_instance_install.md
    ├── skill_library/
    │   ├── README.md
    │   ├── trial1/
    │   │   └── skill/
    │   │       ├── skills.json
    │   │       ├── code/
    │   │       │   ├── collectBamboo.js
    │   │       │   ├── collectFiveCactusBlocks.js
    │   │       │   ├── cookPorkchops.js
    │   │       │   ├── cookSevenMutton.js
    │   │       │   ├── craftAcaciaPlanksAndSticks.js
    │   │       │   ├── craftBucket.js
    │   │       │   ├── craftChest.js
    │   │       │   ├── craftCopperBlock.js
    │   │       │   ├── craftCraftingTable.js
    │   │       │   ├── craftFurnace.js
    │   │       │   ├── craftIronAxe.js
    │   │       │   ├── craftIronChestplate.js
    │   │       │   ├── craftIronHelmet.js
    │   │       │   ├── craftIronHelmetV2.js
    │   │       │   ├── craftIronLeggingsAndBoots.js
    │   │       │   ├── craftIronPickaxe.js
    │   │       │   ├── craftIronPickaxeV2.js
    │   │       │   ├── craftIronShovel.js
    │   │       │   ├── craftIronSword.js
    │   │       │   ├── craftLightningRod.js
    │   │       │   ├── craftOakPlanksAndSticks.js
    │   │       │   ├── craftScaffolding.js
    │   │       │   ├── craftShears.js
    │   │       │   ├── craftShieldImproved.js
    │   │       │   ├── craftStonePickaxe.js
    │   │       │   ├── craftStoneShovel.js
    │   │       │   ├── craftWhiteBed.js
    │   │       │   ├── craftWoodenHoe.js
    │   │       │   ├── craftWoodenPickaxe.js
    │   │       │   ├── craftWoodenSword.js
    │   │       │   ├── eatCookedPorkchop.js
    │   │       │   ├── eatTwoCookedMutton.js
    │   │       │   ├── equipIronArmor.js
    │   │       │   ├── equipIronChestplate.js
    │   │       │   ├── equipIronSword.js
    │   │       │   ├── fillBucketWithWater.js
    │   │       │   ├── killFourSheep.js
    │   │       │   ├── killOneEnderman.js
    │   │       │   ├── killOnePig.js
    │   │       │   ├── killOneSpider.js
    │   │       │   ├── killOneZombie.js
    │   │       │   ├── killTwoPigs.js
    │   │       │   ├── mineFiveCoalOres.js
    │   │       │   ├── mineFiveCoalOresV2.js
    │   │       │   ├── mineFiveCopperOres.js
    │   │       │   ├── mineFiveCopperOresV2.js
    │   │       │   ├── mineFiveIronOres.js
    │   │       │   ├── mineFiveIronOresV2.js
    │   │       │   ├── mineFiveLapisLazuliOres.js
    │   │       │   ├── mineTenCobblestone.js
    │   │       │   ├── mineThreeMoreOakLogs.js
    │   │       │   ├── mineWoodLog.js
    │   │       │   ├── obtainOneMoreAcaciaLog.js
    │   │       │   ├── smeltCactusIntoGreenDye.js
    │   │       │   ├── smeltFiveRawIron.js
    │   │       │   ├── smeltFiveRawIronV2.js
    │   │       │   └── smeltRawCopper.js
    │   │       ├── description/
    │   │       │   ├── collectBamboo.txt
    │   │       │   ├── collectFiveCactusBlocks.txt
    │   │       │   ├── cookPorkchops.txt
    │   │       │   ├── cookSevenMutton.txt
    │   │       │   ├── craftAcaciaPlanksAndSticks.txt
    │   │       │   ├── craftBucket.txt
    │   │       │   ├── craftChest.txt
    │   │       │   ├── craftCopperBlock.txt
    │   │       │   ├── craftCraftingTable.txt
    │   │       │   ├── craftFurnace.txt
    │   │       │   ├── craftIronAxe.txt
    │   │       │   ├── craftIronChestplate.txt
    │   │       │   ├── craftIronHelmet.txt
    │   │       │   ├── craftIronHelmetV2.txt
    │   │       │   ├── craftIronLeggingsAndBoots.txt
    │   │       │   ├── craftIronPickaxe.txt
    │   │       │   ├── craftIronPickaxeV2.txt
    │   │       │   ├── craftIronShovel.txt
    │   │       │   ├── craftIronSword.txt
    │   │       │   ├── craftLightningRod.txt
    │   │       │   ├── craftOakPlanksAndSticks.txt
    │   │       │   ├── craftScaffolding.txt
    │   │       │   ├── craftShears.txt
    │   │       │   ├── craftShieldImproved.txt
    │   │       │   ├── craftStonePickaxe.txt
    │   │       │   ├── craftStoneShovel.txt
    │   │       │   ├── craftWhiteBed.txt
    │   │       │   ├── craftWoodenHoe.txt
    │   │       │   ├── craftWoodenPickaxe.txt
    │   │       │   ├── craftWoodenSword.txt
    │   │       │   ├── eatCookedPorkchop.txt
    │   │       │   ├── eatTwoCookedMutton.txt
    │   │       │   ├── equipIronArmor.txt
    │   │       │   ├── equipIronChestplate.txt
    │   │       │   ├── equipIronSword.txt
    │   │       │   ├── fillBucketWithWater.txt
    │   │       │   ├── killFourSheep.txt
    │   │       │   ├── killOneEnderman.txt
    │   │       │   ├── killOnePig.txt
    │   │       │   ├── killOneSpider.txt
    │   │       │   ├── killOneZombie.txt
    │   │       │   ├── killTwoPigs.txt
    │   │       │   ├── mineFiveCoalOres.txt
    │   │       │   ├── mineFiveCoalOresV2.txt
    │   │       │   ├── mineFiveCopperOres.txt
    │   │       │   ├── mineFiveCopperOresV2.txt
    │   │       │   ├── mineFiveIronOres.txt
    │   │       │   ├── mineFiveIronOresV2.txt
    │   │       │   ├── mineFiveLapisLazuliOres.txt
    │   │       │   ├── mineTenCobblestone.txt
    │   │       │   ├── mineThreeMoreOakLogs.txt
    │   │       │   ├── mineWoodLog.txt
    │   │       │   ├── obtainOneMoreAcaciaLog.txt
    │   │       │   ├── smeltCactusIntoGreenDye.txt
    │   │       │   ├── smeltFiveRawIron.txt
    │   │       │   ├── smeltFiveRawIronV2.txt
    │   │       │   └── smeltRawCopper.txt
    │   │       └── vectordb/
    │   │           ├── chroma-collections.parquet
    │   │           ├── chroma-embeddings.parquet
    │   │           └── index/
    │   │               ├── id_to_uuid_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
    │   │               ├── index_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.bin
    │   │               ├── index_metadata_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
    │   │               └── uuid_to_id_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
    │   ├── trial2/
    │   │   └── skill/
    │   │       ├── skills.json
    │   │       ├── code/
    │   │       │   ├── catchFiveFishSafely.js
    │   │       │   ├── catchThreeFish.js
    │   │       │   ├── checkStonePickaxe.js
    │   │       │   ├── chopDownSpruceLogs.js
    │   │       │   ├── chopDownSpruceLogsV2.js
    │   │       │   ├── chopSpruceLogs.js
    │   │       │   ├── collectWaterWithBucket.js
    │   │       │   ├── cookMutton.js
    │   │       │   ├── craftBucket.js
    │   │       │   ├── craftChest.js
    │   │       │   ├── craftEightSticks.js
    │   │       │   ├── craftEightTorches.js
    │   │       │   ├── craftFishingRod.js
    │   │       │   ├── craftFurnace.js
    │   │       │   ├── craftIronChestplate.js
    │   │       │   ├── craftIronHelmet.js
    │   │       │   ├── craftIronLeggingsAndBoots.js
    │   │       │   ├── craftIronPickaxe.js
    │   │       │   ├── craftIronPickaxeWithMaterials.js
    │   │       │   ├── craftIronSword.js
    │   │       │   ├── craftShieldWithFurnace.js
    │   │       │   ├── craftSixteenTorches.js
    │   │       │   ├── craftSpyglass.js
    │   │       │   ├── craftSticks.js
    │   │       │   ├── craftStoneAxe.js
    │   │       │   ├── craftStoneHoe.js
    │   │       │   ├── craftStonePickaxe.js
    │   │       │   ├── craftStoneShovel.js
    │   │       │   ├── craftStoneSword.js
    │   │       │   ├── craftTorches.js
    │   │       │   ├── craftTwentySprucePlanks.js
    │   │       │   ├── craftWhiteBedWithExploration.js
    │   │       │   ├── craftWoodenHoe.js
    │   │       │   ├── craftWoodenPickaxe.js
    │   │       │   ├── craftWoodenPlanks.js
    │   │       │   ├── eatCookedMutton.js
    │   │       │   ├── eatCookedMuttonV2.js
    │   │       │   ├── eatCookedMuttonV3.js
    │   │       │   ├── equipIronArmor.js
    │   │       │   ├── exploreCave.js
    │   │       │   ├── exploreCaveAndGatherResources.js
    │   │       │   ├── exploreCaveAndGatherResourcesV2.js
    │   │       │   ├── fishInNearbyWaterSafely.js
    │   │       │   ├── mineCoalOre.js
    │   │       │   ├── mineCopperOreWithStonePickaxe.js
    │   │       │   ├── mineFiveCoalOres.js
    │   │       │   ├── mineFiveCoalOresV2.js
    │   │       │   ├── mineFiveCopperOres.js
    │   │       │   ├── mineFiveIronOres.js
    │   │       │   ├── mineLapisOre.js
    │   │       │   ├── mineThreeIronOres.js
    │   │       │   ├── mineWoodLog.js
    │   │       │   ├── smeltOneRawIron.js
    │   │       │   ├── smeltRawCopper.js
    │   │       │   ├── smeltRawIron.js
    │   │       │   ├── smeltSixRawIron.js
    │   │       │   └── smeltTwentyFiveIronIngots.js
    │   │       ├── description/
    │   │       │   ├── catchFiveFishSafely.txt
    │   │       │   ├── catchThreeFish.txt
    │   │       │   ├── checkStonePickaxe.txt
    │   │       │   ├── chopDownSpruceLogs.txt
    │   │       │   ├── chopDownSpruceLogsV2.txt
    │   │       │   ├── chopSpruceLogs.txt
    │   │       │   ├── collectWaterWithBucket.txt
    │   │       │   ├── cookMutton.txt
    │   │       │   ├── craftBucket.txt
    │   │       │   ├── craftChest.txt
    │   │       │   ├── craftEightSticks.txt
    │   │       │   ├── craftEightTorches.txt
    │   │       │   ├── craftFishingRod.txt
    │   │       │   ├── craftFurnace.txt
    │   │       │   ├── craftIronChestplate.txt
    │   │       │   ├── craftIronHelmet.txt
    │   │       │   ├── craftIronLeggingsAndBoots.txt
    │   │       │   ├── craftIronPickaxe.txt
    │   │       │   ├── craftIronPickaxeWithMaterials.txt
    │   │       │   ├── craftIronSword.txt
    │   │       │   ├── craftShieldWithFurnace.txt
    │   │       │   ├── craftSixteenTorches.txt
    │   │       │   ├── craftSpyglass.txt
    │   │       │   ├── craftSticks.txt
    │   │       │   ├── craftStoneAxe.txt
    │   │       │   ├── craftStoneHoe.txt
    │   │       │   ├── craftStonePickaxe.txt
    │   │       │   ├── craftStoneShovel.txt
    │   │       │   ├── craftStoneSword.txt
    │   │       │   ├── craftTorches.txt
    │   │       │   ├── craftTwentySprucePlanks.txt
    │   │       │   ├── craftWhiteBedWithExploration.txt
    │   │       │   ├── craftWoodenHoe.txt
    │   │       │   ├── craftWoodenPickaxe.txt
    │   │       │   ├── craftWoodenPlanks.txt
    │   │       │   ├── eatCookedMutton.txt
    │   │       │   ├── eatCookedMuttonV2.txt
    │   │       │   ├── eatCookedMuttonV3.txt
    │   │       │   ├── equipIronArmor.txt
    │   │       │   ├── exploreCave.txt
    │   │       │   ├── exploreCaveAndGatherResources.txt
    │   │       │   ├── exploreCaveAndGatherResourcesV2.txt
    │   │       │   ├── fishInNearbyWaterSafely.txt
    │   │       │   ├── mineCoalOre.txt
    │   │       │   ├── mineCopperOreWithStonePickaxe.txt
    │   │       │   ├── mineFiveCoalOres.txt
    │   │       │   ├── mineFiveCoalOresV2.txt
    │   │       │   ├── mineFiveCopperOres.txt
    │   │       │   ├── mineFiveIronOres.txt
    │   │       │   ├── mineLapisOre.txt
    │   │       │   ├── mineThreeIronOres.txt
    │   │       │   ├── mineWoodLog.txt
    │   │       │   ├── smeltOneRawIron.txt
    │   │       │   ├── smeltRawCopper.txt
    │   │       │   ├── smeltRawIron.txt
    │   │       │   ├── smeltSixRawIron.txt
    │   │       │   └── smeltTwentyFiveIronIngots.txt
    │   │       └── vectordb/
    │   │           ├── chroma-collections.parquet
    │   │           ├── chroma-embeddings.parquet
    │   │           └── index/
    │   │               ├── id_to_uuid_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
    │   │               ├── index_7b5fd116-0820-46cb-981a-a6d642d4f025.bin
    │   │               ├── index_metadata_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
    │   │               └── uuid_to_id_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
    │   └── trial3/
    │       └── skill/
    │           ├── skills.json
    │           ├── code/
    │           │   ├── cookChicken.js
    │           │   ├── cookRawBeef.js
    │           │   ├── cookRawMutton.js
    │           │   ├── cookThreeRawChicken.js
    │           │   ├── craftBirchBoat.js
    │           │   ├── craftBoneMeal.js
    │           │   ├── craftChest.js
    │           │   ├── craftClock.js
    │           │   ├── craftCopperBlock.js
    │           │   ├── craftDiamondSword.js
    │           │   ├── craftFurnace.js
    │           │   ├── craftIronChestplate.js
    │           │   ├── craftIronHelmet.js
    │           │   ├── craftIronLeggingsAndBoots.js
    │           │   ├── craftIronPickaxe.js
    │           │   ├── craftIronSword.js
    │           │   ├── craftShield.js
    │           │   ├── craftStoneAxe.js
    │           │   ├── craftStoneHoe.js
    │           │   ├── craftStoneHoeV2.js
    │           │   ├── craftStonePickaxe.js
    │           │   ├── craftStoneShovel.js
    │           │   ├── craftStoneSword.js
    │           │   ├── craftStoneTools.js
    │           │   ├── craftTenCobblestoneWalls.js
    │           │   ├── craftWoodenPickaxe.js
    │           │   ├── craftWoodenSword.js
    │           │   ├── eatCookedBeef.js
    │           │   ├── eatCookedBeefV2.js
    │           │   ├── eatCookedBeefV3.js
    │           │   ├── eatCookedMutton.js
    │           │   ├── eatCookedMuttonIfHungry.js
    │           │   ├── equipIronChestplate.js
    │           │   ├── equipIronHelmet.js
    │           │   ├── equipIronLeggingsAndBoots.js
    │           │   ├── equipShield.js
    │           │   ├── killChickenWithIncreasedTime.js
    │           │   ├── killThreeChickens.js
    │           │   ├── killThreeCows.js
    │           │   ├── killThreeSheep.js
    │           │   ├── mineDeepslateOres.js
    │           │   ├── mineEightCobblestone.js
    │           │   ├── mineFiveCoalOre.js
    │           │   ├── mineFiveCopperOre.js
    │           │   ├── mineFourCoalOre.js
    │           │   ├── mineTenCobbledDeepslateBelowY0.js
    │           │   ├── mineThreeIronOre.js
    │           │   ├── mineThreeMoreOakLogs.js
    │           │   ├── mineWoodLog.js
    │           │   ├── obtainBirchLogs.js
    │           │   ├── openChestAndCheckContents.js
    │           │   ├── plantOakSapling.js
    │           │   ├── smeltCopperOre.js
    │           │   ├── smeltFiveRawCopper.js
    │           │   ├── smeltFiveRawGold.js
    │           │   ├── smeltRawIron.js
    │           │   ├── smeltThreeRawCopper.js
    │           │   └── waitAndEatCookedMutton.js
    │           ├── description/
    │           │   ├── cookChicken.txt
    │           │   ├── cookRawBeef.txt
    │           │   ├── cookRawMutton.txt
    │           │   ├── cookThreeRawChicken.txt
    │           │   ├── craftBirchBoat.txt
    │           │   ├── craftBoneMeal.txt
    │           │   ├── craftChest.txt
    │           │   ├── craftClock.txt
    │           │   ├── craftCopperBlock.txt
    │           │   ├── craftDiamondSword.txt
    │           │   ├── craftFurnace.txt
    │           │   ├── craftIronChestplate.txt
    │           │   ├── craftIronHelmet.txt
    │           │   ├── craftIronLeggingsAndBoots.txt
    │           │   ├── craftIronPickaxe.txt
    │           │   ├── craftIronSword.txt
    │           │   ├── craftShield.txt
    │           │   ├── craftStoneAxe.txt
    │           │   ├── craftStoneHoe.txt
    │           │   ├── craftStoneHoeV2.txt
    │           │   ├── craftStonePickaxe.txt
    │           │   ├── craftStoneShovel.txt
    │           │   ├── craftStoneSword.txt
    │           │   ├── craftStoneTools.txt
    │           │   ├── craftTenCobblestoneWalls.txt
    │           │   ├── craftWoodenPickaxe.txt
    │           │   ├── craftWoodenSword.txt
    │           │   ├── eatCookedBeef.txt
    │           │   ├── eatCookedBeefV2.txt
    │           │   ├── eatCookedBeefV3.txt
    │           │   ├── eatCookedMutton.txt
    │           │   ├── eatCookedMuttonIfHungry.txt
    │           │   ├── equipIronChestplate.txt
    │           │   ├── equipIronHelmet.txt
    │           │   ├── equipIronLeggingsAndBoots.txt
    │           │   ├── equipShield.txt
    │           │   ├── killChickenWithIncreasedTime.txt
    │           │   ├── killThreeChickens.txt
    │           │   ├── killThreeCows.txt
    │           │   ├── killThreeSheep.txt
    │           │   ├── mineDeepslateOres.txt
    │           │   ├── mineEightCobblestone.txt
    │           │   ├── mineFiveCoalOre.txt
    │           │   ├── mineFiveCopperOre.txt
    │           │   ├── mineFourCoalOre.txt
    │           │   ├── mineTenCobbledDeepslateBelowY0.txt
    │           │   ├── mineThreeIronOre.txt
    │           │   ├── mineThreeMoreOakLogs.txt
    │           │   ├── mineWoodLog.txt
    │           │   ├── obtainBirchLogs.txt
    │           │   ├── openChestAndCheckContents.txt
    │           │   ├── plantOakSapling.txt
    │           │   ├── smeltCopperOre.txt
    │           │   ├── smeltFiveRawCopper.txt
    │           │   ├── smeltFiveRawGold.txt
    │           │   ├── smeltRawIron.txt
    │           │   ├── smeltThreeRawCopper.txt
    │           │   └── waitAndEatCookedMutton.txt
    │           └── vectordb/
    │               ├── chroma-collections.parquet
    │               ├── chroma-embeddings.parquet
    │               └── index/
    │                   ├── id_to_uuid_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
    │                   ├── index_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.bin
    │                   ├── index_metadata_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
    │                   └── uuid_to_id_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
    ├── voyager/
    │   ├── __init__.py
    │   ├── voyager.py
    │   ├── agents/
    │   │   ├── __init__.py
    │   │   ├── action.py
    │   │   ├── critic.py
    │   │   ├── curriculum.py
    │   │   └── skill.py
    │   ├── control_primitives/
    │   │   ├── __init__.py
    │   │   ├── craftHelper.js
    │   │   ├── craftItem.js
    │   │   ├── exploreUntil.js
    │   │   ├── givePlacedItemBack.js
    │   │   ├── killMob.js
    │   │   ├── mineBlock.js
    │   │   ├── placeItem.js
    │   │   ├── shoot.js
    │   │   ├── smeltItem.js
    │   │   ├── useChest.js
    │   │   ├── waitForMobRemoved.js
    │   │   └── .prettierrc.json
    │   ├── control_primitives_context/
    │   │   ├── __init__.py
    │   │   ├── craftItem.js
    │   │   ├── exploreUntil.js
    │   │   ├── killMob.js
    │   │   ├── mineBlock.js
    │   │   ├── mineflayer.js
    │   │   ├── placeItem.js
    │   │   ├── smeltItem.js
    │   │   ├── useChest.js
    │   │   └── .prettierrc.json
    │   ├── env/
    │   │   ├── __init__.py
    │   │   ├── bridge.py
    │   │   ├── minecraft_launcher.py
    │   │   ├── process_monitor.py
    │   │   ├── .gitignore
    │   │   └── mineflayer/
    │   │       ├── index.js
    │   │       ├── package.json
    │   │       ├── .prettierignore
    │   │       ├── .prettierrc.json
    │   │       ├── lib/
    │   │       │   ├── skillLoader.js
    │   │       │   ├── utils.js
    │   │       │   └── observation/
    │   │       │       ├── base.js
    │   │       │       ├── chests.js
    │   │       │       ├── inventory.js
    │   │       │       ├── onChat.js
    │   │       │       ├── onError.js
    │   │       │       ├── onSave.js
    │   │       │       ├── status.js
    │   │       │       └── voxels.js
    │   │       └── mineflayer-collectblock/
    │   │           ├── README.md
    │   │           ├── _config.yml
    │   │           ├── LICENSE
    │   │           ├── package.json
    │   │           ├── tsconfig.json
    │   │           ├── .gitignore
    │   │           ├── docs/
    │   │           │   └── api.md
    │   │           ├── examples/
    │   │           │   ├── collector.js
    │   │           │   ├── oreMiner.js
    │   │           │   └── storageBot.js
    │   │           └── src/
    │   │               ├── BlockVeins.ts
    │   │               ├── CollectBlock.ts
    │   │               ├── index.ts
    │   │               ├── Inventory.ts
    │   │               ├── Targets.ts
    │   │               ├── TaskQueue.ts
    │   │               ├── TemporarySubscriber.ts
    │   │               └── Util.ts
    │   ├── prompts/
    │   │   ├── __init__.py
    │   │   ├── action_response_format.txt
    │   │   ├── action_template.txt
    │   │   ├── critic.txt
    │   │   ├── curriculum.txt
    │   │   ├── curriculum_qa_step1_ask_questions.txt
    │   │   ├── curriculum_qa_step2_answer_questions.txt
    │   │   ├── curriculum_task_decomposition.txt
    │   │   └── skill.txt
    │   └── utils/
    │       ├── __init__.py
    │       ├── file_utils.py
    │       ├── json_utils.py
    │       └── record_utils.py
    └── .github/
        ├── ISSUE_TEMPLATE/
        │   └── voyager-issue-template.md
        └── workflows/
            └── close_issue.yml

================================================
FILE: README.md
================================================
# Voyager: An Open-Ended Embodied Agent with Large Language Models
<div align="center">

[[Website]](https://voyager.minedojo.org/)
[[Arxiv]](https://arxiv.org/abs/2305.16291)
[[PDF]](https://voyager.minedojo.org/assets/documents/voyager.pdf)
[[Tweet]](https://twitter.com/DrJimFan/status/1662115266933972993?s=20)

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://github.com/MineDojo/Voyager)
[![GitHub license](https://img.shields.io/github/license/MineDojo/Voyager)](https://github.com/MineDojo/Voyager/blob/main/LICENSE)
______________________________________________________________________


https://github.com/MineDojo/Voyager/assets/25460983/ce29f45b-43a5-4399-8fd8-5dd105fd64f2

![](images/pull.png)


</div>

We introduce Voyager, the first LLM-powered embodied lifelong learning agent
in Minecraft that continuously explores the world, acquires diverse skills, and
makes novel discoveries without human intervention. Voyager consists of three
key components: 1) an automatic curriculum that maximizes exploration, 2) an
ever-growing skill library of executable code for storing and retrieving complex
behaviors, and 3) a new iterative prompting mechanism that incorporates environment
feedback, execution errors, and self-verification for program improvement.
Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for
model parameter fine-tuning. The skills developed by Voyager are temporally
extended, interpretable, and compositional, which compounds the agent’s abilities
rapidly and alleviates catastrophic forgetting. Empirically, Voyager shows
strong in-context lifelong learning capability and exhibits exceptional proficiency
in playing Minecraft. It obtains 3.3× more unique items, travels 2.3× longer
distances, and unlocks key tech tree milestones up to 15.3× faster than prior SOTA.
Voyager is able to utilize the learned skill library in a new Minecraft world to
solve novel tasks from scratch, while other techniques struggle to generalize.

In this repo, we provide Voyager code. This codebase is under [MIT License](LICENSE).

# Installation
Voyager requires Python ≥ 3.9 and Node.js ≥ 16.13.0. We have tested on Ubuntu 20.04, Windows 11, and macOS. You need to follow the instructions below to install Voyager.

## Python Install
```
git clone https://github.com/MineDojo/Voyager
cd Voyager
pip install -e .
```

## Node.js Install
In addition to the Python dependencies, you need to install the following Node.js packages:
```
cd voyager/env/mineflayer
npm install -g npx
npm install
cd mineflayer-collectblock
npx tsc
cd ..
npm install
```

## Minecraft Instance Install

Voyager depends on Minecraft game. You need to install Minecraft game and set up a Minecraft instance.

Follow the instructions in [Minecraft Login Tutorial](installation/minecraft_instance_install.md) to set up your Minecraft Instance.

## Fabric Mods Install

You need to install fabric mods to support all the features in Voyager. Remember to use the correct Fabric version of all the mods. 

Follow the instructions in [Fabric Mods Install](installation/fabric_mods_install.md) to install the mods.

# Getting Started
Voyager uses OpenAI's GPT-4 as the language model. You need to have an OpenAI API key to use Voyager. You can get one from [here](https://platform.openai.com/account/api-keys).

After the installation process, you can run Voyager by:
```python
from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
azure_login = {
    "client_id": "YOUR_CLIENT_ID",
    "redirect_url": "https://127.0.0.1/auth-response",
    "secret_value": "[OPTIONAL] YOUR_SECRET_VALUE",
    "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
}
openai_api_key = "YOUR_API_KEY"

voyager = Voyager(
    azure_login=azure_login,
    openai_api_key=openai_api_key,
)

# start lifelong learning
voyager.learn()
```

* If you are running with `Azure Login` for the first time, it will ask you to follow the command line instruction to generate a config file.
* For `Azure Login`, you also need to select the world and open the world to LAN by yourself. After you run `voyager.learn()` the game will pop up soon, you need to:
  1. Select `Singleplayer` and press `Create New World`.
  2. Set Game Mode to `Creative` and Difficulty to `Peaceful`.
  3. After the world is created, press `Esc` key and press `Open to LAN`.
  4. Select `Allow cheats: ON` and press `Start LAN World`. You will see the bot join the world soon. 

# Resume from a checkpoint during learning

If you stop the learning process and want to resume from a checkpoint later, you can instantiate Voyager by:
```python
from voyager import Voyager

voyager = Voyager(
    azure_login=azure_login,
    openai_api_key=openai_api_key,
    ckpt_dir="YOUR_CKPT_DIR",
    resume=True,
)
```

# Run Voyager for a specific task with a learned skill library

If you want to run Voyager for a specific task with a learned skill library, you should first pass the skill library directory to Voyager:
```python
from voyager import Voyager

# First instantiate Voyager with skill_library_dir.
voyager = Voyager(
    azure_login=azure_login,
    openai_api_key=openai_api_key,
    skill_library_dir="./skill_library/trial1", # Load a learned skill library.
    ckpt_dir="YOUR_CKPT_DIR", # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
    resume=False, # Do not resume from a skill library because this is not learning.
)
```
Then, you can run task decomposition. Notice: Occasionally, the task decomposition may not be logical. If you notice the printed sub-goals are flawed, you can rerun the decomposition.
```python
# Run task decomposition
task = "YOUR TASK" # e.g. "Craft a diamond pickaxe"
sub_goals = voyager.decompose_task(task=task)
```
Finally, you can run the sub-goals with the learned skill library:
```python
voyager.inference(sub_goals=sub_goals)
```

For all valid skill libraries, see [Learned Skill Libraries](skill_library/README.md).

# FAQ
If you have any questions, please check our [FAQ](FAQ.md) first before opening an issue.

# Paper and Citation

If you find our work useful, please consider citing us! 

```bibtex
@article{wang2023voyager,
  title   = {Voyager: An Open-Ended Embodied Agent with Large Language Models},
  author  = {Guanzhi Wang and Yuqi Xie and Yunfan Jiang and Ajay Mandlekar and Chaowei Xiao and Yuke Zhu and Linxi Fan and Anima Anandkumar},
  year    = {2023},
  journal = {arXiv preprint arXiv: Arxiv-2305.16291}
}
```

Disclaimer: This project is strictly for research purposes, and not an official product from NVIDIA.



================================================
FILE: FAQ.md
================================================
# Frequently Asked Questions
* [I got connection error after I click on the Azure login link and login to Microsoft account.](#i-got-a-connection-error-after-i-click-on-the-azure-login-link-and-login-to-my-microsoft-account)
* [I got `KeyError: 'access_token'` after I copied the link](#i-got-keyerror-accesstoken-after-i-copied-the-link)
* [I got `Subprocess Mineflayer failed to start` error.](#i-got-subprocess-mineflayer-failed-to-start-error)
* [I saw the bot left and rejoin the game after each task.](#i-saw-the-bot-left-and-rejoin-the-game-after-each-task)
* [How to show the bot's first-person perspective?](#how-to-show-the-bots-first-person-view)
* [Can I use GPT-3.5 instead of GPT-4?](#can-i-use-gpt-35-instead-of-gpt-4)
* [What's the estimated cost of running Voyager?](#whats-the-estimated-cost-of-running-voyager)

## I got a connection error after I click on the Azure login link and login to my Microsoft account.

It's normal that you get a connection refused or 404 error after you log in. You will still see the new URL in your browser. You just need to copy and paste that link. It should contain things like `code=M.C....` in that link.

## I got `KeyError: 'access_token'` after I copied the link

While testing Voyager, we use Redirect URI Type: `Public client/native (mobile & desktop)` in the app registration for Azure Login. However, according to the report in issue [#34](https://github.com/MineDojo/Voyager/issues/34#issuecomment-1567007133), the URI Type was changed to "Web" and it resolved the problem. Feel free to attempt both URI Types to determine which one works for you. If all the approaches fail, please refer to the original tutorial in [minecraft-launcher-lib](https://minecraft-launcher-lib.readthedocs.io/en/stable/tutorial/microsoft_login.html).

Update: This is probably a Microsoft's bug. See [issue #80 in minecraft-launcher-lib](https://codeberg.org/JakobDev/minecraft-launcher-lib/issues/80). If you cannot solve this problem, you can try to use the [Minecraft Official Launcher](./installation/minecraft_instance_install.md#option-2-minecraft-official-launcher) and use mc_port to run.
## I got `Subprocess Mineflayer failed to start` error.

There are many reasons that may cause this problem. You can try with following solutions:
1. Make sure you install nodejs and the dependency packages correctly. You can use the following command to check your installation:
    ```bash
    cd voyager/env/mineflayer
    node index.js
    ```
   If you see `Server started on port {PORT}`, then your installation is correct. You can kill the process by `Ctrl+C`.
2. Make sure you install Fabric correctly. You should be able to select the Fabric version in the Minecraft launcher. 
3. Each Mineflayer process can only listen to one port. If you want to start multiple instances of `Voyager`, you need to manually change the port when initialization:
    ```python
    from voyager import Voyager
    voyager = Voyager(
        server_port=3001, # default is 3000
        ...
    )
    ```
   
## I saw the bot left and rejoin the game after each task.

After completing each task, we'll reset the environment, which means the bot will exit and rejoin the game. This reset is necessary to synchronize Mineflayer with the Minecraft game. We do this because certain commands we utilize might result in lag on the Mineflayer side, causing the inventory stored in Mineflayer to differ from the actual inventory in the game. However, if you wish to avoid the reset, you can use `voyager.learn(reset_env=False)` and consider increasing the `env_wait_ticks` value. This will provide Mineflayer with additional time to sync with the Minecraft game.


## How to show the bot's first-person view?

Due to the Mineflayer's limitation, we currently can not directly get the bot's view in the game. Although there's a plugin called [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer), the video quality is not good enough, so we opt not to use it. Our demo video is generated by [replay-mod](https://www.replaymod.com/). We start the recording and let the bot play for hours, then come back to the recording and render the view from the bot.


## Can I use GPT-3.5 instead of GPT-4?

It's highly recommended to use GPT-4. GPT-3.5 falls behind in terms of code quality and reasoning ability compared to GPT-4. Moreover, GPT-3.5 has a limited context length, which means it may provide incomplete responses. If you insist on using GPT-3.5, it is essential to configure it with `skill_manager_retrieval_top_k` ≤ 2 to reduce the context length of the prompt.

## What's the estimated cost of running Voyager?

Using Voyager for approximately 160 iterations using GPT-4 will cost you around 50 USD. It's important to keep a close eye on your OpenAI API expenses and avoid unnecessary spending. Once Voyager begins running, it's recommended to monitor the bot's behavior for a period and ensure that it successfully completes some tasks.


================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2023 MineDojo Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: requirements.txt
================================================
tqdm
langchain
javascript
setuptools
openai
chardet
cchardet
chromadb==0.3.29
tiktoken
requests
setuptools
gymnasium
psutil
minecraft_launcher_lib



================================================
FILE: setup.py
================================================
import os
import pathlib
import pkg_resources
from setuptools import setup, find_packages


PKG_NAME = "voyager"
VERSION = "0.1"
EXTRAS = {}


def _read_file(fname):
    # this_dir = os.path.abspath(os.path.dirname(__file__))
    # with open(os.path.join(this_dir, fname)) as f:
    with pathlib.Path(fname).open(encoding="utf-8") as fp:
        return fp.read()


def _read_install_requires():
    with pathlib.Path("requirements.txt").open() as fp:
        return [
            str(requirement) for requirement in pkg_resources.parse_requirements(fp)
        ]


def _fill_extras(extras):
    if extras:
        extras["all"] = list(set([item for group in extras.values() for item in group]))
    return extras


setup(
    name=PKG_NAME,
    version=VERSION,
    author=f"MineDojo Team",
    url="https://github.com/MineDojo/Voyager",
    description="research project",
    long_description=_read_file("README.md"),
    long_description_content_type="text/markdown",
    keywords=[
        "Open-Ended Learning",
        "Lifelong Learning",
        "Embodied Agents",
        "Large Language Models",
    ],
    license="MIT License",
    packages=find_packages(include=f"{PKG_NAME}.*"),
    include_package_data=True,
    zip_safe=False,
    install_requires=_read_install_requires(),
    extras_require=_fill_extras(EXTRAS),
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
    ],
)



================================================
FILE: installation/fabric_mods_install.md
================================================
# Fabric Mods Install
In this tutorial, we will install the Fabric launcher and 5 mods. Remember to use the correct Fabric version that matches your game version (1.19) of all the mods. 
1. You can download the latest Fabric Installer from [here](https://fabricmc.net/use/installer/). For Windows users, just download the `.exe` file. For Mac or Ubuntu users, download the jar file and call `java -jar fabric-installer-0.11.2.jar` to install. Select game version to be `1.19` and loader version to be `0.14.18`. It will automatically detect your Minecraft game install location.
2. After installing Fabric, you will have a `YOUR_MINECRAFT_GAME_LOCATION/mods` folder. You need to put all the mods under this folder. Also, you will have a `YOUR_MINECRAFT_GAME_LOCATION/versions/fabric-loader-0.14.18-1.19`. This is the version you will run the game with. 
3. Here are 4 mods that can be directly downloaded to `YOUR_MINECRAFT_GAME_LOCATION/mods` folder: 
   * [Fabric API](https://modrinth.com/mod/fabric-api/version/0.58.0+1.19): Basic Fabric APIs.
   * [Mod Menu](https://cdn.modrinth.com/data/mOgUt4GM/versions/4.0.4/modmenu-4.0.4.jar): Used to manage all the mods that you download.
   * [Complete Config](https://www.curseforge.com/minecraft/mc-mods/completeconfig/download/3821056): Dependency of server pause.
   * [Multi Server Pause](https://www.curseforge.com/minecraft/mc-mods/multiplayer-server-pause-fabric/download/3822586): Used to pause the server when waiting for GPT-4 to reply.
4. For the last mod [Better Respawn](https://github.com/xieleo5/better-respawn/tree/1.19), you need to manually clone and compile.
   
   * After you clone the repo, remove the `'forge'` string in the last line of `settings.gradle`. Then run `gradlew build` to compile the mod. You will find the compiled jar file in `better-respawn/fabric/build/libs/better-respawn-fabric-1.19-2.0.0.jar`. Put the jar file to the mod folder.
     * You will need a Java Runtime Environment v17+ to build `better-respawn`. Some newer JRE versions will error during build. Find the JRE v17 archive [here](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html).
   * After you launch the game, go to `YOUR_MINECRAFT_GAME_LOCATION/config/better-respawn`, and modify the properties file with:
      ```
      respawn_block_range=32
      max_respawn_distance=32
      min_respawn_distance=0
      ```
5. Don't forget to change the `version` in `azure_login` to `fabric-loader-0.14.18-1.19` that you are using. You can find it under `YOUR_MINECRAFT_GAME_LOCATION/version` folder.

You can return to [README.md](../README.md#getting-started) and getting started now.



================================================
FILE: installation/minecraft_instance_install.md
================================================
# Minecraft Instance Install
To start using Voyager, you should first make sure to have an official [Minecraft](https://www.minecraft.net/) game (version 1.19) installed. 

There are two ways to start a Minecraft instance for Voyager. Sometimes GPT-4 will write an infinite loop that runs forever. In this case, there'll be a request timeout. Using Azure login can automatically resume the running if there's a request timeout.

## Option 1: Microsoft Azure Login (Recommended)
Using this method will allow Voyager to automatically resume when there's a request timeout. This is dependent on the [minecraft-launcher-lib](https://minecraft-launcher-lib.readthedocs.io/en/stable/tutorial/microsoft_login.html#let-the-user-log-in) library.

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Go to [Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview).
3. Click on the `App Registrations` tab on the left panel.
4. Click on the `New registration` button.
5. Fill the form with the following values:
    - Name: `YOUR_APP_NAME`
    - Supported account types: `Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts`
    - Redirect URI Type: `Public client/native (mobile & desktop)`, Value: `https://127.0.0.1/auth-response` (If you get `KeyError: 'access_token'` in the end, you can try to change the type to `Web`, see [FAQ](https://github.com/MineDojo/Voyager/blob/main/FAQ.md) for more information)
6. Click on the `Register` button.
7. The `Application (client) ID` will be your `client_id`.
8. [Optional] Go to the `Certificates & Secrets` tab and click on the `New client secret` button. Fill the description by yourself. After you click `Add`, you will see your value, this will be your `secret_value`.
9. Go to your Minecraft install location `YOUR_MINECRAFT_GAME_LOCATION/versions`, and check all the versions you have. All the folder names are your valid `version` value. 

After these steps, you will finally get your azure_login information:
```python
azure_login = {
    "client_id": "CLIENT_ID FROM STEP 7",
    "redirect_url": "https://127.0.0.1/auth-response",
    "secret_value": "[OPTIONAL] SECRET_KEY FROM STEP 8",
    "version": "MINECRAFT VERSION YOU WANT TO USE",
}
```
**Voyager use `fabric-loader-0.14.18-1.19` version to run all the experiments.** You may not have this version currently, you can move on to the [Fabric Mods Install](fabric_mods_install.md#fabric-mods-install) section and follow the instructions there to install the fabric version of the game.

## Option 2: Minecraft Official Launcher

After you install official Minecraft, you should have a Minecraft official launcher, open it, and follow the instructions here:
1. Select the version you want to play and start the game.
2. Select `Singleplayer` and create a new world.
3. Set Game Mode to `Creative` and Difficulty to `Peaceful`.
4. After the world is created, press `Esc` and select `Open to LAN`.
5. Select `Allow cheats: ON` and press `Start LAN World`.
6. You will see a port number in the chat log, that is your `mc-port`, use this number to instantiate Voyager later.




================================================
FILE: skill_library/README.md
================================================
# Learned Skill Libraries

## Ours

* [skill_library/trial1](trial1)
* [skill_library/trial2](trial2)
* [skill_library/trial3](trial3)

## Community Contributions

* [daswer123/Voyager_checkpoint](https://github.com/daswer123/Voyager_checkpoint)
* [swen128/Voyager_checkpoint](https://github.com/swen128/Voyager_checkpoint)
* [DeveloperHarris/voyager_checkpoint](https://github.com/DeveloperHarris/voyager_checkpoint)

### How to resume from a community contribution
First, you need to clone or download their repo. Then, the resume is the same as using ours skill libraries. Just set `skill_library_dir=COMMUNITY_CKPT_DIR` where `COMMUNITY_CKPT_DIR` is the ckpt dir inside the folder you just downloaded.

## How to Contribute

After you run the learning process, you will see a checkpoint directory like:
```
.
├── action
│   └── chest_memory.json
├── curriculum
│   ├── completed_tasks.json
│   ├── failed_tasks.json
│   ├── qa_cache.json
│   └── vectordb
├── events
└── skill
    ├── code
    │   ├── catchThreeFishWithCheck.js
    │   ├── collectBamboo.js
    │   ├── ...
    ├── description
    │   ├── catchThreeFishWithCheck.txt
    │   ├── collectBamboo.txt
    │   └── ...
    ├── skills.json
    └── vectordb
```

Only `YOUR_CKPT_DIR/skill` is a learned skill library, which you can share with others. Create a pull request and add your skill library link to this page.



================================================
FILE: skill_library/trial1/skill/skills.json
================================================
{"mineWoodLog": {"code": "async function mineWoodLog(bot) {\n  const woodLogNames = [\"oak_log\", \"birch_log\", \"spruce_log\", \"jungle_log\", \"acacia_log\", \"dark_oak_log\", \"mangrove_log\"];\n\n  // Find a wood log block\n  const woodLogBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    return bot.findBlock({\n      matching: block => woodLogNames.includes(block.name),\n      maxDistance: 32\n    });\n  });\n  if (!woodLogBlock) {\n    bot.chat(\"Could not find a wood log.\");\n    return;\n  }\n\n  // Mine the wood log block\n  await mineBlock(bot, woodLogBlock.name, 1);\n  bot.chat(\"Wood log mined.\");\n}", "description": "async function mineWoodLog(bot) {\n    // The function is about mining a single wood log block. It searches for a wood log block by exploring the environment until it finds one of the seven types of wood logs. If a wood log block is found, it is mined and a success message is sent. If no wood log block is found, a failure message is sent.\n}"}, "mineThreeMoreOakLogs": {"code": "async function mineThreeMoreOakLogs(bot) {\n  // Check the initial inventory for oak logs\n  const initialOakLogs = bot.inventory.count(mcData.itemsByName.oak_log.id);\n\n  // Find 3 oak_log blocks\n  const oakLogs = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const oakLogs = bot.findBlocks({\n      matching: block => block.name === \"oak_log\",\n      maxDistance: 32,\n      count: 3\n    });\n    return oakLogs.length >= 3 ? oakLogs : null;\n  });\n  if (!oakLogs) {\n    bot.chat(\"Could not find enough oak logs.\");\n    return;\n  }\n\n  // Mine the oak_log blocks\n  await mineBlock(bot, \"oak_log\", 3);\n  bot.chat(\"3 oak logs mined.\");\n\n  // Compare the final inventory with the initial inventory\n  const finalOakLogs = bot.inventory.count(mcData.itemsByName.oak_log.id);\n  if (finalOakLogs - initialOakLogs === 3) {\n    bot.chat(\"Successfully mined 3 more oak logs.\");\n  } else {\n    bot.chat(\"Failed to mine 3 more oak logs.\");\n  }\n}", "description": "async function mineThreeMoreOakLogs(bot) {\n    // The function is about mining 3 oak logs. It first checks the initial inventory for oak logs. Then, it explores the environment until it finds 3 oak log blocks. If it cannot find enough oak logs, it returns. Otherwise, it mines the oak log blocks and compares the final inventory with the initial inventory to determine if it successfully mined 3 more oak logs.\n}"}, "craftCraftingTable": {"code": "async function craftCraftingTable(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 4) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((4 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Craft a crafting table using oak planks\n  await craftItem(bot, \"crafting_table\", 1);\n  bot.chat(\"Crafted a crafting table.\");\n}", "description": "async function craftCraftingTable(bot) {\n    // The function crafts a crafting table using oak planks. It first checks if there are enough oak planks in the inventory, and if not, crafts oak planks from oak logs. Then, it crafts a crafting table using the oak planks.\n}"}, "craftWoodenPickaxe": {"code": "async function craftWoodenPickaxe(bot) {\n  // check if crafting table is in the inventory\n  const craftingTableCount = bot.inventory.count(\n    mcData.itemsByName.crafting_table.id\n  );\n\n  // If not, craft a crafting table\n  if (craftingTableCount === 0) {\n    await craftCraftingTable(bot);\n  }\n\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 6) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((6 - oakPlanksCount) / 4);\n    if (oakLogsCount < planksToCraft) {\n      await mineBlock(bot, \"oak_log\", planksToCraft - oakLogsCount);\n    }\n    await craftItem(bot, \"oak_planks\", planksToCraft);\n    bot.chat(\"Crafted oak planks.\");\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not, craft sticks from oak planks\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a wooden pickaxe using the crafting table\n  await craftItem(bot, \"wooden_pickaxe\", 1);\n  bot.chat(\"Crafted a wooden pickaxe.\");\n}\n", "description": "async function craftWoodenPickaxe(bot) {\n    // The function crafts a wooden pickaxe using oak planks, sticks, and a crafting table. It checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. Then, it places a crafting table near the bot and uses it to craft a wooden pickaxe.\n}"}, "craftWoodenSword": {"code": "async function craftWoodenSword(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 2) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((2 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not, craft sticks from oak planks\n  if (sticksCount < 1) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a wooden sword using the crafting table\n  await craftItem(bot, \"wooden_sword\", 1);\n  bot.chat(\"Crafted a wooden sword.\");\n}", "description": "async function craftWoodenSword(bot) {\n    // The function crafts a wooden sword using oak planks, sticks, and a crafting table. It checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. Then, it places a crafting table near the bot and uses it to craft a wooden sword.\n}"}, "killOnePig": {"code": "async function killOnePig(bot) {\n  // Equip the wooden sword\n  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);\n  await bot.equip(woodenSword, \"hand\");\n\n  // Find the nearest pig\n  const pig = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const pig = bot.nearestEntity(entity => {\n      return entity.name === \"pig\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    return pig;\n  });\n  if (!pig) {\n    bot.chat(\"Could not find a pig.\");\n    return;\n  }\n\n  // Kill the pig using the wooden sword\n  await killMob(bot, \"pig\", 300);\n  bot.chat(\"Killed a pig.\");\n\n  // Collect the dropped items\n  await bot.pathfinder.goto(new GoalBlock(pig.position.x, pig.position.y, pig.position.z));\n  bot.chat(\"Collected dropped items.\");\n}", "description": "async function killOnePig(bot) {\n    // The function is about killing a pig using a wooden sword and collecting the dropped items. First, equip the wooden sword in the hand. Next, explore the environment until finding the nearest pig within 32 blocks. Once a pig is found, kill it using the wooden sword and collect the dropped items by moving to the pig's position.\n}"}, "killFourSheep": {"code": "async function killFourSheep(bot) {\n  // Equip the wooden sword\n  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);\n  await bot.equip(woodenSword, \"hand\");\n\n  // Find and kill the first three sheep\n  for (let i = 1; i <= 3; i++) {\n    await killMob(bot, \"sheep\", 300);\n    bot.chat(`Killed sheep ${i}.`);\n  }\n\n  // Find and kill the fourth sheep\n  await killMob(bot, \"sheep\", 300);\n  bot.chat(\"Killed the fourth sheep.\");\n\n  // Collect the dropped items from the killed sheep\n  const sheepDrops = [\"wool\", \"raw_mutton\"];\n  for (const drop of sheepDrops) {\n    const droppedItem = bot.findBlock({\n      matching: block => block.name === drop,\n      maxDistance: 32\n    });\n    if (droppedItem) {\n      await bot.pathfinder.goto(new GoalBlock(droppedItem.position.x, droppedItem.position.y, droppedItem.position.z));\n    }\n  }\n  bot.chat(\"Collected dropped items from the killed sheep.\");\n}", "description": "async function killFourSheep(bot) {\n    // The function is about killing four sheep and collecting their drops. It equips a wooden sword and kills the first three sheep, then kills the fourth sheep. After that, it collects the dropped items from the killed sheep, which include wool and raw mutton.\n}"}, "craftOakPlanksAndSticks": {"code": "async function craftOakPlanksAndSticks(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 8) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((8 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not, craft sticks from oak planks\n  if (sticksCount < 4) {\n    await craftItem(bot, \"stick\", 2);\n    bot.chat(\"Crafted sticks.\");\n  }\n}", "description": "async function craftOakPlanksAndSticks(bot) {\n    // The function checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. If there are not enough oak planks, it crafts them from oak logs. If there are not enough sticks, it crafts them from oak planks.\n}"}, "mineFiveCoalOres": {"code": "async function mineFiveCoalOres(bot) {\n  // Equip the stone pickaxe\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  await bot.equip(stonePickaxe, \"hand\");\n\n  // Find 5 coal_ore blocks\n  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const coalOres = bot.findBlocks({\n      matching: block => block.name === \"coal_ore\",\n      maxDistance: 32,\n      count: 5\n    });\n    return coalOres.length >= 5 ? coalOres : null;\n  });\n  if (!coalOres) {\n    bot.chat(\"Could not find enough coal ores.\");\n    return;\n  }\n\n  // Mine the 5 coal_ore blocks\n  await mineBlock(bot, \"coal_ore\", 5);\n  bot.chat(\"5 coal ores mined.\");\n}", "description": "async function mineFiveCoalOres(bot) {\n    // The function is about mining 5 coal ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 coal_ore blocks. Once 5 coal_ore blocks are found, mine them using the stone pickaxe.\n}"}, "mineTenCobblestone": {"code": "async function mineTenCobblestone(bot) {\n  // Check if the bot has a pickaxe in the inventory\n  const pickaxe = bot.inventory.items().find(item => item.name.endsWith(\"_pickaxe\"));\n\n  // If not, craft a wooden pickaxe using the available resources in the inventory\n  if (!pickaxe) {\n    await craftWoodenPickaxe(bot);\n  } else {\n    // Equip the pickaxe\n    await bot.equip(pickaxe, \"hand\");\n  }\n\n  // Use the exploreUntil function to find cobblestone blocks\n  const cobblestoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const cobblestoneBlocks = bot.findBlocks({\n      matching: block => block.name === \"stone\",\n      maxDistance: 32,\n      count: 10\n    });\n    return cobblestoneBlocks.length >= 10 ? cobblestoneBlocks : null;\n  });\n  if (!cobblestoneBlocks) {\n    bot.chat(\"Could not find enough cobblestone.\");\n    return;\n  }\n\n  // Mine 10 cobblestone blocks using the mineBlock function\n  await mineBlock(bot, \"stone\", 10);\n  bot.chat(\"10 cobblestone mined.\");\n}", "description": "async function mineTenCobblestone(bot) {\n    // The function is about mining 10 cobblestones using a pickaxe. First, check if the bot has a pickaxe in the inventory. If not, craft a wooden pickaxe using the available resources in the inventory. If the pickaxe is available, equip the pickaxe in the hand. Next, use the exploreUntil function to find cobblestone blocks. Once 10 cobblestone blocks are found, mine them using the mineBlock function.\n}"}, "craftStonePickaxe": {"code": "async function craftStonePickaxe(bot) {\n  // Check if there are enough cobblestone and sticks in the inventory\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough cobblestone or sticks, collect the required items\n  if (cobblestoneCount < 3) {\n    await mineBlock(bot, \"stone\", 3 - cobblestoneCount);\n    bot.chat(\"Collected cobblestone.\");\n  }\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone pickaxe using the crafting table\n  await craftItem(bot, \"stone_pickaxe\", 1);\n  bot.chat(\"Crafted a stone pickaxe.\");\n}", "description": "async function craftStonePickaxe(bot) {\n    // The function crafts a stone pickaxe using cobblestone and sticks. It checks if there are enough cobblestone and sticks in the inventory, and if not, it collects the required items. Then, it places a crafting table near the bot and crafts a stone pickaxe using the crafting table.\n}"}, "mineFiveIronOres": {"code": "async function mineFiveIronOres(bot) {\n  // Equip the stone pickaxe\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  await bot.equip(stonePickaxe, \"hand\");\n\n  // Find 5 iron_ore blocks\n  const ironOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const ironOres = bot.findBlocks({\n      matching: block => block.name === \"iron_ore\",\n      maxDistance: 32,\n      count: 5\n    });\n    return ironOres.length >= 5 ? ironOres : null;\n  });\n  if (!ironOres) {\n    bot.chat(\"Could not find enough iron ores.\");\n    return;\n  }\n\n  // Mine the 5 iron_ore blocks\n  await mineBlock(bot, \"iron_ore\", 5);\n  bot.chat(\"5 iron ores mined.\");\n}", "description": "async function mineFiveIronOres(bot) {\n    // The function is about mining 5 iron ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 iron_ore blocks. Once 5 iron_ore blocks are found, mine them using the stone pickaxe.\n}"}, "craftFurnace": {"code": "async function craftFurnace(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n\n  // If not, mine the required cobblestones\n  if (cobblestoneCount < 8) {\n    await mineBlock(bot, \"stone\", 8 - cobblestoneCount);\n    bot.chat(\"Collected cobblestone.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a furnace using the crafting table\n  await craftItem(bot, \"furnace\", 1);\n  bot.chat(\"Crafted a furnace.\");\n}", "description": "async function craftFurnace(bot) {\n    // The function crafts a furnace using a crafting table and cobblestones. If there are not enough cobblestones in the inventory, it mines the required amount. Then, it places a crafting table near the bot and crafts a furnace using the crafting table. Finally, it sends a chat message indicating that a furnace has been crafted.\n}"}, "smeltFiveRawIron": {"code": "async function findSuitablePosition(bot) {\n  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];\n  for (const offset of offsets) {\n    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);\n    const block = bot.blockAt(position);\n    if (block.name === \"air\") {\n      return position;\n    }\n  }\n  return null;\n}\nasync function smeltFiveRawIron(bot) {\n  // Check if there is coal in the inventory\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n\n  // If not enough coal, mine coal_ore to obtain coal\n  if (coalCount < 3) {\n    await mineBlock(bot, \"coal_ore\", 3 - coalCount);\n    bot.chat(\"Collected coal.\");\n  }\n  // Check if there is a furnace in the inventory\n  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  // If not, craft a furnace using the available cobblestone\n  if (!furnaceItem) {\n    await craftFurnace(bot);\n  }\n  // Find a suitable position to place the furnace\n  const furnacePosition = await findSuitablePosition(bot);\n  if (!furnacePosition) {\n    bot.chat(\"Could not find a suitable position to place the furnace.\");\n    return;\n  }\n  // Place the furnace at the suitable position\n  await placeItem(bot, \"furnace\", furnacePosition);\n  // Smelt 5 raw iron using the available coal as fuel\n  await smeltItem(bot, \"raw_iron\", \"coal\", 5);\n  bot.chat(\"5 raw iron smelted.\");\n}", "description": "async function smeltFiveRawIron(bot) {\n    // The function is about smelting 5 raw iron using a furnace and coal as fuel. If there is no furnace in the inventory, craft one using cobblestone. Find a suitable position to place the furnace and place it there. Then, smelt 5 raw iron using the available coal as fuel.\n}"}, "craftIronPickaxe": {"code": "async function craftIronPickaxe(bot) {\n  // Check if there are enough iron ingots and sticks in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough iron ingots or sticks, collect the required items\n  if (ironIngotsCount < 3) {\n    await mineBlock(bot, \"iron_ore\", 3 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 3 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron pickaxe using the crafting table\n  await craftItem(bot, \"iron_pickaxe\", 1);\n  bot.chat(\"Crafted an iron pickaxe.\");\n}", "description": "async function craftIronPickaxe(bot) {\n    // The function crafts an iron pickaxe using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It then places a crafting table near the bot and crafts an iron pickaxe using the crafting table.\n}"}, "craftIronSword": {"code": "async function craftIronSword(bot) {\n  // Check if there are enough iron ingots and sticks in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough iron ingots or sticks, collect the required items\n  if (ironIngotsCount < 2) {\n    await mineBlock(bot, \"iron_ore\", 2 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 2 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n  if (sticksCount < 1) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron sword using the crafting table\n  await craftItem(bot, \"iron_sword\", 1);\n  bot.chat(\"Crafted an iron sword.\");\n}", "description": "async function craftIronSword(bot) {\n    // The function crafts an iron sword using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, it collects the required items. It then places a crafting table near the bot and crafts an iron sword using the crafting table.\n}"}, "cookPorkchops": {"code": "async function cookPorkchops(bot) {\n  // Check if there is a furnace in the inventory\n  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n\n  // If not, craft a furnace using the available cobblestone\n  if (!furnaceItem) {\n    await craftFurnace(bot);\n  }\n\n  // Place the furnace near the bot\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 2 porkchops using the available coal as fuel\n  await smeltItem(bot, \"porkchop\", \"coal\", 2);\n  bot.chat(\"2 porkchops cooked.\");\n}", "description": "async function cookPorkchops(bot) {\n    // The function is about cooking 2 porkchops using a furnace and coal as fuel. First, it checks if there is a furnace in the inventory. If not, it crafts a furnace using cobblestone. Then, it places the furnace near the bot. Finally, it smelts 2 porkchops using coal as fuel and saves the event of cooking porkchops.\n}"}, "mineFiveLapisLazuliOres": {"code": "async function mineFiveLapisLazuliOres(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find 5 lapis_lazuli_ore blocks\n  const lapisOres = await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {\n    const lapisOres = bot.findBlocks({\n      matching: block => block.name === \"lapis_ore\",\n      maxDistance: 32,\n      count: 5\n    });\n    return lapisOres.length >= 5 ? lapisOres : null;\n  });\n  if (!lapisOres) {\n    bot.chat(\"Could not find enough lapis lazuli ores.\");\n    return;\n  }\n\n  // Mine the 5 lapis_lazuli_ore blocks\n  await mineBlock(bot, \"lapis_ore\", 5);\n  bot.chat(\"5 lapis lazuli ores mined.\");\n}", "description": "async function mineFiveLapisLazuliOres(bot) {\n    // The function is about mining 5 lapis lazuli ores using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 lapis lazuli ore blocks. Once 5 lapis lazuli ore blocks are found, mine them using the iron pickaxe.\n}"}, "craftIronAxe": {"code": "async function craftIronAxe(bot) {\n  // Check if there are enough iron ingots and sticks in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough iron ingots or sticks, collect the required items\n  if (ironIngotsCount < 3) {\n    await mineBlock(bot, \"iron_ore\", 3 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 3 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron axe using the crafting table\n  await craftItem(bot, \"iron_axe\", 1);\n  bot.chat(\"Crafted an iron axe.\");\n}", "description": "async function craftIronAxe(bot) {\n    // The function crafts an iron axe using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It then places a crafting table near the bot and crafts an iron axe using the crafting table.\n}"}, "craftStoneShovel": {"code": "async function craftStoneShovel(bot) {\n  // Check if there are enough cobblestone and sticks in the inventory\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough cobblestone, mine cobblestone\n  if (cobblestoneCount < 1) {\n    await mineBlock(bot, \"stone\", 1);\n    bot.chat(\"Collected cobblestone.\");\n  }\n\n  // If not enough sticks, craft sticks\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone shovel using the crafting table\n  await craftItem(bot, \"stone_shovel\", 1);\n  bot.chat(\"Crafted a stone shovel.\");\n}", "description": "async function craftStoneShovel(bot) {\n    // The function crafts a stone shovel using cobblestone and sticks. It checks if there are enough cobblestone and sticks in the inventory, and if not, it mines cobblestone or crafts sticks. Then, it places a crafting table near the bot and crafts a stone shovel using the crafting table. Finally, it sends a chat message indicating that a stone shovel has been crafted.\n}"}, "cookSevenMutton": {"code": "async function cookSevenMutton(bot) {\n  // Check if there is a furnace in the inventory\n  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n\n  // If not, craft a furnace using the available cobblestone\n  if (!furnaceItem) {\n    await craftFurnace(bot);\n  }\n\n  // Find a suitable position to place the furnace\n  const furnacePosition = await findSuitablePosition(bot);\n  if (!furnacePosition) {\n    bot.chat(\"Could not find a suitable position to place the furnace.\");\n    return;\n  }\n\n  // Place the furnace at the suitable position\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 7 raw mutton using the available coal as fuel\n  await smeltItem(bot, \"mutton\", \"coal\", 7);\n  bot.chat(\"7 mutton cooked.\");\n}", "description": "async function cookSevenMutton(bot) {\n    // The function is about cooking 7 raw mutton using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. After that, it smelts 7 raw mutton using the available coal as fuel and saves the event of cooking 7 mutton.\n}"}, "killTwoPigs": {"code": "async function killTwoPigs(bot) {\n  // Equip the wooden sword\n  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);\n  await bot.equip(woodenSword, \"hand\");\n\n  // Find and kill the first pig\n  await killMob(bot, \"pig\", 300);\n  bot.chat(\"Killed the first pig.\");\n\n  // Find and kill the second pig\n  await killMob(bot, \"pig\", 300);\n  bot.chat(\"Killed the second pig.\");\n\n  // Collect the dropped items from the killed pigs\n  const pigDrops = [\"raw_porkchop\"];\n  for (const drop of pigDrops) {\n    const droppedItem = bot.findBlock({\n      matching: block => block.name === drop,\n      maxDistance: 32\n    });\n    if (droppedItem) {\n      await bot.pathfinder.goto(new GoalBlock(droppedItem.position.x, droppedItem.position.y, droppedItem.position.z));\n    }\n  }\n  bot.chat(\"Collected dropped items from the killed pigs.\");\n}", "description": "async function killTwoPigs(bot) {\n    // The function is about killing two pigs and collecting their dropped items. The function equips a wooden sword and kills two pigs using the `killMob` function. After killing each pig, the function logs a message. Then, the function searches for dropped items from the killed pigs and collects them using the `pathfinder` module. Finally, the function logs a message indicating that the items have been collected.\n}"}, "eatCookedPorkchop": {"code": "async function eatCookedPorkchop(bot) {\n  // Equip the cooked porkchop in the bot's hand\n  const cookedPorkchop = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_porkchop.id);\n  await bot.equip(cookedPorkchop, \"hand\");\n\n  // Consume the cooked porkchop\n  await bot.consume();\n\n  // Send a chat message to indicate the task is completed\n  bot.chat(\"Ate 1 cooked porkchop.\");\n}", "description": "async function eatCookedPorkchop(bot) {\n    // The function is about eating a cooked porkchop. It equips the cooked porkchop in the bot's hand, consumes it, and sends a chat message to indicate the task is completed.\n}"}, "craftWoodenHoe": {"code": "async function craftWoodenHoe(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 2) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((2 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not, craft sticks from oak planks\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a wooden hoe using the crafting table\n  await craftItem(bot, \"wooden_hoe\", 1);\n  bot.chat(\"Crafted a wooden hoe.\");\n}", "description": "async function craftWoodenHoe(bot) {\n    // The function crafts a wooden hoe using oak planks and sticks. If there are not enough oak planks, it crafts them from oak logs. If there are not enough sticks, it crafts them from oak planks. Then, it places a crafting table near the bot and uses it to craft a wooden hoe.\n}"}, "craftWhiteBed": {"code": "async function craftWhiteBed(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 3) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((3 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Check if there are enough white wool in the inventory\n  const whiteWoolCount = bot.inventory.count(mcData.itemsByName.white_wool.id);\n  if (whiteWoolCount < 3) {\n    bot.chat(\"Not enough white wool to craft a bed.\");\n    return;\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a white bed using the crafting table\n  await craftItem(bot, \"white_bed\", 1);\n  bot.chat(\"Crafted a white bed.\");\n}", "description": "async function craftWhiteBed(bot) {\n    // The function crafts a white bed using oak planks and white wool. If there are not enough oak planks in the inventory, it crafts oak planks from oak logs. If there are not enough white wool in the inventory, it stops the function. Then, it places a crafting table near the bot and crafts a white bed using the crafting table.\n}"}, "killOneEnderman": {"code": "async function killOneEnderman(bot) {\n  // Equip the iron sword\n  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n  await bot.equip(ironSword, \"hand\");\n\n  // Find the nearest enderman\n  const enderman = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const enderman = bot.nearestEntity(entity => {\n      return entity.name === \"enderman\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    return enderman;\n  });\n  if (!enderman) {\n    bot.chat(\"Could not find an enderman.\");\n    return;\n  }\n\n  // Kill the enderman using the iron sword\n  await killMob(bot, \"enderman\", 300);\n  bot.chat(\"Killed an enderman.\");\n\n  // Collect the dropped items\n  await bot.pathfinder.goto(new GoalBlock(enderman.position.x, enderman.position.y, enderman.position.z));\n  bot.chat(\"Collected dropped items.\");\n}", "description": "async function killOneEnderman(bot) {\n    // The function is about killing one enderman using an iron sword. First, equip the iron sword in the hand. Next, explore the environment until finding the nearest enderman within 32 blocks. Once an enderman is found, kill it using the iron sword. After killing the enderman, collect the dropped items by moving to the enderman's position.\n}"}, "craftIronChestplate": {"code": "async function craftIronChestplate(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n\n  // If not enough iron ingots, mine iron ores and smelt them into iron ingots\n  if (ironIngotsCount < 8) {\n    await mineBlock(bot, \"iron_ore\", 8 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 8 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron chestplate using the crafting table\n  await craftItem(bot, \"iron_chestplate\", 1);\n  bot.chat(\"Crafted an iron chestplate.\");\n}", "description": "async function craftIronChestplate(bot) {\n    // The function crafts an iron chestplate using a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into iron ingots. Then it places a crafting table near the bot and crafts an iron chestplate using the crafting table.\n}"}, "mineFiveCopperOres": {"code": "async function mineFiveCopperOres(bot) {\n  // Check if the bot already has 5 or more copper ores in the inventory\n  const copperOres = bot.inventory.items().filter(item => item.name === \"copper_ore\");\n  const totalCopperOres = copperOres.reduce((total, item) => total + item.count, 0);\n  if (totalCopperOres >= 5) {\n    bot.chat(\"Task already completed. There are already \" + totalCopperOres + \" copper ores in the inventory.\");\n  } else {\n    bot.chat(\"Need to mine \" + (5 - totalCopperOres) + \" more copper ores.\");\n    // You can call the mineFiveCopperOres function from the previous response here\n  }\n}", "description": "async function mineFiveCopperOres(bot) {\n    // The function checks if the bot already has 5 or more copper ores in the inventory. If not, it outputs how many more copper ores are needed to complete the task.\n}"}, "equipIronChestplate": {"code": "async function equipIronChestplate(bot) {\n  // Find the iron chestplate in the inventory\n  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id);\n\n  // Equip the iron chestplate\n  if (ironChestplate) {\n    await bot.equip(ironChestplate, \"torso\");\n    bot.chat(\"Equipped iron chestplate.\");\n  } else {\n    bot.chat(\"Iron chestplate not found in inventory.\");\n  }\n}", "description": "async function equipIronChestplate(bot) {\n    // The function is about equipping an iron chestplate on the bot's torso. It first finds the iron chestplate in the inventory and then equips it. If the iron chestplate is not found in the inventory, it sends a message saying that it was not found.\n}"}, "smeltRawCopper": {"code": "async function smeltRawCopper(bot) {\n  // Check if there is a furnace in the inventory\n  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n\n  // If not, craft a furnace using the available cobblestone\n  if (!furnaceItem) {\n    await craftFurnace(bot);\n  }\n\n  // Find a suitable position to place the furnace\n  const furnacePosition = await findSuitablePosition(bot);\n  if (!furnacePosition) {\n    bot.chat(\"Could not find a suitable position to place the furnace.\");\n    return;\n  }\n\n  // Place the furnace at the suitable position\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 19 raw copper using the available coal as fuel\n  await smeltItem(bot, \"raw_copper\", \"coal\", 19);\n  bot.chat(\"19 raw copper smelted.\");\n}", "description": "async function smeltRawCopper(bot) {\n    // The function is about smelting 19 raw copper using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. Finally, it smelts the raw copper using the furnace and coal as fuel.\n}"}, "craftIronHelmet": {"code": "async function craftIronHelmet(bot) {\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron helmet using the crafting table\n  await craftItem(bot, \"iron_helmet\", 1);\n  bot.chat(\"Crafted an iron helmet.\");\n}", "description": "async function craftIronHelmet(bot) {\n    // The function is about crafting an iron helmet using a crafting table. First, place the crafting table near the bot. Then, craft an iron helmet using the crafting table and save it to the inventory.\n}"}, "craftChest": {"code": "async function craftChest(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, craft oak planks from oak logs\n  if (oakPlanksCount < 8) {\n    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((8 - oakPlanksCount) / 4);\n    if (oakLogsCount >= planksToCraft) {\n      await craftItem(bot, \"oak_planks\", planksToCraft);\n      bot.chat(\"Crafted oak planks.\");\n    } else {\n      bot.chat(\"Not enough oak logs to craft oak planks.\");\n      return;\n    }\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a chest using the crafting table\n  await craftItem(bot, \"chest\", 1);\n  bot.chat(\"Crafted a chest.\");\n}", "description": "async function craftChest(bot) {\n    // The function crafts a chest using a crafting table and oak planks. If there are not enough oak planks in the inventory, it crafts oak planks from oak logs. Once there are enough oak planks, it places a crafting table near the bot and crafts a chest using the crafting table.\n}"}, "equipIronSword": {"code": "async function equipIronSword(bot) {\n  // Find the iron sword in the inventory\n  let ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n\n  // If the iron sword is not found in the inventory, check the chest\n  if (!ironSword) {\n    const chestPosition = new Vec3(89, 41, 206);\n    const itemsToGet = {\n      \"iron_sword\": 1\n    };\n    await getItemFromChest(bot, chestPosition, itemsToGet);\n    ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n  }\n\n  // Equip the iron sword\n  if (ironSword) {\n    await bot.equip(ironSword, \"hand\");\n    bot.chat(\"Equipped iron sword.\");\n  } else {\n    bot.chat(\"Iron sword not found in inventory or chest.\");\n  }\n}", "description": "async function equipIronSword(bot) {\n    // The function is about equipping an iron sword. It first checks if the iron sword is in the inventory. If not, it checks a chest for the iron sword. If the iron sword is found, it is equipped in the hand. If the iron sword is not found, a message is sent to the chat.\n}"}, "craftLightningRod": {"code": "async function findSuitablePosition(bot) {\n  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];\n  for (const offset of offsets) {\n    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);\n    const block = bot.blockAt(position);\n    if (block.name === \"air\") {\n      return position;\n    }\n  }\n  return null;\n}\n\nasync function craftLightningRod(bot) {\n  // Find a suitable position to place the crafting table\n  const craftingTablePosition = await findSuitablePosition(bot);\n\n  // Place the crafting table at the found position\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Check if there are enough copper ingots in the inventory\n  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);\n\n  // If not enough copper ingots, mine copper ores and smelt them into copper ingots\n  if (copperIngotsCount < 3) {\n    await mineBlock(bot, \"copper_ore\", 3 - copperIngotsCount);\n    bot.chat(\"Collected copper ores.\");\n    await smeltItem(bot, \"copper_ore\", \"coal\", 3 - copperIngotsCount);\n    bot.chat(\"Smelted copper ores into copper ingots.\");\n  }\n\n  // Craft a lightning rod using the crafting table\n  await craftItem(bot, \"lightning_rod\", 1);\n  bot.chat(\"Crafted a lightning rod.\");\n}", "description": "async function craftLightningRod(bot) {\n    // The function is about crafting a lightning rod. It first finds a suitable position to place the crafting table and places it there. Then it checks if there are enough copper ingots in the inventory, and if not, it mines copper ores and smelts them into copper ingots. Finally, it crafts a lightning rod using the crafting table.\n}"}, "craftCopperBlock": {"code": "async function craftCopperBlock(bot) {\n  // Check if there are enough copper ingots in the inventory\n  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);\n\n  // If not enough copper ingots, mine copper ores and smelt them into copper ingots\n  if (copperIngotsCount < 9) {\n    await mineBlock(bot, \"copper_ore\", 9 - copperIngotsCount);\n    bot.chat(\"Collected copper ores.\");\n    await smeltItem(bot, \"copper_ore\", \"coal\", 9 - copperIngotsCount);\n    bot.chat(\"Smelted copper ores into copper ingots.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a copper block using the crafting table\n  await craftItem(bot, \"copper_block\", 1);\n  bot.chat(\"Crafted a copper block.\");\n}", "description": "async function craftCopperBlock(bot) {\n    // The function crafts a copper block using a crafting table. It first checks if there are enough copper ingots in the inventory, and if not, it mines copper ores and smelts them into copper ingots. Then it places a crafting table near the bot and crafts a copper block using the crafting table.\n}"}, "killOneSpider": {"code": "async function killOneSpider(bot) {\n  // Equip the iron sword\n  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n  await bot.equip(ironSword, \"hand\");\n\n  // Find the nearest spider\n  const spider = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const spider = bot.nearestEntity(entity => {\n      return entity.name === \"spider\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    return spider;\n  });\n  if (!spider) {\n    bot.chat(\"Could not find a spider.\");\n    return;\n  }\n\n  // Kill the spider using the iron sword\n  await killMob(bot, \"spider\", 300);\n  bot.chat(\"Killed a spider.\");\n\n  // Collect the dropped items\n  await bot.pathfinder.goto(new GoalBlock(spider.position.x, spider.position.y, spider.position.z));\n  bot.chat(\"Collected dropped items.\");\n}", "description": "async function killOneSpider(bot) {\n    // The function is about killing a spider using an iron sword. First, equip the iron sword in the hand. Then, explore the environment until finding the nearest spider within 32 blocks. Once a spider is found, kill it using the iron sword. After killing the spider, collect the dropped items by moving to the spider's position.\n}"}, "killOneZombie": {"code": "async function killOneZombie(bot) {\n  // Equip the iron sword\n  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n  await bot.equip(ironSword, \"hand\");\n\n  // Find the nearest zombie\n  const zombie = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const zombie = bot.nearestEntity(entity => {\n      return entity.name === \"zombie\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    return zombie;\n  });\n  if (!zombie) {\n    bot.chat(\"Could not find a zombie.\");\n    return;\n  }\n\n  // Kill the zombie using the iron sword\n  await killMob(bot, \"zombie\", 300);\n  bot.chat(\"Killed a zombie.\");\n\n  // Collect the dropped items\n  await bot.pathfinder.goto(new GoalBlock(zombie.position.x, zombie.position.y, zombie.position.z));\n  bot.chat(\"Collected dropped items.\");\n}", "description": "async function killOneZombie(bot) {\n    // The function is about killing a single zombie using an iron sword. First, equip the iron sword in the hand. Then, explore the environment until finding the nearest zombie within 32 blocks. Once a zombie is found, kill it using the iron sword and collect the dropped items.\n}"}, "craftIronLeggingsAndBoots": {"code": "async function craftIronLeggingsAndBoots(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n\n  // If not enough iron ingots, mine iron ores and smelt them into iron ingots\n  if (ironIngotsCount < 11) {\n    await mineBlock(bot, \"iron_ore\", 11 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 11 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft iron leggings using the crafting table\n  await craftItem(bot, \"iron_leggings\", 1);\n  bot.chat(\"Crafted iron leggings.\");\n\n  // Craft iron boots using the crafting table\n  await craftItem(bot, \"iron_boots\", 1);\n  bot.chat(\"Crafted iron boots.\");\n}", "description": "async function craftIronLeggingsAndBoots(bot) {\n    // The function crafts iron leggings and boots using a crafting table. If there are not enough iron ingots in the inventory, the bot mines iron ores and smelts them into iron ingots. Then, the bot places a crafting table near itself and crafts iron leggings and boots using the crafting table.\n}"}, "equipIronArmor": {"code": "async function equipIronArmor(bot) {\n  // Find the iron_leggings, iron_boots, and iron_helmet in the inventory\n  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id);\n  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id);\n  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id);\n\n  // Equip the iron_leggings, iron_boots, and iron_helmet in the appropriate slots (legs, feet, and head)\n  if (ironLeggings) {\n    await bot.equip(ironLeggings, \"legs\");\n    bot.chat(\"Equipped iron leggings.\");\n  } else {\n    bot.chat(\"Iron leggings not found in inventory.\");\n  }\n  if (ironBoots) {\n    await bot.equip(ironBoots, \"feet\");\n    bot.chat(\"Equipped iron boots.\");\n  } else {\n    bot.chat(\"Iron boots not found in inventory.\");\n  }\n  if (ironHelmet) {\n    await bot.equip(ironHelmet, \"head\");\n    bot.chat(\"Equipped iron helmet.\");\n  } else {\n    bot.chat(\"Iron helmet not found in inventory.\");\n  }\n}", "description": "async function equipIronArmor(bot) {\n    // The function is about equipping iron armor (leggings, boots, and helmet) in the appropriate slots (legs, feet, and head) if they are available in the inventory. If any of the items are not found in the inventory, the function will output a message indicating that the item is not available.\n}"}, "craftShieldImproved": {"code": "async function craftShieldImproved(bot) {\n  // Check if there are enough oak planks in the inventory\n  let oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n\n  // If not, check if there are enough oak logs in the inventory\n  if (oakPlanksCount < 6) {\n    let oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);\n    const planksToCraft = Math.ceil((6 - oakPlanksCount) / 4);\n\n    // If not, explore to find and mine oak logs\n    if (oakLogsCount < planksToCraft) {\n      await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n        const oak_log = bot.findBlock({\n          matching: mcData.blocksByName[\"oak_log\"].id,\n          maxDistance: 32\n        });\n        return oak_log;\n      });\n      await mineBlock(bot, \"oak_log\", planksToCraft - oakLogsCount);\n      bot.chat(\"Collected oak logs.\");\n    }\n\n    // Craft oak planks from oak logs\n    await craftItem(bot, \"oak_planks\", planksToCraft);\n    bot.chat(\"Crafted oak planks.\");\n    oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);\n  }\n\n  // Check if there are enough iron ingots in the inventory\n  let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n\n  // If not, explore to find and mine iron ores\n  if (ironIngotsCount < 1) {\n    await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {\n      const iron_ore = bot.findBlock({\n        matching: mcData.blocksByName[\"iron_ore\"].id,\n        maxDistance: 32\n      });\n      return iron_ore;\n    });\n    await mineBlock(bot, \"iron_ore\", 1);\n    bot.chat(\"Collected iron ores.\");\n\n    // Smelt iron ores into iron ingots\n    await smeltItem(bot, \"iron_ore\", \"coal\", 1);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a shield using the crafting table\n  await craftItem(bot, \"shield\", 1);\n  bot.chat(\"Crafted a shield.\");\n}", "description": "async function craftShieldImproved(bot) {\n    // The function crafts a shield using oak planks and iron ingots. It checks if there are enough oak planks and iron ingots in the inventory, and if not, it explores the environment to find and collect the required materials. It then places a crafting table near the bot and crafts a shield using the crafting table.\n}"}, "craftBucket": {"code": "async function craftBucket(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n\n  // If not enough iron ingots, mine iron ores and smelt them into iron ingots\n  if (ironIngotsCount < 3) {\n    await mineBlock(bot, \"iron_ore\", 3 - ironIngotsCount);\n    bot.chat(\"Collected iron ores.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 3 - ironIngotsCount);\n    bot.chat(\"Smelted iron ores into iron ingots.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a bucket using the crafting table\n  await craftItem(bot, \"bucket\", 1);\n  bot.chat(\"Crafted a bucket.\");\n}", "description": "async function craftBucket(bot) {\n    // The function crafts a bucket using a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into iron ingots. Then, it places a crafting table near the bot and crafts a bucket using the crafting table.\n}"}, "fillBucketWithWater": {"code": "async function fillBucketWithWater(bot) {\n  // Find a water block nearby\n  const waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const water = bot.findBlock({\n      matching: mcData.blocksByName.water.id,\n      maxDistance: 32,\n    });\n    return water;\n  });\n  if (!waterBlock) {\n    bot.chat(\"Could not find water.\");\n    return;\n  }\n\n  const adjacentBlock = waterBlock.position.offset(0, 1, 0);\n  // Go to the water block\n  await bot.pathfinder.goto(\n    new GoalGetToBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z)\n  );\n\n  // Equip the bucket\n  const bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);\n  await bot.equip(bucket, \"hand\");\n\n  // Look at the water block\n  await bot.lookAt(waterBlock.position);\n\n  // Activate the bucket to collect water\n  await bot.activateItem();\n  bot.chat(\"Filled the bucket with water.\");\n}\n", "description": "async function fillBucketWithWater(bot) {\n    // This function fills a bucket with water by first finding a nearby water block. After locating the water block, the bot moves to it and equips the bucket in its hand. The bot then looks at the water block and activates the bucket to collect water.\n}"}, "craftIronShovel": {"code": "async function craftIronShovel(bot) {\n  // Check if there are enough iron ingots and sticks in the inventory\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n\n  // If not enough iron ingots or sticks, collect the required items\n  if (ironIngotsCount < 1) {\n    await mineBlock(bot, \"iron_ore\", 1);\n    bot.chat(\"Collected iron ore.\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", 1);\n    bot.chat(\"Smelted iron ore into iron ingot.\");\n  }\n  if (sticksCount < 2) {\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Crafted sticks.\");\n  }\n\n  // Find a suitable position to place the crafting table\n  const suitablePosition = bot.entity.position.offset(1, 0, 0);\n  const block = bot.blockAt(suitablePosition);\n  if (block.name === \"grass_block\" || block.name === \"dirt\") {\n    await bot.dig(block);\n  }\n\n  // Place the crafting table at the suitable position\n  await placeItem(bot, \"crafting_table\", suitablePosition);\n\n  // Craft an iron shovel using the crafting table\n  await craftItem(bot, \"iron_shovel\", 1);\n  bot.chat(\"Crafted an iron shovel.\");\n}", "description": "async function craftIronShovel(bot) {\n    // The function crafts an iron shovel using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It finds a suitable position to place the crafting table and places it there. Then, it crafts an iron shovel using the crafting table.\n}"}, "obtainOneMoreAcaciaLog": {"code": "async function obtainOneMoreAcaciaLog(bot) {\n  // Check the initial inventory for acacia logs\n  const initialAcaciaLogs = bot.inventory.count(mcData.itemsByName.acacia_log.id);\n\n  // If the number of acacia logs is less than 5, find and mine one more acacia log\n  if (initialAcaciaLogs < 5) {\n    const acaciaLog = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      return bot.findBlock({\n        matching: block => block.name === \"acacia_log\",\n        maxDistance: 32\n      });\n    });\n    if (!acaciaLog) {\n      bot.chat(\"Could not find an acacia log.\");\n      return;\n    }\n    await mineBlock(bot, \"acacia_log\", 1);\n    bot.chat(\"1 more acacia log obtained.\");\n  }\n\n  // Check the final number of acacia logs in the inventory\n  const finalAcaciaLogs = bot.inventory.count(mcData.itemsByName.acacia_log.id);\n  if (finalAcaciaLogs >= 5) {\n    bot.chat(\"Successfully obtained 5 acacia logs.\");\n  } else {\n    bot.chat(\"Failed to obtain 5 acacia logs.\");\n  }\n}", "description": "async function obtainOneMoreAcaciaLog(bot) {\n    // The function checks if there are less than 5 acacia logs in the inventory, and if so, finds and mines one more acacia log. If the bot successfully obtains 5 acacia logs, it sends a success message, otherwise it sends a failure message.\n}"}, "craftAcaciaPlanksAndSticks": {"code": "async function craftAcaciaPlanksAndSticks(bot) {\n  // Check if there are enough acacia logs in the inventory\n  const acaciaLogsCount = bot.inventory.count(mcData.itemsByName.acacia_log.id);\n\n  // If not, mine more acacia logs\n  if (acaciaLogsCount < 5) {\n    await mineBlock(bot, \"acacia_log\", 5 - acaciaLogsCount);\n    bot.chat(\"Mined acacia logs.\");\n  }\n\n  // Craft 20 acacia planks from acacia logs\n  await craftItem(bot, \"acacia_planks\", 5);\n  bot.chat(\"Crafted 20 acacia planks.\");\n\n  // Check if there are enough acacia planks in the inventory to craft 10 sticks\n  const acaciaPlanksCount = bot.inventory.count(mcData.itemsByName.acacia_planks.id);\n\n  // If not, mine more acacia logs and craft more acacia planks\n  if (acaciaPlanksCount < 5) {\n    await mineBlock(bot, \"acacia_log\", 5 - acaciaLogsCount);\n    bot.chat(\"Mined more acacia logs.\");\n    await craftItem(bot, \"acacia_planks\", 5 - acaciaPlanksCount);\n    bot.chat(\"Crafted more acacia planks.\");\n  }\n\n  // Craft 10 sticks from acacia planks\n  await craftItem(bot, \"stick\", 3);\n  bot.chat(\"Crafted 10 sticks.\");\n}", "description": "async function craftAcaciaPlanksAndSticks(bot) {\n    // The function is about crafting 20 acacia planks and 10 sticks. It checks if there are enough acacia logs in the inventory, and if not, it mines more acacia logs. Then it crafts 20 acacia planks from the acacia logs. If there are not enough acacia planks in the inventory to craft 10 sticks, it mines more acacia logs and crafts more acacia planks. Finally, it crafts 10 sticks from the acacia planks.\n}"}, "eatTwoCookedMutton": {"code": "async function eatTwoCookedMutton(bot) {\n  // Check if there are 2 cooked mutton in the inventory\n  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);\n  if (!cookedMutton || cookedMutton.count < 2) {\n    bot.chat(\"Not enough cooked mutton in the inventory.\");\n    return;\n  }\n\n  // Equip the cooked mutton in the bot's hand\n  await bot.equip(cookedMutton, \"hand\");\n\n  // Consume the cooked mutton twice\n  await bot.consume();\n  await bot.consume();\n\n  // Send a chat message to indicate the task is completed\n  bot.chat(\"Ate 2 cooked mutton.\");\n}", "description": "async function eatTwoCookedMutton(bot) {\n    // The function is about eating two cooked muttons. It checks if there are at least 2 cooked muttons in the inventory, and if not, it returns. If there are 2 or more cooked muttons, it equips one in the bot's hand and consumes it twice. Finally, it sends a chat message to indicate that the task is completed.\n}"}, "collectBamboo": {"code": "async function collectBamboo(bot) {\n  // Equip the iron sword\n  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);\n  await bot.equip(ironSword, \"hand\");\n\n  // Find bamboo plants using the exploreUntil function\n  const bambooPlants = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const bambooPlants = bot.findBlocks({\n      matching: block => block.name === \"bamboo\",\n      maxDistance: 32,\n      count: 10\n    });\n    return bambooPlants.length >= 10 ? bambooPlants : null;\n  });\n  if (!bambooPlants) {\n    bot.chat(\"Could not find enough bamboo plants.\");\n    return;\n  }\n\n  // Break 10 bamboo plants using the iron sword\n  for (const bambooPlant of bambooPlants) {\n    const block = bot.blockAt(bambooPlant);\n    await bot.dig(block);\n  }\n  bot.chat(\"Broke 10 bamboo plants.\");\n\n  // Collect the dropped bamboo items\n  for (const bambooPlant of bambooPlants) {\n    await bot.pathfinder.goto(new GoalBlock(bambooPlant.x, bambooPlant.y, bambooPlant.z));\n  }\n  bot.chat(\"Collected 10 bamboo.\");\n}", "description": "async function collectBamboo(bot) {\n    // The function is about collecting 10 bamboo plants. It equips the iron sword and uses the `exploreUntil` function to find 10 bamboo plants within a certain distance. If enough bamboo plants are found, it breaks them using the iron sword and collects the dropped bamboo items by moving to their location. If not enough bamboo plants are found, it returns an error message.\n}"}, "craftScaffolding": {"code": "async function craftScaffolding(bot) {\n  // Check if we have a crafting table in the inventory\n  const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);\n\n  // If not, craft a crafting table\n  if (craftingTableCount === 0) {\n    await craftItem(bot, \"crafting_table\", 1);\n    bot.chat(\"Crafted a crafting table.\");\n  }\n\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft 10 scaffolding using the crafting table\n  await craftItem(bot, \"scaffolding\", 1);\n  bot.chat(\"Crafted 10 scaffolding.\");\n}", "description": "async function craftScaffolding(bot) {\n    // The function is about crafting 10 scaffolding using a crafting table. First, it checks if there is a crafting table in the inventory. If not, it crafts one. Then, it places the crafting table near the bot. After that, it crafts 10 scaffolding using the crafting table and saves the event.\n}"}, "collectFiveCactusBlocks": {"code": "async function collectFiveCactusBlocks(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find 5 cactus blocks using the exploreUntil function\n  const cactusBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const cactusBlocks = bot.findBlocks({\n      matching: block => block.name === \"cactus\",\n      maxDistance: 32,\n      count: 5\n    });\n    return cactusBlocks.length >= 5 ? cactusBlocks : null;\n  });\n  if (!cactusBlocks) {\n    bot.chat(\"Could not find enough cactus blocks.\");\n    return;\n  }\n\n  // Mine the 5 cactus blocks using the mineBlock function\n  await mineBlock(bot, \"cactus\", 5);\n  bot.chat(\"5 cactus blocks mined.\");\n\n  // Collect the dropped cactus items\n  for (const cactusBlock of cactusBlocks) {\n    await bot.pathfinder.goto(new GoalBlock(cactusBlock.x, cactusBlock.y, cactusBlock.z));\n  }\n  bot.chat(\"Collected 5 cactus blocks.\");\n}", "description": "async function collectFiveCactusBlocks(bot) {\n    // The function is about collecting 5 cactus blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 cactus blocks using the `exploreUntil` function. If 5 cactus blocks are not found, return. Otherwise, mine the 5 cactus blocks using the `mineBlock` function. Finally, collect the dropped cactus items by moving to each block's location.\n}"}, "smeltCactusIntoGreenDye": {"code": "async function smeltCactusIntoGreenDye(bot) {\n  // Check if there is a furnace in the inventory\n  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n\n  // If not, craft a furnace using the available cobblestone\n  if (!furnaceItem) {\n    await craftFurnace(bot);\n  }\n\n  // Find a suitable position to place the furnace\n  const furnacePosition = await findSuitablePosition(bot);\n  if (!furnacePosition) {\n    bot.chat(\"Could not find a suitable position to place the furnace.\");\n    return;\n  }\n\n  // Place the furnace at the suitable position\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 5 cactus using the available coal as fuel\n  await smeltItem(bot, \"cactus\", \"coal\", 5);\n  bot.chat(\"5 cactus smelted into green dye.\");\n}", "description": "async function smeltCactusIntoGreenDye(bot) {\n    // The function is about smelting 5 cactus into green dye using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. Finally, it smelts the cactus using coal as fuel and saves the event of smelting 5 cactus into green dye.\n}"}, "craftShears": {"code": "async function craftShears(bot) {\n  // Place the crafting table near the bot\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a pair of shears using the crafting table\n  await craftItem(bot, \"shears\", 1);\n  bot.chat(\"Crafted a pair of shears.\");\n}", "description": "async function craftShears(bot) {\n    // The function is about crafting a pair of shears. First, place a crafting table near the bot. Then, craft a pair of shears using the crafting table. Finally, the bot will chat that it has crafted a pair of shears.\n}"}}


================================================
FILE: skill_library/trial1/skill/code/collectBamboo.js
================================================
async function collectBamboo(bot) {
  // Equip the iron sword
  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
  await bot.equip(ironSword, "hand");

  // Find bamboo plants using the exploreUntil function
  const bambooPlants = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const bambooPlants = bot.findBlocks({
      matching: block => block.name === "bamboo",
      maxDistance: 32,
      count: 10
    });
    return bambooPlants.length >= 10 ? bambooPlants : null;
  });
  if (!bambooPlants) {
    bot.chat("Could not find enough bamboo plants.");
    return;
  }

  // Break 10 bamboo plants using the iron sword
  for (const bambooPlant of bambooPlants) {
    const block = bot.blockAt(bambooPlant);
    await bot.dig(block);
  }
  bot.chat("Broke 10 bamboo plants.");

  // Collect the dropped bamboo items
  for (const bambooPlant of bambooPlants) {
    await bot.pathfinder.goto(new GoalBlock(bambooPlant.x, bambooPlant.y, bambooPlant.z));
  }
  bot.chat("Collected 10 bamboo.");
}


================================================
FILE: skill_library/trial1/skill/code/collectFiveCactusBlocks.js
================================================
async function collectFiveCactusBlocks(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
  await bot.equip(ironPickaxe, "hand");

  // Find 5 cactus blocks using the exploreUntil function
  const cactusBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const cactusBlocks = bot.findBlocks({
      matching: block => block.name === "cactus",
      maxDistance: 32,
      count: 5
    });
    return cactusBlocks.length >= 5 ? cactusBlocks : null;
  });
  if (!cactusBlocks) {
    bot.chat("Could not find enough cactus blocks.");
    return;
  }

  // Mine the 5 cactus blocks using the mineBlock function
  await mineBlock(bot, "cactus", 5);
  bot.chat("5 cactus blocks mined.");

  // Collect the dropped cactus items
  for (const cactusBlock of cactusBlocks) {
    await bot.pathfinder.goto(new GoalBlock(cactusBlock.x, cactusBlock.y, cactusBlock.z));
  }
  bot.chat("Collected 5 cactus blocks.");
}


================================================
FILE: skill_library/trial1/skill/code/cookPorkchops.js
================================================
async function cookPorkchops(bot) {
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Place the furnace near the bot
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 2 porkchops using the available coal as fuel
  await smeltItem(bot, "porkchop", "coal", 2);
  bot.chat("2 porkchops cooked.");
}


================================================
FILE: skill_library/trial1/skill/code/cookSevenMutton.js
================================================
async function cookSevenMutton(bot) {
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Find a suitable position to place the furnace
  const furnacePosition = await findSuitablePosition(bot);
  if (!furnacePosition) {
    bot.chat("Could not find a suitable position to place the furnace.");
    return;
  }

  // Place the furnace at the suitable position
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 7 raw mutton using the available coal as fuel
  await smeltItem(bot, "mutton", "coal", 7);
  bot.chat("7 mutton cooked.");
}


================================================
FILE: skill_library/trial1/skill/code/craftAcaciaPlanksAndSticks.js
================================================
async function craftAcaciaPlanksAndSticks(bot) {
  // Check if there are enough acacia logs in the inventory
  const acaciaLogsCount = bot.inventory.count(mcData.itemsByName.acacia_log.id);

  // If not, mine more acacia logs
  if (acaciaLogsCount < 5) {
    await mineBlock(bot, "acacia_log", 5 - acaciaLogsCount);
    bot.chat("Mined acacia logs.");
  }

  // Craft 20 acacia planks from acacia logs
  await craftItem(bot, "acacia_planks", 5);
  bot.chat("Crafted 20 acacia planks.");

  // Check if there are enough acacia planks in the inventory to craft 10 sticks
  const acaciaPlanksCount = bot.inventory.count(mcData.itemsByName.acacia_planks.id);

  // If not, mine more acacia logs and craft more acacia planks
  if (acaciaPlanksCount < 5) {
    await mineBlock(bot, "acacia_log", 5 - acaciaLogsCount);
    bot.chat("Mined more acacia logs.");
    await craftItem(bot, "acacia_planks", 5 - acaciaPlanksCount);
    bot.chat("Crafted more acacia planks.");
  }

  // Craft 10 sticks from acacia planks
  await craftItem(bot, "stick", 3);
  bot.chat("Crafted 10 sticks.");
}


================================================
FILE: skill_library/trial1/skill/code/craftBucket.js
================================================
async function craftBucket(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  if (ironIngotsCount < 3) {
    await mineBlock(bot, "iron_ore", 3 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 3 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a bucket using the crafting table
  await craftItem(bot, "bucket", 1);
  bot.chat("Crafted a bucket.");
}


================================================
FILE: skill_library/trial1/skill/code/craftChest.js
================================================
async function craftChest(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 8) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((8 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a chest using the crafting table
  await craftItem(bot, "chest", 1);
  bot.chat("Crafted a chest.");
}


================================================
FILE: skill_library/trial1/skill/code/craftCopperBlock.js
================================================
async function craftCopperBlock(bot) {
  // Check if there are enough copper ingots in the inventory
  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);

  // If not enough copper ingots, mine copper ores and smelt them into copper ingots
  if (copperIngotsCount < 9) {
    await mineBlock(bot, "copper_ore", 9 - copperIngotsCount);
    bot.chat("Collected copper ores.");
    await smeltItem(bot, "copper_ore", "coal", 9 - copperIngotsCount);
    bot.chat("Smelted copper ores into copper ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a copper block using the crafting table
  await craftItem(bot, "copper_block", 1);
  bot.chat("Crafted a copper block.");
}


================================================
FILE: skill_library/trial1/skill/code/craftCraftingTable.js
================================================
async function craftCraftingTable(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 4) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((4 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Craft a crafting table using oak planks
  await craftItem(bot, "crafting_table", 1);
  bot.chat("Crafted a crafting table.");
}


================================================
FILE: skill_library/trial1/skill/code/craftFurnace.js
================================================
async function craftFurnace(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);

  // If not, mine the required cobblestones
  if (cobblestoneCount < 8) {
    await mineBlock(bot, "stone", 8 - cobblestoneCount);
    bot.chat("Collected cobblestone.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a furnace using the crafting table
  await craftItem(bot, "furnace", 1);
  bot.chat("Crafted a furnace.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronAxe.js
================================================
async function craftIronAxe(bot) {
  // Check if there are enough iron ingots and sticks in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough iron ingots or sticks, collect the required items
  if (ironIngotsCount < 3) {
    await mineBlock(bot, "iron_ore", 3 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 3 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron axe using the crafting table
  await craftItem(bot, "iron_axe", 1);
  bot.chat("Crafted an iron axe.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronChestplate.js
================================================
async function craftIronChestplate(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  if (ironIngotsCount < 8) {
    await mineBlock(bot, "iron_ore", 8 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 8 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron chestplate using the crafting table
  await craftItem(bot, "iron_chestplate", 1);
  bot.chat("Crafted an iron chestplate.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronHelmet.js
================================================
async function craftIronHelmet(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  if (ironIngotsCount < 5) {
    await mineBlock(bot, "iron_ore", 5 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 5 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron helmet using the crafting table
  await craftItem(bot, "iron_helmet", 1);
  bot.chat("Crafted an iron helmet.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronHelmetV2.js
================================================
async function craftIronHelmet(bot) {
  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron helmet using the crafting table
  await craftItem(bot, "iron_helmet", 1);
  bot.chat("Crafted an iron helmet.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronLeggingsAndBoots.js
================================================
async function craftIronLeggingsAndBoots(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  if (ironIngotsCount < 11) {
    await mineBlock(bot, "iron_ore", 11 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 11 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft iron leggings using the crafting table
  await craftItem(bot, "iron_leggings", 1);
  bot.chat("Crafted iron leggings.");

  // Craft iron boots using the crafting table
  await craftItem(bot, "iron_boots", 1);
  bot.chat("Crafted iron boots.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronPickaxe.js
================================================
async function craftIronPickaxe(bot) {
  // Check if there are enough iron ingots and sticks in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough iron ingots or sticks, collect the required items
  if (ironIngotsCount < 3) {
    await mineBlock(bot, "iron_ore", 3 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 3 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron pickaxe using the crafting table
  await craftItem(bot, "iron_pickaxe", 1);
  bot.chat("Crafted an iron pickaxe.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronPickaxeV2.js
================================================
async function craftIronPickaxe(bot) {
  // Check if there are enough iron ingots and sticks in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough iron ingots or sticks, collect the required items
  if (ironIngotsCount < 3) {
    await mineBlock(bot, "iron_ore", 3 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 3 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron pickaxe using the crafting table
  await craftItem(bot, "iron_pickaxe", 1);
  bot.chat("Crafted an iron pickaxe.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronShovel.js
================================================
async function craftIronShovel(bot) {
  // Check if there are enough iron ingots and sticks in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough iron ingots or sticks, collect the required items
  if (ironIngotsCount < 1) {
    await mineBlock(bot, "iron_ore", 1);
    bot.chat("Collected iron ore.");
    await smeltItem(bot, "iron_ore", "coal", 1);
    bot.chat("Smelted iron ore into iron ingot.");
  }
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Find a suitable position to place the crafting table
  const suitablePosition = bot.entity.position.offset(1, 0, 0);
  const block = bot.blockAt(suitablePosition);
  if (block.name === "grass_block" || block.name === "dirt") {
    await bot.dig(block);
  }

  // Place the crafting table at the suitable position
  await placeItem(bot, "crafting_table", suitablePosition);

  // Craft an iron shovel using the crafting table
  await craftItem(bot, "iron_shovel", 1);
  bot.chat("Crafted an iron shovel.");
}


================================================
FILE: skill_library/trial1/skill/code/craftIronSword.js
================================================
async function craftIronSword(bot) {
  // Check if there are enough iron ingots and sticks in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough iron ingots or sticks, collect the required items
  if (ironIngotsCount < 2) {
    await mineBlock(bot, "iron_ore", 2 - ironIngotsCount);
    bot.chat("Collected iron ores.");
    await smeltItem(bot, "iron_ore", "coal", 2 - ironIngotsCount);
    bot.chat("Smelted iron ores into iron ingots.");
  }
  if (sticksCount < 1) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron sword using the crafting table
  await craftItem(bot, "iron_sword", 1);
  bot.chat("Crafted an iron sword.");
}


================================================
FILE: skill_library/trial1/skill/code/craftLightningRod.js
================================================
async function findSuitablePosition(bot) {
  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];
  for (const offset of offsets) {
    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);
    const block = bot.blockAt(position);
    if (block.name === "air") {
      return position;
    }
  }
  return null;
}

async function craftLightningRod(bot) {
  // Find a suitable position to place the crafting table
  const craftingTablePosition = await findSuitablePosition(bot);

  // Place the crafting table at the found position
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Check if there are enough copper ingots in the inventory
  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);

  // If not enough copper ingots, mine copper ores and smelt them into copper ingots
  if (copperIngotsCount < 3) {
    await mineBlock(bot, "copper_ore", 3 - copperIngotsCount);
    bot.chat("Collected copper ores.");
    await smeltItem(bot, "copper_ore", "coal", 3 - copperIngotsCount);
    bot.chat("Smelted copper ores into copper ingots.");
  }

  // Craft a lightning rod using the crafting table
  await craftItem(bot, "lightning_rod", 1);
  bot.chat("Crafted a lightning rod.");
}


================================================
FILE: skill_library/trial1/skill/code/craftOakPlanksAndSticks.js
================================================
async function craftOakPlanksAndSticks(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 8) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((8 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Check if there are enough sticks in the inventory
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not, craft sticks from oak planks
  if (sticksCount < 4) {
    await craftItem(bot, "stick", 2);
    bot.chat("Crafted sticks.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/craftScaffolding.js
================================================
async function craftScaffolding(bot) {
  // Check if we have a crafting table in the inventory
  const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);

  // If not, craft a crafting table
  if (craftingTableCount === 0) {
    await craftItem(bot, "crafting_table", 1);
    bot.chat("Crafted a crafting table.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft 10 scaffolding using the crafting table
  await craftItem(bot, "scaffolding", 1);
  bot.chat("Crafted 10 scaffolding.");
}


================================================
FILE: skill_library/trial1/skill/code/craftShears.js
================================================
async function craftShears(bot) {
  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a pair of shears using the crafting table
  await craftItem(bot, "shears", 1);
  bot.chat("Crafted a pair of shears.");
}


================================================
FILE: skill_library/trial1/skill/code/craftShieldImproved.js
================================================
async function craftShieldImproved(bot) {
  // Check if there are enough oak planks in the inventory
  let oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, check if there are enough oak logs in the inventory
  if (oakPlanksCount < 6) {
    let oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((6 - oakPlanksCount) / 4);

    // If not, explore to find and mine oak logs
    if (oakLogsCount < planksToCraft) {
      await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const oak_log = bot.findBlock({
          matching: mcData.blocksByName["oak_log"].id,
          maxDistance: 32
        });
        return oak_log;
      });
      await mineBlock(bot, "oak_log", planksToCraft - oakLogsCount);
      bot.chat("Collected oak logs.");
    }

    // Craft oak planks from oak logs
    await craftItem(bot, "oak_planks", planksToCraft);
    bot.chat("Crafted oak planks.");
    oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);
  }

  // Check if there are enough iron ingots in the inventory
  let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not, explore to find and mine iron ores
  if (ironIngotsCount < 1) {
    await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
      const iron_ore = bot.findBlock({
        matching: mcData.blocksByName["iron_ore"].id,
        maxDistance: 32
      });
      return iron_ore;
    });
    await mineBlock(bot, "iron_ore", 1);
    bot.chat("Collected iron ores.");

    // Smelt iron ores into iron ingots
    await smeltItem(bot, "iron_ore", "coal", 1);
    bot.chat("Smelted iron ores into iron ingots.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a shield using the crafting table
  await craftItem(bot, "shield", 1);
  bot.chat("Crafted a shield.");
}


================================================
FILE: skill_library/trial1/skill/code/craftStonePickaxe.js
================================================
async function craftStonePickaxe(bot) {
  // Check if there are enough cobblestone and sticks in the inventory
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough cobblestone or sticks, collect the required items
  if (cobblestoneCount < 3) {
    await mineBlock(bot, "stone", 3 - cobblestoneCount);
    bot.chat("Collected cobblestone.");
  }
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone pickaxe using the crafting table
  await craftItem(bot, "stone_pickaxe", 1);
  bot.chat("Crafted a stone pickaxe.");
}


================================================
FILE: skill_library/trial1/skill/code/craftStoneShovel.js
================================================
async function craftStoneShovel(bot) {
  // Check if there are enough cobblestone and sticks in the inventory
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not enough cobblestone, mine cobblestone
  if (cobblestoneCount < 1) {
    await mineBlock(bot, "stone", 1);
    bot.chat("Collected cobblestone.");
  }

  // If not enough sticks, craft sticks
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone shovel using the crafting table
  await craftItem(bot, "stone_shovel", 1);
  bot.chat("Crafted a stone shovel.");
}


================================================
FILE: skill_library/trial1/skill/code/craftWhiteBed.js
================================================
async function craftWhiteBed(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 3) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((3 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Check if there are enough white wool in the inventory
  const whiteWoolCount = bot.inventory.count(mcData.itemsByName.white_wool.id);
  if (whiteWoolCount < 3) {
    bot.chat("Not enough white wool to craft a bed.");
    return;
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a white bed using the crafting table
  await craftItem(bot, "white_bed", 1);
  bot.chat("Crafted a white bed.");
}


================================================
FILE: skill_library/trial1/skill/code/craftWoodenHoe.js
================================================
async function craftWoodenHoe(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 2) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((2 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Check if there are enough sticks in the inventory
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not, craft sticks from oak planks
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a wooden hoe using the crafting table
  await craftItem(bot, "wooden_hoe", 1);
  bot.chat("Crafted a wooden hoe.");
}


================================================
FILE: skill_library/trial1/skill/code/craftWoodenPickaxe.js
================================================
async function craftWoodenPickaxe(bot) {
  // check if crafting table is in the inventory
  const craftingTableCount = bot.inventory.count(
    mcData.itemsByName.crafting_table.id
  );

  // If not, craft a crafting table
  if (craftingTableCount === 0) {
    await craftCraftingTable(bot);
  }

  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 6) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((6 - oakPlanksCount) / 4);
    if (oakLogsCount < planksToCraft) {
      await mineBlock(bot, "oak_log", planksToCraft - oakLogsCount);
    }
    await craftItem(bot, "oak_planks", planksToCraft);
    bot.chat("Crafted oak planks.");
  }

  // Check if there are enough sticks in the inventory
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not, craft sticks from oak planks
  if (sticksCount < 2) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a wooden pickaxe using the crafting table
  await craftItem(bot, "wooden_pickaxe", 1);
  bot.chat("Crafted a wooden pickaxe.");
}



================================================
FILE: skill_library/trial1/skill/code/craftWoodenSword.js
================================================
async function craftWoodenSword(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanksCount = bot.inventory.count(mcData.itemsByName.oak_planks.id);

  // If not, craft oak planks from oak logs
  if (oakPlanksCount < 2) {
    const oakLogsCount = bot.inventory.count(mcData.itemsByName.oak_log.id);
    const planksToCraft = Math.ceil((2 - oakPlanksCount) / 4);
    if (oakLogsCount >= planksToCraft) {
      await craftItem(bot, "oak_planks", planksToCraft);
      bot.chat("Crafted oak planks.");
    } else {
      bot.chat("Not enough oak logs to craft oak planks.");
      return;
    }
  }

  // Check if there are enough sticks in the inventory
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

  // If not, craft sticks from oak planks
  if (sticksCount < 1) {
    await craftItem(bot, "stick", 1);
    bot.chat("Crafted sticks.");
  }

  // Place the crafting table near the bot
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a wooden sword using the crafting table
  await craftItem(bot, "wooden_sword", 1);
  bot.chat("Crafted a wooden sword.");
}


================================================
FILE: skill_library/trial1/skill/code/eatCookedPorkchop.js
================================================
async function eatCookedPorkchop(bot) {
  // Equip the cooked porkchop in the bot's hand
  const cookedPorkchop = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_porkchop.id);
  await bot.equip(cookedPorkchop, "hand");

  // Consume the cooked porkchop
  await bot.consume();

  // Send a chat message to indicate the task is completed
  bot.chat("Ate 1 cooked porkchop.");
}


================================================
FILE: skill_library/trial1/skill/code/eatTwoCookedMutton.js
================================================
async function eatTwoCookedMutton(bot) {
  // Check if there are 2 cooked mutton in the inventory
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);
  if (!cookedMutton || cookedMutton.count < 2) {
    bot.chat("Not enough cooked mutton in the inventory.");
    return;
  }

  // Equip the cooked mutton in the bot's hand
  await bot.equip(cookedMutton, "hand");

  // Consume the cooked mutton twice
  await bot.consume();
  await bot.consume();

  // Send a chat message to indicate the task is completed
  bot.chat("Ate 2 cooked mutton.");
}


================================================
FILE: skill_library/trial1/skill/code/equipIronArmor.js
================================================
async function equipIronArmor(bot) {
  // Find the iron_leggings, iron_boots, and iron_helmet in the inventory
  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id);
  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id);
  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id);

  // Equip the iron_leggings, iron_boots, and iron_helmet in the appropriate slots (legs, feet, and head)
  if (ironLeggings) {
    await bot.equip(ironLeggings, "legs");
    bot.chat("Equipped iron leggings.");
  } else {
    bot.chat("Iron leggings not found in inventory.");
  }
  if (ironBoots) {
    await bot.equip(ironBoots, "feet");
    bot.chat("Equipped iron boots.");
  } else {
    bot.chat("Iron boots not found in inventory.");
  }
  if (ironHelmet) {
    await bot.equip(ironHelmet, "head");
    bot.chat("Equipped iron helmet.");
  } else {
    bot.chat("Iron helmet not found in inventory.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/equipIronChestplate.js
================================================
async function equipIronChestplate(bot) {
  // Find the iron chestplate in the inventory
  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id);

  // Equip the iron chestplate
  if (ironChestplate) {
    await bot.equip(ironChestplate, "torso");
    bot.chat("Equipped iron chestplate.");
  } else {
    bot.chat("Iron chestplate not found in inventory.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/equipIronSword.js
================================================
async function equipIronSword(bot) {
  // Find the iron sword in the inventory
  let ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);

  // If the iron sword is not found in the inventory, check the chest
  if (!ironSword) {
    const chestPosition = new Vec3(89, 41, 206);
    const itemsToGet = {
      "iron_sword": 1
    };
    await getItemFromChest(bot, chestPosition, itemsToGet);
    ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
  }

  // Equip the iron sword
  if (ironSword) {
    await bot.equip(ironSword, "hand");
    bot.chat("Equipped iron sword.");
  } else {
    bot.chat("Iron sword not found in inventory or chest.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/fillBucketWithWater.js
================================================
async function fillBucketWithWater(bot) {
  // Find a water block nearby
  const waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const water = bot.findBlock({
      matching: mcData.blocksByName.water.id,
      maxDistance: 32,
    });
    return water;
  });
  if (!waterBlock) {
    bot.chat("Could not find water.");
    return;
  }

  const adjacentBlock = waterBlock.position.offset(0, 1, 0);
  // Go to the water block
  await bot.pathfinder.goto(
    new GoalGetToBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z)
  );

  // Equip the bucket
  const bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);
  await bot.equip(bucket, "hand");

  // Look at the water block
  await bot.lookAt(waterBlock.position);

  // Activate the bucket to collect water
  await bot.activateItem();
  bot.chat("Filled the bucket with water.");
}



================================================
FILE: skill_library/trial1/skill/code/killFourSheep.js
================================================
async function killFourSheep(bot) {
  // Equip the wooden sword
  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
  await bot.equip(woodenSword, "hand");

  // Find and kill the first three sheep
  for (let i = 1; i <= 3; i++) {
    await killMob(bot, "sheep", 300);
    bot.chat(`Killed sheep ${i}.`);
  }

  // Find and kill the fourth sheep
  await killMob(bot, "sheep", 300);
  bot.chat("Killed the fourth sheep.");

  // Collect the dropped items from the killed sheep
  const sheepDrops = ["wool", "raw_mutton"];
  for (const drop of sheepDrops) {
    const droppedItem = bot.findBlock({
      matching: block => block.name === drop,
      maxDistance: 32
    });
    if (droppedItem) {
      await bot.pathfinder.goto(new GoalBlock(droppedItem.position.x, droppedItem.position.y, droppedItem.position.z));
    }
  }
  bot.chat("Collected dropped items from the killed sheep.");
}


================================================
FILE: skill_library/trial1/skill/code/killOneEnderman.js
================================================
async function killOneEnderman(bot) {
  // Equip the iron sword
  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
  await bot.equip(ironSword, "hand");

  // Find the nearest enderman
  const enderman = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const enderman = bot.nearestEntity(entity => {
      return entity.name === "enderman" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return enderman;
  });
  if (!enderman) {
    bot.chat("Could not find an enderman.");
    return;
  }

  // Kill the enderman using the iron sword
  await killMob(bot, "enderman", 300);
  bot.chat("Killed an enderman.");

  // Collect the dropped items
  await bot.pathfinder.goto(new GoalBlock(enderman.position.x, enderman.position.y, enderman.position.z));
  bot.chat("Collected dropped items.");
}


================================================
FILE: skill_library/trial1/skill/code/killOnePig.js
================================================
async function killOnePig(bot) {
  // Equip the wooden sword
  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
  await bot.equip(woodenSword, "hand");

  // Find the nearest pig
  const pig = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const pig = bot.nearestEntity(entity => {
      return entity.name === "pig" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return pig;
  });
  if (!pig) {
    bot.chat("Could not find a pig.");
    return;
  }

  // Kill the pig using the wooden sword
  await killMob(bot, "pig", 300);
  bot.chat("Killed a pig.");

  // Collect the dropped items
  await bot.pathfinder.goto(new GoalBlock(pig.position.x, pig.position.y, pig.position.z));
  bot.chat("Collected dropped items.");
}


================================================
FILE: skill_library/trial1/skill/code/killOneSpider.js
================================================
async function killOneSpider(bot) {
  // Equip the iron sword
  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
  await bot.equip(ironSword, "hand");

  // Find the nearest spider
  const spider = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const spider = bot.nearestEntity(entity => {
      return entity.name === "spider" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return spider;
  });
  if (!spider) {
    bot.chat("Could not find a spider.");
    return;
  }

  // Kill the spider using the iron sword
  await killMob(bot, "spider", 300);
  bot.chat("Killed a spider.");

  // Collect the dropped items
  await bot.pathfinder.goto(new GoalBlock(spider.position.x, spider.position.y, spider.position.z));
  bot.chat("Collected dropped items.");
}


================================================
FILE: skill_library/trial1/skill/code/killOneZombie.js
================================================
async function killOneZombie(bot) {
  // Equip the iron sword
  const ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
  await bot.equip(ironSword, "hand");

  // Find the nearest zombie
  const zombie = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const zombie = bot.nearestEntity(entity => {
      return entity.name === "zombie" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return zombie;
  });
  if (!zombie) {
    bot.chat("Could not find a zombie.");
    return;
  }

  // Kill the zombie using the iron sword
  await killMob(bot, "zombie", 300);
  bot.chat("Killed a zombie.");

  // Collect the dropped items
  await bot.pathfinder.goto(new GoalBlock(zombie.position.x, zombie.position.y, zombie.position.z));
  bot.chat("Collected dropped items.");
}


================================================
FILE: skill_library/trial1/skill/code/killTwoPigs.js
================================================
async function killTwoPigs(bot) {
  // Equip the wooden sword
  const woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
  await bot.equip(woodenSword, "hand");

  // Find and kill the first pig
  await killMob(bot, "pig", 300);
  bot.chat("Killed the first pig.");

  // Find and kill the second pig
  await killMob(bot, "pig", 300);
  bot.chat("Killed the second pig.");

  // Collect the dropped items from the killed pigs
  const pigDrops = ["raw_porkchop"];
  for (const drop of pigDrops) {
    const droppedItem = bot.findBlock({
      matching: block => block.name === drop,
      maxDistance: 32
    });
    if (droppedItem) {
      await bot.pathfinder.goto(new GoalBlock(droppedItem.position.x, droppedItem.position.y, droppedItem.position.z));
    }
  }
  bot.chat("Collected dropped items from the killed pigs.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveCoalOres.js
================================================
async function mineFiveCoalOres(bot) {
  // Equip the wooden pickaxe
  const woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
  await bot.equip(woodenPickaxe, "hand");

  // Find 5 coal_ore blocks
  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const coalOres = bot.findBlocks({
      matching: block => block.name === "coal_ore",
      maxDistance: 32,
      count: 5
    });
    return coalOres.length >= 5 ? coalOres : null;
  });
  if (!coalOres) {
    bot.chat("Could not find enough coal ores.");
    return;
  }

  // Mine the 5 coal_ore blocks
  await mineBlock(bot, "coal_ore", 5);
  bot.chat("5 coal ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveCoalOresV2.js
================================================
async function mineFiveCoalOres(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  await bot.equip(stonePickaxe, "hand");

  // Find 5 coal_ore blocks
  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const coalOres = bot.findBlocks({
      matching: block => block.name === "coal_ore",
      maxDistance: 32,
      count: 5
    });
    return coalOres.length >= 5 ? coalOres : null;
  });
  if (!coalOres) {
    bot.chat("Could not find enough coal ores.");
    return;
  }

  // Mine the 5 coal_ore blocks
  await mineBlock(bot, "coal_ore", 5);
  bot.chat("5 coal ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveCopperOres.js
================================================
async function mineFiveCopperOres(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  await bot.equip(stonePickaxe, "hand");

  // Find 5 copper_ore blocks
  const copperOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const copperOres = bot.findBlocks({
      matching: block => block.name === "copper_ore",
      maxDistance: 32,
      count: 5
    });
    return copperOres.length >= 5 ? copperOres : null;
  });
  if (!copperOres) {
    bot.chat("Could not find enough copper ores.");
    return;
  }

  // Mine the 5 copper_ore blocks
  await mineBlock(bot, "copper_ore", 5);
  bot.chat("5 copper ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveCopperOresV2.js
================================================
async function mineFiveCopperOres(bot) {
  // Check if the bot already has 5 or more copper ores in the inventory
  const copperOres = bot.inventory.items().filter(item => item.name === "copper_ore");
  const totalCopperOres = copperOres.reduce((total, item) => total + item.count, 0);
  if (totalCopperOres >= 5) {
    bot.chat("Task already completed. There are already " + totalCopperOres + " copper ores in the inventory.");
  } else {
    bot.chat("Need to mine " + (5 - totalCopperOres) + " more copper ores.");
    // You can call the mineFiveCopperOres function from the previous response here
  }
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveIronOres.js
================================================
async function mineFiveIronOres(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  await bot.equip(stonePickaxe, "hand");

  // Find 5 iron_ore blocks
  const ironOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const ironOres = bot.findBlocks({
      matching: block => block.name === "iron_ore",
      maxDistance: 32,
      count: 5
    });
    return ironOres.length >= 5 ? ironOres : null;
  });
  if (!ironOres) {
    bot.chat("Could not find enough iron ores.");
    return;
  }

  // Mine the 5 iron_ore blocks
  await mineBlock(bot, "iron_ore", 5);
  bot.chat("5 iron ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveIronOresV2.js
================================================
async function mineFiveIronOres(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  await bot.equip(stonePickaxe, "hand");

  // Find 5 iron_ore blocks
  const ironOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const ironOres = bot.findBlocks({
      matching: block => block.name === "iron_ore",
      maxDistance: 32,
      count: 5
    });
    return ironOres.length >= 5 ? ironOres : null;
  });
  if (!ironOres) {
    bot.chat("Could not find enough iron ores.");
    return;
  }

  // Mine the 5 iron_ore blocks
  await mineBlock(bot, "iron_ore", 5);
  bot.chat("5 iron ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineFiveLapisLazuliOres.js
================================================
async function mineFiveLapisLazuliOres(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
  await bot.equip(ironPickaxe, "hand");

  // Find 5 lapis_lazuli_ore blocks
  const lapisOres = await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {
    const lapisOres = bot.findBlocks({
      matching: block => block.name === "lapis_ore",
      maxDistance: 32,
      count: 5
    });
    return lapisOres.length >= 5 ? lapisOres : null;
  });
  if (!lapisOres) {
    bot.chat("Could not find enough lapis lazuli ores.");
    return;
  }

  // Mine the 5 lapis_lazuli_ore blocks
  await mineBlock(bot, "lapis_ore", 5);
  bot.chat("5 lapis lazuli ores mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineTenCobblestone.js
================================================
async function mineTenCobblestone(bot) {
  // Check if the bot has a pickaxe in the inventory
  const pickaxe = bot.inventory.items().find(item => item.name.endsWith("_pickaxe"));

  // If not, craft a wooden pickaxe using the available resources in the inventory
  if (!pickaxe) {
    await craftWoodenPickaxe(bot);
  } else {
    // Equip the pickaxe
    await bot.equip(pickaxe, "hand");
  }

  // Use the exploreUntil function to find cobblestone blocks
  const cobblestoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const cobblestoneBlocks = bot.findBlocks({
      matching: block => block.name === "stone",
      maxDistance: 32,
      count: 10
    });
    return cobblestoneBlocks.length >= 10 ? cobblestoneBlocks : null;
  });
  if (!cobblestoneBlocks) {
    bot.chat("Could not find enough cobblestone.");
    return;
  }

  // Mine 10 cobblestone blocks using the mineBlock function
  await mineBlock(bot, "stone", 10);
  bot.chat("10 cobblestone mined.");
}


================================================
FILE: skill_library/trial1/skill/code/mineThreeMoreOakLogs.js
================================================
async function mineThreeMoreOakLogs(bot) {
  // Check the initial inventory for oak logs
  const initialOakLogs = bot.inventory.count(mcData.itemsByName.oak_log.id);

  // Find 3 oak_log blocks
  const oakLogs = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const oakLogs = bot.findBlocks({
      matching: block => block.name === "oak_log",
      maxDistance: 32,
      count: 3
    });
    return oakLogs.length >= 3 ? oakLogs : null;
  });
  if (!oakLogs) {
    bot.chat("Could not find enough oak logs.");
    return;
  }

  // Mine the oak_log blocks
  await mineBlock(bot, "oak_log", 3);
  bot.chat("3 oak logs mined.");

  // Compare the final inventory with the initial inventory
  const finalOakLogs = bot.inventory.count(mcData.itemsByName.oak_log.id);
  if (finalOakLogs - initialOakLogs === 3) {
    bot.chat("Successfully mined 3 more oak logs.");
  } else {
    bot.chat("Failed to mine 3 more oak logs.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/mineWoodLog.js
================================================
async function mineWoodLog(bot) {
  const woodLogNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];

  // Find a wood log block
  const woodLogBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    return bot.findBlock({
      matching: block => woodLogNames.includes(block.name),
      maxDistance: 32
    });
  });
  if (!woodLogBlock) {
    bot.chat("Could not find a wood log.");
    return;
  }

  // Mine the wood log block
  await mineBlock(bot, woodLogBlock.name, 1);
  bot.chat("Wood log mined.");
}


================================================
FILE: skill_library/trial1/skill/code/obtainOneMoreAcaciaLog.js
================================================
async function obtainOneMoreAcaciaLog(bot) {
  // Check the initial inventory for acacia logs
  const initialAcaciaLogs = bot.inventory.count(mcData.itemsByName.acacia_log.id);

  // If the number of acacia logs is less than 5, find and mine one more acacia log
  if (initialAcaciaLogs < 5) {
    const acaciaLog = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      return bot.findBlock({
        matching: block => block.name === "acacia_log",
        maxDistance: 32
      });
    });
    if (!acaciaLog) {
      bot.chat("Could not find an acacia log.");
      return;
    }
    await mineBlock(bot, "acacia_log", 1);
    bot.chat("1 more acacia log obtained.");
  }

  // Check the final number of acacia logs in the inventory
  const finalAcaciaLogs = bot.inventory.count(mcData.itemsByName.acacia_log.id);
  if (finalAcaciaLogs >= 5) {
    bot.chat("Successfully obtained 5 acacia logs.");
  } else {
    bot.chat("Failed to obtain 5 acacia logs.");
  }
}


================================================
FILE: skill_library/trial1/skill/code/smeltCactusIntoGreenDye.js
================================================
async function smeltCactusIntoGreenDye(bot) {
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Find a suitable position to place the furnace
  const furnacePosition = await findSuitablePosition(bot);
  if (!furnacePosition) {
    bot.chat("Could not find a suitable position to place the furnace.");
    return;
  }

  // Place the furnace at the suitable position
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 5 cactus using the available coal as fuel
  await smeltItem(bot, "cactus", "coal", 5);
  bot.chat("5 cactus smelted into green dye.");
}


================================================
FILE: skill_library/trial1/skill/code/smeltFiveRawIron.js
================================================
async function smeltFiveRawIron(bot) {
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Place the furnace near the bot
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 5 raw iron using the available coal as fuel
  await smeltItem(bot, "raw_iron", "coal", 5);
  bot.chat("5 raw iron smelted.");
}


================================================
FILE: skill_library/trial1/skill/code/smeltFiveRawIronV2.js
================================================
async function findSuitablePosition(bot) {
  const offsets = [
    new Vec3(1, 0, 0),
    new Vec3(-1, 0, 0),
    new Vec3(0, 0, 1),
    new Vec3(0, 0, -1),
  ];
  for (const offset of offsets) {
    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);
    const block = bot.blockAt(position);
    if (block.name === "air") {
      return position;
    }
  }
  return null;
}

async function smeltFiveRawIron(bot) {
  // Check if there is coal in the inventory
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  // If not enough coal, mine coal_ore to obtain coal
  if (coalCount < 3) {
    await mineBlock(bot, "coal_ore", 3 - coalCount);
    bot.chat("Collected coal.");
  }
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(
    mcData.itemsByName.furnace.id
  );

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Find a suitable position to place the furnace
  const furnacePosition = await findSuitablePosition(bot);
  if (!furnacePosition) {
    bot.chat("Could not find a suitable position to place the furnace.");
    return;
  }

  // Place the furnace at the suitable position
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 5 raw iron using the available coal as fuel
  await smeltItem(bot, "raw_iron", "coal", 5);
  bot.chat("5 raw iron smelted.");
}



================================================
FILE: skill_library/trial1/skill/code/smeltRawCopper.js
================================================
async function smeltRawCopper(bot) {
  // Check if there is a furnace in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);

  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Find a suitable position to place the furnace
  const furnacePosition = await findSuitablePosition(bot);
  if (!furnacePosition) {
    bot.chat("Could not find a suitable position to place the furnace.");
    return;
  }

  // Place the furnace at the suitable position
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 19 raw copper using the available coal as fuel
  await smeltItem(bot, "raw_copper", "coal", 19);
  bot.chat("19 raw copper smelted.");
}


================================================
FILE: skill_library/trial1/skill/description/collectBamboo.txt
================================================
async function collectBamboo(bot) {
    // The function is about collecting 10 bamboo plants. It equips the iron sword and uses the `exploreUntil` function to find 10 bamboo plants within a certain distance. If enough bamboo plants are found, it breaks them using the iron sword and collects the dropped bamboo items by moving to their location. If not enough bamboo plants are found, it returns an error message.
}


================================================
FILE: skill_library/trial1/skill/description/collectFiveCactusBlocks.txt
================================================
async function collectFiveCactusBlocks(bot) {
    // The function is about collecting 5 cactus blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 cactus blocks using the `exploreUntil` function. If 5 cactus blocks are not found, return. Otherwise, mine the 5 cactus blocks using the `mineBlock` function. Finally, collect the dropped cactus items by moving to each block's location.
}


================================================
FILE: skill_library/trial1/skill/description/cookPorkchops.txt
================================================
async function cookPorkchops(bot) {
    // The function is about cooking 2 porkchops using a furnace and coal as fuel. First, it checks if there is a furnace in the inventory. If not, it crafts a furnace using cobblestone. Then, it places the furnace near the bot. Finally, it smelts 2 porkchops using coal as fuel and saves the event of cooking porkchops.
}


================================================
FILE: skill_library/trial1/skill/description/cookSevenMutton.txt
================================================
async function cookSevenMutton(bot) {
    // The function is about cooking 7 raw mutton using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. After that, it smelts 7 raw mutton using the available coal as fuel and saves the event of cooking 7 mutton.
}


================================================
FILE: skill_library/trial1/skill/description/craftAcaciaPlanksAndSticks.txt
================================================
async function craftAcaciaPlanksAndSticks(bot) {
    // The function is about crafting 20 acacia planks and 10 sticks. It checks if there are enough acacia logs in the inventory, and if not, it mines more acacia logs. Then it crafts 20 acacia planks from the acacia logs. If there are not enough acacia planks in the inventory to craft 10 sticks, it mines more acacia logs and crafts more acacia planks. Finally, it crafts 10 sticks from the acacia planks.
}


================================================
FILE: skill_library/trial1/skill/description/craftBucket.txt
================================================
async function craftBucket(bot) {
    // The function crafts a bucket using a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into iron ingots. Then, it places a crafting table near the bot and crafts a bucket using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftChest.txt
================================================
async function craftChest(bot) {
    // The function crafts a chest using a crafting table and oak planks. If there are not enough oak planks in the inventory, it crafts oak planks from oak logs. Once there are enough oak planks, it places a crafting table near the bot and crafts a chest using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftCopperBlock.txt
================================================
async function craftCopperBlock(bot) {
    // The function crafts a copper block using a crafting table. It first checks if there are enough copper ingots in the inventory, and if not, it mines copper ores and smelts them into copper ingots. Then it places a crafting table near the bot and crafts a copper block using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftCraftingTable.txt
================================================
async function craftCraftingTable(bot) {
    // The function crafts a crafting table using oak planks. It first checks if there are enough oak planks in the inventory, and if not, crafts oak planks from oak logs. Then, it crafts a crafting table using the oak planks.
}


================================================
FILE: skill_library/trial1/skill/description/craftFurnace.txt
================================================
async function craftFurnace(bot) {
    // The function crafts a furnace using a crafting table and cobblestones. If there are not enough cobblestones in the inventory, it mines the required amount. Then, it places a crafting table near the bot and crafts a furnace using the crafting table. Finally, it sends a chat message indicating that a furnace has been crafted.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronAxe.txt
================================================
async function craftIronAxe(bot) {
    // The function crafts an iron axe using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It then places a crafting table near the bot and crafts an iron axe using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronChestplate.txt
================================================
async function craftIronChestplate(bot) {
    // The function crafts an iron chestplate using a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into iron ingots. Then it places a crafting table near the bot and crafts an iron chestplate using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronHelmet.txt
================================================
async function craftIronHelmet(bot) {
    // The function crafts an iron helmet using a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into iron ingots. Then it places a crafting table near the bot and crafts an iron helmet using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronHelmetV2.txt
================================================
async function craftIronHelmet(bot) {
    // The function is about crafting an iron helmet using a crafting table. First, place the crafting table near the bot. Then, craft an iron helmet using the crafting table and save it to the inventory.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronLeggingsAndBoots.txt
================================================
async function craftIronLeggingsAndBoots(bot) {
    // The function crafts iron leggings and boots using a crafting table. If there are not enough iron ingots in the inventory, the bot mines iron ores and smelts them into iron ingots. Then, the bot places a crafting table near itself and crafts iron leggings and boots using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronPickaxe.txt
================================================
async function craftIronPickaxe(bot) {
    // The function crafts an iron pickaxe using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It then places a crafting table near the bot and crafts an iron pickaxe using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronPickaxeV2.txt
================================================
async function craftIronPickaxe(bot) {
    // The function crafts an iron pickaxe using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It then places a crafting table near the bot and crafts an iron pickaxe using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronShovel.txt
================================================
async function craftIronShovel(bot) {
    // The function crafts an iron shovel using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, collects the required items. It finds a suitable position to place the crafting table and places it there. Then, it crafts an iron shovel using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftIronSword.txt
================================================
async function craftIronSword(bot) {
    // The function crafts an iron sword using a crafting table. It checks if there are enough iron ingots and sticks in the inventory, and if not, it collects the required items. It then places a crafting table near the bot and crafts an iron sword using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftLightningRod.txt
================================================
async function craftLightningRod(bot) {
    // The function is about crafting a lightning rod. It first finds a suitable position to place the crafting table and places it there. Then it checks if there are enough copper ingots in the inventory, and if not, it mines copper ores and smelts them into copper ingots. Finally, it crafts a lightning rod using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftOakPlanksAndSticks.txt
================================================
async function craftOakPlanksAndSticks(bot) {
    // The function checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. If there are not enough oak planks, it crafts them from oak logs. If there are not enough sticks, it crafts them from oak planks.
}


================================================
FILE: skill_library/trial1/skill/description/craftScaffolding.txt
================================================
async function craftScaffolding(bot) {
    // The function is about crafting 10 scaffolding using a crafting table. First, it checks if there is a crafting table in the inventory. If not, it crafts one. Then, it places the crafting table near the bot. After that, it crafts 10 scaffolding using the crafting table and saves the event.
}


================================================
FILE: skill_library/trial1/skill/description/craftShears.txt
================================================
async function craftShears(bot) {
    // The function is about crafting a pair of shears. First, place a crafting table near the bot. Then, craft a pair of shears using the crafting table. Finally, the bot will chat that it has crafted a pair of shears.
}


================================================
FILE: skill_library/trial1/skill/description/craftShieldImproved.txt
================================================
async function craftShieldImproved(bot) {
    // The function crafts a shield using oak planks and iron ingots. It checks if there are enough oak planks and iron ingots in the inventory, and if not, it explores the environment to find and collect the required materials. It then places a crafting table near the bot and crafts a shield using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftStonePickaxe.txt
================================================
async function craftStonePickaxe(bot) {
    // The function crafts a stone pickaxe using cobblestone and sticks. It checks if there are enough cobblestone and sticks in the inventory, and if not, it collects the required items. Then, it places a crafting table near the bot and crafts a stone pickaxe using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftStoneShovel.txt
================================================
async function craftStoneShovel(bot) {
    // The function crafts a stone shovel using cobblestone and sticks. It checks if there are enough cobblestone and sticks in the inventory, and if not, it mines cobblestone or crafts sticks. Then, it places a crafting table near the bot and crafts a stone shovel using the crafting table. Finally, it sends a chat message indicating that a stone shovel has been crafted.
}


================================================
FILE: skill_library/trial1/skill/description/craftWhiteBed.txt
================================================
async function craftWhiteBed(bot) {
    // The function crafts a white bed using oak planks and white wool. If there are not enough oak planks in the inventory, it crafts oak planks from oak logs. If there are not enough white wool in the inventory, it stops the function. Then, it places a crafting table near the bot and crafts a white bed using the crafting table.
}


================================================
FILE: skill_library/trial1/skill/description/craftWoodenHoe.txt
================================================
async function craftWoodenHoe(bot) {
    // The function crafts a wooden hoe using oak planks and sticks. If there are not enough oak planks, it crafts them from oak logs. If there are not enough sticks, it crafts them from oak planks. Then, it places a crafting table near the bot and uses it to craft a wooden hoe.
}


================================================
FILE: skill_library/trial1/skill/description/craftWoodenPickaxe.txt
================================================
async function craftWoodenPickaxe(bot) {
    // The function crafts a wooden pickaxe using oak planks, sticks, and a crafting table. It checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. Then, it places a crafting table near the bot and uses it to craft a wooden pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/craftWoodenSword.txt
================================================
async function craftWoodenSword(bot) {
    // The function crafts a wooden sword using oak planks, sticks, and a crafting table. It checks if there are enough oak planks and sticks in the inventory, and crafts them if necessary. Then, it places a crafting table near the bot and uses it to craft a wooden sword.
}


================================================
FILE: skill_library/trial1/skill/description/eatCookedPorkchop.txt
================================================
async function eatCookedPorkchop(bot) {
    // The function is about eating a cooked porkchop. It equips the cooked porkchop in the bot's hand, consumes it, and sends a chat message to indicate the task is completed.
}


================================================
FILE: skill_library/trial1/skill/description/eatTwoCookedMutton.txt
================================================
async function eatTwoCookedMutton(bot) {
    // The function is about eating two cooked muttons. It checks if there are at least 2 cooked muttons in the inventory, and if not, it returns. If there are 2 or more cooked muttons, it equips one in the bot's hand and consumes it twice. Finally, it sends a chat message to indicate that the task is completed.
}


================================================
FILE: skill_library/trial1/skill/description/equipIronArmor.txt
================================================
async function equipIronArmor(bot) {
    // The function is about equipping iron armor (leggings, boots, and helmet) in the appropriate slots (legs, feet, and head) if they are available in the inventory. If any of the items are not found in the inventory, the function will output a message indicating that the item is not available.
}


================================================
FILE: skill_library/trial1/skill/description/equipIronChestplate.txt
================================================
async function equipIronChestplate(bot) {
    // The function is about equipping an iron chestplate on the bot's torso. It first finds the iron chestplate in the inventory and then equips it. If the iron chestplate is not found in the inventory, it sends a message saying that it was not found.
}


================================================
FILE: skill_library/trial1/skill/description/equipIronSword.txt
================================================
async function equipIronSword(bot) {
    // The function is about equipping an iron sword. It first checks if the iron sword is in the inventory. If not, it checks a chest for the iron sword. If the iron sword is found, it is equipped in the hand. If the iron sword is not found, a message is sent to the chat.
}


================================================
FILE: skill_library/trial1/skill/description/fillBucketWithWater.txt
================================================
async function fillBucketWithWater(bot) {
    // This function fills a bucket with water by first finding a nearby water block. After locating the water block, the bot moves to it and equips the bucket in its hand. The bot then looks at the water block and activates the bucket to collect water.
}


================================================
FILE: skill_library/trial1/skill/description/killFourSheep.txt
================================================
async function killFourSheep(bot) {
    // The function is about killing four sheep and collecting their drops. It equips a wooden sword and kills the first three sheep, then kills the fourth sheep. After that, it collects the dropped items from the killed sheep, which include wool and raw mutton.
}


================================================
FILE: skill_library/trial1/skill/description/killOneEnderman.txt
================================================
async function killOneEnderman(bot) {
    // The function is about killing one enderman using an iron sword. First, equip the iron sword in the hand. Next, explore the environment until finding the nearest enderman within 32 blocks. Once an enderman is found, kill it using the iron sword. After killing the enderman, collect the dropped items by moving to the enderman's position.
}


================================================
FILE: skill_library/trial1/skill/description/killOnePig.txt
================================================
async function killOnePig(bot) {
    // The function is about killing a pig using a wooden sword and collecting the dropped items. First, equip the wooden sword in the hand. Next, explore the environment until finding the nearest pig within 32 blocks. Once a pig is found, kill it using the wooden sword and collect the dropped items by moving to the pig's position.
}


================================================
FILE: skill_library/trial1/skill/description/killOneSpider.txt
================================================
async function killOneSpider(bot) {
    // The function is about killing a spider using an iron sword. First, equip the iron sword in the hand. Then, explore the environment until finding the nearest spider within 32 blocks. Once a spider is found, kill it using the iron sword. After killing the spider, collect the dropped items by moving to the spider's position.
}


================================================
FILE: skill_library/trial1/skill/description/killOneZombie.txt
================================================
async function killOneZombie(bot) {
    // The function is about killing a single zombie using an iron sword. First, equip the iron sword in the hand. Then, explore the environment until finding the nearest zombie within 32 blocks. Once a zombie is found, kill it using the iron sword and collect the dropped items.
}


================================================
FILE: skill_library/trial1/skill/description/killTwoPigs.txt
================================================
async function killTwoPigs(bot) {
    // The function is about killing two pigs and collecting their dropped items. The function equips a wooden sword and kills two pigs using the `killMob` function. After killing each pig, the function logs a message. Then, the function searches for dropped items from the killed pigs and collects them using the `pathfinder` module. Finally, the function logs a message indicating that the items have been collected.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveCoalOres.txt
================================================
async function mineFiveCoalOres(bot) {
    // The function is about mining 5 coal ores using a wooden pickaxe. The function first equips the wooden pickaxe in the hand. Then, it explores the environment until it finds 5 coal_ore blocks within a maximum distance of 32 blocks. Once 5 coal_ore blocks are found, it mines them using the wooden pickaxe and saves the event of mining 5 coal ores. If it cannot find enough coal ores, it sends a chat message indicating that it could not find enough coal ores.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveCoalOresV2.txt
================================================
async function mineFiveCoalOres(bot) {
    // The function is about mining 5 coal ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 coal_ore blocks. Once 5 coal_ore blocks are found, mine them using the stone pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveCopperOres.txt
================================================
async function mineFiveCopperOres(bot) {
    // The function is about mining 5 copper ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 copper_ore blocks. Once 5 copper_ore blocks are found, mine them using the stone pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveCopperOresV2.txt
================================================
async function mineFiveCopperOres(bot) {
    // The function checks if the bot already has 5 or more copper ores in the inventory. If not, it outputs how many more copper ores are needed to complete the task.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveIronOres.txt
================================================
async function mineFiveIronOres(bot) {
    // The function is about mining 5 iron ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 iron_ore blocks. Once 5 iron_ore blocks are found, mine them using the stone pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveIronOresV2.txt
================================================
async function mineFiveIronOres(bot) {
    // The function is about mining 5 iron ores using a stone pickaxe. First, equip the stone pickaxe in the hand. Next, explore the environment until finding 5 iron_ore blocks. Once 5 iron_ore blocks are found, mine them using the stone pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/mineFiveLapisLazuliOres.txt
================================================
async function mineFiveLapisLazuliOres(bot) {
    // The function is about mining 5 lapis lazuli ores using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 lapis lazuli ore blocks. Once 5 lapis lazuli ore blocks are found, mine them using the iron pickaxe.
}


================================================
FILE: skill_library/trial1/skill/description/mineTenCobblestone.txt
================================================
async function mineTenCobblestone(bot) {
    // The function is about mining 10 cobblestones using a pickaxe. First, check if the bot has a pickaxe in the inventory. If not, craft a wooden pickaxe using the available resources in the inventory. If the pickaxe is available, equip the pickaxe in the hand. Next, use the exploreUntil function to find cobblestone blocks. Once 10 cobblestone blocks are found, mine them using the mineBlock function.
}


================================================
FILE: skill_library/trial1/skill/description/mineThreeMoreOakLogs.txt
================================================
async function mineThreeMoreOakLogs(bot) {
    // The function is about mining 3 oak logs. It first checks the initial inventory for oak logs. Then, it explores the environment until it finds 3 oak log blocks. If it cannot find enough oak logs, it returns. Otherwise, it mines the oak log blocks and compares the final inventory with the initial inventory to determine if it successfully mined 3 more oak logs.
}


================================================
FILE: skill_library/trial1/skill/description/mineWoodLog.txt
================================================
async function mineWoodLog(bot) {
    // The function is about mining a single wood log block. It searches for a wood log block by exploring the environment until it finds one of the seven types of wood logs. If a wood log block is found, it is mined and a success message is sent. If no wood log block is found, a failure message is sent.
}


================================================
FILE: skill_library/trial1/skill/description/obtainOneMoreAcaciaLog.txt
================================================
async function obtainOneMoreAcaciaLog(bot) {
    // The function checks if there are less than 5 acacia logs in the inventory, and if so, finds and mines one more acacia log. If the bot successfully obtains 5 acacia logs, it sends a success message, otherwise it sends a failure message.
}


================================================
FILE: skill_library/trial1/skill/description/smeltCactusIntoGreenDye.txt
================================================
async function smeltCactusIntoGreenDye(bot) {
    // The function is about smelting 5 cactus into green dye using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. Finally, it smelts the cactus using coal as fuel and saves the event of smelting 5 cactus into green dye.
}


================================================
FILE: skill_library/trial1/skill/description/smeltFiveRawIron.txt
================================================
async function smeltFiveRawIron(bot) {
    // The function is about smelting 5 raw iron using a furnace and coal as fuel. First, it checks if there is a furnace in the inventory, and if not, it crafts one. Then, it places the furnace near the bot. Finally, it smelts 5 raw iron using the available coal as fuel and sends a chat message when finished.
}


================================================
FILE: skill_library/trial1/skill/description/smeltFiveRawIronV2.txt
================================================
async function smeltFiveRawIron(bot) {
    // The function is about smelting 5 raw iron using a furnace and coal as fuel. If there is no furnace in the inventory, craft one using cobblestone. Find a suitable position to place the furnace and place it there. Then, smelt 5 raw iron using the available coal as fuel.
}


================================================
FILE: skill_library/trial1/skill/description/smeltRawCopper.txt
================================================
async function smeltRawCopper(bot) {
    // The function is about smelting 19 raw copper using a furnace and coal as fuel. It checks if there is a furnace in the inventory, and if not, it crafts one. Then it finds a suitable position to place the furnace and places it there. Finally, it smelts the raw copper using the furnace and coal as fuel.
}


================================================
FILE: skill_library/trial1/skill/vectordb/chroma-collections.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial1/skill/vectordb/chroma-embeddings.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial1/skill/vectordb/index/id_to_uuid_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial1/skill/vectordb/index/index_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.bin
================================================
[Non-text file]


================================================
FILE: skill_library/trial1/skill/vectordb/index/index_metadata_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial1/skill/vectordb/index/uuid_to_id_e1bd933d-d62f-46c2-884d-d75ef3bcb09e.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/skills.json
================================================
{"mineWoodLog": {"code": "async function mineWoodLog(bot) {\n  const logNames = [\"oak_log\", \"birch_log\", \"spruce_log\", \"jungle_log\", \"acacia_log\", \"dark_oak_log\", \"mangrove_log\"];\n  const logBlock = bot.findBlock({\n    matching: block => logNames.includes(block.name),\n    maxDistance: 32\n  });\n  if (!logBlock) {\n    bot.chat(\"No wood log found nearby. Exploring...\");\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundLog = bot.findBlock({\n        matching: block => logNames.includes(block.name),\n        maxDistance: 32\n      });\n      return foundLog;\n    });\n  }\n  await mineBlock(bot, logBlock.name, 1);\n  bot.chat(\"Wood log mined.\");\n}", "description": "async function mineWoodLog(bot) {\n    // The function is about mining a single wood log. It first searches for a nearby wood log within a certain distance. If it cannot find one, it explores the environment until it finds a wood log. Once a wood log is found, it mines it and saves the event of mining the wood log.\n}"}, "craftWoodenPlanks": {"code": "async function craftWoodenPlanks(bot) {\n  const logNames = [\"oak_log\", \"birch_log\", \"spruce_log\", \"jungle_log\", \"acacia_log\", \"dark_oak_log\", \"mangrove_log\"];\n  const plankNames = [\"oak_planks\", \"birch_planks\", \"spruce_planks\", \"jungle_planks\", \"acacia_planks\", \"dark_oak_planks\", \"mangrove_planks\"];\n  const logInInventory = logNames.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);\n  if (!logInInventory) {\n    bot.chat(\"No wooden log in inventory. Mining a wooden log...\");\n    await mineWoodLog(bot);\n  }\n  const logIndex = logNames.indexOf(logInInventory);\n  const plankName = plankNames[logIndex];\n  bot.chat(`Crafting 4 ${plankName}...`);\n  await craftItem(bot, plankName, 1);\n  bot.chat(`4 ${plankName} crafted.`);\n}", "description": "async function craftWoodenPlanks(bot) {\n    // The function crafts 4 wooden planks using any type of wooden log available in the inventory. If there is no wooden log in the inventory, it will mine one. It then finds the index of the log in the `logNames` array and uses that index to determine the corresponding plank name in the `plankNames` array. Finally, it crafts 4 planks of the corresponding type and saves the event.\n}"}, "craftWoodenPickaxe": {"code": "async function craftWoodenPickaxe(bot) {\n  const requiredPlanks = 3;\n  const requiredSticks = 2;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Not enough spruce_planks. Crafting more...\");\n    await craftItem(bot, \"spruce_planks\", requiredPlanks - planksCount);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n  bot.chat(\"Crafting_table placed.\");\n  await craftItem(bot, \"wooden_pickaxe\", 1);\n  bot.chat(\"Wooden pickaxe crafted.\");\n}", "description": "async function craftWoodenPickaxe(bot) {\n    // The function crafts a wooden pickaxe by checking if there are enough spruce planks and sticks in the inventory, and crafting more if necessary. It then places a crafting table and crafts a wooden pickaxe using the newly crafted items.\n}"}, "mineCopperOreWithStonePickaxe": {"code": "async function mineCopperOreWithStonePickaxe(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  if (!stonePickaxe) {\n    bot.chat(\"No stone pickaxe found. Mining cobblestone and crafting one...\");\n    await mineBlock(bot, \"stone\", 3);\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    await craftItem(bot, \"stone_pickaxe\", 1);\n    bot.chat(\"Stone pickaxe crafted.\");\n  }\n  await bot.equip(mcData.itemsByName.stone_pickaxe.id, \"hand\");\n  const copperOreBlock = bot.findBlock({\n    matching: mcData.blocksByName.copper_ore.id,\n    maxDistance: 32\n  });\n  if (!copperOreBlock) {\n    bot.chat(\"No copper ore found nearby. Exploring...\");\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundCopperOre = bot.findBlock({\n        matching: mcData.blocksByName.copper_ore.id,\n        maxDistance: 32\n      });\n      return foundCopperOre;\n    });\n  }\n  await mineBlock(bot, \"copper_ore\", 1);\n  bot.chat(\"Copper ore mined.\");\n}", "description": "async function mineCopperOreWithStonePickaxe(bot) {\n    // The function is about mining a single copper ore block using a stone pickaxe. If the stone pickaxe is not in the inventory, the bot will mine 3 cobblestone blocks and craft a stone pickaxe. Once the stone pickaxe is available, it will be equipped in the hand. The bot will then explore the environment until finding a copper ore block. Once a copper ore block is found, the bot will mine it and save the event.\n}"}, "craftSticks": {"code": "async function craftSticks(bot) {\n  const requiredPlanks = 2;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Not enough spruce_planks. Mining a spruce_log and crafting more...\");\n    await mineBlock(bot, \"spruce_log\", 1);\n    await craftItem(bot, \"spruce_planks\", 1);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n  bot.chat(\"Crafting_table placed.\");\n  await craftItem(bot, \"stick\", 1);\n  bot.chat(\"4 sticks crafted.\");\n}", "description": "async function craftSticks(bot) {\n    // The function crafts 4 sticks using a crafting table. If there are not enough spruce planks, it mines a spruce log and crafts the planks. Then, it places a crafting table next to the bot and crafts 4 sticks.\n}"}, "chopSpruceLogs": {"code": "async function chopSpruceLogs(bot) {\n  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);\n  const logsToMine = 3 - spruceLogCount;\n  if (logsToMine > 0) {\n    bot.chat(\"Chopping down spruce logs...\");\n    await mineBlock(bot, \"spruce_log\", logsToMine);\n    bot.chat(\"Chopped down 3 spruce logs.\");\n  } else {\n    bot.chat(\"Already have 3 spruce logs in inventory.\");\n  }\n}", "description": "async function chopSpruceLogs(bot) {\n    // The function is about chopping down spruce logs until there are 3 in the inventory. It first checks how many spruce logs are in the inventory and calculates how many more need to be mined. If there are less than 3, it mines the remaining logs and saves them in the inventory. If there are already 3 logs in the inventory, it does nothing.\n}"}, "chopDownSpruceLogs": {"code": "async function chopDownSpruceLogs(bot) {\n  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);\n  const logsToMine = 5 - spruceLogCount;\n  if (logsToMine > 0) {\n    bot.chat(\"Chopping down spruce logs...\");\n    await mineBlock(bot, \"spruce_log\", logsToMine);\n    bot.chat(\"Chopped down 5 spruce logs.\");\n  } else {\n    bot.chat(\"Already have 5 spruce logs in inventory.\");\n  }\n}", "description": "async function chopDownSpruceLogs(bot) {\n    // The function is about chopping down spruce logs until there are 5 in the inventory. It first checks how many spruce logs are in the inventory and calculates how many more need to be mined. If there are less than 5, it mines the remaining amount and saves the event. If there are already 5 spruce logs in the inventory, it does nothing.\n}"}, "craftTwentySprucePlanks": {"code": "async function craftTwentySprucePlanks(bot) {\n  const requiredLogs = 5;\n  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);\n  const logsToMine = requiredLogs - spruceLogCount;\n  if (logsToMine > 0) {\n    bot.chat(\"Not enough spruce logs. Chopping down more...\");\n    await mineBlock(bot, \"spruce_log\", logsToMine);\n    bot.chat(\"Spruce logs chopped down.\");\n  }\n  bot.chat(\"Crafting 20 spruce planks...\");\n  await craftItem(bot, \"spruce_planks\", requiredLogs);\n  bot.chat(\"20 spruce planks crafted.\");\n}", "description": "async function craftTwentySprucePlanks(bot) {\n    // The function crafts 20 spruce planks using spruce logs. If there are not enough spruce logs in the inventory, it will mine the required amount. Once enough logs are available, it will craft 20 spruce planks and save the event.\n}"}, "mineCoalOre": {"code": "async function mineCoalOre(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  if (!stonePickaxe) {\n    bot.chat(\"No stone pickaxe found in inventory.\");\n    return;\n  }\n  await bot.equip(mcData.itemsByName.stone_pickaxe.id, \"hand\");\n  const coalOreBlock = bot.findBlock({\n    matching: mcData.blocksByName.coal_ore.id,\n    maxDistance: 32\n  });\n  if (!coalOreBlock) {\n    bot.chat(\"No coal ore found nearby. Exploring...\");\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundCoalOre = bot.findBlock({\n        matching: mcData.blocksByName.coal_ore.id,\n        maxDistance: 32\n      });\n      return foundCoalOre;\n    });\n  }\n  await mineBlock(bot, \"coal_ore\", 1);\n  bot.chat(\"Coal ore mined.\");\n}", "description": "async function mineCoalOre(bot) {\n    // The function is about mining a single coal ore block using a stone pickaxe. First, it checks if a stone pickaxe is in the inventory. If not, it returns. If the stone pickaxe is available, it equips it in the hand. Next, it searches for a nearby coal ore block. If it is not found, it explores the environment until it finds one. Once a coal ore block is found, it mines it and sends a message to the chat.\n}"}, "craftFurnace": {"code": "async function craftFurnace(bot) {\n  const requiredCobblestones = 8;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones to craft a furnace.\");\n    return;\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"furnace\", 1);\n  bot.chat(\"Furnace crafted.\");\n}", "description": "async function craftFurnace(bot) {\n    // The function crafts a furnace using 8 cobblestones and a crafting table. If there are not enough cobblestones, the function will return. If there is no crafting table nearby, the function will place one. Finally, the function crafts a furnace and sends a chat message.\n}"}, "smeltRawCopper": {"code": "async function smeltRawCopper(bot) {\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  const requiredCoal = 7;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more coal...\");\n    await mineCoalOre(bot);\n  }\n  await smeltItem(bot, \"raw_copper\", \"coal\", 7);\n  bot.chat(\"7 raw copper smelted.\");\n}", "description": "async function smeltRawCopper(bot) {\n    // The function is about smelting 7 raw copper using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. Then it places the furnace next to the bot and checks if there is coal ore nearby. If there is not enough coal in the inventory, it mines more coal ore. Finally, it smelts 7 raw copper using the furnace and coal.\n}"}, "mineFiveCoalOres": {"code": "async function mineFiveCoalOres(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  if (!stonePickaxe) {\n    bot.chat(\"No stone pickaxe found in inventory.\");\n    return;\n  }\n  await bot.equip(mcData.itemsByName.stone_pickaxe.id, \"hand\");\n  await mineBlock(bot, \"coal_ore\", 5);\n  bot.chat(\"5 coal ores mined.\");\n}", "description": "async function mineFiveCoalOres(bot) {\n    // The function is about mining 5 coal ores using a stone pickaxe. First, check if a stone pickaxe is in the inventory. If not, return. If the stone pickaxe is available, equip the stone pickaxe in the hand. Next, mine a total of 5 coal ores using the stone pickaxe. Finally, send a chat message indicating that 5 coal ores have been mined.\n}"}, "craftStoneSword": {"code": "async function craftStoneSword(bot) {\n  const requiredCobblestones = 2;\n  const requiredSticks = 1;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones. Mining more...\");\n    await mineBlock(bot, \"stone\", requiredCobblestones - cobblestoneCount);\n    bot.chat(\"Cobblestones mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftSticks(bot);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stone_sword\", 1);\n  bot.chat(\"Stone sword crafted.\");\n}", "description": "async function craftStoneSword(bot) {\n    // The function crafts a stone sword using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone sword and logs a message.\n}"}, "mineThreeIronOres": {"code": "async function mineThreeIronOres(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  if (!stonePickaxe) {\n    bot.chat(\"No stone pickaxe found. Mining cobblestone and crafting one...\");\n    await mineBlock(bot, \"stone\", 3);\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    await craftItem(bot, \"stone_pickaxe\", 1);\n    bot.chat(\"Stone pickaxe crafted.\");\n  }\n  await bot.equip(mcData.itemsByName.stone_pickaxe.id, \"hand\");\n  const ironOreBlock = await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {\n    const foundIronOre = bot.findBlock({\n      matching: mcData.blocksByName.iron_ore.id,\n      maxDistance: 32\n    });\n    return foundIronOre;\n  });\n  if (!ironOreBlock) {\n    bot.chat(\"No iron ore found nearby. Exploring...\");\n  }\n  await mineBlock(bot, \"iron_ore\", 3);\n  bot.chat(\"3 iron ores mined.\");\n}", "description": "async function mineThreeIronOres(bot) {\n    // The function is about mining 3 iron ores using a stone pickaxe. If the stone pickaxe is not in the inventory, the bot will mine cobblestone and craft one. Once the stone pickaxe is available, it will be equipped in the hand. The bot will explore the environment until finding an iron ore block. Once an iron ore block is found, the bot will mine a total of 3 iron ores using the stone pickaxe.\n}"}, "smeltRawIron": {"code": "async function smeltRawIron(bot) {\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  const requiredCoal = 3;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more coal...\");\n    await mineBlock(bot, \"coal_ore\", requiredCoal - coalCount);\n  }\n  await smeltItem(bot, \"raw_iron\", \"coal\", 3);\n  bot.chat(\"3 raw iron smelted.\");\n}", "description": "async function smeltRawIron(bot) {\n    // The function is about smelting 3 raw iron using a furnace and coal. First, it checks if there is a furnace in the inventory, and if not, it returns a message to craft one. Then, it places the furnace next to the bot. If there is coal in the inventory, it uses it to smelt the raw iron. Otherwise, it mines coal ore to obtain the required amount of coal. Finally, it smelts the raw iron and returns a message indicating that the process is complete.\n}"}, "craftIronPickaxe": {"code": "async function craftIronPickaxe(bot) {\n  const requiredIronIngots = 3;\n  const requiredSticks = 2;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (ironIngotsCount < requiredIronIngots || sticksCount < requiredSticks) {\n    bot.chat(\"Not enough iron ingots or sticks to craft an iron pickaxe.\");\n    return;\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"iron_pickaxe\", 1);\n  bot.chat(\"Iron pickaxe crafted.\");\n}", "description": "async function craftIronPickaxe(bot) {\n    // The function crafts an iron pickaxe using 3 iron ingots and 2 sticks. It checks if there are enough resources in the inventory to craft the pickaxe, and if not, it returns. If there is a crafting table nearby, it crafts the pickaxe. If not, it places a crafting table and then crafts the pickaxe. Finally, it sends a chat message indicating that the iron pickaxe has been crafted.\n}"}, "mineFiveCopperOres": {"code": "async function mineFiveCopperOres(bot) {\n  const copperOreCount = bot.inventory.count(mcData.itemsByName.copper_ore.id);\n  if (copperOreCount >= 5) {\n    bot.chat(\"Already have 5 copper ores in inventory.\");\n    return;\n  }\n  await bot.equip(mcData.itemsByName.iron_pickaxe.id, \"hand\");\n  await mineBlock(bot, \"copper_ore\", 5 - copperOreCount);\n  bot.chat(\"5 copper ores mined.\");\n}", "description": "async function mineFiveCopperOres(bot) {\n    // The function is about mining 5 copper ores using an iron pickaxe. It first checks if there are already 5 copper ores in the inventory, and if so, it returns. Otherwise, it equips the iron pickaxe in the hand and mines copper ores until there are 5 in the inventory. Finally, it sends a chat message indicating that 5 copper ores have been mined.\n}"}, "craftStoneAxe": {"code": "async function craftStoneAxe(bot) {\n  const requiredCobblestones = 3;\n  const requiredSticks = 2;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones. Mining more...\");\n    await mineBlock(bot, \"stone\", requiredCobblestones - cobblestoneCount);\n    bot.chat(\"Cobblestones mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stone_axe\", 1);\n  bot.chat(\"Stone axe crafted.\");\n}", "description": "async function craftStoneAxe(bot) {\n    // The function crafts a stone axe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone axe and sends a chat message.\n}"}, "mineFiveIronOres": {"code": "async function mineFiveIronOres(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);\n  if (!stonePickaxe && !ironPickaxe) {\n    bot.chat(\"No stone or iron pickaxe found. Mining cobblestone and crafting a stone pickaxe...\");\n    await mineBlock(bot, \"stone\", 3);\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    await craftItem(bot, \"stone_pickaxe\", 1);\n    bot.chat(\"Stone pickaxe crafted.\");\n  }\n  const pickaxeToUse = ironPickaxe || stonePickaxe;\n  await bot.equip(pickaxeToUse, \"hand\");\n  await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {\n    const foundIronOre = bot.findBlock({\n      matching: mcData.blocksByName.iron_ore.id,\n      maxDistance: 32\n    });\n    return foundIronOre;\n  });\n  await mineBlock(bot, \"iron_ore\", 5);\n  bot.chat(\"5 iron ores mined.\");\n}", "description": "async function mineFiveIronOres(bot) {\n    // The function is about mining 5 iron ores using either a stone or iron pickaxe. If neither pickaxe is found in the inventory, the bot will mine cobblestone and craft a stone pickaxe. Once a pickaxe is available, the bot will equip it and explore the environment until finding an iron ore block. Once an iron ore block is found, the bot will mine a total of 5 iron ores using the equipped pickaxe.\n}"}, "craftTorches": {"code": "async function craftTorches(bot) {\n  const requiredCoal = 2;\n  const requiredSticks = 2;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more...\");\n    await mineBlock(bot, \"coal_ore\", requiredCoal - coalCount);\n    bot.chat(\"Coal mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"torch\", 1);\n  bot.chat(\"8 torches crafted.\");\n}", "description": "async function craftTorches(bot) {\n    // The function crafts 8 torches using coal and sticks. It checks if there is enough coal and sticks in the inventory, and if not, it mines coal or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts 8 torches and saves the event.\n}"}, "exploreCave": {"code": "async function exploreCave(bot) {\n  const torches = bot.inventory.findInventoryItem(mcData.itemsByName.torch.id);\n  if (!torches) {\n    bot.chat(\"No torches found in inventory. Crafting torches...\");\n    await craftTorches(bot);\n  }\n  await bot.equip(mcData.itemsByName.torch.id, \"hand\");\n  const caveEntrance = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const caveBlock = bot.findBlock({\n      matching: block => {\n        return block && block.name === \"air\" && block.position && block.position.y < 60;\n      },\n      maxDistance: 32\n    });\n    return caveBlock;\n  });\n  if (!caveEntrance) {\n    bot.chat(\"No cave entrance found nearby.\");\n    return;\n  }\n  bot.chat(\"Cave entrance found. Exploring the cave...\");\n  await exploreUntil(bot, new Vec3(1, 0, 1), 300, () => {\n    const caveBlock = bot.findBlock({\n      matching: block => {\n        return block && block.name === \"air\" && block.position && block.position.y < 60;\n      },\n      maxDistance: 32\n    });\n    if (caveBlock) {\n      bot.placeBlock(caveBlock, new Vec3(0, 1, 0));\n    }\n    const mob = bot.nearestEntity(entity => {\n      return entity.type === \"mob\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    if (mob) {\n      killMob(bot, mob.name, 300);\n    }\n    return null; // Continue exploring until the time limit is reached\n  });\n\n  bot.chat(\"Finished exploring the cave.\");\n}", "description": "async function exploreCave(bot) {\n    // The function is about exploring a nearby cave. First, check if there are torches in the inventory. If not, craft torches. Equip the torches in the hand and explore the environment until finding a cave entrance. Once a cave entrance is found, explore the cave by placing torches and killing mobs until the time limit is reached.\n}"}, "smeltSixRawIron": {"code": "async function smeltSixRawIron(bot) {\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  const requiredCoal = 6;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more coal...\");\n    await mineBlock(bot, \"coal_ore\", requiredCoal - coalCount);\n  }\n  await smeltItem(bot, \"raw_iron\", \"coal\", 6);\n  bot.chat(\"6 raw iron smelted.\");\n}", "description": "async function smeltSixRawIron(bot) {\n    // The function is about smelting 6 raw iron using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. It then places the furnace next to the player and checks if there is enough coal in the inventory. If there isn't, it mines coal until there are 6 pieces. Finally, it smelts 6 raw iron using the furnace and coal, and returns a message indicating that the process is complete.\n}"}, "mineLapisOre": {"code": "async function mineLapisOre(bot) {\n  const pickaxeTypes = [mcData.itemsByName.stone_pickaxe.id, mcData.itemsByName.iron_pickaxe.id, mcData.itemsByName.diamond_pickaxe.id, mcData.itemsByName.netherite_pickaxe.id];\n  let pickaxe = bot.inventory.items().find(item => pickaxeTypes.includes(item.type));\n  if (!pickaxe) {\n    bot.chat(\"No suitable pickaxe found. Mining cobblestone and crafting a stone pickaxe...\");\n    await mineBlock(bot, \"stone\", 3);\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    await craftItem(bot, \"stone_pickaxe\", 1);\n    pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n    bot.chat(\"Stone pickaxe crafted.\");\n  }\n  await bot.equip(pickaxe, \"hand\");\n  const lapisOreBlock = await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {\n    const foundLapisOre = bot.findBlock({\n      matching: mcData.blocksByName.lapis_ore.id,\n      maxDistance: 32\n    });\n    return foundLapisOre;\n  });\n  if (!lapisOreBlock) {\n    bot.chat(\"No lapis ore found nearby. Exploring...\");\n  }\n  await mineBlock(bot, \"lapis_ore\", 1);\n  bot.chat(\"Lapis ore mined.\");\n}", "description": "async function mineLapisOre(bot) {\n    // The function is about mining a single lapis ore block using the best available pickaxe. If the bot does not have a suitable pickaxe, it will mine cobblestone and craft a stone pickaxe. Once the pickaxe is available, it will equip it and explore the environment until finding a lapis ore block. Once a lapis ore block is found, it will mine it and save the event of mining the lapis ore.\n}"}, "craftBucket": {"code": "async function craftBucket(bot) {\n  const requiredIronIngots = 3;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots to craft a bucket.\");\n    return;\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"bucket\", 1);\n  bot.chat(\"Bucket crafted.\");\n}", "description": "async function craftBucket(bot) {\n    // The function crafts a bucket using 3 iron ingots. If there are not enough iron ingots, it returns. If there is no crafting table nearby, it places one. Then it crafts a bucket and sends a chat message.\n}"}, "craftStoneShovel": {"code": "async function craftStoneShovel(bot) {\n  const requiredCobblestones = 1;\n  const requiredSticks = 2;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones. Mining more...\");\n    await mineBlock(bot, \"stone\", requiredCobblestones - cobblestoneCount);\n    bot.chat(\"Cobblestones mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stone_shovel\", 1);\n  bot.chat(\"Stone shovel crafted.\");\n}", "description": "async function craftStoneShovel(bot) {\n    // The function crafts a stone shovel using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone shovel and logs a message.\n}"}, "checkStonePickaxe": {"code": "async function checkStonePickaxe(bot) {\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);\n  if (stonePickaxe) {\n    bot.chat(\"The bot already has a stone pickaxe in its inventory.\");\n  } else {\n    bot.chat(\"The bot does not have a stone pickaxe in its inventory.\");\n  }\n}", "description": "async function checkStonePickaxe(bot) {\n    // The function checks if the bot has a stone pickaxe in its inventory and sends a chat message indicating whether it has one or not.\n}"}, "craftEightTorches": {"code": "async function craftEightTorches(bot) {\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"torch\", 1);\n  bot.chat(\"8 torches crafted.\");\n}", "description": "async function craftEightTorches(bot) {\n    // The function is about crafting 8 torches. First, it checks if there is a crafting table nearby. If not, it places one. Then, it crafts 1 torch and saves it to the inventory. Finally, it outputs a message indicating that 8 torches have been crafted.\n}"}, "craftIronPickaxeWithMaterials": {"code": "async function craftIronPickaxeWithMaterials(bot) {\n  const requiredIronIngots = 3;\n  const requiredSticks = 2;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots. Mining iron ores...\");\n    await mineBlock(bot, \"iron_ore\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ores mined. Smelting iron ingots...\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ingots smelted.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"iron_pickaxe\", 1);\n  bot.chat(\"Iron pickaxe crafted.\");\n}", "description": "async function craftIronPickaxeWithMaterials(bot) {\n    // The function crafts an iron pickaxe using 3 iron ingots and 2 sticks. If there are not enough iron ingots, it mines iron ores and smelts them into ingots. If there are not enough sticks, it crafts them. If there is no crafting table nearby, it places one. Finally, it crafts an iron pickaxe and logs the result.\n}"}, "craftChest": {"code": "async function craftChest(bot) {\n  const requiredPlanks = 8;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Not enough spruce_planks. Mining a spruce_log and crafting more...\");\n    await mineBlock(bot, \"spruce_log\", 1);\n    await craftItem(bot, \"spruce_planks\", 1);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  bot.chat(\"Crafting a chest...\");\n  await craftItem(bot, \"chest\", 1);\n  bot.chat(\"Chest crafted.\");\n}", "description": "async function craftChest(bot) {\n    // The function crafts a chest using spruce planks and a crafting table. If there are not enough spruce planks, it mines a spruce log and crafts more planks. If there is no crafting table nearby, it places one. Finally, it crafts a chest and logs the event.\n}"}, "craftEightSticks": {"code": "async function craftEightSticks(bot) {\n  const requiredPlanks = 2;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Not enough spruce_planks. Mining a spruce_log and crafting more...\");\n    await mineBlock(bot, \"spruce_log\", 1);\n    await craftItem(bot, \"spruce_planks\", 1);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stick\", 2);\n  bot.chat(\"8 sticks crafted.\");\n}", "description": "async function craftEightSticks(bot) {\n    // The function crafts 8 sticks using spruce planks. If there are not enough spruce planks, it mines a spruce log and crafts more planks. If there is no crafting table nearby, it places one. Finally, it crafts 2 sticks and repeats the process until 8 sticks are crafted.\n}"}, "exploreCaveAndGatherResources": {"code": "async function exploreCaveAndGatherResources(bot) {\n  // Equip torches\n  const torches = bot.inventory.findInventoryItem(mcData.itemsByName.torch.id);\n  if (!torches) {\n    bot.chat(\"No torches found in inventory. Crafting torches...\");\n    await craftTorches(bot);\n  }\n  await bot.equip(mcData.itemsByName.torch.id, \"hand\");\n\n  // Find a cave entrance and start exploring\n  const caveEntrance = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const caveBlock = bot.findBlock({\n      matching: block => {\n        return block && block.name === \"air\" && block.position && block.position.y < 60;\n      },\n      maxDistance: 32\n    });\n    return caveBlock;\n  });\n  if (!caveEntrance) {\n    bot.chat(\"No cave entrance found nearby.\");\n    return;\n  }\n  bot.chat(\"Cave entrance found. Exploring the cave...\");\n\n  // Explore the cave and gather resources\n  await exploreUntil(bot, new Vec3(1, 0, 1), 300, () => {\n    const caveBlock = bot.findBlock({\n      matching: block => {\n        return block && block.name === \"air\" && block.position && block.position.y < 60;\n      },\n      maxDistance: 32\n    });\n    if (caveBlock) {\n      bot.placeBlock(caveBlock, new Vec3(0, 1, 0));\n    }\n    const mob = bot.nearestEntity(entity => {\n      return entity.type === \"mob\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    if (mob) {\n      killMob(bot, mob.name, 300);\n    }\n    const ores = [\"coal_ore\", \"iron_ore\", \"gold_ore\", \"diamond_ore\"];\n    for (const ore of ores) {\n      const oreBlock = bot.findBlock({\n        matching: mcData.blocksByName[ore].id,\n        maxDistance: 32\n      });\n      if (oreBlock) {\n        mineBlock(bot, ore, 1);\n      }\n    }\n    return null; // Continue exploring until the time limit is reached\n  });\n\n  bot.chat(\"Finished exploring the cave and gathering resources.\");\n}", "description": "async function exploreCaveAndGatherResources(bot) {\n    // The function is about exploring a nearby cave and gathering resources. First, equip torches and find a cave entrance. Once a cave entrance is found, explore the cave and gather resources such as coal, iron, gold, and diamond ores. While exploring, place torches to light up the cave, kill nearby mobs, and mine ores. The function will continue exploring until the time limit is reached. Finally, the function will output a message indicating that the exploration and resource gathering is finished.\n}"}, "craftWhiteBedWithExploration": {"code": "async function craftWhiteBedWithExploration(bot) {\n  // Step 1: Explore the area to find and kill sheep to collect the required wool blocks if needed\n  const requiredWool = 3;\n  const woolCount = bot.inventory.count(mcData.itemsByName.white_wool.id);\n  if (woolCount < requiredWool) {\n    bot.chat(\"Collecting wool from sheep...\");\n    for (let i = 0; i < requiredWool - woolCount; i++) {\n      const sheep = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n        const sheep = bot.nearestEntity(entity => {\n          return entity.name === \"sheep\" && entity.position.distanceTo(bot.entity.position) < 32;\n        });\n        return sheep;\n      });\n      if (sheep) {\n        await killMob(bot, \"sheep\");\n      } else {\n        bot.chat(\"No sheep found. Please try again later.\");\n        return;\n      }\n    }\n    bot.chat(\"Wool collected.\");\n  }\n\n  // Step 2: Craft 2 more spruce planks if needed\n  const requiredPlanks = 3;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Crafting more spruce_planks...\");\n    await craftItem(bot, \"spruce_planks\", requiredPlanks - planksCount);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n\n  // Step 3: Place a crafting table if not already placed\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n\n  // Step 4: Craft a white bed using the 3 white wool blocks and 3 spruce planks\n  bot.chat(\"Crafting a white bed...\");\n  await craftItem(bot, \"white_bed\", 1);\n  bot.chat(\"White bed crafted.\");\n}", "description": "async function craftWhiteBedWithExploration(bot) {\n    // The function crafts a white bed using 3 white wool blocks and 3 spruce planks. If there are not enough wool blocks, the bot explores the area to find and kill sheep to collect the wool. If there are not enough spruce planks, the bot crafts more. If there is no crafting table nearby, the bot places one.\n}"}, "cookMutton": {"code": "async function cookMutton(bot) {\n  const rawMuttonCount = bot.inventory.count(mcData.itemsByName.mutton.id);\n  if (rawMuttonCount < 5) {\n    bot.chat(\"Not enough raw mutton to cook. Please collect more first.\");\n    return;\n  }\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  const requiredCoal = 5;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more coal...\");\n    await mineBlock(bot, \"coal_ore\", requiredCoal - coalCount);\n  }\n  await smeltItem(bot, \"mutton\", \"coal\", 5);\n  bot.chat(\"5 mutton cooked.\");\n}", "description": "async function cookMutton(bot) {\n    // The function is about cooking 5 raw muttons using a furnace and coal. It first checks if there are at least 5 raw muttons in the inventory, and if not, it returns a message to collect more. Then it checks if there is a furnace in the inventory, and if not, it returns a message to craft one. It places the furnace next to the player and checks if there is enough coal in the inventory. If not, it mines coal until there are 5 pieces. Finally, it smelts 5 raw muttons using coal and returns a message that 5 muttons have been cooked.\n}"}, "eatCookedMutton": {"code": "async function eatCookedMutton(bot) {\n  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);\n  await bot.equip(cookedMutton, \"hand\");\n  await bot.consume();\n  bot.chat(\"Cooked mutton eaten.\");\n}", "description": "async function eatCookedMutton(bot) {\n    // The function is about eating cooked mutton. It first checks if there is any cooked mutton in the inventory. If there is, it equips the cooked mutton in the hand and consumes it. Finally, it sends a chat message indicating that the cooked mutton has been eaten.\n}"}, "collectWaterWithBucket": {"code": "async function collectWaterWithBucket(bot) {\n  const waterBlock = bot.findBlock({\n    matching: mcData.blocksByName.water.id,\n    maxDistance: 32\n  });\n  if (!waterBlock) {\n    bot.chat(\"No water block found nearby. Exploring...\");\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundWaterBlock = bot.findBlock({\n        matching: mcData.blocksByName.water.id,\n        maxDistance: 32\n      });\n      return foundWaterBlock;\n    });\n  }\n  const bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);\n  await bot.equip(bucket, \"hand\");\n  await bot.lookAt(waterBlock.position);\n  await bot.activateItem();\n  bot.chat(\"Water collected with bucket.\");\n}", "description": "async function collectWaterWithBucket(bot) {\n    // The function is about collecting water with a bucket. It first searches for a water block within a certain distance. If no water block is found, it explores the environment until it finds one. Once a water block is found, it equips the bucket in the hand, looks at the water block, and activates the item to collect water. Finally, it sends a chat message indicating that water has been collected.\n}"}, "craftFishingRod": {"code": "async function craftFishingRod(bot) {\n  // Check if we have enough strings\n  const requiredStrings = 2;\n  const stringsCount = bot.inventory.count(mcData.itemsByName.string.id);\n  if (stringsCount < requiredStrings) {\n    // Find and kill spiders to obtain strings\n    while (bot.inventory.count(mcData.itemsByName.string.id) < requiredStrings) {\n      bot.chat(\"Finding a spider to obtain strings...\");\n      const spider = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n        const spider = bot.nearestEntity(entity => {\n          return entity.name === \"spider\" && entity.position.distanceTo(bot.entity.position) < 32;\n        });\n        return spider;\n      });\n      if (spider) {\n        bot.chat(\"Spider found. Killing it...\");\n        await killMob(bot, \"spider\", 300);\n        bot.chat(\"Spider killed.\");\n      } else {\n        bot.chat(\"Could not find a spider. Trying again...\");\n      }\n    }\n  }\n\n  // Place a crafting table if not already placed\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n\n  // Craft a fishing rod using the 3 sticks and 2 strings\n  await craftItem(bot, \"fishing_rod\", 1);\n  bot.chat(\"Fishing rod crafted.\");\n}", "description": "async function craftFishingRod(bot) {\n    // The function crafts a fishing rod using 2 strings and 3 sticks. If there are not enough strings, the bot will find and kill spiders to obtain them. If a crafting table is not already placed, the bot will place one. Finally, the bot will craft a fishing rod and output a message.\n}"}, "fishInNearbyWaterSafely": {"code": "async function fishInNearbyWaterSafely(bot) {\n  // Check if the bot has a fishing rod in its inventory\n  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  if (!fishingRod) {\n    await craftFishingRod(bot);\n    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  }\n\n  // Find a nearby water block\n  const waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const foundWaterBlock = bot.findBlock({\n      matching: mcData.blocksByName.water.id,\n      maxDistance: 32\n    });\n    return foundWaterBlock;\n  });\n\n  // Move to a block adjacent to the water block\n  const adjacentBlock = waterBlock.position.offset(0, 1, 0);\n  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));\n\n  // Look at the water block\n  await bot.lookAt(waterBlock.position);\n\n  // Equip the fishing rod\n  await bot.equip(fishingRod, \"hand\");\n\n  // Check for hostile mobs nearby and kill them if necessary\n  const hostileMobs = [\"zombie\", \"skeleton\", \"creeper\"];\n  for (const mobName of hostileMobs) {\n    const mob = bot.nearestEntity(entity => {\n      return entity.name === mobName && entity.position.distanceTo(bot.entity.position) < 16;\n    });\n    if (mob) {\n      await killMob(bot, mobName, 300);\n    }\n  }\n\n  // Fish in the water\n  try {\n    await bot.fish();\n    bot.chat(\"Fished in the nearby water.\");\n  } catch (error) {\n    if (error.message === \"Fishing cancelled\") {\n      bot.chat(\"Fishing was cancelled. Trying again...\");\n      await fishInNearbyWaterSafely(bot);\n    } else {\n      throw error;\n    }\n  }\n}", "description": "async function fishInNearbyWaterSafely(bot) {\n    // The function is about fishing in a nearby water block safely. It first checks if the bot has a fishing rod in its inventory, and crafts one if it doesn't. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and checks for hostile mobs nearby, killing them if necessary. Finally, it fishes in the water and retries if the fishing is cancelled.\n}"}, "craftSpyglass": {"code": "async function craftSpyglass(bot) {\n  const requiredCopperIngots = 2;\n  const requiredAmethystShards = 1;\n  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);\n  const amethystShardsCount = bot.inventory.count(mcData.itemsByName.amethyst_shard.id);\n  if (copperIngotsCount < requiredCopperIngots || amethystShardsCount < requiredAmethystShards) {\n    bot.chat(\"Not enough copper ingots or amethyst shards to craft a spyglass.\");\n    return;\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"spyglass\", 1);\n  bot.chat(\"Spyglass crafted.\");\n}", "description": "async function craftSpyglass(bot) {\n    // The function crafts a spyglass using 2 copper ingots and 1 amethyst shard. It checks if there are enough materials in the inventory, and if not, it returns. If there is a crafting table nearby, it crafts the spyglass. If not, it places a crafting table and then crafts the spyglass. Finally, it sends a chat message indicating that the spyglass has been crafted.\n}"}, "craftWoodenHoe": {"code": "async function craftWoodenHoe(bot) {\n  const requiredPlanks = 2;\n  const requiredSticks = 2;\n  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (planksCount < requiredPlanks) {\n    bot.chat(\"Not enough spruce_planks. Crafting more...\");\n    await craftItem(bot, \"spruce_planks\", requiredPlanks - planksCount);\n    bot.chat(\"Spruce_planks crafted.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"wooden_hoe\", 1);\n  bot.chat(\"Wooden hoe crafted.\");\n}", "description": "async function craftWoodenHoe(bot) {\n    // The function crafts a wooden hoe using 2 spruce planks and 2 sticks. It checks if there are enough planks and sticks in the inventory, and crafts more if necessary. If there is no crafting table nearby, it places one. Finally, it crafts a wooden hoe and logs a message.\n}"}, "catchThreeFish": {"code": "async function catchThreeFish(bot) {\n  // Check if the bot has a fishing rod in its inventory\n  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  if (!fishingRod) {\n    await craftFishingRod(bot);\n    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  }\n\n  // Find a nearby water block\n  let waterBlock;\n  while (!waterBlock) {\n    waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundWaterBlock = bot.findBlock({\n        matching: mcData.blocksByName.water.id,\n        maxDistance: 32\n      });\n      return foundWaterBlock;\n    });\n    if (!waterBlock) {\n      bot.chat(\"No path to the water block. Trying to find another water block...\");\n    }\n  }\n\n  // Move to a block adjacent to the water block\n  const adjacentBlock = waterBlock.position.offset(0, 1, 0);\n  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));\n\n  // Look at the water block\n  await bot.lookAt(waterBlock.position);\n\n  // Equip the fishing rod\n  await bot.equip(fishingRod, \"hand\");\n\n  // Fish in the water 3 times\n  for (let i = 0; i < 3; i++) {\n    try {\n      await bot.fish();\n      bot.chat(`Fish ${i + 1} caught.`);\n    } catch (error) {\n      if (error.message === \"Fishing cancelled\") {\n        bot.chat(\"Fishing was cancelled. Trying again...\");\n        i--; // Retry the same iteration\n      } else {\n        throw error;\n      }\n    }\n  }\n}", "description": "async function catchThreeFish(bot) {\n    // The function is about catching three fish using a fishing rod. First, it checks if the bot has a fishing rod in its inventory. If not, it crafts one. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and fishes in the water three times. If fishing is cancelled, it retries the same iteration.\n}"}, "craftShieldWithFurnace": {"code": "async function craftShieldWithFurnace(bot) {\n  const requiredIronIngots = 1;\n  const requiredSprucePlanks = 6;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sprucePlanksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots. Smelting iron ingots...\");\n    const furnace = bot.findBlock({\n      matching: mcData.blocksByName.furnace.id,\n      maxDistance: 32\n    });\n    if (!furnace) {\n      const furnacePosition = bot.entity.position.offset(1, 0, 0);\n      await placeItem(bot, \"furnace\", furnacePosition);\n      bot.chat(\"Furnace placed.\");\n    }\n    await smeltItem(bot, \"raw_iron\", \"coal\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ingots smelted.\");\n  }\n  if (sprucePlanksCount < requiredSprucePlanks) {\n    bot.chat(\"Not enough spruce planks. Crafting more...\");\n    await craftItem(bot, \"spruce_planks\", requiredSprucePlanks - sprucePlanksCount);\n    bot.chat(\"Spruce planks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"shield\", 1);\n  bot.chat(\"Shield crafted.\");\n}", "description": "async function craftShieldWithFurnace(bot) {\n    // The function crafts a shield using a furnace and a crafting table. It checks if there are enough iron ingots and spruce planks in the inventory, and if not, it smelts iron ingots and crafts spruce planks. If a furnace or a crafting table is not nearby, it places one. Finally, it crafts a shield using the crafting table and logs a message.\n}"}, "smeltOneRawIron": {"code": "async function smeltOneRawIron(bot) {\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  await smeltItem(bot, \"raw_iron\", \"coal\", 1);\n  bot.chat(\"1 raw iron smelted.\");\n}", "description": "async function smeltOneRawIron(bot) {\n    // The function is about smelting one raw iron using a furnace. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. It then places the furnace next to the bot and smelts one raw iron using coal as fuel. Finally, it sends a message indicating that one raw iron has been smelted.\n}"}, "craftStoneHoe": {"code": "async function craftStoneHoe(bot) {\n  const requiredCobblestones = 2;\n  const requiredSticks = 2;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones. Mining more...\");\n    await mineBlock(bot, \"stone\", requiredCobblestones - cobblestoneCount);\n    bot.chat(\"Cobblestones mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stone_hoe\", 1);\n  bot.chat(\"Stone hoe crafted.\");\n}", "description": "async function craftStoneHoe(bot) {\n    // The function crafts a stone hoe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone hoe and logs a message.\n}"}, "craftStonePickaxe": {"code": "async function craftStonePickaxe(bot) {\n  const requiredCobblestones = 3;\n  const requiredSticks = 2;\n  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (cobblestoneCount < requiredCobblestones) {\n    bot.chat(\"Not enough cobblestones. Mining more...\");\n    await mineBlock(bot, \"stone\", requiredCobblestones - cobblestoneCount);\n    bot.chat(\"Cobblestones mined.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  let craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"stone_pickaxe\", 1);\n  bot.chat(\"Stone pickaxe crafted.\");\n}", "description": "async function craftStonePickaxe(bot) {\n    // The function crafts a stone pickaxe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone pickaxe and sends a chat message.\n}"}, "craftSixteenTorches": {"code": "async function craftSixteenTorches(bot) {\n  const requiredSticks = 4;\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", 1);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"torch\", 2);\n  bot.chat(\"16 torches crafted.\");\n}", "description": "async function craftSixteenTorches(bot) {\n    // The function crafts 16 torches using sticks and a crafting table. It checks if there are enough sticks in the inventory, and if not, crafts more. If there is no crafting table nearby, it places one. Finally, it crafts 16 torches and saves the event.\n}"}, "smeltTwentyFiveIronIngots": {"code": "async function smeltTwentyFiveIronIngots(bot) {\n  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);\n  if (!furnaceInInventory) {\n    bot.chat(\"No furnace found in inventory. Please craft one first.\");\n    return;\n  }\n  let furnacePosition = bot.entity.position.offset(1, 0, 0);\n  const blockAtFurnacePosition = bot.blockAt(furnacePosition);\n  if (blockAtFurnacePosition.name === \"coal_ore\") {\n    furnacePosition = bot.entity.position.offset(-1, 0, 0);\n  }\n  await placeItem(bot, \"furnace\", furnacePosition);\n  bot.chat(\"Furnace placed.\");\n  const requiredCoal = 25;\n  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);\n  if (coalCount < requiredCoal) {\n    bot.chat(\"Not enough coal. Mining more coal...\");\n    await mineBlock(bot, \"coal_ore\", requiredCoal - coalCount);\n  }\n  await smeltItem(bot, \"raw_iron\", \"coal\", 25);\n  bot.chat(\"25 raw iron smelted.\");\n}", "description": "async function smeltTwentyFiveIronIngots(bot) {\n    // The function is about smelting 25 raw iron ingots using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. Then it places the furnace next to the bot, and checks if there is enough coal in the inventory. If there isn't, it mines coal until there are 25 pieces. Finally, it smelts 25 raw iron ingots using the furnace and coal, and returns a message indicating that the process is complete.\n}"}, "craftIronHelmet": {"code": "async function craftIronHelmet(bot) {\n  const requiredIronIngots = 5;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots to craft an iron helmet.\");\n    return;\n  }\n  let craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n    // Update the craftingTable variable after placing it\n    craftingTable = bot.blockAt(craftingTablePosition);\n  }\n  await craftItem(bot, \"iron_helmet\", 1);\n  bot.chat(\"Iron helmet crafted.\");\n}", "description": "async function craftIronHelmet(bot) {\n    // The function crafts an iron helmet using 5 iron ingots. If there are not enough iron ingots, it returns. If there is no crafting table nearby, it places one and updates the variable. Then, it crafts an iron helmet and sends a chat message.\n}"}, "craftIronChestplate": {"code": "async function craftIronChestplate(bot) {\n  const requiredIronIngots = 8;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots. Mining iron ores...\");\n    await mineBlock(bot, \"iron_ore\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ores mined. Smelting iron ingots...\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ingots smelted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"iron_chestplate\", 1);\n  bot.chat(\"Iron chestplate crafted.\");\n}", "description": "async function craftIronChestplate(bot) {\n    // The function crafts an iron chestplate using iron ingots. If there are not enough iron ingots in the inventory, the bot will mine iron ores and smelt them into iron ingots. Then, the bot will search for a nearby crafting table and place one if it is not found. Finally, the bot will craft an iron chestplate and chat a message indicating that the item has been crafted.\n}"}, "craftIronSword": {"code": "async function craftIronSword(bot) {\n  const requiredIronIngots = 2;\n  const requiredSticks = 1;\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots. Mining iron ores...\");\n    await mineBlock(bot, \"iron_ore\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ores mined. Smelting iron ingots...\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ingots smelted.\");\n  }\n  if (sticksCount < requiredSticks) {\n    bot.chat(\"Not enough sticks. Crafting more...\");\n    await craftItem(bot, \"stick\", requiredSticks - sticksCount);\n    bot.chat(\"Sticks crafted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"iron_sword\", 1);\n  bot.chat(\"Iron sword crafted.\");\n}", "description": "async function craftIronSword(bot) {\n    // The function crafts an iron sword using 2 iron ingots and 1 stick. If there are not enough iron ingots, it mines iron ores and smelts them into ingots. If there are not enough sticks, it crafts them. It then looks for a crafting table within 32 blocks, and if it doesn't find one, it places one nearby. Finally, it crafts an iron sword and logs a message.\n}"}, "craftIronLeggingsAndBoots": {"code": "async function craftIronLeggingsAndBoots(bot) {\n  const requiredIronIngots = 11; // 7 for leggings, 4 for boots\n  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);\n  if (ironIngotsCount < requiredIronIngots) {\n    bot.chat(\"Not enough iron ingots. Mining iron ores...\");\n    await mineBlock(bot, \"iron_ore\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ores mined. Smelting iron ingots...\");\n    await smeltItem(bot, \"iron_ore\", \"coal\", requiredIronIngots - ironIngotsCount);\n    bot.chat(\"Iron ingots smelted.\");\n  }\n  const craftingTable = bot.findBlock({\n    matching: mcData.blocksByName.crafting_table.id,\n    maxDistance: 32\n  });\n  if (!craftingTable) {\n    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"crafting_table\", craftingTablePosition);\n    bot.chat(\"Crafting_table placed.\");\n  }\n  await craftItem(bot, \"iron_leggings\", 1);\n  bot.chat(\"Iron leggings crafted.\");\n  await craftItem(bot, \"iron_boots\", 1);\n  bot.chat(\"Iron boots crafted.\");\n}", "description": "async function craftIronLeggingsAndBoots(bot) {\n    // The function crafts iron leggings and boots. It checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into ingots. If there is no crafting table nearby, it places one. Finally, it crafts one pair of iron leggings and one pair of iron boots.\n}"}, "catchFiveFishSafely": {"code": "async function catchFiveFishSafely(bot) {\n  // Check if the bot has a fishing rod in its inventory\n  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  if (!fishingRod) {\n    await craftFishingRod(bot);\n    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);\n  }\n\n  // Find a nearby water block\n  let waterBlock;\n  while (!waterBlock) {\n    waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const foundWaterBlock = bot.findBlock({\n        matching: mcData.blocksByName.water.id,\n        maxDistance: 32\n      });\n      return foundWaterBlock;\n    });\n    if (!waterBlock) {\n      bot.chat(\"No path to the water block. Trying to find another water block...\");\n    }\n  }\n\n  // Move to a block adjacent to the water block\n  const adjacentBlock = waterBlock.position.offset(0, 1, 0);\n  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));\n\n  // Look at the water block\n  await bot.lookAt(waterBlock.position);\n\n  // Equip the fishing rod\n  await bot.equip(fishingRod, \"hand\");\n\n  // Fish in the water 5 times\n  for (let i = 0; i < 5; i++) {\n    try {\n      await bot.fish();\n      bot.chat(`Fish ${i + 1} caught.`);\n    } catch (error) {\n      if (error.message === \"Fishing cancelled\") {\n        bot.chat(\"Fishing was cancelled. Trying again...\");\n        i--; // Retry the same iteration\n      } else {\n        throw error;\n      }\n    }\n  }\n}", "description": "async function catchFiveFishSafely(bot) {\n    // The function is about catching five fish safely using a fishing rod. First, it checks if the bot has a fishing rod in its inventory. If not, it crafts one. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and fishes in the water five times. If fishing is cancelled, it retries the same iteration.\n}"}, "equipIronArmor": {"code": "async function equipIronArmor(bot) {\n  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id);\n  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id);\n  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id);\n  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id);\n  if (ironHelmet) {\n    await bot.equip(ironHelmet, \"head\");\n    bot.chat(\"Iron helmet equipped.\");\n  } else {\n    bot.chat(\"Iron helmet not found in inventory.\");\n  }\n  if (ironChestplate) {\n    await bot.equip(ironChestplate, \"torso\");\n    bot.chat(\"Iron chestplate equipped.\");\n  } else {\n    bot.chat(\"Iron chestplate not found in inventory.\");\n  }\n  if (ironLeggings) {\n    await bot.equip(ironLeggings, \"legs\");\n    bot.chat(\"Iron leggings equipped.\");\n  } else {\n    bot.chat(\"Iron leggings not found in inventory.\");\n  }\n  if (ironBoots) {\n    await bot.equip(ironBoots, \"feet\");\n    bot.chat(\"Iron boots equipped.\");\n  } else {\n    bot.chat(\"Iron boots not found in inventory.\");\n  }\n}", "description": "async function equipIronArmor(bot) {\n    // The function equips the player with iron armor if it is available in the inventory. It checks for the presence of each piece of iron armor (helmet, chestplate, leggings, and boots) and equips them one by one. If a piece of armor is not found in the inventory, it sends a message to the chat indicating that it is not available.\n}"}}


================================================
FILE: skill_library/trial2/skill/code/catchFiveFishSafely.js
================================================
async function catchFiveFishSafely(bot) {
  // Check if the bot has a fishing rod in its inventory
  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  if (!fishingRod) {
    await craftFishingRod(bot);
    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  }

  // Find a nearby water block
  let waterBlock;
  while (!waterBlock) {
    waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundWaterBlock = bot.findBlock({
        matching: mcData.blocksByName.water.id,
        maxDistance: 32
      });
      return foundWaterBlock;
    });
    if (!waterBlock) {
      bot.chat("No path to the water block. Trying to find another water block...");
    }
  }

  // Move to a block adjacent to the water block
  const adjacentBlock = waterBlock.position.offset(0, 1, 0);
  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));

  // Look at the water block
  await bot.lookAt(waterBlock.position);

  // Equip the fishing rod
  await bot.equip(fishingRod, "hand");

  // Fish in the water 5 times
  for (let i = 0; i < 5; i++) {
    try {
      await bot.fish();
      bot.chat(`Fish ${i + 1} caught.`);
    } catch (error) {
      if (error.message === "Fishing cancelled") {
        bot.chat("Fishing was cancelled. Trying again...");
        i--; // Retry the same iteration
      } else {
        throw error;
      }
    }
  }
}


================================================
FILE: skill_library/trial2/skill/code/catchThreeFish.js
================================================
async function catchThreeFish(bot) {
  // Check if the bot has a fishing rod in its inventory
  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  if (!fishingRod) {
    await craftFishingRod(bot);
    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  }

  // Find a nearby water block
  let waterBlock;
  while (!waterBlock) {
    waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundWaterBlock = bot.findBlock({
        matching: mcData.blocksByName.water.id,
        maxDistance: 32
      });
      return foundWaterBlock;
    });
    if (!waterBlock) {
      bot.chat("No path to the water block. Trying to find another water block...");
    }
  }

  // Move to a block adjacent to the water block
  const adjacentBlock = waterBlock.position.offset(0, 1, 0);
  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));

  // Look at the water block
  await bot.lookAt(waterBlock.position);

  // Equip the fishing rod
  await bot.equip(fishingRod, "hand");

  // Fish in the water 3 times
  for (let i = 0; i < 3; i++) {
    try {
      await bot.fish();
      bot.chat(`Fish ${i + 1} caught.`);
    } catch (error) {
      if (error.message === "Fishing cancelled") {
        bot.chat("Fishing was cancelled. Trying again...");
        i--; // Retry the same iteration
      } else {
        throw error;
      }
    }
  }
}


================================================
FILE: skill_library/trial2/skill/code/checkStonePickaxe.js
================================================
async function checkStonePickaxe(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (stonePickaxe) {
    bot.chat("The bot already has a stone pickaxe in its inventory.");
  } else {
    bot.chat("The bot does not have a stone pickaxe in its inventory.");
  }
}


================================================
FILE: skill_library/trial2/skill/code/chopDownSpruceLogs.js
================================================
async function chopDownSpruceLogs(bot) {
  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);
  const logsToMine = 5 - spruceLogCount;
  if (logsToMine > 0) {
    bot.chat("Chopping down spruce logs...");
    await mineBlock(bot, "spruce_log", logsToMine);
    bot.chat("Chopped down 5 spruce logs.");
  } else {
    bot.chat("Already have 5 spruce logs in inventory.");
  }
}


================================================
FILE: skill_library/trial2/skill/code/chopDownSpruceLogsV2.js
================================================
async function chopDownSpruceLogs(bot) {
  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);
  const logsToMine = 5 - spruceLogCount;
  if (logsToMine > 0) {
    bot.chat("Chopping down spruce logs...");
    await mineBlock(bot, "spruce_log", logsToMine);
    bot.chat("Chopped down 5 spruce logs.");
  } else {
    bot.chat("Already have 5 spruce logs in inventory.");
  }
}


================================================
FILE: skill_library/trial2/skill/code/chopSpruceLogs.js
================================================
async function chopSpruceLogs(bot) {
  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);
  const logsToMine = 3 - spruceLogCount;
  if (logsToMine > 0) {
    bot.chat("Chopping down spruce logs...");
    await mineBlock(bot, "spruce_log", logsToMine);
    bot.chat("Chopped down 3 spruce logs.");
  } else {
    bot.chat("Already have 3 spruce logs in inventory.");
  }
}


================================================
FILE: skill_library/trial2/skill/code/collectWaterWithBucket.js
================================================
async function collectWaterWithBucket(bot) {
  const waterBlock = bot.findBlock({
    matching: mcData.blocksByName.water.id,
    maxDistance: 32
  });
  if (!waterBlock) {
    bot.chat("No water block found nearby. Exploring...");
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundWaterBlock = bot.findBlock({
        matching: mcData.blocksByName.water.id,
        maxDistance: 32
      });
      return foundWaterBlock;
    });
  }
  const bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);
  await bot.equip(bucket, "hand");
  await bot.lookAt(waterBlock.position);
  await bot.activateItem();
  bot.chat("Water collected with bucket.");
}


================================================
FILE: skill_library/trial2/skill/code/cookMutton.js
================================================
async function cookMutton(bot) {
  const rawMuttonCount = bot.inventory.count(mcData.itemsByName.mutton.id);
  if (rawMuttonCount < 5) {
    bot.chat("Not enough raw mutton to cook. Please collect more first.");
    return;
  }
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  const requiredCoal = 5;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more coal...");
    await mineBlock(bot, "coal_ore", requiredCoal - coalCount);
  }
  await smeltItem(bot, "mutton", "coal", 5);
  bot.chat("5 mutton cooked.");
}


================================================
FILE: skill_library/trial2/skill/code/craftBucket.js
================================================
async function craftBucket(bot) {
  const requiredIronIngots = 3;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots to craft a bucket.");
    return;
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "bucket", 1);
  bot.chat("Bucket crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftChest.js
================================================
async function craftChest(bot) {
  const requiredPlanks = 8;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Not enough spruce_planks. Mining a spruce_log and crafting more...");
    await mineBlock(bot, "spruce_log", 1);
    await craftItem(bot, "spruce_planks", 1);
    bot.chat("Spruce_planks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  bot.chat("Crafting a chest...");
  await craftItem(bot, "chest", 1);
  bot.chat("Chest crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftEightSticks.js
================================================
async function craftEightSticks(bot) {
  const requiredPlanks = 2;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Not enough spruce_planks. Mining a spruce_log and crafting more...");
    await mineBlock(bot, "spruce_log", 1);
    await craftItem(bot, "spruce_planks", 1);
    bot.chat("Spruce_planks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stick", 2);
  bot.chat("8 sticks crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftEightTorches.js
================================================
async function craftEightTorches(bot) {
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "torch", 1);
  bot.chat("8 torches crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftFishingRod.js
================================================
async function craftFishingRod(bot) {
  // Check if we have enough strings
  const requiredStrings = 2;
  const stringsCount = bot.inventory.count(mcData.itemsByName.string.id);
  if (stringsCount < requiredStrings) {
    // Find and kill spiders to obtain strings
    while (bot.inventory.count(mcData.itemsByName.string.id) < requiredStrings) {
      bot.chat("Finding a spider to obtain strings...");
      const spider = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const spider = bot.nearestEntity(entity => {
          return entity.name === "spider" && entity.position.distanceTo(bot.entity.position) < 32;
        });
        return spider;
      });
      if (spider) {
        bot.chat("Spider found. Killing it...");
        await killMob(bot, "spider", 300);
        bot.chat("Spider killed.");
      } else {
        bot.chat("Could not find a spider. Trying again...");
      }
    }
  }

  // Place a crafting table if not already placed
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }

  // Craft a fishing rod using the 3 sticks and 2 strings
  await craftItem(bot, "fishing_rod", 1);
  bot.chat("Fishing rod crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftFurnace.js
================================================
async function craftFurnace(bot) {
  const requiredCobblestones = 8;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones to craft a furnace.");
    return;
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "furnace", 1);
  bot.chat("Furnace crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronChestplate.js
================================================
async function craftIronChestplate(bot) {
  const requiredIronIngots = 8;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots. Mining iron ores...");
    await mineBlock(bot, "iron_ore", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ores mined. Smelting iron ingots...");
    await smeltItem(bot, "iron_ore", "coal", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ingots smelted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "iron_chestplate", 1);
  bot.chat("Iron chestplate crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronHelmet.js
================================================
async function craftIronHelmet(bot) {
  const requiredIronIngots = 5;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots to craft an iron helmet.");
    return;
  }
  let craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
    // Update the craftingTable variable after placing it
    craftingTable = bot.blockAt(craftingTablePosition);
  }
  await craftItem(bot, "iron_helmet", 1);
  bot.chat("Iron helmet crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronLeggingsAndBoots.js
================================================
async function craftIronLeggingsAndBoots(bot) {
  const requiredIronIngots = 11; // 7 for leggings, 4 for boots
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots. Mining iron ores...");
    await mineBlock(bot, "iron_ore", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ores mined. Smelting iron ingots...");
    await smeltItem(bot, "iron_ore", "coal", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ingots smelted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "iron_leggings", 1);
  bot.chat("Iron leggings crafted.");
  await craftItem(bot, "iron_boots", 1);
  bot.chat("Iron boots crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronPickaxe.js
================================================
async function craftIronPickaxe(bot) {
  const requiredIronIngots = 3;
  const requiredSticks = 2;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (ironIngotsCount < requiredIronIngots || sticksCount < requiredSticks) {
    bot.chat("Not enough iron ingots or sticks to craft an iron pickaxe.");
    return;
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "iron_pickaxe", 1);
  bot.chat("Iron pickaxe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronPickaxeWithMaterials.js
================================================
async function craftIronPickaxeWithMaterials(bot) {
  const requiredIronIngots = 3;
  const requiredSticks = 2;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots. Mining iron ores...");
    await mineBlock(bot, "iron_ore", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ores mined. Smelting iron ingots...");
    await smeltItem(bot, "iron_ore", "coal", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ingots smelted.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "iron_pickaxe", 1);
  bot.chat("Iron pickaxe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftIronSword.js
================================================
async function craftIronSword(bot) {
  const requiredIronIngots = 2;
  const requiredSticks = 1;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots. Mining iron ores...");
    await mineBlock(bot, "iron_ore", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ores mined. Smelting iron ingots...");
    await smeltItem(bot, "iron_ore", "coal", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ingots smelted.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "iron_sword", 1);
  bot.chat("Iron sword crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftShieldWithFurnace.js
================================================
async function craftShieldWithFurnace(bot) {
  const requiredIronIngots = 1;
  const requiredSprucePlanks = 6;
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sprucePlanksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  if (ironIngotsCount < requiredIronIngots) {
    bot.chat("Not enough iron ingots. Smelting iron ingots...");
    const furnace = bot.findBlock({
      matching: mcData.blocksByName.furnace.id,
      maxDistance: 32
    });
    if (!furnace) {
      const furnacePosition = bot.entity.position.offset(1, 0, 0);
      await placeItem(bot, "furnace", furnacePosition);
      bot.chat("Furnace placed.");
    }
    await smeltItem(bot, "raw_iron", "coal", requiredIronIngots - ironIngotsCount);
    bot.chat("Iron ingots smelted.");
  }
  if (sprucePlanksCount < requiredSprucePlanks) {
    bot.chat("Not enough spruce planks. Crafting more...");
    await craftItem(bot, "spruce_planks", requiredSprucePlanks - sprucePlanksCount);
    bot.chat("Spruce planks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "shield", 1);
  bot.chat("Shield crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftSixteenTorches.js
================================================
async function craftSixteenTorches(bot) {
  const requiredSticks = 4;
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", 1);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "torch", 2);
  bot.chat("16 torches crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftSpyglass.js
================================================
async function craftSpyglass(bot) {
  const requiredCopperIngots = 2;
  const requiredAmethystShards = 1;
  const copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);
  const amethystShardsCount = bot.inventory.count(mcData.itemsByName.amethyst_shard.id);
  if (copperIngotsCount < requiredCopperIngots || amethystShardsCount < requiredAmethystShards) {
    bot.chat("Not enough copper ingots or amethyst shards to craft a spyglass.");
    return;
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "spyglass", 1);
  bot.chat("Spyglass crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftSticks.js
================================================
async function craftSticks(bot) {
  const requiredPlanks = 2;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Not enough spruce_planks. Mining a spruce_log and crafting more...");
    await mineBlock(bot, "spruce_log", 1);
    await craftItem(bot, "spruce_planks", 1);
    bot.chat("Spruce_planks crafted.");
  }
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);
  bot.chat("Crafting_table placed.");
  await craftItem(bot, "stick", 1);
  bot.chat("4 sticks crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftStoneAxe.js
================================================
async function craftStoneAxe(bot) {
  const requiredCobblestones = 3;
  const requiredSticks = 2;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones. Mining more...");
    await mineBlock(bot, "stone", requiredCobblestones - cobblestoneCount);
    bot.chat("Cobblestones mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stone_axe", 1);
  bot.chat("Stone axe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftStoneHoe.js
================================================
async function craftStoneHoe(bot) {
  const requiredCobblestones = 2;
  const requiredSticks = 2;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones. Mining more...");
    await mineBlock(bot, "stone", requiredCobblestones - cobblestoneCount);
    bot.chat("Cobblestones mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stone_hoe", 1);
  bot.chat("Stone hoe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftStonePickaxe.js
================================================
async function craftStonePickaxe(bot) {
  const requiredCobblestones = 3;
  const requiredSticks = 2;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones. Mining more...");
    await mineBlock(bot, "stone", requiredCobblestones - cobblestoneCount);
    bot.chat("Cobblestones mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  let craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stone_pickaxe", 1);
  bot.chat("Stone pickaxe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftStoneShovel.js
================================================
async function craftStoneShovel(bot) {
  const requiredCobblestones = 1;
  const requiredSticks = 2;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones. Mining more...");
    await mineBlock(bot, "stone", requiredCobblestones - cobblestoneCount);
    bot.chat("Cobblestones mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stone_shovel", 1);
  bot.chat("Stone shovel crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftStoneSword.js
================================================
async function craftStoneSword(bot) {
  const requiredCobblestones = 2;
  const requiredSticks = 1;
  const cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (cobblestoneCount < requiredCobblestones) {
    bot.chat("Not enough cobblestones. Mining more...");
    await mineBlock(bot, "stone", requiredCobblestones - cobblestoneCount);
    bot.chat("Cobblestones mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftSticks(bot);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "stone_sword", 1);
  bot.chat("Stone sword crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftTorches.js
================================================
async function craftTorches(bot) {
  const requiredCoal = 2;
  const requiredSticks = 2;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more...");
    await mineBlock(bot, "coal_ore", requiredCoal - coalCount);
    bot.chat("Coal mined.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", 1);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "torch", 1);
  bot.chat("8 torches crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftTwentySprucePlanks.js
================================================
async function craftTwentySprucePlanks(bot) {
  const requiredLogs = 5;
  const spruceLogCount = bot.inventory.count(mcData.itemsByName.spruce_log.id);
  const logsToMine = requiredLogs - spruceLogCount;
  if (logsToMine > 0) {
    bot.chat("Not enough spruce logs. Chopping down more...");
    await mineBlock(bot, "spruce_log", logsToMine);
    bot.chat("Spruce logs chopped down.");
  }
  bot.chat("Crafting 20 spruce planks...");
  await craftItem(bot, "spruce_planks", requiredLogs);
  bot.chat("20 spruce planks crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftWhiteBedWithExploration.js
================================================
async function craftWhiteBedWithExploration(bot) {
  // Step 1: Explore the area to find and kill sheep to collect the required wool blocks if needed
  const requiredWool = 3;
  const woolCount = bot.inventory.count(mcData.itemsByName.white_wool.id);
  if (woolCount < requiredWool) {
    bot.chat("Collecting wool from sheep...");
    for (let i = 0; i < requiredWool - woolCount; i++) {
      const sheep = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const sheep = bot.nearestEntity(entity => {
          return entity.name === "sheep" && entity.position.distanceTo(bot.entity.position) < 32;
        });
        return sheep;
      });
      if (sheep) {
        await killMob(bot, "sheep");
      } else {
        bot.chat("No sheep found. Please try again later.");
        return;
      }
    }
    bot.chat("Wool collected.");
  }

  // Step 2: Craft 2 more spruce planks if needed
  const requiredPlanks = 3;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Crafting more spruce_planks...");
    await craftItem(bot, "spruce_planks", requiredPlanks - planksCount);
    bot.chat("Spruce_planks crafted.");
  }

  // Step 3: Place a crafting table if not already placed
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }

  // Step 4: Craft a white bed using the 3 white wool blocks and 3 spruce planks
  bot.chat("Crafting a white bed...");
  await craftItem(bot, "white_bed", 1);
  bot.chat("White bed crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftWoodenHoe.js
================================================
async function craftWoodenHoe(bot) {
  const requiredPlanks = 2;
  const requiredSticks = 2;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Not enough spruce_planks. Crafting more...");
    await craftItem(bot, "spruce_planks", requiredPlanks - planksCount);
    bot.chat("Spruce_planks crafted.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTable = bot.findBlock({
    matching: mcData.blocksByName.crafting_table.id,
    maxDistance: 32
  });
  if (!craftingTable) {
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    bot.chat("Crafting_table placed.");
  }
  await craftItem(bot, "wooden_hoe", 1);
  bot.chat("Wooden hoe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftWoodenPickaxe.js
================================================
async function craftWoodenPickaxe(bot) {
  const requiredPlanks = 3;
  const requiredSticks = 2;
  const planksCount = bot.inventory.count(mcData.itemsByName.spruce_planks.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  if (planksCount < requiredPlanks) {
    bot.chat("Not enough spruce_planks. Crafting more...");
    await craftItem(bot, "spruce_planks", requiredPlanks - planksCount);
    bot.chat("Spruce_planks crafted.");
  }
  if (sticksCount < requiredSticks) {
    bot.chat("Not enough sticks. Crafting more...");
    await craftItem(bot, "stick", requiredSticks - sticksCount);
    bot.chat("Sticks crafted.");
  }
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);
  bot.chat("Crafting_table placed.");
  await craftItem(bot, "wooden_pickaxe", 1);
  bot.chat("Wooden pickaxe crafted.");
}


================================================
FILE: skill_library/trial2/skill/code/craftWoodenPlanks.js
================================================
async function craftWoodenPlanks(bot) {
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
  const plankNames = ["oak_planks", "birch_planks", "spruce_planks", "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks"];
  const logInInventory = logNames.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);
  if (!logInInventory) {
    bot.chat("No wooden log in inventory. Mining a wooden log...");
    await mineWoodLog(bot);
  }
  const logIndex = logNames.indexOf(logInInventory);
  const plankName = plankNames[logIndex];
  bot.chat(`Crafting 4 ${plankName}...`);
  await craftItem(bot, plankName, 1);
  bot.chat(`4 ${plankName} crafted.`);
}


================================================
FILE: skill_library/trial2/skill/code/eatCookedMutton.js
================================================
async function eatCookedMutton(bot) {
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);
  await bot.equip(cookedMutton, "hand");
  await bot.consume();
  bot.chat("Cooked mutton eaten.");
}


================================================
FILE: skill_library/trial2/skill/code/eatCookedMuttonV2.js
================================================
async function eatCookedMutton(bot) {
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);
  await bot.equip(cookedMutton, "hand");
  await bot.consume();
  bot.chat("Cooked mutton eaten.");
}


================================================
FILE: skill_library/trial2/skill/code/eatCookedMuttonV3.js
================================================
async function eatCookedMutton(bot) {
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName.cooked_mutton.id);
  await bot.equip(cookedMutton, "hand");
  await bot.consume();
  bot.chat("Cooked mutton eaten.");
}


================================================
FILE: skill_library/trial2/skill/code/equipIronArmor.js
================================================
async function equipIronArmor(bot) {
  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id);
  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id);
  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id);
  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id);
  if (ironHelmet) {
    await bot.equip(ironHelmet, "head");
    bot.chat("Iron helmet equipped.");
  } else {
    bot.chat("Iron helmet not found in inventory.");
  }
  if (ironChestplate) {
    await bot.equip(ironChestplate, "torso");
    bot.chat("Iron chestplate equipped.");
  } else {
    bot.chat("Iron chestplate not found in inventory.");
  }
  if (ironLeggings) {
    await bot.equip(ironLeggings, "legs");
    bot.chat("Iron leggings equipped.");
  } else {
    bot.chat("Iron leggings not found in inventory.");
  }
  if (ironBoots) {
    await bot.equip(ironBoots, "feet");
    bot.chat("Iron boots equipped.");
  } else {
    bot.chat("Iron boots not found in inventory.");
  }
}


================================================
FILE: skill_library/trial2/skill/code/exploreCave.js
================================================
async function exploreCave(bot) {
  const torches = bot.inventory.findInventoryItem(mcData.itemsByName.torch.id);
  if (!torches) {
    bot.chat("No torches found in inventory. Crafting torches...");
    await craftTorches(bot);
  }
  await bot.equip(mcData.itemsByName.torch.id, "hand");
  const caveEntrance = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    return caveBlock;
  });
  if (!caveEntrance) {
    bot.chat("No cave entrance found nearby.");
    return;
  }
  bot.chat("Cave entrance found. Exploring the cave...");
  await exploreUntil(bot, new Vec3(1, 0, 1), 300, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    if (caveBlock) {
      bot.placeBlock(caveBlock, new Vec3(0, 1, 0));
    }
    const mob = bot.nearestEntity(entity => {
      return entity.type === "mob" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    if (mob) {
      killMob(bot, mob.name, 300);
    }
    return null; // Continue exploring until the time limit is reached
  });

  bot.chat("Finished exploring the cave.");
}


================================================
FILE: skill_library/trial2/skill/code/exploreCaveAndGatherResources.js
================================================
async function exploreCaveAndGatherResources(bot) {
  // Equip torches
  const torches = bot.inventory.findInventoryItem(mcData.itemsByName.torch.id);
  if (!torches) {
    bot.chat("No torches found in inventory. Crafting torches...");
    await craftTorches(bot);
  }
  await bot.equip(mcData.itemsByName.torch.id, "hand");

  // Find a cave entrance and start exploring
  const caveEntrance = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    return caveBlock;
  });
  if (!caveEntrance) {
    bot.chat("No cave entrance found nearby.");
    return;
  }
  bot.chat("Cave entrance found. Exploring the cave...");

  // Explore the cave and gather resources
  await exploreUntil(bot, new Vec3(1, 0, 1), 300, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    if (caveBlock) {
      bot.placeBlock(caveBlock, new Vec3(0, 1, 0));
    }
    const mob = bot.nearestEntity(entity => {
      return entity.type === "mob" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    if (mob) {
      killMob(bot, mob.name, 300);
    }
    const ores = ["coal_ore", "iron_ore", "gold_ore", "diamond_ore"];
    for (const ore of ores) {
      const oreBlock = bot.findBlock({
        matching: mcData.blocksByName[ore].id,
        maxDistance: 32
      });
      if (oreBlock) {
        mineBlock(bot, ore, 1);
      }
    }
    return null; // Continue exploring until the time limit is reached
  });

  bot.chat("Finished exploring the cave and gathering resources.");
}


================================================
FILE: skill_library/trial2/skill/code/exploreCaveAndGatherResourcesV2.js
================================================
async function exploreCaveAndGatherResources(bot) {
  // Equip torches
  const torches = bot.inventory.findInventoryItem(mcData.itemsByName.torch.id);
  if (!torches) {
    bot.chat("No torches found in inventory. Crafting torches...");
    await craftTorches(bot);
  }
  await bot.equip(mcData.itemsByName.torch.id, "hand");

  // Find a cave entrance and start exploring
  const caveEntrance = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    return caveBlock;
  });
  if (!caveEntrance) {
    bot.chat("No cave entrance found nearby.");
    return;
  }
  bot.chat("Cave entrance found. Exploring the cave...");

  // Explore the cave and gather resources
  await exploreUntil(bot, new Vec3(1, 0, 1), 300, () => {
    const caveBlock = bot.findBlock({
      matching: block => {
        return block && block.name === "air" && block.position && block.position.y < 60;
      },
      maxDistance: 32
    });
    if (caveBlock) {
      bot.placeBlock(caveBlock, new Vec3(0, 1, 0));
    }
    const mob = bot.nearestEntity(entity => {
      return entity.type === "mob" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    if (mob) {
      killMob(bot, mob.name, 300);
    }
    const ores = ["coal_ore", "iron_ore", "gold_ore", "diamond_ore"];
    for (const ore of ores) {
      const oreBlock = bot.findBlock({
        matching: mcData.blocksByName[ore].id,
        maxDistance: 32
      });
      if (oreBlock) {
        mineBlock(bot, ore, 1);
      }
    }
    return null; // Continue exploring until the time limit is reached
  });

  bot.chat("Finished exploring the cave and gathering resources.");
}


================================================
FILE: skill_library/trial2/skill/code/fishInNearbyWaterSafely.js
================================================
async function fishInNearbyWaterSafely(bot) {
  // Check if the bot has a fishing rod in its inventory
  let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  if (!fishingRod) {
    await craftFishingRod(bot);
    fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
  }

  // Find a nearby water block
  const waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const foundWaterBlock = bot.findBlock({
      matching: mcData.blocksByName.water.id,
      maxDistance: 32
    });
    return foundWaterBlock;
  });

  // Move to a block adjacent to the water block
  const adjacentBlock = waterBlock.position.offset(0, 1, 0);
  await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));

  // Look at the water block
  await bot.lookAt(waterBlock.position);

  // Equip the fishing rod
  await bot.equip(fishingRod, "hand");

  // Check for hostile mobs nearby and kill them if necessary
  const hostileMobs = ["zombie", "skeleton", "creeper"];
  for (const mobName of hostileMobs) {
    const mob = bot.nearestEntity(entity => {
      return entity.name === mobName && entity.position.distanceTo(bot.entity.position) < 16;
    });
    if (mob) {
      await killMob(bot, mobName, 300);
    }
  }

  // Fish in the water
  try {
    await bot.fish();
    bot.chat("Fished in the nearby water.");
  } catch (error) {
    if (error.message === "Fishing cancelled") {
      bot.chat("Fishing was cancelled. Trying again...");
      await fishInNearbyWaterSafely(bot);
    } else {
      throw error;
    }
  }
}


================================================
FILE: skill_library/trial2/skill/code/mineCoalOre.js
================================================
async function mineCoalOre(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (!stonePickaxe) {
    bot.chat("No stone pickaxe found in inventory.");
    return;
  }
  await bot.equip(mcData.itemsByName.stone_pickaxe.id, "hand");
  const coalOreBlock = bot.findBlock({
    matching: mcData.blocksByName.coal_ore.id,
    maxDistance: 32
  });
  if (!coalOreBlock) {
    bot.chat("No coal ore found nearby. Exploring...");
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundCoalOre = bot.findBlock({
        matching: mcData.blocksByName.coal_ore.id,
        maxDistance: 32
      });
      return foundCoalOre;
    });
  }
  await mineBlock(bot, "coal_ore", 1);
  bot.chat("Coal ore mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineCopperOreWithStonePickaxe.js
================================================
async function mineCopperOreWithStonePickaxe(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (!stonePickaxe) {
    bot.chat("No stone pickaxe found. Mining cobblestone and crafting one...");
    await mineBlock(bot, "stone", 3);
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    await craftItem(bot, "stone_pickaxe", 1);
    bot.chat("Stone pickaxe crafted.");
  }
  await bot.equip(mcData.itemsByName.stone_pickaxe.id, "hand");
  const copperOreBlock = bot.findBlock({
    matching: mcData.blocksByName.copper_ore.id,
    maxDistance: 32
  });
  if (!copperOreBlock) {
    bot.chat("No copper ore found nearby. Exploring...");
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundCopperOre = bot.findBlock({
        matching: mcData.blocksByName.copper_ore.id,
        maxDistance: 32
      });
      return foundCopperOre;
    });
  }
  await mineBlock(bot, "copper_ore", 1);
  bot.chat("Copper ore mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineFiveCoalOres.js
================================================
async function mineFiveCoalOres(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (!stonePickaxe) {
    bot.chat("No stone pickaxe found in inventory.");
    return;
  }
  await bot.equip(mcData.itemsByName.stone_pickaxe.id, "hand");
  await mineBlock(bot, "coal_ore", 5);
  bot.chat("5 coal ores mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineFiveCoalOresV2.js
================================================
async function mineFiveCoalOres(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (!stonePickaxe) {
    bot.chat("No stone pickaxe found in inventory.");
    return;
  }
  await bot.equip(mcData.itemsByName.stone_pickaxe.id, "hand");
  await mineBlock(bot, "coal_ore", 5);
  bot.chat("5 coal ores mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineFiveCopperOres.js
================================================
async function mineFiveCopperOres(bot) {
  const copperOreCount = bot.inventory.count(mcData.itemsByName.copper_ore.id);
  if (copperOreCount >= 5) {
    bot.chat("Already have 5 copper ores in inventory.");
    return;
  }
  await bot.equip(mcData.itemsByName.iron_pickaxe.id, "hand");
  await mineBlock(bot, "copper_ore", 5 - copperOreCount);
  bot.chat("5 copper ores mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineFiveIronOres.js
================================================
async function mineFiveIronOres(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
  if (!stonePickaxe && !ironPickaxe) {
    bot.chat("No stone or iron pickaxe found. Mining cobblestone and crafting a stone pickaxe...");
    await mineBlock(bot, "stone", 3);
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    await craftItem(bot, "stone_pickaxe", 1);
    bot.chat("Stone pickaxe crafted.");
  }
  const pickaxeToUse = ironPickaxe || stonePickaxe;
  await bot.equip(pickaxeToUse, "hand");
  await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
    const foundIronOre = bot.findBlock({
      matching: mcData.blocksByName.iron_ore.id,
      maxDistance: 32
    });
    return foundIronOre;
  });
  await mineBlock(bot, "iron_ore", 5);
  bot.chat("5 iron ores mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineLapisOre.js
================================================
async function mineLapisOre(bot) {
  const pickaxeTypes = [mcData.itemsByName.stone_pickaxe.id, mcData.itemsByName.iron_pickaxe.id, mcData.itemsByName.diamond_pickaxe.id, mcData.itemsByName.netherite_pickaxe.id];
  let pickaxe = bot.inventory.items().find(item => pickaxeTypes.includes(item.type));
  if (!pickaxe) {
    bot.chat("No suitable pickaxe found. Mining cobblestone and crafting a stone pickaxe...");
    await mineBlock(bot, "stone", 3);
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    await craftItem(bot, "stone_pickaxe", 1);
    pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
    bot.chat("Stone pickaxe crafted.");
  }
  await bot.equip(pickaxe, "hand");
  const lapisOreBlock = await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
    const foundLapisOre = bot.findBlock({
      matching: mcData.blocksByName.lapis_ore.id,
      maxDistance: 32
    });
    return foundLapisOre;
  });
  if (!lapisOreBlock) {
    bot.chat("No lapis ore found nearby. Exploring...");
  }
  await mineBlock(bot, "lapis_ore", 1);
  bot.chat("Lapis ore mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineThreeIronOres.js
================================================
async function mineThreeIronOres(bot) {
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
  if (!stonePickaxe) {
    bot.chat("No stone pickaxe found. Mining cobblestone and crafting one...");
    await mineBlock(bot, "stone", 3);
    const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    await craftItem(bot, "stone_pickaxe", 1);
    bot.chat("Stone pickaxe crafted.");
  }
  await bot.equip(mcData.itemsByName.stone_pickaxe.id, "hand");
  const ironOreBlock = await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
    const foundIronOre = bot.findBlock({
      matching: mcData.blocksByName.iron_ore.id,
      maxDistance: 32
    });
    return foundIronOre;
  });
  if (!ironOreBlock) {
    bot.chat("No iron ore found nearby. Exploring...");
  }
  await mineBlock(bot, "iron_ore", 3);
  bot.chat("3 iron ores mined.");
}


================================================
FILE: skill_library/trial2/skill/code/mineWoodLog.js
================================================
async function mineWoodLog(bot) {
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
  const logBlock = bot.findBlock({
    matching: block => logNames.includes(block.name),
    maxDistance: 32
  });
  if (!logBlock) {
    bot.chat("No wood log found nearby. Exploring...");
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundLog = bot.findBlock({
        matching: block => logNames.includes(block.name),
        maxDistance: 32
      });
      return foundLog;
    });
  }
  await mineBlock(bot, logBlock.name, 1);
  bot.chat("Wood log mined.");
}


================================================
FILE: skill_library/trial2/skill/code/smeltOneRawIron.js
================================================
async function smeltOneRawIron(bot) {
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  await smeltItem(bot, "raw_iron", "coal", 1);
  bot.chat("1 raw iron smelted.");
}


================================================
FILE: skill_library/trial2/skill/code/smeltRawCopper.js
================================================
async function smeltRawCopper(bot) {
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  const requiredCoal = 7;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more coal...");
    await mineCoalOre(bot);
  }
  await smeltItem(bot, "raw_copper", "coal", 7);
  bot.chat("7 raw copper smelted.");
}


================================================
FILE: skill_library/trial2/skill/code/smeltRawIron.js
================================================
async function smeltRawIron(bot) {
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  const requiredCoal = 3;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more coal...");
    await mineBlock(bot, "coal_ore", requiredCoal - coalCount);
  }
  await smeltItem(bot, "raw_iron", "coal", 3);
  bot.chat("3 raw iron smelted.");
}


================================================
FILE: skill_library/trial2/skill/code/smeltSixRawIron.js
================================================
async function smeltSixRawIron(bot) {
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  const requiredCoal = 6;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more coal...");
    await mineBlock(bot, "coal_ore", requiredCoal - coalCount);
  }
  await smeltItem(bot, "raw_iron", "coal", 6);
  bot.chat("6 raw iron smelted.");
}


================================================
FILE: skill_library/trial2/skill/code/smeltTwentyFiveIronIngots.js
================================================
async function smeltTwentyFiveIronIngots(bot) {
  const furnaceInInventory = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  if (!furnaceInInventory) {
    bot.chat("No furnace found in inventory. Please craft one first.");
    return;
  }
  let furnacePosition = bot.entity.position.offset(1, 0, 0);
  const blockAtFurnacePosition = bot.blockAt(furnacePosition);
  if (blockAtFurnacePosition.name === "coal_ore") {
    furnacePosition = bot.entity.position.offset(-1, 0, 0);
  }
  await placeItem(bot, "furnace", furnacePosition);
  bot.chat("Furnace placed.");
  const requiredCoal = 25;
  const coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
  if (coalCount < requiredCoal) {
    bot.chat("Not enough coal. Mining more coal...");
    await mineBlock(bot, "coal_ore", requiredCoal - coalCount);
  }
  await smeltItem(bot, "raw_iron", "coal", 25);
  bot.chat("25 raw iron smelted.");
}


================================================
FILE: skill_library/trial2/skill/description/catchFiveFishSafely.txt
================================================
async function catchFiveFishSafely(bot) {
    // The function is about catching five fish safely using a fishing rod. First, it checks if the bot has a fishing rod in its inventory. If not, it crafts one. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and fishes in the water five times. If fishing is cancelled, it retries the same iteration.
}


================================================
FILE: skill_library/trial2/skill/description/catchThreeFish.txt
================================================
async function catchThreeFish(bot) {
    // The function is about catching three fish using a fishing rod. First, it checks if the bot has a fishing rod in its inventory. If not, it crafts one. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and fishes in the water three times. If fishing is cancelled, it retries the same iteration.
}


================================================
FILE: skill_library/trial2/skill/description/checkStonePickaxe.txt
================================================
async function checkStonePickaxe(bot) {
    // The function checks if the bot has a stone pickaxe in its inventory and sends a chat message indicating whether it has one or not.
}


================================================
FILE: skill_library/trial2/skill/description/chopDownSpruceLogs.txt
================================================
async function chopDownSpruceLogs(bot) {
    // The function is about chopping down spruce logs until there are 5 in the inventory. It first checks how many spruce logs are in the inventory and calculates how many more need to be mined. If there are less than 5, it mines the remaining logs and saves the event. If there are already 5 logs in the inventory, it does nothing.
}


================================================
FILE: skill_library/trial2/skill/description/chopDownSpruceLogsV2.txt
================================================
async function chopDownSpruceLogs(bot) {
    // The function is about chopping down spruce logs until there are 5 in the inventory. It first checks how many spruce logs are in the inventory and calculates how many more need to be mined. If there are less than 5, it mines the remaining amount and saves the event. If there are already 5 spruce logs in the inventory, it does nothing.
}


================================================
FILE: skill_library/trial2/skill/description/chopSpruceLogs.txt
================================================
async function chopSpruceLogs(bot) {
    // The function is about chopping down spruce logs until there are 3 in the inventory. It first checks how many spruce logs are in the inventory and calculates how many more need to be mined. If there are less than 3, it mines the remaining logs and saves them in the inventory. If there are already 3 logs in the inventory, it does nothing.
}


================================================
FILE: skill_library/trial2/skill/description/collectWaterWithBucket.txt
================================================
async function collectWaterWithBucket(bot) {
    // The function is about collecting water with a bucket. It first searches for a water block within a certain distance. If no water block is found, it explores the environment until it finds one. Once a water block is found, it equips the bucket in the hand, looks at the water block, and activates the item to collect water. Finally, it sends a chat message indicating that water has been collected.
}


================================================
FILE: skill_library/trial2/skill/description/cookMutton.txt
================================================
async function cookMutton(bot) {
    // The function is about cooking 5 raw muttons using a furnace and coal. It first checks if there are at least 5 raw muttons in the inventory, and if not, it returns a message to collect more. Then it checks if there is a furnace in the inventory, and if not, it returns a message to craft one. It places the furnace next to the player and checks if there is enough coal in the inventory. If not, it mines coal until there are 5 pieces. Finally, it smelts 5 raw muttons using coal and returns a message that 5 muttons have been cooked.
}


================================================
FILE: skill_library/trial2/skill/description/craftBucket.txt
================================================
async function craftBucket(bot) {
    // The function crafts a bucket using 3 iron ingots. If there are not enough iron ingots, it returns. If there is no crafting table nearby, it places one. Then it crafts a bucket and sends a chat message.
}


================================================
FILE: skill_library/trial2/skill/description/craftChest.txt
================================================
async function craftChest(bot) {
    // The function crafts a chest using spruce planks and a crafting table. If there are not enough spruce planks, it mines a spruce log and crafts more planks. If there is no crafting table nearby, it places one. Finally, it crafts a chest and logs the event.
}


================================================
FILE: skill_library/trial2/skill/description/craftEightSticks.txt
================================================
async function craftEightSticks(bot) {
    // The function crafts 8 sticks using spruce planks. If there are not enough spruce planks, it mines a spruce log and crafts more planks. If there is no crafting table nearby, it places one. Finally, it crafts 2 sticks and repeats the process until 8 sticks are crafted.
}


================================================
FILE: skill_library/trial2/skill/description/craftEightTorches.txt
================================================
async function craftEightTorches(bot) {
    // The function is about crafting 8 torches. First, it checks if there is a crafting table nearby. If not, it places one. Then, it crafts 1 torch and saves it to the inventory. Finally, it outputs a message indicating that 8 torches have been crafted.
}


================================================
FILE: skill_library/trial2/skill/description/craftFishingRod.txt
================================================
async function craftFishingRod(bot) {
    // The function crafts a fishing rod using 2 strings and 3 sticks. If there are not enough strings, the bot will find and kill spiders to obtain them. If a crafting table is not already placed, the bot will place one. Finally, the bot will craft a fishing rod and output a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftFurnace.txt
================================================
async function craftFurnace(bot) {
    // The function crafts a furnace using 8 cobblestones and a crafting table. If there are not enough cobblestones, the function will return. If there is no crafting table nearby, the function will place one. Finally, the function crafts a furnace and sends a chat message.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronChestplate.txt
================================================
async function craftIronChestplate(bot) {
    // The function crafts an iron chestplate using iron ingots. If there are not enough iron ingots in the inventory, the bot will mine iron ores and smelt them into iron ingots. Then, the bot will search for a nearby crafting table and place one if it is not found. Finally, the bot will craft an iron chestplate and chat a message indicating that the item has been crafted.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronHelmet.txt
================================================
async function craftIronHelmet(bot) {
    // The function crafts an iron helmet using 5 iron ingots. If there are not enough iron ingots, it returns. If there is no crafting table nearby, it places one and updates the variable. Then, it crafts an iron helmet and sends a chat message.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronLeggingsAndBoots.txt
================================================
async function craftIronLeggingsAndBoots(bot) {
    // The function crafts iron leggings and boots. It checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and smelts them into ingots. If there is no crafting table nearby, it places one. Finally, it crafts one pair of iron leggings and one pair of iron boots.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronPickaxe.txt
================================================
async function craftIronPickaxe(bot) {
    // The function crafts an iron pickaxe using 3 iron ingots and 2 sticks. It checks if there are enough resources in the inventory to craft the pickaxe, and if not, it returns. If there is a crafting table nearby, it crafts the pickaxe. If not, it places a crafting table and then crafts the pickaxe. Finally, it sends a chat message indicating that the iron pickaxe has been crafted.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronPickaxeWithMaterials.txt
================================================
async function craftIronPickaxeWithMaterials(bot) {
    // The function crafts an iron pickaxe using 3 iron ingots and 2 sticks. If there are not enough iron ingots, it mines iron ores and smelts them into ingots. If there are not enough sticks, it crafts them. If there is no crafting table nearby, it places one. Finally, it crafts an iron pickaxe and logs the result.
}


================================================
FILE: skill_library/trial2/skill/description/craftIronSword.txt
================================================
async function craftIronSword(bot) {
    // The function crafts an iron sword using 2 iron ingots and 1 stick. If there are not enough iron ingots, it mines iron ores and smelts them into ingots. If there are not enough sticks, it crafts them. It then looks for a crafting table within 32 blocks, and if it doesn't find one, it places one nearby. Finally, it crafts an iron sword and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftShieldWithFurnace.txt
================================================
async function craftShieldWithFurnace(bot) {
    // The function crafts a shield using a furnace and a crafting table. It checks if there are enough iron ingots and spruce planks in the inventory, and if not, it smelts iron ingots and crafts spruce planks. If a furnace or a crafting table is not nearby, it places one. Finally, it crafts a shield using the crafting table and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftSixteenTorches.txt
================================================
async function craftSixteenTorches(bot) {
    // The function crafts 16 torches using sticks and a crafting table. It checks if there are enough sticks in the inventory, and if not, crafts more. If there is no crafting table nearby, it places one. Finally, it crafts 16 torches and saves the event.
}


================================================
FILE: skill_library/trial2/skill/description/craftSpyglass.txt
================================================
async function craftSpyglass(bot) {
    // The function crafts a spyglass using 2 copper ingots and 1 amethyst shard. It checks if there are enough materials in the inventory, and if not, it returns. If there is a crafting table nearby, it crafts the spyglass. If not, it places a crafting table and then crafts the spyglass. Finally, it sends a chat message indicating that the spyglass has been crafted.
}


================================================
FILE: skill_library/trial2/skill/description/craftSticks.txt
================================================
async function craftSticks(bot) {
    // The function crafts 4 sticks using a crafting table. If there are not enough spruce planks, it mines a spruce log and crafts the planks. Then, it places a crafting table next to the bot and crafts 4 sticks.
}


================================================
FILE: skill_library/trial2/skill/description/craftStoneAxe.txt
================================================
async function craftStoneAxe(bot) {
    // The function crafts a stone axe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone axe and sends a chat message.
}


================================================
FILE: skill_library/trial2/skill/description/craftStoneHoe.txt
================================================
async function craftStoneHoe(bot) {
    // The function crafts a stone hoe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone hoe and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftStonePickaxe.txt
================================================
async function craftStonePickaxe(bot) {
    // The function crafts a stone pickaxe using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone pickaxe and sends a chat message.
}


================================================
FILE: skill_library/trial2/skill/description/craftStoneShovel.txt
================================================
async function craftStoneShovel(bot) {
    // The function crafts a stone shovel using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone shovel and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftStoneSword.txt
================================================
async function craftStoneSword(bot) {
    // The function crafts a stone sword using cobblestones and sticks. It checks if there are enough cobblestones and sticks in the inventory, and if not, it mines cobblestones or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts a stone sword and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftTorches.txt
================================================
async function craftTorches(bot) {
    // The function crafts 8 torches using coal and sticks. It checks if there is enough coal and sticks in the inventory, and if not, it mines coal or crafts sticks. If there is no crafting table nearby, it places one. Finally, it crafts 8 torches and saves the event.
}


================================================
FILE: skill_library/trial2/skill/description/craftTwentySprucePlanks.txt
================================================
async function craftTwentySprucePlanks(bot) {
    // The function crafts 20 spruce planks using spruce logs. If there are not enough spruce logs in the inventory, it will mine the required amount. Once enough logs are available, it will craft 20 spruce planks and save the event.
}


================================================
FILE: skill_library/trial2/skill/description/craftWhiteBedWithExploration.txt
================================================
async function craftWhiteBedWithExploration(bot) {
    // The function crafts a white bed using 3 white wool blocks and 3 spruce planks. If there are not enough wool blocks, the bot explores the area to find and kill sheep to collect the wool. If there are not enough spruce planks, the bot crafts more. If there is no crafting table nearby, the bot places one.
}


================================================
FILE: skill_library/trial2/skill/description/craftWoodenHoe.txt
================================================
async function craftWoodenHoe(bot) {
    // The function crafts a wooden hoe using 2 spruce planks and 2 sticks. It checks if there are enough planks and sticks in the inventory, and crafts more if necessary. If there is no crafting table nearby, it places one. Finally, it crafts a wooden hoe and logs a message.
}


================================================
FILE: skill_library/trial2/skill/description/craftWoodenPickaxe.txt
================================================
async function craftWoodenPickaxe(bot) {
    // The function crafts a wooden pickaxe by checking if there are enough spruce planks and sticks in the inventory, and crafting more if necessary. It then places a crafting table and crafts a wooden pickaxe using the newly crafted items.
}


================================================
FILE: skill_library/trial2/skill/description/craftWoodenPlanks.txt
================================================
async function craftWoodenPlanks(bot) {
    // The function crafts 4 wooden planks using any type of wooden log available in the inventory. If there is no wooden log in the inventory, it will mine one. It then finds the index of the log in the `logNames` array and uses that index to determine the corresponding plank name in the `plankNames` array. Finally, it crafts 4 planks of the corresponding type and saves the event.
}


================================================
FILE: skill_library/trial2/skill/description/eatCookedMutton.txt
================================================
async function eatCookedMutton(bot) {
    // The function is about eating cooked mutton. It first checks if there is any cooked mutton in the inventory. If there is, it equips the cooked mutton in the hand and consumes it. Finally, it sends a chat message indicating that the cooked mutton has been eaten.
}


================================================
FILE: skill_library/trial2/skill/description/eatCookedMuttonV2.txt
================================================
async function eatCookedMutton(bot) {
    // The function is about eating cooked mutton. It first checks if there is any cooked mutton in the inventory. If there is, it equips the cooked mutton in the hand and consumes it. Finally, it sends a chat message indicating that the cooked mutton has been eaten.
}


================================================
FILE: skill_library/trial2/skill/description/eatCookedMuttonV3.txt
================================================
async function eatCookedMutton(bot) {
    // The function is about eating cooked mutton. It first checks if there is any cooked mutton in the inventory. If there is, it equips the cooked mutton in the hand and consumes it. Finally, it sends a chat message indicating that the cooked mutton has been eaten.
}


================================================
FILE: skill_library/trial2/skill/description/equipIronArmor.txt
================================================
async function equipIronArmor(bot) {
    // The function equips the player with iron armor if it is available in the inventory. It checks for the presence of each piece of iron armor (helmet, chestplate, leggings, and boots) and equips them one by one. If a piece of armor is not found in the inventory, it sends a message to the chat indicating that it is not available.
}


================================================
FILE: skill_library/trial2/skill/description/exploreCave.txt
================================================
async function exploreCave(bot) {
    // The function is about exploring a nearby cave. First, check if there are torches in the inventory. If not, craft torches. Equip the torches in the hand and explore the environment until finding a cave entrance. Once a cave entrance is found, explore the cave by placing torches and killing mobs until the time limit is reached.
}


================================================
FILE: skill_library/trial2/skill/description/exploreCaveAndGatherResources.txt
================================================
async function exploreCaveAndGatherResources(bot) {
    // The function is about exploring a nearby cave and gathering resources. First, equip torches and find a cave entrance. Once a cave entrance is found, explore the cave and gather resources such as coal, iron, gold, and diamond ores. While exploring, place torches to light up the cave, kill nearby mobs, and mine ores. The function will continue exploring until the time limit is reached. Finally, the function will output a message indicating that the exploration and resource gathering is finished.
}


================================================
FILE: skill_library/trial2/skill/description/exploreCaveAndGatherResourcesV2.txt
================================================
async function exploreCaveAndGatherResources(bot) {
    // The function is about exploring a nearby cave and gathering resources. First, equip torches and find a cave entrance. Once a cave entrance is found, explore the cave and gather resources such as coal, iron, gold, and diamond ores. While exploring, place torches to light up the cave, kill nearby mobs, and mine ores. The function will continue exploring until the time limit is reached. Finally, the function will output a message indicating that the exploration and resource gathering is finished.
}


================================================
FILE: skill_library/trial2/skill/description/fishInNearbyWaterSafely.txt
================================================
async function fishInNearbyWaterSafely(bot) {
    // The function is about fishing in a nearby water block safely. It first checks if the bot has a fishing rod in its inventory, and crafts one if it doesn't. Then, it finds a nearby water block and moves to a block adjacent to it. After looking at the water block, it equips the fishing rod and checks for hostile mobs nearby, killing them if necessary. Finally, it fishes in the water and retries if the fishing is cancelled.
}


================================================
FILE: skill_library/trial2/skill/description/mineCoalOre.txt
================================================
async function mineCoalOre(bot) {
    // The function is about mining a single coal ore block using a stone pickaxe. First, it checks if a stone pickaxe is in the inventory. If not, it returns. If the stone pickaxe is available, it equips it in the hand. Next, it searches for a nearby coal ore block. If it is not found, it explores the environment until it finds one. Once a coal ore block is found, it mines it and sends a message to the chat.
}


================================================
FILE: skill_library/trial2/skill/description/mineCopperOreWithStonePickaxe.txt
================================================
async function mineCopperOreWithStonePickaxe(bot) {
    // The function is about mining a single copper ore block using a stone pickaxe. If the stone pickaxe is not in the inventory, the bot will mine 3 cobblestone blocks and craft a stone pickaxe. Once the stone pickaxe is available, it will be equipped in the hand. The bot will then explore the environment until finding a copper ore block. Once a copper ore block is found, the bot will mine it and save the event.
}


================================================
FILE: skill_library/trial2/skill/description/mineFiveCoalOres.txt
================================================
async function mineFiveCoalOres(bot) {
    // The function is about mining 5 coal ores using a stone pickaxe. First, check if a stone pickaxe is in the inventory. If not, return. If the stone pickaxe is available, equip the stone pickaxe in the hand. Next, mine a total of 5 coal ores using the stone pickaxe. Finally, send a chat message indicating that 5 coal ores have been mined.
}


================================================
FILE: skill_library/trial2/skill/description/mineFiveCoalOresV2.txt
================================================
async function mineFiveCoalOres(bot) {
    // The function is about mining 5 coal ores using a stone pickaxe. First, check if a stone pickaxe is in the inventory. If not, return. If the stone pickaxe is available, equip the stone pickaxe in the hand. Next, mine a total of 5 coal ores using the stone pickaxe. Finally, send a chat message indicating that 5 coal ores have been mined.
}


================================================
FILE: skill_library/trial2/skill/description/mineFiveCopperOres.txt
================================================
async function mineFiveCopperOres(bot) {
    // The function is about mining 5 copper ores using an iron pickaxe. It first checks if there are already 5 copper ores in the inventory, and if so, it returns. Otherwise, it equips the iron pickaxe in the hand and mines copper ores until there are 5 in the inventory. Finally, it sends a chat message indicating that 5 copper ores have been mined.
}


================================================
FILE: skill_library/trial2/skill/description/mineFiveIronOres.txt
================================================
async function mineFiveIronOres(bot) {
    // The function is about mining 5 iron ores using either a stone or iron pickaxe. If neither pickaxe is found in the inventory, the bot will mine cobblestone and craft a stone pickaxe. Once a pickaxe is available, the bot will equip it and explore the environment until finding an iron ore block. Once an iron ore block is found, the bot will mine a total of 5 iron ores using the equipped pickaxe.
}


================================================
FILE: skill_library/trial2/skill/description/mineLapisOre.txt
================================================
async function mineLapisOre(bot) {
    // The function is about mining a single lapis ore block using the best available pickaxe. If the bot does not have a suitable pickaxe, it will mine cobblestone and craft a stone pickaxe. Once the pickaxe is available, it will equip it and explore the environment until finding a lapis ore block. Once a lapis ore block is found, it will mine it and save the event of mining the lapis ore.
}


================================================
FILE: skill_library/trial2/skill/description/mineThreeIronOres.txt
================================================
async function mineThreeIronOres(bot) {
    // The function is about mining 3 iron ores using a stone pickaxe. If the stone pickaxe is not in the inventory, the bot will mine cobblestone and craft one. Once the stone pickaxe is available, it will be equipped in the hand. The bot will explore the environment until finding an iron ore block. Once an iron ore block is found, the bot will mine a total of 3 iron ores using the stone pickaxe.
}


================================================
FILE: skill_library/trial2/skill/description/mineWoodLog.txt
================================================
async function mineWoodLog(bot) {
    // The function is about mining a single wood log. It first searches for a nearby wood log within a certain distance. If it cannot find one, it explores the environment until it finds a wood log. Once a wood log is found, it mines it and saves the event of mining the wood log.
}


================================================
FILE: skill_library/trial2/skill/description/smeltOneRawIron.txt
================================================
async function smeltOneRawIron(bot) {
    // The function is about smelting one raw iron using a furnace. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. It then places the furnace next to the bot and smelts one raw iron using coal as fuel. Finally, it sends a message indicating that one raw iron has been smelted.
}


================================================
FILE: skill_library/trial2/skill/description/smeltRawCopper.txt
================================================
async function smeltRawCopper(bot) {
    // The function is about smelting 7 raw copper using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. Then it places the furnace next to the bot and checks if there is coal ore nearby. If there is not enough coal in the inventory, it mines more coal ore. Finally, it smelts 7 raw copper using the furnace and coal.
}


================================================
FILE: skill_library/trial2/skill/description/smeltRawIron.txt
================================================
async function smeltRawIron(bot) {
    // The function is about smelting 3 raw iron using a furnace and coal. First, it checks if there is a furnace in the inventory, and if not, it returns a message to craft one. Then, it places the furnace next to the bot. If there is coal in the inventory, it uses it to smelt the raw iron. Otherwise, it mines coal ore to obtain the required amount of coal. Finally, it smelts the raw iron and returns a message indicating that the process is complete.
}


================================================
FILE: skill_library/trial2/skill/description/smeltSixRawIron.txt
================================================
async function smeltSixRawIron(bot) {
    // The function is about smelting 6 raw iron using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. It then places the furnace next to the player and checks if there is enough coal in the inventory. If there isn't, it mines coal until there are 6 pieces. Finally, it smelts 6 raw iron using the furnace and coal, and returns a message indicating that the process is complete.
}


================================================
FILE: skill_library/trial2/skill/description/smeltTwentyFiveIronIngots.txt
================================================
async function smeltTwentyFiveIronIngots(bot) {
    // The function is about smelting 25 raw iron ingots using a furnace and coal. It first checks if a furnace is in the inventory, and if not, it returns a message to craft one. Then it places the furnace next to the bot, and checks if there is enough coal in the inventory. If there isn't, it mines coal until there are 25 pieces. Finally, it smelts 25 raw iron ingots using the furnace and coal, and returns a message indicating that the process is complete.
}


================================================
FILE: skill_library/trial2/skill/vectordb/chroma-collections.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/vectordb/chroma-embeddings.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/vectordb/index/id_to_uuid_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/vectordb/index/index_7b5fd116-0820-46cb-981a-a6d642d4f025.bin
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/vectordb/index/index_metadata_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial2/skill/vectordb/index/uuid_to_id_7b5fd116-0820-46cb-981a-a6d642d4f025.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/skills.json
================================================
{"mineWoodLog": {"code": "async function mineWoodLog(bot) {\n  const logNames = [\"oak_log\", \"birch_log\", \"spruce_log\", \"jungle_log\", \"acacia_log\", \"dark_oak_log\", \"mangrove_log\"];\n\n  // Find a wood log block\n  const logBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    for (const logName of logNames) {\n      const log = bot.findBlock({\n        matching: mcData.blocksByName[logName].id,\n        maxDistance: 32\n      });\n      if (log) return log;\n    }\n    return null;\n  });\n  if (!logBlock) {\n    bot.chat(\"Could not find a wood log.\");\n    return;\n  }\n\n  // Mine the wood log block\n  await mineBlock(bot, logBlock.name, 1);\n  bot.chat(\"Wood log mined.\");\n}", "description": "async function mineWoodLog(bot) {\n    // The function is about mining a single wood log block. It searches for any of the seven types of wood logs within a certain distance. Once a wood log block is found, it is mined using the `mineBlock` function. If no wood log block is found, the function returns and a message is sent to the chat.\n}"}, "mineThreeMoreOakLogs": {"code": "async function mineThreeMoreOakLogs(bot) {\n  for (let i = 0; i < 3; i++) {\n    const oakLogBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const oakLog = bot.findBlock({\n        matching: mcData.blocksByName[\"oak_log\"].id,\n        maxDistance: 32\n      });\n      return oakLog;\n    });\n    if (!oakLogBlock) {\n      bot.chat(\"Could not find an oak log.\");\n      return;\n    }\n    await mineBlock(bot, \"oak_log\", 1);\n  }\n  bot.chat(\"3 more oak logs mined.\");\n}", "description": "async function mineThreeMoreOakLogs(bot) {\n    // The function is about mining three oak logs. It uses a for loop to mine three oak logs. It explores the environment until finding an oak log block, and then mines one oak log block. If it cannot find an oak log block, it returns. Once three oak logs are mined, it sends a chat message.\n}"}, "craftWoodenPickaxe": {"code": "async function craftWoodenPickaxe(bot) {\n  // Check if there are enough oak logs in the inventory\n  const oakLogs = bot.inventory.count(mcData.itemsByName[\"oak_log\"].id);\n  if (oakLogs < 4) {\n    // Mine more oak logs\n    await mineBlock(bot, \"oak_log\", 4 - oakLogs);\n  }\n\n  // Craft a crafting table using oak logs\n  await craftItem(bot, \"crafting_table\", 1);\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft oak planks using oak logs\n  await craftItem(bot, \"oak_planks\", 4, craftingTablePosition);\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks, craftingTablePosition);\n  }\n\n  // Craft a wooden pickaxe using oak planks and sticks with the crafting table\n  await craftItem(bot, \"wooden_pickaxe\", 1, craftingTablePosition);\n  bot.chat(\"Wooden pickaxe crafted.\");\n}", "description": "async function craftWoodenPickaxe(bot) {\n    // The function crafts a wooden pickaxe using oak logs, oak planks, and sticks. It first checks if there are enough oak logs in the inventory, and if not, mines more. Then, it crafts a crafting table using oak logs and places it near the player. Next, it crafts oak planks using oak logs and checks if there are enough sticks in the inventory. If not, it crafts sticks using oak planks. Finally, it crafts a wooden pickaxe using oak planks and sticks with the crafting table.\n}"}, "craftWoodenSword": {"code": "async function craftWoodenSword(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanks = bot.inventory.count(mcData.itemsByName[\"oak_planks\"].id);\n  if (oakPlanks < 2) {\n    // Craft more oak planks using oak logs\n    await craftItem(bot, \"oak_planks\", 2 - oakPlanks);\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 1) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 1 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a wooden sword using oak planks and sticks with the crafting table\n  await craftItem(bot, \"wooden_sword\", 1, craftingTablePosition);\n  bot.chat(\"Wooden sword crafted.\");\n}", "description": "async function craftWoodenSword(bot) {\n    // The function crafts a wooden sword using oak planks and sticks. It checks if there are enough oak planks and sticks in the inventory, and crafts more if necessary. It then places a crafting table near the player and uses it to craft a wooden sword. Finally, it sends a chat message indicating that the wooden sword has been crafted.\n}"}, "mineEightCobblestone": {"code": "async function mineEightCobblestone(bot) {\n  // Equip the wooden pickaxe\n  const woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"wooden_pickaxe\"].id);\n  await bot.equip(woodenPickaxe, \"hand\");\n\n  // Find stone blocks\n  const stoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const stone = bot.findBlock({\n      matching: mcData.blocksByName[\"stone\"].id,\n      maxDistance: 32\n    });\n    return stone;\n  });\n\n  // Mine 8 cobblestone\n  await mineBlock(bot, \"stone\", 8);\n  bot.chat(\"8 cobblestone mined.\");\n}", "description": "async function mineEightCobblestone(bot) {\n    // The function is about mining 8 cobblestones using a wooden pickaxe. It equips the wooden pickaxe and explores the environment until finding a stone block. Once a stone block is found, it mines a total of 8 cobblestone blocks using the wooden pickaxe. Finally, it sends a chat message indicating that 8 cobblestones have been mined.\n}"}, "craftStonePickaxe": {"code": "async function craftStonePickaxe(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 3) {\n    bot.chat(\"Not enough cobblestones to craft a stone pickaxe.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone pickaxe using cobblestones and sticks with the crafting table\n  await craftItem(bot, \"stone_pickaxe\", 1, craftingTablePosition);\n  bot.chat(\"Stone pickaxe crafted.\");\n}", "description": "async function craftStonePickaxe(bot) {\n    // The function crafts a stone pickaxe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a stone pickaxe.\n}"}, "mineFourCoalOre": {"code": "async function mineFourCoalOre(bot) {\n  // Equip the stone pickaxe\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_pickaxe\"].id);\n  await bot.equip(stonePickaxe, \"hand\");\n\n  // Find and mine 4 coal ore blocks\n  await mineBlock(bot, \"coal_ore\", 4);\n  bot.chat(\"4 coal ore mined.\");\n}", "description": "async function mineFourCoalOre(bot) {\n    // The function is about mining 4 coal ore blocks using a stone pickaxe. The function equips the stone pickaxe in the hand and then mines 4 coal ore blocks. Once the mining is complete, the function sends a chat message indicating that 4 coal ore blocks have been mined.\n}"}, "craftFurnace": {"code": "async function craftFurnace(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 8) {\n    bot.chat(\"Not enough cobblestones to craft a furnace.\");\n    return;\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a furnace using cobblestones and the crafting table\n  await craftItem(bot, \"furnace\", 1, craftingTablePosition);\n  bot.chat(\"Furnace crafted.\");\n}", "description": "async function craftFurnace(bot) {\n    // The function crafts a furnace using cobblestones and a crafting table. It first checks if there are enough cobblestones in the inventory. If there are, it places a crafting table near the player and crafts a furnace using the cobblestones and the crafting table. Finally, it sends a chat message indicating that the furnace has been crafted.\n}"}, "mineThreeIronOre": {"code": "async function mineThreeIronOre(bot) {\n  // Equip the stone pickaxe\n  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_pickaxe\"].id);\n  await bot.equip(stonePickaxe, \"hand\");\n\n  // Find and mine 3 iron ore blocks\n  await mineBlock(bot, \"iron_ore\", 3);\n  bot.chat(\"3 iron ore mined.\");\n}", "description": "async function mineThreeIronOre(bot) {\n    // The function is about mining 3 iron ore blocks using a stone pickaxe. The function equips the stone pickaxe in the hand and then mines 3 iron ore blocks. Once the mining is complete, the function sends a chat message indicating that 3 iron ore blocks have been mined.\n}"}, "smeltRawIron": {"code": "async function smeltRawIron(bot) {\n  // Find a suitable location to place the furnace\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n\n  // Place the furnace\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 3 raw iron using coal as fuel\n  await smeltItem(bot, \"raw_iron\", \"coal\", 3);\n  bot.chat(\"3 raw iron smelted.\");\n}", "description": "async function smeltRawIron(bot) {\n    // The function is about smelting 3 raw iron using coal as fuel. First, find a suitable location to place the furnace. Then, place the furnace at the found location. Finally, smelt 3 raw iron using coal as fuel and save the event of smelting 3 raw iron.\n}"}, "craftIronPickaxe": {"code": "async function craftIronPickaxe(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 3) {\n    bot.chat(\"Not enough iron ingots to craft an iron pickaxe.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron pickaxe using iron ingots and sticks with the crafting table\n  await craftItem(bot, \"iron_pickaxe\", 1, craftingTablePosition);\n  bot.chat(\"Iron pickaxe crafted.\");\n}", "description": "async function craftIronPickaxe(bot) {\n    // The function crafts an iron pickaxe using iron ingots and sticks. It first checks if there are enough iron ingots and sticks in the inventory, and crafts more sticks if necessary. Then it places a crafting table near the player and uses it to craft an iron pickaxe. Finally, it sends a chat message indicating that the iron pickaxe has been crafted.\n}"}, "smeltCopperOre": {"code": "async function smeltCopperOre(bot) {\n  // Check if there is a furnace in the inventory\n  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName[\"furnace\"].id);\n\n  // If there is no furnace, craft one using cobblestone\n  if (!furnace) {\n    await craftItem(bot, \"furnace\", 1);\n  }\n\n  // Place the furnace near the player\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Find a copper ore block\n  const copperOre = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const copperOre = bot.findBlock({\n      matching: mcData.blocksByName[\"copper_ore\"].id,\n      maxDistance: 32\n    });\n    return copperOre;\n  });\n\n  // Mine the copper ore block\n  await mineBlock(bot, \"copper_ore\", 1);\n\n  // Smelt the raw copper using coal as fuel in the furnace\n  await smeltItem(bot, \"raw_copper\", \"coal\", 1);\n\n  // Collect the smelted copper ingot\n  bot.chat(\"1 copper ore smelted.\");\n}", "description": "async function smeltCopperOre(bot) {\n    // The function is about smelting one copper ore block into a copper ingot using a furnace and coal as fuel. First, check if there is a furnace in the inventory. If not, craft one using cobblestone. Then, place the furnace near the player. Next, explore the environment until finding a copper ore block. Once a copper ore block is found, mine it and smelt the raw copper using coal as fuel in the furnace. Finally, collect the smelted copper ingot.\n}"}, "smeltThreeRawCopper": {"code": "async function smeltThreeRawCopper(bot) {\n  // Find a suitable location to place the furnace\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n\n  // Place the furnace\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 3 raw copper using coal as fuel\n  await smeltItem(bot, \"raw_copper\", \"coal\", 3);\n  bot.chat(\"3 raw copper smelted.\");\n}", "description": "async function smeltThreeRawCopper(bot) {\n    // The function is about smelting 3 raw copper using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 3 raw copper using coal as fuel and saves the event of smelting 3 raw copper.\n}"}, "craftStoneSword": {"code": "async function craftStoneSword(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 2) {\n    bot.chat(\"Not enough cobblestones to craft a stone sword.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 1) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 1 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone sword using cobblestones and sticks with the crafting table\n  await craftItem(bot, \"stone_sword\", 1, craftingTablePosition);\n  bot.chat(\"Stone sword crafted.\");\n}", "description": "async function craftStoneSword(bot) {\n    // The function crafts a stone sword using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough cobblestones, it returns. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone sword using the crafting table. Finally, it sends a chat message indicating that the stone sword has been crafted.\n}"}, "mineFiveCopperOre": {"code": "async function mineFiveCopperOre(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_pickaxe\"].id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find 5 copper ore blocks\n  const copperOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const copperOres = bot.findBlocks({\n      matching: mcData.blocksByName[\"copper_ore\"].id,\n      maxDistance: 32,\n      count: 5\n    });\n    return copperOres.length >= 5 ? copperOres : null;\n  });\n\n  // Mine the 5 copper ore blocks\n  await mineBlock(bot, \"copper_ore\", 5);\n  bot.chat(\"5 copper ore mined.\");\n}", "description": "async function mineFiveCopperOre(bot) {\n    // The function is about mining 5 copper ore blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 copper ore blocks. Once 5 copper ore blocks are found, mine them using the iron pickaxe and save the event of mining 5 copper ore.\n}"}, "smeltFiveRawCopper": {"code": "async function smeltFiveRawCopper(bot) {\n  // Find a suitable location to place the furnace\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n\n  // Place the furnace\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 5 raw copper using coal as fuel\n  await smeltItem(bot, \"raw_copper\", \"coal\", 5);\n  bot.chat(\"5 raw copper smelted.\");\n}", "description": "async function smeltFiveRawCopper(bot) {\n    // The function is about smelting 5 raw copper using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 5 raw copper using coal as fuel and sends a chat message indicating that 5 raw copper has been smelted.\n}"}, "craftStoneShovel": {"code": "async function craftStoneShovel(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 1) {\n    bot.chat(\"Not enough cobblestones to craft a stone shovel.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone shovel using cobblestones and sticks with the crafting table\n  await craftItem(bot, \"stone_shovel\", 1, craftingTablePosition);\n  bot.chat(\"Stone shovel crafted.\");\n}", "description": "async function craftStoneShovel(bot) {\n    // The function crafts a stone shovel using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a stone shovel. Finally, it sends a chat message indicating that the stone shovel has been crafted.\n}"}, "craftCopperBlock": {"code": "async function craftCopperBlock(bot) {\n  // Check if there are enough copper ingots in the inventory\n  const copperIngots = bot.inventory.count(mcData.itemsByName[\"copper_ingot\"].id);\n  if (copperIngots < 9) {\n    bot.chat(\"Not enough copper ingots to craft a copper block.\");\n    return;\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a copper block using copper ingots and the crafting table\n  await craftItem(bot, \"copper_block\", 1, craftingTablePosition);\n  bot.chat(\"Copper block crafted.\");\n}", "description": "async function craftCopperBlock(bot) {\n    // The function crafts a copper block using 9 copper ingots and a crafting table. It first checks if there are enough copper ingots in the inventory, and if not, it returns. Then, it places a crafting table near the player and crafts a copper block using the crafting table. Finally, it sends a chat message indicating that the copper block has been crafted.\n}"}, "killChickenWithIncreasedTime": {"code": "async function killChickenWithIncreasedTime(bot) {\n  // Explore the area to find a chicken with an increased exploration time limit\n  const chicken = await exploreUntil(bot, new Vec3(1, 0, 1), 120, () => {\n    const chicken = bot.nearestEntity(entity => {\n      return entity.name === \"chicken\" && entity.position.distanceTo(bot.entity.position) < 32;\n    });\n    return chicken;\n  });\n  if (!chicken) {\n    bot.chat(\"No chicken found.\");\n    return;\n  }\n\n  // Equip a weapon (preferably a sword) to kill the chicken\n  const sword = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_sword\"].id) || bot.inventory.findInventoryItem(mcData.itemsByName[\"wooden_sword\"].id);\n  if (sword) {\n    await bot.equip(sword, \"hand\");\n  } else {\n    bot.chat(\"No sword found, using bare hands.\");\n  }\n\n  // Kill the chicken\n  await killMob(bot, \"chicken\", 300);\n\n  // Report the completion of the task\n  bot.chat(\"1 chicken killed.\");\n}", "description": "async function killChickenWithIncreasedTime(bot) {\n    // The function is about killing a chicken with an increased exploration time limit. It explores the area to find a chicken within a certain distance. If a chicken is found, it equips a sword (if available) to kill the chicken. Otherwise, it uses bare hands. After killing the chicken, it reports the completion of the task.\n}"}, "cookChicken": {"code": "async function cookChicken(bot) {\n  // Check if there is a furnace in the inventory\n  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName[\"furnace\"].id);\n\n  // If there is no furnace, craft one using cobblestone\n  if (!furnace) {\n    await craftItem(bot, \"furnace\", 1);\n  }\n\n  // Place the furnace near the player\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt the raw chicken using coal as fuel in the furnace\n  await smeltItem(bot, \"chicken\", \"coal\", 1);\n\n  // Collect the cooked chicken\n  bot.chat(\"1 chicken cooked.\");\n}", "description": "async function cookChicken(bot) {\n    // The function is about cooking a raw chicken using a furnace and coal as fuel. First, it checks if there is a furnace in the inventory. If not, it crafts one using cobblestone. Then, it places the furnace near the player. Next, it smelts the raw chicken using coal as fuel in the furnace. Finally, it collects the cooked chicken and sends a chat message.\n}"}, "killThreeCows": {"code": "async function killThreeCows(bot) {\n  // Explore the area to find 3 cows\n  let cows = [];\n  while (cows.length < 3) {\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const nearbyCow = bot.nearestEntity(entity => {\n        return entity.name === \"cow\" && entity.position.distanceTo(bot.entity.position) < 32;\n      });\n      if (nearbyCow && !cows.includes(nearbyCow)) {\n        cows.push(nearbyCow);\n        return cows.length === 3 ? cows : null;\n      }\n      return null;\n    });\n  }\n\n  // Equip a weapon (preferably a sword) to kill the cows\n  const sword = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_sword\"].id) || bot.inventory.findInventoryItem(mcData.itemsByName[\"wooden_sword\"].id);\n  if (sword) {\n    await bot.equip(sword, \"hand\");\n  } else {\n    bot.chat(\"No sword found, using bare hands.\");\n  }\n\n  // Kill each cow one by one\n  for (const cow of cows) {\n    await killMob(bot, cow.name, 300);\n  }\n\n  // Report the completion of the task\n  bot.chat(\"3 cows killed.\");\n}", "description": "async function killThreeCows(bot) {\n    // The function is about killing 3 cows. It explores the environment to find 3 cows within a certain distance. Once 3 cows are found, it equips a sword (if available) to kill the cows one by one. If no sword is found, it uses bare hands. After killing all 3 cows, it reports the completion of the task.\n}"}, "cookRawBeef": {"code": "async function cookRawBeef(bot) {\n  // Check if there is a furnace in the inventory\n  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName[\"furnace\"].id);\n\n  // If there is no furnace, craft one using cobblestone\n  if (!furnace) {\n    await craftItem(bot, \"furnace\", 1);\n  }\n\n  // Place the furnace near the player\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt the 6 raw beef using coal as fuel in the furnace\n  await smeltItem(bot, \"beef\", \"coal\", 6);\n\n  // Collect the cooked beef\n  bot.chat(\"6 raw beef cooked.\");\n}", "description": "async function cookRawBeef(bot) {\n    // The function is about cooking 6 raw beef using a furnace and coal as fuel. It first checks if there is a furnace in the inventory, and if not, crafts one using cobblestone. Then, it places the furnace near the player and smelts the 6 raw beef using coal as fuel in the furnace. Finally, it collects the cooked beef and sends a chat message.\n}"}, "eatCookedBeef": {"code": "async function eatCookedBeef(bot) {\n  // Equip a cooked beef in the bot's hand\n  const cookedBeef = bot.inventory.findInventoryItem(mcData.itemsByName[\"cooked_beef\"].id);\n  await bot.equip(cookedBeef, \"hand\");\n\n  // Consume the cooked beef\n  await bot.consume();\n  bot.chat(\"1 cooked beef eaten.\");\n}", "description": "async function eatCookedBeef(bot) {\n    // The function is about making the bot eat a cooked beef. It equips a cooked beef in the bot's hand and then consumes it. Finally, it sends a message to the chat indicating that one cooked beef has been eaten.\n}"}, "killThreeChickens": {"code": "async function killThreeChickens(bot) {\n  // Equip a weapon (preferably a sword) to kill the chickens\n  const sword = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_sword\"].id) || bot.inventory.findInventoryItem(mcData.itemsByName[\"wooden_sword\"].id);\n  if (sword) {\n    await bot.equip(sword, \"hand\");\n  } else {\n    bot.chat(\"No sword found, using bare hands.\");\n  }\n\n  // Explore the area to find 3 chickens\n  let chickens = [];\n  while (chickens.length < 3) {\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const nearbyChicken = bot.nearestEntity(entity => {\n        return entity.name === \"chicken\" && entity.position.distanceTo(bot.entity.position) < 32;\n      });\n      if (nearbyChicken && !chickens.includes(nearbyChicken)) {\n        chickens.push(nearbyChicken);\n        return chickens.length === 3 ? chickens : null;\n      }\n      return null;\n    });\n  }\n\n  // Kill each chicken one by one\n  for (const chicken of chickens) {\n    await killMob(bot, chicken.name, 300);\n  }\n\n  // Report the completion of the task\n  bot.chat(\"3 chickens killed.\");\n}", "description": "async function killThreeChickens(bot) {\n    // The function is about killing 3 chickens. First, it equips a sword to kill the chickens, and if there is no sword, it uses bare hands. Then, it explores the environment to find 3 chickens within a 32 block radius. Once 3 chickens are found, it kills each chicken one by one using the equipped weapon. Finally, it reports the completion of the task by sending a chat message.\n}"}, "killThreeSheep": {"code": "async function killThreeSheep(bot) {\n  // Equip a weapon (preferably a sword) to kill the sheep\n  const sword = bot.inventory.findInventoryItem(mcData.itemsByName[\"stone_sword\"].id) || bot.inventory.findInventoryItem(mcData.itemsByName[\"wooden_sword\"].id);\n  if (sword) {\n    await bot.equip(sword, \"hand\");\n  } else {\n    bot.chat(\"No sword found, using bare hands.\");\n  }\n\n  // Explore the area to find 3 sheep\n  let sheep = [];\n  while (sheep.length < 3) {\n    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n      const nearbySheep = bot.nearestEntity(entity => {\n        return entity.name === \"sheep\" && entity.position.distanceTo(bot.entity.position) < 32;\n      });\n      if (nearbySheep && !sheep.includes(nearbySheep)) {\n        sheep.push(nearbySheep);\n        return sheep.length === 3 ? sheep : null;\n      }\n      return null;\n    });\n  }\n\n  // Kill each sheep one by one\n  for (const singleSheep of sheep) {\n    await killMob(bot, singleSheep.name, 300);\n  }\n\n  // Report the completion of the task\n  bot.chat(\"3 sheep killed.\");\n}", "description": "async function killThreeSheep(bot) {\n    // The function is about killing 3 sheep. First, it equips a weapon (preferably a sword) to kill the sheep. Then, it explores the environment to find 3 sheep. Once 3 sheep are found, it kills each sheep one by one. Finally, it reports the completion of the task by sending a chat message.\n}"}, "craftStoneAxe": {"code": "async function craftStoneAxe(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 3) {\n    bot.chat(\"Not enough cobblestones to craft a stone axe.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone axe using cobblestones and sticks with the crafting table\n  await craftItem(bot, \"stone_axe\", 1, craftingTablePosition);\n  bot.chat(\"Stone axe crafted.\");\n}", "description": "async function craftStoneAxe(bot) {\n    // The function crafts a stone axe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone axe using the cobblestones and sticks with the crafting table. Finally, it sends a chat message indicating that the stone axe has been crafted.\n}"}, "cookThreeRawChicken": {"code": "async function cookThreeRawChicken(bot) {\n  // Find a suitable location to place the furnace\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n\n  // Place the furnace\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt 3 raw chicken using coal as fuel\n  await smeltItem(bot, \"chicken\", \"coal\", 3);\n  bot.chat(\"3 raw chicken cooked.\");\n}", "description": "async function cookThreeRawChicken(bot) {\n    // The function is about cooking 3 raw chicken using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 3 raw chicken using coal as fuel and sends a chat message indicating that the chicken has been cooked.\n}"}, "craftStoneTools": {"code": "async function craftStoneTools(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 6) {\n    // Mine more cobblestones\n    await mineBlock(bot, \"stone\", 6 - cobblestones);\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 5) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 5 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone sword, a stone axe, and a stone shovel using the crafting table\n  await craftItem(bot, \"stone_sword\", 1, craftingTablePosition);\n  await craftItem(bot, \"stone_axe\", 1, craftingTablePosition);\n  await craftItem(bot, \"stone_shovel\", 1, craftingTablePosition);\n  bot.chat(\"Stone sword, stone axe, and stone shovel crafted.\");\n}", "description": "async function craftStoneTools(bot) {\n    // The function crafts stone tools (sword, axe, and shovel) using a crafting table. It checks if there are enough cobblestones and sticks in the inventory, and mines more cobblestones or crafts more sticks if necessary. Then, it places a crafting table near the player and crafts the stone tools using the crafting table. Finally, it sends a chat message indicating that the tools have been crafted.\n}"}, "cookRawMutton": {"code": "async function cookRawMutton(bot) {\n  // Check if there is a furnace in the inventory\n  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName[\"furnace\"].id);\n\n  // If there is no furnace, craft one using cobblestone\n  if (!furnace) {\n    await craftItem(bot, \"furnace\", 1);\n  }\n\n  // Place the furnace near the player\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt the 4 raw mutton using coal as fuel in the furnace\n  await smeltItem(bot, \"mutton\", \"coal\", 4);\n\n  // Collect the cooked mutton\n  bot.chat(\"4 raw mutton cooked.\");\n}", "description": "async function cookRawMutton(bot) {\n    // The function is about cooking 4 raw mutton using a furnace and coal as fuel. If there is no furnace in the inventory, the bot will craft one using cobblestone. Then, the bot will place the furnace near the player and smelt the 4 raw mutton using coal as fuel. Finally, the bot will collect the cooked mutton and print a message in the chat.\n}"}, "plantOakSapling": {"code": "async function plantOakSapling(bot) {\n  // Find a suitable location to plant the oak sapling\n  const targetBlock = bot.findBlock({\n    matching: block => {\n      return block.name === \"grass_block\" || block.name === \"dirt\";\n    },\n    maxDistance: 32\n  });\n  if (!targetBlock) {\n    bot.chat(\"Could not find a suitable location to plant the oak sapling.\");\n    return;\n  }\n\n  // Go to the location\n  await bot.pathfinder.goto(new GoalBlock(targetBlock.position.x, targetBlock.position.y, targetBlock.position.z));\n\n  // Equip the oak sapling in the bot's hand\n  const oakSapling = bot.inventory.findInventoryItem(mcData.itemsByName[\"oak_sapling\"].id);\n  await bot.equip(oakSapling, \"hand\");\n\n  // Right-click on the ground to plant the oak sapling\n  await bot.activateBlock(targetBlock);\n\n  // Send a chat message to indicate the oak sapling has been planted\n  bot.chat(\"Oak sapling planted.\");\n}", "description": "async function plantOakSapling(bot) {\n    // The function is about finding a suitable location to plant an oak sapling, going to that location, equipping the oak sapling in the bot's hand, right-clicking on the ground to plant the oak sapling, and sending a chat message to indicate the oak sapling has been planted. If a suitable location cannot be found, the function will return without planting the oak sapling.\n}"}, "craftStoneHoe": {"code": "async function craftStoneHoe(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 2) {\n    bot.chat(\"Not enough cobblestones to craft a stone hoe.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 2) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 2 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a stone hoe using cobblestones and sticks with the crafting table\n  await craftItem(bot, \"stone_hoe\", 1, craftingTablePosition);\n  bot.chat(\"Stone hoe crafted.\");\n}", "description": "async function craftStoneHoe(bot) {\n    // The function crafts a stone hoe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone hoe using the cobblestones and sticks with the crafting table. Finally, it sends a chat message indicating that the stone hoe has been crafted.\n}"}, "craftTenCobblestoneWalls": {"code": "async function craftTenCobblestoneWalls(bot) {\n  // Check if there are enough cobblestones in the inventory\n  const cobblestones = bot.inventory.count(mcData.itemsByName[\"cobblestone\"].id);\n  if (cobblestones < 32) {\n    bot.chat(\"Not enough cobblestones to craft 10 cobblestone walls.\");\n    return;\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft 6 cobblestone walls using the crafting table\n  await craftItem(bot, \"cobblestone_wall\", 1, craftingTablePosition);\n\n  // Craft 6 more cobblestone walls using the crafting table\n  await craftItem(bot, \"cobblestone_wall\", 1, craftingTablePosition);\n  bot.chat(\"10 cobblestone walls crafted.\");\n}", "description": "async function craftTenCobblestoneWalls(bot) {\n    // The function crafts 10 cobblestone walls using a crafting table. It first checks if there are enough cobblestones in the inventory, and if not, it returns. Then, it places a crafting table near the player and crafts 6 cobblestone walls using the crafting table. It repeats the process to craft 6 more cobblestone walls and outputs a message when the process is complete.\n}"}, "openChestAndCheckContents": {"code": "async function openChestAndCheckContents(bot) {\n  const targetChestPosition = new Vec3(5, 61, 134);\n\n  // Find the chest at the specified position\n  const chestPosition = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const chest = bot.findBlock({\n      matching: mcData.blocksByName[\"chest\"].id,\n      maxDistance: 32,\n      position: targetChestPosition\n    });\n    return chest ? chest.position : null;\n  });\n\n  // Check the contents of the chest\n  await checkItemInsideChest(bot, chestPosition);\n  bot.chat(\"Chest at (5, 61, 134) opened and contents checked.\");\n}", "description": "async function openChestAndCheckContents(bot) {\n    // The function is about finding a chest at a specified position, opening it, and checking its contents. It uses the `exploreUntil` helper function to find the chest and the `checkItemInsideChest` helper function to check the contents of the chest. The position of the chest is specified by `targetChestPosition`. Once the chest is found, the function checks its contents and sends a chat message indicating that the chest has been opened and its contents have been checked.\n}"}, "mineTenCobbledDeepslateBelowY0": {"code": "async function mineTenCobbledDeepslateBelowY0(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_pickaxe\"].id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find cobbled_deepslate blocks below Y=0\n  const cobbledDeepslateBlocks = await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {\n    const cobbledDeepslate = bot.findBlock({\n      matching: mcData.blocksByName[\"cobbled_deepslate\"].id,\n      maxDistance: 32,\n      position: pos => pos.y < 0\n    });\n    return cobbledDeepslate;\n  });\n\n  // Mine 10 cobbled_deepslate blocks\n  await mineBlock(bot, \"cobbled_deepslate\", 10);\n  bot.chat(\"10 cobbled_deepslate mined below Y=0.\");\n}", "description": "async function mineTenCobbledDeepslateBelowY0(bot) {\n    // The function is about mining 10 cobbled_deepslate blocks below Y=0 using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding a cobbled_deepslate block below Y=0. Once 10 cobbled_deepslate blocks are found, mine them using the iron pickaxe. Finally, a message is sent to the chat indicating that 10 cobbled_deepslate blocks have been mined below Y=0.\n}"}, "mineDeepslateOres": {"code": "async function mineDeepslateOres(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_pickaxe\"].id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find and mine 1 deepslate_redstone_ore\n  await mineBlock(bot, \"deepslate_redstone_ore\", 1);\n  bot.chat(\"1 deepslate_redstone_ore mined.\");\n\n  // Find and mine 1 deepslate_gold_ore\n  await mineBlock(bot, \"deepslate_gold_ore\", 1);\n  bot.chat(\"1 deepslate_gold_ore mined.\");\n}", "description": "async function mineDeepslateOres(bot) {\n    // The function is about mining 1 deepslate_redstone_ore and 1 deepslate_gold_ore using an iron pickaxe. The function first equips the iron pickaxe in the hand. Then, it finds and mines 1 deepslate_redstone_ore and 1 deepslate_gold_ore using the mineBlock function. Finally, it sends a chat message indicating the number of ores mined.\n}"}, "craftChest": {"code": "async function craftChest(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanks = bot.inventory.count(mcData.itemsByName[\"oak_planks\"].id);\n  if (oakPlanks < 8) {\n    // Mine more oak logs\n    await mineBlock(bot, \"oak_log\", 8 - oakPlanks);\n    // Craft oak planks using oak logs\n    await craftItem(bot, \"oak_planks\", 8 - oakPlanks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a chest using oak planks with the crafting table\n  await craftItem(bot, \"chest\", 1, craftingTablePosition);\n  bot.chat(\"Chest crafted.\");\n}", "description": "async function craftChest(bot) {\n    // The function crafts a chest using oak planks. It checks if there are enough oak planks in the inventory, and if not, it mines oak logs and crafts oak planks. It then places a crafting table near the player and crafts a chest using oak planks with the crafting table. Finally, it sends a chat message indicating that the chest has been crafted.\n}"}, "smeltFiveRawGold": {"code": "async function smeltFiveRawGold(bot) {\n  // Check if there is a furnace in the inventory\n  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName[\"furnace\"].id);\n\n  // If there is no furnace, craft one using cobblestone\n  if (!furnace) {\n    await craftItem(bot, \"furnace\", 1);\n  }\n\n  // Place the furnace near the player\n  const furnacePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"furnace\", furnacePosition);\n\n  // Smelt the 5 raw gold using coal as fuel in the furnace\n  await smeltItem(bot, \"raw_gold\", \"coal\", 5);\n\n  // Collect the smelted gold ingots\n  bot.chat(\"5 raw gold smelted.\");\n}", "description": "async function smeltFiveRawGold(bot) {\n    // The function is about smelting 5 raw gold into gold ingots using a furnace and coal as fuel. If there is no furnace in the inventory, the bot will craft one using cobblestone. Then, the bot will place the furnace near the player and smelt the 5 raw gold using coal as fuel. Finally, the bot will collect the smelted gold ingots and print a message in the chat.\n}"}, "craftClock": {"code": "async function craftClock(bot) {\n  // Check if there is a crafting table in the inventory\n  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName[\"crafting_table\"].id);\n\n  // If there is no crafting table, craft one using oak planks\n  if (!craftingTable) {\n    await craftItem(bot, \"crafting_table\", 1);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a clock using 4 gold ingots and 1 redstone dust with the crafting table\n  await craftItem(bot, \"clock\", 1, craftingTablePosition);\n  bot.chat(\"Clock crafted.\");\n}", "description": "async function craftClock(bot) {\n    // The function crafts a clock using 4 gold ingots and 1 redstone dust. It first checks if there is a crafting table in the inventory, and if not, crafts one using oak planks. Then, it places the crafting table near the player. Finally, it crafts a clock using the crafting table and saves the event of crafting a clock.\n}"}, "craftIronSword": {"code": "async function craftIronSword(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 2) {\n    bot.chat(\"Not enough iron ingots to craft an iron sword.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 1) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 1 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron sword using iron ingots and sticks with the crafting table\n  await craftItem(bot, \"iron_sword\", 1, craftingTablePosition);\n  bot.chat(\"Iron sword crafted.\");\n}", "description": "async function craftIronSword(bot) {\n    // The function crafts an iron sword using iron ingots and sticks. It first checks if there are enough iron ingots and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts an iron sword using the crafting table. Finally, it sends a chat message indicating that the iron sword has been crafted.\n}"}, "obtainBirchLogs": {"code": "async function obtainBirchLogs(bot) {\n  // Check if there are enough birch logs in the inventory\n  const birchLogs = bot.inventory.count(mcData.itemsByName[\"birch_log\"].id);\n  const logsNeeded = 5 - birchLogs;\n  if (logsNeeded > 0) {\n    // Mine the required number of birch logs\n    await mineBlock(bot, \"birch_log\", logsNeeded);\n    bot.chat(\"5 birch logs obtained.\");\n  } else {\n    bot.chat(\"Already have 5 birch logs in the inventory.\");\n  }\n}", "description": "async function obtainBirchLogs(bot) {\n    // The function is about obtaining 5 birch logs. It checks if there are enough birch logs in the inventory and mines the required number of birch logs if necessary. Once 5 birch logs are obtained, it sends a chat message. If there are already 5 birch logs in the inventory, it sends a different chat message.\n}"}, "mineFiveCoalOre": {"code": "async function mineFiveCoalOre(bot) {\n  // Equip the iron pickaxe\n  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_pickaxe\"].id);\n  await bot.equip(ironPickaxe, \"hand\");\n\n  // Find 5 coal ore blocks\n  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {\n    const coalOres = bot.findBlocks({\n      matching: mcData.blocksByName[\"coal_ore\"].id,\n      maxDistance: 32,\n      count: 5\n    });\n    return coalOres.length >= 5 ? coalOres : null;\n  });\n\n  // Mine the 5 coal ore blocks\n  await mineBlock(bot, \"coal_ore\", 5);\n  bot.chat(\"5 coal ore mined.\");\n}", "description": "async function mineFiveCoalOre(bot) {\n    // The function is about mining 5 coal ore blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 coal ore blocks. Once 5 coal ore blocks are found, mine them using the iron pickaxe and save the event of mining 5 coal ore blocks.\n}"}, "craftShield": {"code": "async function craftShield(bot) {\n  // Check if there are enough oak planks in the inventory\n  const oakPlanks = bot.inventory.count(mcData.itemsByName[\"oak_planks\"].id);\n  if (oakPlanks < 6) {\n    // Craft more oak planks using oak logs\n    await craftItem(bot, \"oak_planks\", 6 - oakPlanks);\n  }\n\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 1) {\n    bot.chat(\"Not enough iron ingots to craft a shield.\");\n    return;\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a shield using oak planks and iron ingots with the crafting table\n  await craftItem(bot, \"shield\", 1, craftingTablePosition);\n  bot.chat(\"Shield crafted.\");\n}", "description": "async function craftShield(bot) {\n    // The function crafts a shield using oak planks and iron ingots. It checks if there are enough oak planks and iron ingots in the inventory, and crafts more oak planks if necessary. If there are not enough iron ingots, it returns. It then places a crafting table near the player and crafts a shield using the crafting table. Finally, it sends a chat message indicating that the shield has been crafted.\n}"}, "craftDiamondSword": {"code": "async function craftDiamondSword(bot) {\n  // Check if there are enough diamonds in the inventory\n  const diamonds = bot.inventory.count(mcData.itemsByName[\"diamond\"].id);\n  if (diamonds < 2) {\n    bot.chat(\"Not enough diamonds to craft a diamond sword.\");\n    return;\n  }\n\n  // Check if there are enough sticks in the inventory\n  const sticks = bot.inventory.count(mcData.itemsByName[\"stick\"].id);\n  if (sticks < 1) {\n    // Craft more sticks using oak planks\n    await craftItem(bot, \"stick\", 1 - sticks);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a diamond sword using diamonds and sticks with the crafting table\n  await craftItem(bot, \"diamond_sword\", 1, craftingTablePosition);\n  bot.chat(\"Diamond sword crafted.\");\n}", "description": "async function craftDiamondSword(bot) {\n    // The function crafts a diamond sword using diamonds and sticks. It first checks if there are enough diamonds and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a diamond sword. Finally, it sends a chat message indicating that the diamond sword has been crafted.\n}"}, "craftIronHelmet": {"code": "async function craftIronHelmet(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 5) {\n    // Mine iron ores\n    await mineBlock(bot, \"iron_ore\", 5 - ironIngots);\n\n    // Place a furnace near the player\n    const furnacePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"furnace\", furnacePosition);\n\n    // Smelt iron ores into iron ingots\n    for (let i = 0; i < 5 - ironIngots; i++) {\n      await smeltItem(bot, \"raw_iron\", \"coal\");\n    }\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft an iron helmet using iron ingots and the crafting table\n  await craftItem(bot, \"iron_helmet\", 1, craftingTablePosition);\n  bot.chat(\"Iron helmet crafted.\");\n}", "description": "async function craftIronHelmet(bot) {\n    // The function crafts an iron helmet using iron ingots and a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores, places a furnace, and smelts the ores into ingots. Then it places a crafting table near the player and crafts an iron helmet using the ingots and the crafting table. Finally, it sends a chat message indicating that the iron helmet has been crafted.\n}"}, "equipIronHelmet": {"code": "async function equipIronHelmet(bot) {\n  // Find the iron helmet in the bot's inventory\n  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_helmet\"].id);\n\n  // Equip the iron helmet in the head slot\n  await bot.equip(ironHelmet, \"head\");\n  bot.chat(\"Iron helmet equipped.\");\n}", "description": "async function equipIronHelmet(bot) {\n    // The function is about equipping an iron helmet in the head slot of the bot's inventory. It first finds the iron helmet in the bot's inventory and then equips it in the head slot. Finally, it sends a chat message confirming that the iron helmet has been equipped.\n}"}, "craftIronChestplate": {"code": "async function craftIronChestplate(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 8) {\n    // Mine iron ores\n    await mineBlock(bot, \"iron_ore\", 8 - ironIngots);\n\n    // Place a furnace near the player\n    const furnacePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"furnace\", furnacePosition);\n\n    // Smelt iron ores into iron ingots\n    for (let i = 0; i < 8 - ironIngots; i++) {\n      await smeltItem(bot, \"raw_iron\", \"coal\");\n    }\n  }\n\n  // Check if there is a crafting table in the inventory\n  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName[\"crafting_table\"].id);\n  if (!craftingTable) {\n    // Craft a crafting table\n    await craftItem(bot, \"crafting_table\", 1);\n  }\n\n  // Try to place the crafting table near the player at different positions until it is successfully placed\n  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];\n  let craftingTablePosition = null;\n  for (const offset of offsets) {\n    try {\n      craftingTablePosition = bot.entity.position.offset(offset.x, offset.y, offset.z);\n      await placeItem(bot, \"crafting_table\", craftingTablePosition);\n      break;\n    } catch (error) {\n      console.log(\"Error placing crafting_table:\", error.message);\n    }\n  }\n  if (!craftingTablePosition) {\n    bot.chat(\"Failed to place crafting table. Please try again.\");\n    return;\n  }\n\n  // Craft an iron chestplate using iron ingots and the crafting table\n  await craftItem(bot, \"iron_chestplate\", 1, craftingTablePosition);\n  bot.chat(\"Iron chestplate crafted.\");\n}", "description": "async function craftIronChestplate(bot) {\n    // The function crafts an iron chestplate using iron ingots and a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores, places a furnace, and smelts the ores into ingots. Then it checks if there is a crafting table in the inventory, and if not, it crafts one. Next, it tries to place the crafting table near the player at different positions until it is successfully placed. Finally, it crafts an iron chestplate using the iron ingots and the crafting table.\n}"}, "equipShield": {"code": "async function equipShield(bot) {\n  // Find the shield in the bot's inventory\n  const shield = bot.inventory.findInventoryItem(mcData.itemsByName[\"shield\"].id);\n\n  // Equip the shield in the off-hand slot\n  await bot.equip(shield, \"off-hand\");\n  bot.chat(\"Shield equipped.\");\n}", "description": "async function equipShield(bot) {\n    // The function equips a shield in the off-hand slot of the bot's inventory. It first finds the shield in the bot's inventory and then equips it in the off-hand slot. Finally, it sends a chat message confirming that the shield has been equipped.\n}"}, "equipIronChestplate": {"code": "async function equipIronChestplate(bot) {\n  // Find the iron chestplate in the bot's inventory\n  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_chestplate\"].id);\n\n  // Equip the iron chestplate in the torso slot\n  await bot.equip(ironChestplate, \"torso\");\n  bot.chat(\"Iron chestplate equipped.\");\n}", "description": "async function equipIronChestplate(bot) {\n    // The function equips an iron chestplate in the torso slot of the bot's armor. It first finds the iron chestplate in the bot's inventory and then equips it using the `bot.equip` function. Finally, it sends a chat message confirming that the iron chestplate has been equipped.\n}"}, "craftIronLeggingsAndBoots": {"code": "async function craftIronLeggingsAndBoots(bot) {\n  // Check if there are enough iron ingots in the inventory\n  const ironIngots = bot.inventory.count(mcData.itemsByName[\"iron_ingot\"].id);\n  if (ironIngots < 11) {\n    // Mine iron ores\n    await mineBlock(bot, \"iron_ore\", 11 - ironIngots);\n\n    // Check if there are enough coal in the inventory\n    const coalCount = bot.inventory.count(mcData.itemsByName[\"coal\"].id);\n    if (coalCount < 11 - ironIngots) {\n      // Mine coal\n      await mineBlock(bot, \"coal_ore\", 11 - ironIngots - coalCount);\n    }\n\n    // Place a furnace near the player\n    const furnacePosition = bot.entity.position.offset(1, 0, 0);\n    await placeItem(bot, \"furnace\", furnacePosition);\n\n    // Smelt iron ores into iron ingots\n    for (let i = 0; i < 11 - ironIngots; i++) {\n      await smeltItem(bot, \"raw_iron\", \"coal\");\n    }\n  }\n\n  // Check if there is a crafting table in the inventory\n  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName[\"crafting_table\"].id);\n  if (!craftingTable) {\n    // Craft a crafting table\n    await craftItem(bot, \"crafting_table\", 1);\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft iron leggings using the crafting table\n  await craftItem(bot, \"iron_leggings\", 1);\n\n  // Craft iron boots using the crafting table\n  await craftItem(bot, \"iron_boots\", 1);\n  bot.chat(\"Iron leggings and iron boots crafted.\");\n}", "description": "async function craftIronLeggingsAndBoots(bot) {\n    // The function crafts iron leggings and boots. It checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and coal to smelt them into iron ingots. It then checks if there is a crafting table in the inventory, and if not, it crafts one. The function places the crafting table and a furnace near the player, and uses the furnace to smelt the iron ores. Finally, it crafts iron leggings and boots using the crafting table.\n}"}, "equipIronLeggingsAndBoots": {"code": "async function equipIronLeggingsAndBoots(bot) {\n  // Find the iron leggings and iron boots in the bot's inventory\n  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_leggings\"].id);\n  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName[\"iron_boots\"].id);\n\n  // Check if the bot has iron leggings and iron boots\n  if (ironLeggings && ironBoots) {\n    // Equip the iron leggings in the legs slot\n    await bot.equip(ironLeggings, \"legs\");\n\n    // Equip the iron boots in the feet slot\n    await bot.equip(ironBoots, \"feet\");\n\n    // Send a chat message to indicate that the iron leggings and iron boots have been equipped\n    bot.chat(\"Iron leggings and iron boots equipped.\");\n  } else {\n    bot.chat(\"Iron leggings and/or iron boots not found in inventory.\");\n  }\n}", "description": "async function equipIronLeggingsAndBoots(bot) {\n    // The function equips the bot with iron leggings and iron boots if they are available in the inventory, and sends a chat message indicating that they have been equipped. If the items are not found in the inventory, it sends a chat message indicating that they were not found.\n}"}, "waitAndEatCookedMutton": {"code": "async function waitAndEatCookedMutton(bot) {\n  // Wait until the bot's hunger is less than 20\n  while (bot.food >= 20) {\n    await bot.waitForTicks(20);\n  }\n\n  // Equip a cooked mutton in the bot's hand\n  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName[\"cooked_mutton\"].id);\n  await bot.equip(cookedMutton, \"hand\");\n\n  // Consume the cooked mutton\n  await bot.consume();\n  bot.chat(\"1 cooked mutton eaten.\");\n}", "description": "async function waitAndEatCookedMutton(bot) {\n    // The function waits until the bot's hunger is less than 20, equips a cooked mutton in the bot's hand, consumes it, and then sends a chat message indicating that 1 cooked mutton has been eaten.\n}"}, "eatCookedMuttonIfHungry": {"code": "async function eatCookedMuttonIfHungry(bot) {\n  // Check if the bot's hunger is less than 20\n  if (bot.food < 20) {\n    // Equip the cooked mutton in the bot's hand\n    const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName[\"cooked_mutton\"].id);\n    await bot.equip(cookedMutton, \"hand\");\n\n    // Consume the cooked mutton\n    await bot.consume();\n    bot.chat(\"1 cooked mutton eaten.\");\n  } else {\n    bot.chat(\"Hunger is full, no need to eat cooked mutton.\");\n  }\n}", "description": "async function eatCookedMuttonIfHungry(bot) {\n    // The function checks if the bot's hunger is less than 20, and if so, equips and consumes a cooked mutton to restore hunger. If the hunger is already full, it will not eat the cooked mutton.\n}"}, "eatCookedMutton": {"code": "async function eatCookedMutton(bot) {\n  // Equip a cooked mutton in the bot's hand\n  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName[\"cooked_mutton\"].id);\n  await bot.equip(cookedMutton, \"hand\");\n\n  // Consume the cooked mutton\n  await bot.consume();\n  bot.chat(\"1 cooked mutton eaten.\");\n}", "description": "async function eatCookedMutton(bot) {\n    // The function is about making the bot eat a cooked mutton. First, it equips a cooked mutton in the bot's hand. Then, it consumes the cooked mutton and sends a chat message indicating that 1 cooked mutton has been eaten.\n}"}, "craftBirchBoat": {"code": "async function findSuitablePosition(bot) {\n  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];\n  for (const offset of offsets) {\n    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);\n    const blockBelow = bot.blockAt(position.offset(0, -1, 0));\n    if (blockBelow && blockBelow.name !== \"air\") {\n      return position;\n    }\n  }\n  return null;\n}\n\nasync function craftBirchBoat(bot) {\n  // Check if there are enough birch logs in the inventory\n  const birchLogs = bot.inventory.count(mcData.itemsByName[\"birch_log\"].id);\n  if (birchLogs < 5) {\n    // Mine more birch logs\n    await mineBlock(bot, \"birch_log\", 5 - birchLogs);\n  }\n\n  // Craft birch planks using birch logs\n  await craftItem(bot, \"birch_planks\", 5);\n\n  // Check if there is a crafting table in the inventory\n  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName[\"crafting_table\"].id);\n  if (!craftingTable) {\n    // Craft a crafting table\n    await craftItem(bot, \"crafting_table\", 1);\n  }\n\n  // Find a suitable position to place the crafting table\n  const craftingTablePosition = await findSuitablePosition(bot);\n  if (!craftingTablePosition) {\n    bot.chat(\"Failed to find a suitable position to place the crafting table. Please try again.\");\n    return;\n  }\n\n  // Place the crafting table at the suitable position\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft a birch boat using birch planks and the crafting table\n  await craftItem(bot, \"birch_boat\", 1, craftingTablePosition);\n  bot.chat(\"Birch boat crafted.\");\n}", "description": "async function craftBirchBoat(bot) {\n    // The function crafts a birch boat using birch logs and a crafting table. It first checks if there are enough birch logs in the inventory, and if not, mines more. Then, it crafts birch planks using the birch logs. If there is no crafting table in the inventory, it crafts one. It finds a suitable position to place the crafting table and places it there. Finally, it crafts a birch boat using the birch planks and the crafting table.\n}"}, "craftBoneMeal": {"code": "async function craftBoneMeal(bot) {\n  // Check if there are enough bones in the inventory\n  const bones = bot.inventory.count(mcData.itemsByName[\"bone\"].id);\n  if (bones < 2) {\n    bot.chat(\"Not enough bones to craft 4 bone meal.\");\n    return;\n  }\n\n  // Place the crafting table near the player\n  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);\n  await placeItem(bot, \"crafting_table\", craftingTablePosition);\n\n  // Craft 4 bone meal using 2 bones and the crafting table\n  await craftItem(bot, \"bone_meal\", 2, craftingTablePosition);\n  bot.chat(\"4 bone meal crafted.\");\n}", "description": "async function craftBoneMeal(bot) {\n    // The function is about crafting 4 bone meal using 2 bones and a crafting table. It first checks if there are enough bones in the inventory, and if not, it returns. Then, it places a crafting table near the player using the `placeItem` helper function. Finally, it crafts 4 bone meal using 2 bones and the crafting table, and sends a chat message indicating that the bone meal has been crafted.\n}"}}


================================================
FILE: skill_library/trial3/skill/code/cookChicken.js
================================================
async function cookChicken(bot) {
  // Check if there is a furnace in the inventory
  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName["furnace"].id);

  // If there is no furnace, craft one using cobblestone
  if (!furnace) {
    await craftItem(bot, "furnace", 1);
  }

  // Place the furnace near the player
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt the raw chicken using coal as fuel in the furnace
  await smeltItem(bot, "chicken", "coal", 1);

  // Collect the cooked chicken
  bot.chat("1 chicken cooked.");
}


================================================
FILE: skill_library/trial3/skill/code/cookRawBeef.js
================================================
async function cookRawBeef(bot) {
  // Check if there is a furnace in the inventory
  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName["furnace"].id);

  // If there is no furnace, craft one using cobblestone
  if (!furnace) {
    await craftItem(bot, "furnace", 1);
  }

  // Place the furnace near the player
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt the 6 raw beef using coal as fuel in the furnace
  await smeltItem(bot, "beef", "coal", 6);

  // Collect the cooked beef
  bot.chat("6 raw beef cooked.");
}


================================================
FILE: skill_library/trial3/skill/code/cookRawMutton.js
================================================
async function cookRawMutton(bot) {
  // Check if there is a furnace in the inventory
  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName["furnace"].id);

  // If there is no furnace, craft one using cobblestone
  if (!furnace) {
    await craftItem(bot, "furnace", 1);
  }

  // Place the furnace near the player
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt the 4 raw mutton using coal as fuel in the furnace
  await smeltItem(bot, "mutton", "coal", 4);

  // Collect the cooked mutton
  bot.chat("4 raw mutton cooked.");
}


================================================
FILE: skill_library/trial3/skill/code/cookThreeRawChicken.js
================================================
async function cookThreeRawChicken(bot) {
  // Find a suitable location to place the furnace
  const furnacePosition = bot.entity.position.offset(1, 0, 0);

  // Place the furnace
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 3 raw chicken using coal as fuel
  await smeltItem(bot, "chicken", "coal", 3);
  bot.chat("3 raw chicken cooked.");
}


================================================
FILE: skill_library/trial3/skill/code/craftBirchBoat.js
================================================
async function findSuitablePosition(bot) {
  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];
  for (const offset of offsets) {
    const position = bot.entity.position.offset(offset.x, offset.y, offset.z);
    const blockBelow = bot.blockAt(position.offset(0, -1, 0));
    if (blockBelow && blockBelow.name !== "air") {
      return position;
    }
  }
  return null;
}

async function craftBirchBoat(bot) {
  // Check if there are enough birch logs in the inventory
  const birchLogs = bot.inventory.count(mcData.itemsByName["birch_log"].id);
  if (birchLogs < 5) {
    // Mine more birch logs
    await mineBlock(bot, "birch_log", 5 - birchLogs);
  }

  // Craft birch planks using birch logs
  await craftItem(bot, "birch_planks", 5);

  // Check if there is a crafting table in the inventory
  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName["crafting_table"].id);
  if (!craftingTable) {
    // Craft a crafting table
    await craftItem(bot, "crafting_table", 1);
  }

  // Find a suitable position to place the crafting table
  const craftingTablePosition = await findSuitablePosition(bot);
  if (!craftingTablePosition) {
    bot.chat("Failed to find a suitable position to place the crafting table. Please try again.");
    return;
  }

  // Place the crafting table at the suitable position
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a birch boat using birch planks and the crafting table
  await craftItem(bot, "birch_boat", 1, craftingTablePosition);
  bot.chat("Birch boat crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftBoneMeal.js
================================================
async function craftBoneMeal(bot) {
  // Check if there are enough bones in the inventory
  const bones = bot.inventory.count(mcData.itemsByName["bone"].id);
  if (bones < 2) {
    bot.chat("Not enough bones to craft 4 bone meal.");
    return;
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft 4 bone meal using 2 bones and the crafting table
  await craftItem(bot, "bone_meal", 2, craftingTablePosition);
  bot.chat("4 bone meal crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftChest.js
================================================
async function craftChest(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanks = bot.inventory.count(mcData.itemsByName["oak_planks"].id);
  if (oakPlanks < 8) {
    // Mine more oak logs
    await mineBlock(bot, "oak_log", 8 - oakPlanks);
    // Craft oak planks using oak logs
    await craftItem(bot, "oak_planks", 8 - oakPlanks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a chest using oak planks with the crafting table
  await craftItem(bot, "chest", 1, craftingTablePosition);
  bot.chat("Chest crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftClock.js
================================================
async function craftClock(bot) {
  // Check if there is a crafting table in the inventory
  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName["crafting_table"].id);

  // If there is no crafting table, craft one using oak planks
  if (!craftingTable) {
    await craftItem(bot, "crafting_table", 1);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a clock using 4 gold ingots and 1 redstone dust with the crafting table
  await craftItem(bot, "clock", 1, craftingTablePosition);
  bot.chat("Clock crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftCopperBlock.js
================================================
async function craftCopperBlock(bot) {
  // Check if there are enough copper ingots in the inventory
  const copperIngots = bot.inventory.count(mcData.itemsByName["copper_ingot"].id);
  if (copperIngots < 9) {
    bot.chat("Not enough copper ingots to craft a copper block.");
    return;
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a copper block using copper ingots and the crafting table
  await craftItem(bot, "copper_block", 1, craftingTablePosition);
  bot.chat("Copper block crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftDiamondSword.js
================================================
async function craftDiamondSword(bot) {
  // Check if there are enough diamonds in the inventory
  const diamonds = bot.inventory.count(mcData.itemsByName["diamond"].id);
  if (diamonds < 2) {
    bot.chat("Not enough diamonds to craft a diamond sword.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 1) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 1 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a diamond sword using diamonds and sticks with the crafting table
  await craftItem(bot, "diamond_sword", 1, craftingTablePosition);
  bot.chat("Diamond sword crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftFurnace.js
================================================
async function craftFurnace(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 8) {
    bot.chat("Not enough cobblestones to craft a furnace.");
    return;
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a furnace using cobblestones and the crafting table
  await craftItem(bot, "furnace", 1, craftingTablePosition);
  bot.chat("Furnace crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftIronChestplate.js
================================================
async function craftIronChestplate(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 8) {
    // Mine iron ores
    await mineBlock(bot, "iron_ore", 8 - ironIngots);

    // Place a furnace near the player
    const furnacePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "furnace", furnacePosition);

    // Smelt iron ores into iron ingots
    for (let i = 0; i < 8 - ironIngots; i++) {
      await smeltItem(bot, "raw_iron", "coal");
    }
  }

  // Check if there is a crafting table in the inventory
  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName["crafting_table"].id);
  if (!craftingTable) {
    // Craft a crafting table
    await craftItem(bot, "crafting_table", 1);
  }

  // Try to place the crafting table near the player at different positions until it is successfully placed
  const offsets = [new Vec3(1, 0, 0), new Vec3(-1, 0, 0), new Vec3(0, 0, 1), new Vec3(0, 0, -1)];
  let craftingTablePosition = null;
  for (const offset of offsets) {
    try {
      craftingTablePosition = bot.entity.position.offset(offset.x, offset.y, offset.z);
      await placeItem(bot, "crafting_table", craftingTablePosition);
      break;
    } catch (error) {
      console.log("Error placing crafting_table:", error.message);
    }
  }
  if (!craftingTablePosition) {
    bot.chat("Failed to place crafting table. Please try again.");
    return;
  }

  // Craft an iron chestplate using iron ingots and the crafting table
  await craftItem(bot, "iron_chestplate", 1, craftingTablePosition);
  bot.chat("Iron chestplate crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftIronHelmet.js
================================================
async function craftIronHelmet(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 5) {
    // Mine iron ores
    await mineBlock(bot, "iron_ore", 5 - ironIngots);

    // Place a furnace near the player
    const furnacePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "furnace", furnacePosition);

    // Smelt iron ores into iron ingots
    for (let i = 0; i < 5 - ironIngots; i++) {
      await smeltItem(bot, "raw_iron", "coal");
    }
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron helmet using iron ingots and the crafting table
  await craftItem(bot, "iron_helmet", 1, craftingTablePosition);
  bot.chat("Iron helmet crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftIronLeggingsAndBoots.js
================================================
async function craftIronLeggingsAndBoots(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 11) {
    // Mine iron ores
    await mineBlock(bot, "iron_ore", 11 - ironIngots);

    // Check if there are enough coal in the inventory
    const coalCount = bot.inventory.count(mcData.itemsByName["coal"].id);
    if (coalCount < 11 - ironIngots) {
      // Mine coal
      await mineBlock(bot, "coal_ore", 11 - ironIngots - coalCount);
    }

    // Place a furnace near the player
    const furnacePosition = bot.entity.position.offset(1, 0, 0);
    await placeItem(bot, "furnace", furnacePosition);

    // Smelt iron ores into iron ingots
    for (let i = 0; i < 11 - ironIngots; i++) {
      await smeltItem(bot, "raw_iron", "coal");
    }
  }

  // Check if there is a crafting table in the inventory
  const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName["crafting_table"].id);
  if (!craftingTable) {
    // Craft a crafting table
    await craftItem(bot, "crafting_table", 1);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft iron leggings using the crafting table
  await craftItem(bot, "iron_leggings", 1);

  // Craft iron boots using the crafting table
  await craftItem(bot, "iron_boots", 1);
  bot.chat("Iron leggings and iron boots crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftIronPickaxe.js
================================================
async function craftIronPickaxe(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 3) {
    bot.chat("Not enough iron ingots to craft an iron pickaxe.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron pickaxe using iron ingots and sticks with the crafting table
  await craftItem(bot, "iron_pickaxe", 1, craftingTablePosition);
  bot.chat("Iron pickaxe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftIronSword.js
================================================
async function craftIronSword(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 2) {
    bot.chat("Not enough iron ingots to craft an iron sword.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 1) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 1 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft an iron sword using iron ingots and sticks with the crafting table
  await craftItem(bot, "iron_sword", 1, craftingTablePosition);
  bot.chat("Iron sword crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftShield.js
================================================
async function craftShield(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanks = bot.inventory.count(mcData.itemsByName["oak_planks"].id);
  if (oakPlanks < 6) {
    // Craft more oak planks using oak logs
    await craftItem(bot, "oak_planks", 6 - oakPlanks);
  }

  // Check if there are enough iron ingots in the inventory
  const ironIngots = bot.inventory.count(mcData.itemsByName["iron_ingot"].id);
  if (ironIngots < 1) {
    bot.chat("Not enough iron ingots to craft a shield.");
    return;
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a shield using oak planks and iron ingots with the crafting table
  await craftItem(bot, "shield", 1, craftingTablePosition);
  bot.chat("Shield crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneAxe.js
================================================
async function craftStoneAxe(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 3) {
    bot.chat("Not enough cobblestones to craft a stone axe.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone axe using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_axe", 1, craftingTablePosition);
  bot.chat("Stone axe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneHoe.js
================================================
async function craftStoneHoe(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 2) {
    bot.chat("Not enough cobblestones to craft a stone hoe.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone hoe using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_hoe", 1, craftingTablePosition);
  bot.chat("Stone hoe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneHoeV2.js
================================================
async function craftStoneHoe(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 2) {
    bot.chat("Not enough cobblestones to craft a stone hoe.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone hoe using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_hoe", 1, craftingTablePosition);
  bot.chat("Stone hoe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStonePickaxe.js
================================================
async function craftStonePickaxe(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 3) {
    bot.chat("Not enough cobblestones to craft a stone pickaxe.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone pickaxe using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_pickaxe", 1, craftingTablePosition);
  bot.chat("Stone pickaxe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneShovel.js
================================================
async function craftStoneShovel(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 1) {
    bot.chat("Not enough cobblestones to craft a stone shovel.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone shovel using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_shovel", 1, craftingTablePosition);
  bot.chat("Stone shovel crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneSword.js
================================================
async function craftStoneSword(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 2) {
    bot.chat("Not enough cobblestones to craft a stone sword.");
    return;
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 1) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 1 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone sword using cobblestones and sticks with the crafting table
  await craftItem(bot, "stone_sword", 1, craftingTablePosition);
  bot.chat("Stone sword crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftStoneTools.js
================================================
async function craftStoneTools(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 6) {
    // Mine more cobblestones
    await mineBlock(bot, "stone", 6 - cobblestones);
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 5) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 5 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a stone sword, a stone axe, and a stone shovel using the crafting table
  await craftItem(bot, "stone_sword", 1, craftingTablePosition);
  await craftItem(bot, "stone_axe", 1, craftingTablePosition);
  await craftItem(bot, "stone_shovel", 1, craftingTablePosition);
  bot.chat("Stone sword, stone axe, and stone shovel crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftTenCobblestoneWalls.js
================================================
async function craftTenCobblestoneWalls(bot) {
  // Check if there are enough cobblestones in the inventory
  const cobblestones = bot.inventory.count(mcData.itemsByName["cobblestone"].id);
  if (cobblestones < 32) {
    bot.chat("Not enough cobblestones to craft 10 cobblestone walls.");
    return;
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft 6 cobblestone walls using the crafting table
  await craftItem(bot, "cobblestone_wall", 1, craftingTablePosition);

  // Craft 6 more cobblestone walls using the crafting table
  await craftItem(bot, "cobblestone_wall", 1, craftingTablePosition);
  bot.chat("10 cobblestone walls crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftWoodenPickaxe.js
================================================
async function craftWoodenPickaxe(bot) {
  // Check if there are enough oak logs in the inventory
  const oakLogs = bot.inventory.count(mcData.itemsByName["oak_log"].id);
  if (oakLogs < 4) {
    // Mine more oak logs
    await mineBlock(bot, "oak_log", 4 - oakLogs);
  }

  // Craft a crafting table using oak logs
  await craftItem(bot, "crafting_table", 1);

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft oak planks using oak logs
  await craftItem(bot, "oak_planks", 4, craftingTablePosition);

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 2) {
    // Craft sticks using oak planks
    await craftItem(bot, "stick", 2 - sticks, craftingTablePosition);
  }

  // Craft a wooden pickaxe using oak planks and sticks with the crafting table
  await craftItem(bot, "wooden_pickaxe", 1, craftingTablePosition);
  bot.chat("Wooden pickaxe crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/craftWoodenSword.js
================================================
async function craftWoodenSword(bot) {
  // Check if there are enough oak planks in the inventory
  const oakPlanks = bot.inventory.count(mcData.itemsByName["oak_planks"].id);
  if (oakPlanks < 2) {
    // Craft more oak planks using oak logs
    await craftItem(bot, "oak_planks", 2 - oakPlanks);
  }

  // Check if there are enough sticks in the inventory
  const sticks = bot.inventory.count(mcData.itemsByName["stick"].id);
  if (sticks < 1) {
    // Craft more sticks using oak planks
    await craftItem(bot, "stick", 1 - sticks);
  }

  // Place the crafting table near the player
  const craftingTablePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a wooden sword using oak planks and sticks with the crafting table
  await craftItem(bot, "wooden_sword", 1, craftingTablePosition);
  bot.chat("Wooden sword crafted.");
}


================================================
FILE: skill_library/trial3/skill/code/eatCookedBeef.js
================================================
async function eatCookedBeef(bot) {
  // Equip a cooked beef in the bot's hand
  const cookedBeef = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_beef"].id);
  await bot.equip(cookedBeef, "hand");

  // Consume the cooked beef
  await bot.consume();
  bot.chat("1 cooked beef eaten.");
}


================================================
FILE: skill_library/trial3/skill/code/eatCookedBeefV2.js
================================================
async function eatCookedBeef(bot) {
  // Equip a cooked beef in the bot's hand
  const cookedBeef = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_beef"].id);
  await bot.equip(cookedBeef, "hand");

  // Consume the cooked beef
  await bot.consume();
  bot.chat("1 cooked beef eaten.");
}


================================================
FILE: skill_library/trial3/skill/code/eatCookedBeefV3.js
================================================
async function eatCookedBeef(bot) {
  // Equip a cooked beef in the bot's hand
  const cookedBeef = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_beef"].id);
  await bot.equip(cookedBeef, "hand");

  // Consume the cooked beef
  await bot.consume();
  bot.chat("1 cooked beef eaten.");
}


================================================
FILE: skill_library/trial3/skill/code/eatCookedMutton.js
================================================
async function eatCookedMutton(bot) {
  // Equip a cooked mutton in the bot's hand
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_mutton"].id);
  await bot.equip(cookedMutton, "hand");

  // Consume the cooked mutton
  await bot.consume();
  bot.chat("1 cooked mutton eaten.");
}


================================================
FILE: skill_library/trial3/skill/code/eatCookedMuttonIfHungry.js
================================================
async function eatCookedMuttonIfHungry(bot) {
  // Check if the bot's hunger is less than 20
  if (bot.food < 20) {
    // Equip the cooked mutton in the bot's hand
    const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_mutton"].id);
    await bot.equip(cookedMutton, "hand");

    // Consume the cooked mutton
    await bot.consume();
    bot.chat("1 cooked mutton eaten.");
  } else {
    bot.chat("Hunger is full, no need to eat cooked mutton.");
  }
}


================================================
FILE: skill_library/trial3/skill/code/equipIronChestplate.js
================================================
async function equipIronChestplate(bot) {
  // Find the iron chestplate in the bot's inventory
  const ironChestplate = bot.inventory.findInventoryItem(mcData.itemsByName["iron_chestplate"].id);

  // Equip the iron chestplate in the torso slot
  await bot.equip(ironChestplate, "torso");
  bot.chat("Iron chestplate equipped.");
}


================================================
FILE: skill_library/trial3/skill/code/equipIronHelmet.js
================================================
async function equipIronHelmet(bot) {
  // Find the iron helmet in the bot's inventory
  const ironHelmet = bot.inventory.findInventoryItem(mcData.itemsByName["iron_helmet"].id);

  // Equip the iron helmet in the head slot
  await bot.equip(ironHelmet, "head");
  bot.chat("Iron helmet equipped.");
}


================================================
FILE: skill_library/trial3/skill/code/equipIronLeggingsAndBoots.js
================================================
async function equipIronLeggingsAndBoots(bot) {
  // Find the iron leggings and iron boots in the bot's inventory
  const ironLeggings = bot.inventory.findInventoryItem(mcData.itemsByName["iron_leggings"].id);
  const ironBoots = bot.inventory.findInventoryItem(mcData.itemsByName["iron_boots"].id);

  // Check if the bot has iron leggings and iron boots
  if (ironLeggings && ironBoots) {
    // Equip the iron leggings in the legs slot
    await bot.equip(ironLeggings, "legs");

    // Equip the iron boots in the feet slot
    await bot.equip(ironBoots, "feet");

    // Send a chat message to indicate that the iron leggings and iron boots have been equipped
    bot.chat("Iron leggings and iron boots equipped.");
  } else {
    bot.chat("Iron leggings and/or iron boots not found in inventory.");
  }
}


================================================
FILE: skill_library/trial3/skill/code/equipShield.js
================================================
async function equipShield(bot) {
  // Find the shield in the bot's inventory
  const shield = bot.inventory.findInventoryItem(mcData.itemsByName["shield"].id);

  // Equip the shield in the off-hand slot
  await bot.equip(shield, "off-hand");
  bot.chat("Shield equipped.");
}


================================================
FILE: skill_library/trial3/skill/code/killChickenWithIncreasedTime.js
================================================
async function killChickenWithIncreasedTime(bot) {
  // Explore the area to find a chicken with an increased exploration time limit
  const chicken = await exploreUntil(bot, new Vec3(1, 0, 1), 120, () => {
    const chicken = bot.nearestEntity(entity => {
      return entity.name === "chicken" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return chicken;
  });
  if (!chicken) {
    bot.chat("No chicken found.");
    return;
  }

  // Equip a weapon (preferably a sword) to kill the chicken
  const sword = bot.inventory.findInventoryItem(mcData.itemsByName["stone_sword"].id) || bot.inventory.findInventoryItem(mcData.itemsByName["wooden_sword"].id);
  if (sword) {
    await bot.equip(sword, "hand");
  } else {
    bot.chat("No sword found, using bare hands.");
  }

  // Kill the chicken
  await killMob(bot, "chicken", 300);

  // Report the completion of the task
  bot.chat("1 chicken killed.");
}


================================================
FILE: skill_library/trial3/skill/code/killThreeChickens.js
================================================
async function killThreeChickens(bot) {
  // Equip a weapon (preferably a sword) to kill the chickens
  const sword = bot.inventory.findInventoryItem(mcData.itemsByName["stone_sword"].id) || bot.inventory.findInventoryItem(mcData.itemsByName["wooden_sword"].id);
  if (sword) {
    await bot.equip(sword, "hand");
  } else {
    bot.chat("No sword found, using bare hands.");
  }

  // Explore the area to find 3 chickens
  let chickens = [];
  while (chickens.length < 3) {
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const nearbyChicken = bot.nearestEntity(entity => {
        return entity.name === "chicken" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      if (nearbyChicken && !chickens.includes(nearbyChicken)) {
        chickens.push(nearbyChicken);
        return chickens.length === 3 ? chickens : null;
      }
      return null;
    });
  }

  // Kill each chicken one by one
  for (const chicken of chickens) {
    await killMob(bot, chicken.name, 300);
  }

  // Report the completion of the task
  bot.chat("3 chickens killed.");
}


================================================
FILE: skill_library/trial3/skill/code/killThreeCows.js
================================================
async function killThreeCows(bot) {
  // Explore the area to find 3 cows
  let cows = [];
  while (cows.length < 3) {
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const nearbyCow = bot.nearestEntity(entity => {
        return entity.name === "cow" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      if (nearbyCow && !cows.includes(nearbyCow)) {
        cows.push(nearbyCow);
        return cows.length === 3 ? cows : null;
      }
      return null;
    });
  }

  // Equip a weapon (preferably a sword) to kill the cows
  const sword = bot.inventory.findInventoryItem(mcData.itemsByName["stone_sword"].id) || bot.inventory.findInventoryItem(mcData.itemsByName["wooden_sword"].id);
  if (sword) {
    await bot.equip(sword, "hand");
  } else {
    bot.chat("No sword found, using bare hands.");
  }

  // Kill each cow one by one
  for (const cow of cows) {
    await killMob(bot, cow.name, 300);
  }

  // Report the completion of the task
  bot.chat("3 cows killed.");
}


================================================
FILE: skill_library/trial3/skill/code/killThreeSheep.js
================================================
async function killThreeSheep(bot) {
  // Equip a weapon (preferably a sword) to kill the sheep
  const sword = bot.inventory.findInventoryItem(mcData.itemsByName["stone_sword"].id) || bot.inventory.findInventoryItem(mcData.itemsByName["wooden_sword"].id);
  if (sword) {
    await bot.equip(sword, "hand");
  } else {
    bot.chat("No sword found, using bare hands.");
  }

  // Explore the area to find 3 sheep
  let sheep = [];
  while (sheep.length < 3) {
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const nearbySheep = bot.nearestEntity(entity => {
        return entity.name === "sheep" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      if (nearbySheep && !sheep.includes(nearbySheep)) {
        sheep.push(nearbySheep);
        return sheep.length === 3 ? sheep : null;
      }
      return null;
    });
  }

  // Kill each sheep one by one
  for (const singleSheep of sheep) {
    await killMob(bot, singleSheep.name, 300);
  }

  // Report the completion of the task
  bot.chat("3 sheep killed.");
}


================================================
FILE: skill_library/trial3/skill/code/mineDeepslateOres.js
================================================
async function mineDeepslateOres(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["iron_pickaxe"].id);
  await bot.equip(ironPickaxe, "hand");

  // Find and mine 1 deepslate_redstone_ore
  await mineBlock(bot, "deepslate_redstone_ore", 1);
  bot.chat("1 deepslate_redstone_ore mined.");

  // Find and mine 1 deepslate_gold_ore
  await mineBlock(bot, "deepslate_gold_ore", 1);
  bot.chat("1 deepslate_gold_ore mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineEightCobblestone.js
================================================
async function mineEightCobblestone(bot) {
  // Equip the wooden pickaxe
  const woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["wooden_pickaxe"].id);
  await bot.equip(woodenPickaxe, "hand");

  // Find stone blocks
  const stoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const stone = bot.findBlock({
      matching: mcData.blocksByName["stone"].id,
      maxDistance: 32
    });
    return stone;
  });

  // Mine 8 cobblestone
  await mineBlock(bot, "stone", 8);
  bot.chat("8 cobblestone mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineFiveCoalOre.js
================================================
async function mineFiveCoalOre(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["iron_pickaxe"].id);
  await bot.equip(ironPickaxe, "hand");

  // Find 5 coal ore blocks
  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const coalOres = bot.findBlocks({
      matching: mcData.blocksByName["coal_ore"].id,
      maxDistance: 32,
      count: 5
    });
    return coalOres.length >= 5 ? coalOres : null;
  });

  // Mine the 5 coal ore blocks
  await mineBlock(bot, "coal_ore", 5);
  bot.chat("5 coal ore mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineFiveCopperOre.js
================================================
async function mineFiveCopperOre(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["iron_pickaxe"].id);
  await bot.equip(ironPickaxe, "hand");

  // Find 5 copper ore blocks
  const copperOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const copperOres = bot.findBlocks({
      matching: mcData.blocksByName["copper_ore"].id,
      maxDistance: 32,
      count: 5
    });
    return copperOres.length >= 5 ? copperOres : null;
  });

  // Mine the 5 copper ore blocks
  await mineBlock(bot, "copper_ore", 5);
  bot.chat("5 copper ore mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineFourCoalOre.js
================================================
async function mineFourCoalOre(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["stone_pickaxe"].id);
  await bot.equip(stonePickaxe, "hand");

  // Find and mine 4 coal ore blocks
  await mineBlock(bot, "coal_ore", 4);
  bot.chat("4 coal ore mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineTenCobbledDeepslateBelowY0.js
================================================
async function mineTenCobbledDeepslateBelowY0(bot) {
  // Equip the iron pickaxe
  const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["iron_pickaxe"].id);
  await bot.equip(ironPickaxe, "hand");

  // Find cobbled_deepslate blocks below Y=0
  const cobbledDeepslateBlocks = await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {
    const cobbledDeepslate = bot.findBlock({
      matching: mcData.blocksByName["cobbled_deepslate"].id,
      maxDistance: 32,
      position: pos => pos.y < 0
    });
    return cobbledDeepslate;
  });

  // Mine 10 cobbled_deepslate blocks
  await mineBlock(bot, "cobbled_deepslate", 10);
  bot.chat("10 cobbled_deepslate mined below Y=0.");
}


================================================
FILE: skill_library/trial3/skill/code/mineThreeIronOre.js
================================================
async function mineThreeIronOre(bot) {
  // Equip the stone pickaxe
  const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["stone_pickaxe"].id);
  await bot.equip(stonePickaxe, "hand");

  // Find and mine 3 iron ore blocks
  await mineBlock(bot, "iron_ore", 3);
  bot.chat("3 iron ore mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineThreeMoreOakLogs.js
================================================
async function mineThreeMoreOakLogs(bot) {
  for (let i = 0; i < 3; i++) {
    const oakLogBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const oakLog = bot.findBlock({
        matching: mcData.blocksByName["oak_log"].id,
        maxDistance: 32
      });
      return oakLog;
    });
    if (!oakLogBlock) {
      bot.chat("Could not find an oak log.");
      return;
    }
    await mineBlock(bot, "oak_log", 1);
  }
  bot.chat("3 more oak logs mined.");
}


================================================
FILE: skill_library/trial3/skill/code/mineWoodLog.js
================================================
async function mineWoodLog(bot) {
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];

  // Find a wood log block
  const logBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    for (const logName of logNames) {
      const log = bot.findBlock({
        matching: mcData.blocksByName[logName].id,
        maxDistance: 32
      });
      if (log) return log;
    }
    return null;
  });
  if (!logBlock) {
    bot.chat("Could not find a wood log.");
    return;
  }

  // Mine the wood log block
  await mineBlock(bot, logBlock.name, 1);
  bot.chat("Wood log mined.");
}


================================================
FILE: skill_library/trial3/skill/code/obtainBirchLogs.js
================================================
async function obtainBirchLogs(bot) {
  // Check if there are enough birch logs in the inventory
  const birchLogs = bot.inventory.count(mcData.itemsByName["birch_log"].id);
  const logsNeeded = 5 - birchLogs;
  if (logsNeeded > 0) {
    // Mine the required number of birch logs
    await mineBlock(bot, "birch_log", logsNeeded);
    bot.chat("5 birch logs obtained.");
  } else {
    bot.chat("Already have 5 birch logs in the inventory.");
  }
}


================================================
FILE: skill_library/trial3/skill/code/openChestAndCheckContents.js
================================================
async function openChestAndCheckContents(bot) {
  const targetChestPosition = new Vec3(5, 61, 134);

  // Find the chest at the specified position
  const chestPosition = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const chest = bot.findBlock({
      matching: mcData.blocksByName["chest"].id,
      maxDistance: 32,
      position: targetChestPosition
    });
    return chest ? chest.position : null;
  });

  // Check the contents of the chest
  await checkItemInsideChest(bot, chestPosition);
  bot.chat("Chest at (5, 61, 134) opened and contents checked.");
}


================================================
FILE: skill_library/trial3/skill/code/plantOakSapling.js
================================================
async function plantOakSapling(bot) {
  // Find a suitable location to plant the oak sapling
  const targetBlock = bot.findBlock({
    matching: block => {
      return block.name === "grass_block" || block.name === "dirt";
    },
    maxDistance: 32
  });
  if (!targetBlock) {
    bot.chat("Could not find a suitable location to plant the oak sapling.");
    return;
  }

  // Go to the location
  await bot.pathfinder.goto(new GoalBlock(targetBlock.position.x, targetBlock.position.y, targetBlock.position.z));

  // Equip the oak sapling in the bot's hand
  const oakSapling = bot.inventory.findInventoryItem(mcData.itemsByName["oak_sapling"].id);
  await bot.equip(oakSapling, "hand");

  // Right-click on the ground to plant the oak sapling
  await bot.activateBlock(targetBlock);

  // Send a chat message to indicate the oak sapling has been planted
  bot.chat("Oak sapling planted.");
}


================================================
FILE: skill_library/trial3/skill/code/smeltCopperOre.js
================================================
async function smeltCopperOre(bot) {
  // Check if there is a furnace in the inventory
  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName["furnace"].id);

  // If there is no furnace, craft one using cobblestone
  if (!furnace) {
    await craftItem(bot, "furnace", 1);
  }

  // Place the furnace near the player
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Find a copper ore block
  const copperOre = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const copperOre = bot.findBlock({
      matching: mcData.blocksByName["copper_ore"].id,
      maxDistance: 32
    });
    return copperOre;
  });

  // Mine the copper ore block
  await mineBlock(bot, "copper_ore", 1);

  // Smelt the raw copper using coal as fuel in the furnace
  await smeltItem(bot, "raw_copper", "coal", 1);

  // Collect the smelted copper ingot
  bot.chat("1 copper ore smelted.");
}


================================================
FILE: skill_library/trial3/skill/code/smeltFiveRawCopper.js
================================================
async function smeltFiveRawCopper(bot) {
  // Find a suitable location to place the furnace
  const furnacePosition = bot.entity.position.offset(1, 0, 0);

  // Place the furnace
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 5 raw copper using coal as fuel
  await smeltItem(bot, "raw_copper", "coal", 5);
  bot.chat("5 raw copper smelted.");
}


================================================
FILE: skill_library/trial3/skill/code/smeltFiveRawGold.js
================================================
async function smeltFiveRawGold(bot) {
  // Check if there is a furnace in the inventory
  const furnace = bot.inventory.findInventoryItem(mcData.itemsByName["furnace"].id);

  // If there is no furnace, craft one using cobblestone
  if (!furnace) {
    await craftItem(bot, "furnace", 1);
  }

  // Place the furnace near the player
  const furnacePosition = bot.entity.position.offset(1, 0, 0);
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt the 5 raw gold using coal as fuel in the furnace
  await smeltItem(bot, "raw_gold", "coal", 5);

  // Collect the smelted gold ingots
  bot.chat("5 raw gold smelted.");
}


================================================
FILE: skill_library/trial3/skill/code/smeltRawIron.js
================================================
async function smeltRawIron(bot) {
  // Find a suitable location to place the furnace
  const furnacePosition = bot.entity.position.offset(1, 0, 0);

  // Place the furnace
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 3 raw iron using coal as fuel
  await smeltItem(bot, "raw_iron", "coal", 3);
  bot.chat("3 raw iron smelted.");
}


================================================
FILE: skill_library/trial3/skill/code/smeltThreeRawCopper.js
================================================
async function smeltThreeRawCopper(bot) {
  // Find a suitable location to place the furnace
  const furnacePosition = bot.entity.position.offset(1, 0, 0);

  // Place the furnace
  await placeItem(bot, "furnace", furnacePosition);

  // Smelt 3 raw copper using coal as fuel
  await smeltItem(bot, "raw_copper", "coal", 3);
  bot.chat("3 raw copper smelted.");
}


================================================
FILE: skill_library/trial3/skill/code/waitAndEatCookedMutton.js
================================================
async function waitAndEatCookedMutton(bot) {
  // Wait until the bot's hunger is less than 20
  while (bot.food >= 20) {
    await bot.waitForTicks(20);
  }

  // Equip a cooked mutton in the bot's hand
  const cookedMutton = bot.inventory.findInventoryItem(mcData.itemsByName["cooked_mutton"].id);
  await bot.equip(cookedMutton, "hand");

  // Consume the cooked mutton
  await bot.consume();
  bot.chat("1 cooked mutton eaten.");
}


================================================
FILE: skill_library/trial3/skill/description/cookChicken.txt
================================================
async function cookChicken(bot) {
    // The function is about cooking a raw chicken using a furnace and coal as fuel. First, it checks if there is a furnace in the inventory. If not, it crafts one using cobblestone. Then, it places the furnace near the player. Next, it smelts the raw chicken using coal as fuel in the furnace. Finally, it collects the cooked chicken and sends a chat message.
}


================================================
FILE: skill_library/trial3/skill/description/cookRawBeef.txt
================================================
async function cookRawBeef(bot) {
    // The function is about cooking 6 raw beef using a furnace and coal as fuel. It first checks if there is a furnace in the inventory, and if not, crafts one using cobblestone. Then, it places the furnace near the player and smelts the 6 raw beef using coal as fuel in the furnace. Finally, it collects the cooked beef and sends a chat message.
}


================================================
FILE: skill_library/trial3/skill/description/cookRawMutton.txt
================================================
async function cookRawMutton(bot) {
    // The function is about cooking 4 raw mutton using a furnace and coal as fuel. If there is no furnace in the inventory, the bot will craft one using cobblestone. Then, the bot will place the furnace near the player and smelt the 4 raw mutton using coal as fuel. Finally, the bot will collect the cooked mutton and print a message in the chat.
}


================================================
FILE: skill_library/trial3/skill/description/cookThreeRawChicken.txt
================================================
async function cookThreeRawChicken(bot) {
    // The function is about cooking 3 raw chicken using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 3 raw chicken using coal as fuel and sends a chat message indicating that the chicken has been cooked.
}


================================================
FILE: skill_library/trial3/skill/description/craftBirchBoat.txt
================================================
async function craftBirchBoat(bot) {
    // The function crafts a birch boat using birch logs and a crafting table. It first checks if there are enough birch logs in the inventory, and if not, mines more. Then, it crafts birch planks using the birch logs. If there is no crafting table in the inventory, it crafts one. It finds a suitable position to place the crafting table and places it there. Finally, it crafts a birch boat using the birch planks and the crafting table.
}


================================================
FILE: skill_library/trial3/skill/description/craftBoneMeal.txt
================================================
async function craftBoneMeal(bot) {
    // The function is about crafting 4 bone meal using 2 bones and a crafting table. It first checks if there are enough bones in the inventory, and if not, it returns. Then, it places a crafting table near the player using the `placeItem` helper function. Finally, it crafts 4 bone meal using 2 bones and the crafting table, and sends a chat message indicating that the bone meal has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftChest.txt
================================================
async function craftChest(bot) {
    // The function crafts a chest using oak planks. It checks if there are enough oak planks in the inventory, and if not, it mines oak logs and crafts oak planks. It then places a crafting table near the player and crafts a chest using oak planks with the crafting table. Finally, it sends a chat message indicating that the chest has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftClock.txt
================================================
async function craftClock(bot) {
    // The function crafts a clock using 4 gold ingots and 1 redstone dust. It first checks if there is a crafting table in the inventory, and if not, crafts one using oak planks. Then, it places the crafting table near the player. Finally, it crafts a clock using the crafting table and saves the event of crafting a clock.
}


================================================
FILE: skill_library/trial3/skill/description/craftCopperBlock.txt
================================================
async function craftCopperBlock(bot) {
    // The function crafts a copper block using 9 copper ingots and a crafting table. It first checks if there are enough copper ingots in the inventory, and if not, it returns. Then, it places a crafting table near the player and crafts a copper block using the crafting table. Finally, it sends a chat message indicating that the copper block has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftDiamondSword.txt
================================================
async function craftDiamondSword(bot) {
    // The function crafts a diamond sword using diamonds and sticks. It first checks if there are enough diamonds and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a diamond sword. Finally, it sends a chat message indicating that the diamond sword has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftFurnace.txt
================================================
async function craftFurnace(bot) {
    // The function crafts a furnace using cobblestones and a crafting table. It first checks if there are enough cobblestones in the inventory. If there are, it places a crafting table near the player and crafts a furnace using the cobblestones and the crafting table. Finally, it sends a chat message indicating that the furnace has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftIronChestplate.txt
================================================
async function craftIronChestplate(bot) {
    // The function crafts an iron chestplate using iron ingots and a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores, places a furnace, and smelts the ores into ingots. Then it checks if there is a crafting table in the inventory, and if not, it crafts one. Next, it tries to place the crafting table near the player at different positions until it is successfully placed. Finally, it crafts an iron chestplate using the iron ingots and the crafting table.
}


================================================
FILE: skill_library/trial3/skill/description/craftIronHelmet.txt
================================================
async function craftIronHelmet(bot) {
    // The function crafts an iron helmet using iron ingots and a crafting table. It first checks if there are enough iron ingots in the inventory, and if not, it mines iron ores, places a furnace, and smelts the ores into ingots. Then it places a crafting table near the player and crafts an iron helmet using the ingots and the crafting table. Finally, it sends a chat message indicating that the iron helmet has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftIronLeggingsAndBoots.txt
================================================
async function craftIronLeggingsAndBoots(bot) {
    // The function crafts iron leggings and boots. It checks if there are enough iron ingots in the inventory, and if not, it mines iron ores and coal to smelt them into iron ingots. It then checks if there is a crafting table in the inventory, and if not, it crafts one. The function places the crafting table and a furnace near the player, and uses the furnace to smelt the iron ores. Finally, it crafts iron leggings and boots using the crafting table.
}


================================================
FILE: skill_library/trial3/skill/description/craftIronPickaxe.txt
================================================
async function craftIronPickaxe(bot) {
    // The function crafts an iron pickaxe using iron ingots and sticks. It first checks if there are enough iron ingots and sticks in the inventory, and crafts more sticks if necessary. Then it places a crafting table near the player and uses it to craft an iron pickaxe. Finally, it sends a chat message indicating that the iron pickaxe has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftIronSword.txt
================================================
async function craftIronSword(bot) {
    // The function crafts an iron sword using iron ingots and sticks. It first checks if there are enough iron ingots and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts an iron sword using the crafting table. Finally, it sends a chat message indicating that the iron sword has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftShield.txt
================================================
async function craftShield(bot) {
    // The function crafts a shield using oak planks and iron ingots. It checks if there are enough oak planks and iron ingots in the inventory, and crafts more oak planks if necessary. If there are not enough iron ingots, it returns. It then places a crafting table near the player and crafts a shield using the crafting table. Finally, it sends a chat message indicating that the shield has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneAxe.txt
================================================
async function craftStoneAxe(bot) {
    // The function crafts a stone axe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone axe using the cobblestones and sticks with the crafting table. Finally, it sends a chat message indicating that the stone axe has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneHoe.txt
================================================
async function craftStoneHoe(bot) {
    // The function crafts a stone hoe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone hoe using the cobblestones and sticks with the crafting table. Finally, it sends a chat message indicating that the stone hoe has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneHoeV2.txt
================================================
async function craftStoneHoe(bot) {
    // The function crafts a stone hoe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone hoe using the cobblestones and sticks with the crafting table. Finally, it sends a chat message indicating that the stone hoe has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStonePickaxe.txt
================================================
async function craftStonePickaxe(bot) {
    // The function crafts a stone pickaxe using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a stone pickaxe.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneShovel.txt
================================================
async function craftStoneShovel(bot) {
    // The function crafts a stone shovel using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and uses it to craft a stone shovel. Finally, it sends a chat message indicating that the stone shovel has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneSword.txt
================================================
async function craftStoneSword(bot) {
    // The function crafts a stone sword using cobblestones and sticks. It first checks if there are enough cobblestones and sticks in the inventory. If there are not enough cobblestones, it returns. If there are not enough sticks, it crafts more using oak planks. Then, it places a crafting table near the player and crafts a stone sword using the crafting table. Finally, it sends a chat message indicating that the stone sword has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftStoneTools.txt
================================================
async function craftStoneTools(bot) {
    // The function crafts stone tools (sword, axe, and shovel) using a crafting table. It checks if there are enough cobblestones and sticks in the inventory, and mines more cobblestones or crafts more sticks if necessary. Then, it places a crafting table near the player and crafts the stone tools using the crafting table. Finally, it sends a chat message indicating that the tools have been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/craftTenCobblestoneWalls.txt
================================================
async function craftTenCobblestoneWalls(bot) {
    // The function crafts 10 cobblestone walls using a crafting table. It first checks if there are enough cobblestones in the inventory, and if not, it returns. Then, it places a crafting table near the player and crafts 6 cobblestone walls using the crafting table. It repeats the process to craft 6 more cobblestone walls and outputs a message when the process is complete.
}


================================================
FILE: skill_library/trial3/skill/description/craftWoodenPickaxe.txt
================================================
async function craftWoodenPickaxe(bot) {
    // The function crafts a wooden pickaxe using oak logs, oak planks, and sticks. It first checks if there are enough oak logs in the inventory, and if not, mines more. Then, it crafts a crafting table using oak logs and places it near the player. Next, it crafts oak planks using oak logs and checks if there are enough sticks in the inventory. If not, it crafts sticks using oak planks. Finally, it crafts a wooden pickaxe using oak planks and sticks with the crafting table.
}


================================================
FILE: skill_library/trial3/skill/description/craftWoodenSword.txt
================================================
async function craftWoodenSword(bot) {
    // The function crafts a wooden sword using oak planks and sticks. It checks if there are enough oak planks and sticks in the inventory, and crafts more if necessary. It then places a crafting table near the player and uses it to craft a wooden sword. Finally, it sends a chat message indicating that the wooden sword has been crafted.
}


================================================
FILE: skill_library/trial3/skill/description/eatCookedBeef.txt
================================================
async function eatCookedBeef(bot) {
    // The function is about making the bot eat a cooked beef. It equips a cooked beef in the bot's hand and then consumes it. Finally, it sends a message to the chat saying that 1 cooked beef has been eaten.
}


================================================
FILE: skill_library/trial3/skill/description/eatCookedBeefV2.txt
================================================
async function eatCookedBeef(bot) {
    // The function is about making the bot eat a cooked beef. It equips a cooked beef in the bot's hand and then consumes it. Finally, it sends a message to the chat indicating that one cooked beef has been eaten.
}


================================================
FILE: skill_library/trial3/skill/description/eatCookedBeefV3.txt
================================================
async function eatCookedBeef(bot) {
    // The function is about making the bot eat a cooked beef. It equips a cooked beef in the bot's hand and then consumes it. Finally, it sends a message to the chat indicating that one cooked beef has been eaten.
}


================================================
FILE: skill_library/trial3/skill/description/eatCookedMutton.txt
================================================
async function eatCookedMutton(bot) {
    // The function is about making the bot eat a cooked mutton. First, it equips a cooked mutton in the bot's hand. Then, it consumes the cooked mutton and sends a chat message indicating that 1 cooked mutton has been eaten.
}


================================================
FILE: skill_library/trial3/skill/description/eatCookedMuttonIfHungry.txt
================================================
async function eatCookedMuttonIfHungry(bot) {
    // The function checks if the bot's hunger is less than 20, and if so, equips and consumes a cooked mutton to restore hunger. If the hunger is already full, it will not eat the cooked mutton.
}


================================================
FILE: skill_library/trial3/skill/description/equipIronChestplate.txt
================================================
async function equipIronChestplate(bot) {
    // The function equips an iron chestplate in the torso slot of the bot's armor. It first finds the iron chestplate in the bot's inventory and then equips it using the `bot.equip` function. Finally, it sends a chat message confirming that the iron chestplate has been equipped.
}


================================================
FILE: skill_library/trial3/skill/description/equipIronHelmet.txt
================================================
async function equipIronHelmet(bot) {
    // The function is about equipping an iron helmet in the head slot of the bot's inventory. It first finds the iron helmet in the bot's inventory and then equips it in the head slot. Finally, it sends a chat message confirming that the iron helmet has been equipped.
}


================================================
FILE: skill_library/trial3/skill/description/equipIronLeggingsAndBoots.txt
================================================
async function equipIronLeggingsAndBoots(bot) {
    // The function equips the bot with iron leggings and iron boots if they are available in the inventory, and sends a chat message indicating that they have been equipped. If the items are not found in the inventory, it sends a chat message indicating that they were not found.
}


================================================
FILE: skill_library/trial3/skill/description/equipShield.txt
================================================
async function equipShield(bot) {
    // The function equips a shield in the off-hand slot of the bot's inventory. It first finds the shield in the bot's inventory and then equips it in the off-hand slot. Finally, it sends a chat message confirming that the shield has been equipped.
}


================================================
FILE: skill_library/trial3/skill/description/killChickenWithIncreasedTime.txt
================================================
async function killChickenWithIncreasedTime(bot) {
    // The function is about killing a chicken with an increased exploration time limit. It explores the area to find a chicken within a certain distance. If a chicken is found, it equips a sword (if available) to kill the chicken. Otherwise, it uses bare hands. After killing the chicken, it reports the completion of the task.
}


================================================
FILE: skill_library/trial3/skill/description/killThreeChickens.txt
================================================
async function killThreeChickens(bot) {
    // The function is about killing 3 chickens. First, it equips a sword to kill the chickens, and if there is no sword, it uses bare hands. Then, it explores the environment to find 3 chickens within a 32 block radius. Once 3 chickens are found, it kills each chicken one by one using the equipped weapon. Finally, it reports the completion of the task by sending a chat message.
}


================================================
FILE: skill_library/trial3/skill/description/killThreeCows.txt
================================================
async function killThreeCows(bot) {
    // The function is about killing 3 cows. It explores the environment to find 3 cows within a certain distance. Once 3 cows are found, it equips a sword (if available) to kill the cows one by one. If no sword is found, it uses bare hands. After killing all 3 cows, it reports the completion of the task.
}


================================================
FILE: skill_library/trial3/skill/description/killThreeSheep.txt
================================================
async function killThreeSheep(bot) {
    // The function is about killing 3 sheep. First, it equips a weapon (preferably a sword) to kill the sheep. Then, it explores the environment to find 3 sheep. Once 3 sheep are found, it kills each sheep one by one. Finally, it reports the completion of the task by sending a chat message.
}


================================================
FILE: skill_library/trial3/skill/description/mineDeepslateOres.txt
================================================
async function mineDeepslateOres(bot) {
    // The function is about mining 1 deepslate_redstone_ore and 1 deepslate_gold_ore using an iron pickaxe. The function first equips the iron pickaxe in the hand. Then, it finds and mines 1 deepslate_redstone_ore and 1 deepslate_gold_ore using the mineBlock function. Finally, it sends a chat message indicating the number of ores mined.
}


================================================
FILE: skill_library/trial3/skill/description/mineEightCobblestone.txt
================================================
async function mineEightCobblestone(bot) {
    // The function is about mining 8 cobblestones using a wooden pickaxe. It equips the wooden pickaxe and explores the environment until finding a stone block. Once a stone block is found, it mines a total of 8 cobblestone blocks using the wooden pickaxe. Finally, it sends a chat message indicating that 8 cobblestones have been mined.
}


================================================
FILE: skill_library/trial3/skill/description/mineFiveCoalOre.txt
================================================
async function mineFiveCoalOre(bot) {
    // The function is about mining 5 coal ore blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 coal ore blocks. Once 5 coal ore blocks are found, mine them using the iron pickaxe and save the event of mining 5 coal ore blocks.
}


================================================
FILE: skill_library/trial3/skill/description/mineFiveCopperOre.txt
================================================
async function mineFiveCopperOre(bot) {
    // The function is about mining 5 copper ore blocks using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding 5 copper ore blocks. Once 5 copper ore blocks are found, mine them using the iron pickaxe and save the event of mining 5 copper ore.
}


================================================
FILE: skill_library/trial3/skill/description/mineFourCoalOre.txt
================================================
async function mineFourCoalOre(bot) {
    // The function is about mining 4 coal ore blocks using a stone pickaxe. The function equips the stone pickaxe in the hand and then mines 4 coal ore blocks. Once the mining is complete, the function sends a chat message indicating that 4 coal ore blocks have been mined.
}


================================================
FILE: skill_library/trial3/skill/description/mineTenCobbledDeepslateBelowY0.txt
================================================
async function mineTenCobbledDeepslateBelowY0(bot) {
    // The function is about mining 10 cobbled_deepslate blocks below Y=0 using an iron pickaxe. First, equip the iron pickaxe in the hand. Next, explore the environment until finding a cobbled_deepslate block below Y=0. Once 10 cobbled_deepslate blocks are found, mine them using the iron pickaxe. Finally, a message is sent to the chat indicating that 10 cobbled_deepslate blocks have been mined below Y=0.
}


================================================
FILE: skill_library/trial3/skill/description/mineThreeIronOre.txt
================================================
async function mineThreeIronOre(bot) {
    // The function is about mining 3 iron ore blocks using a stone pickaxe. The function equips the stone pickaxe in the hand and then mines 3 iron ore blocks. Once the mining is complete, the function sends a chat message indicating that 3 iron ore blocks have been mined.
}


================================================
FILE: skill_library/trial3/skill/description/mineThreeMoreOakLogs.txt
================================================
async function mineThreeMoreOakLogs(bot) {
    // The function is about mining three oak logs. It uses a for loop to mine three oak logs. It explores the environment until finding an oak log block, and then mines one oak log block. If it cannot find an oak log block, it returns. Once three oak logs are mined, it sends a chat message.
}


================================================
FILE: skill_library/trial3/skill/description/mineWoodLog.txt
================================================
async function mineWoodLog(bot) {
    // The function is about mining a single wood log block. It searches for any of the seven types of wood logs within a certain distance. Once a wood log block is found, it is mined using the `mineBlock` function. If no wood log block is found, the function returns and a message is sent to the chat.
}


================================================
FILE: skill_library/trial3/skill/description/obtainBirchLogs.txt
================================================
async function obtainBirchLogs(bot) {
    // The function is about obtaining 5 birch logs. It checks if there are enough birch logs in the inventory and mines the required number of birch logs if necessary. Once 5 birch logs are obtained, it sends a chat message. If there are already 5 birch logs in the inventory, it sends a different chat message.
}


================================================
FILE: skill_library/trial3/skill/description/openChestAndCheckContents.txt
================================================
async function openChestAndCheckContents(bot) {
    // The function is about finding a chest at a specified position, opening it, and checking its contents. It uses the `exploreUntil` helper function to find the chest and the `checkItemInsideChest` helper function to check the contents of the chest. The position of the chest is specified by `targetChestPosition`. Once the chest is found, the function checks its contents and sends a chat message indicating that the chest has been opened and its contents have been checked.
}


================================================
FILE: skill_library/trial3/skill/description/plantOakSapling.txt
================================================
async function plantOakSapling(bot) {
    // The function is about finding a suitable location to plant an oak sapling, going to that location, equipping the oak sapling in the bot's hand, right-clicking on the ground to plant the oak sapling, and sending a chat message to indicate the oak sapling has been planted. If a suitable location cannot be found, the function will return without planting the oak sapling.
}


================================================
FILE: skill_library/trial3/skill/description/smeltCopperOre.txt
================================================
async function smeltCopperOre(bot) {
    // The function is about smelting one copper ore block into a copper ingot using a furnace and coal as fuel. First, check if there is a furnace in the inventory. If not, craft one using cobblestone. Then, place the furnace near the player. Next, explore the environment until finding a copper ore block. Once a copper ore block is found, mine it and smelt the raw copper using coal as fuel in the furnace. Finally, collect the smelted copper ingot.
}


================================================
FILE: skill_library/trial3/skill/description/smeltFiveRawCopper.txt
================================================
async function smeltFiveRawCopper(bot) {
    // The function is about smelting 5 raw copper using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 5 raw copper using coal as fuel and sends a chat message indicating that 5 raw copper has been smelted.
}


================================================
FILE: skill_library/trial3/skill/description/smeltFiveRawGold.txt
================================================
async function smeltFiveRawGold(bot) {
    // The function is about smelting 5 raw gold into gold ingots using a furnace and coal as fuel. If there is no furnace in the inventory, the bot will craft one using cobblestone. Then, the bot will place the furnace near the player and smelt the 5 raw gold using coal as fuel. Finally, the bot will collect the smelted gold ingots and print a message in the chat.
}


================================================
FILE: skill_library/trial3/skill/description/smeltRawIron.txt
================================================
async function smeltRawIron(bot) {
    // The function is about smelting 3 raw iron using coal as fuel. First, find a suitable location to place the furnace. Then, place the furnace at the found location. Finally, smelt 3 raw iron using coal as fuel and save the event of smelting 3 raw iron.
}


================================================
FILE: skill_library/trial3/skill/description/smeltThreeRawCopper.txt
================================================
async function smeltThreeRawCopper(bot) {
    // The function is about smelting 3 raw copper using a furnace and coal as fuel. First, it finds a suitable location to place the furnace. Then, it places the furnace at that location. Finally, it smelts 3 raw copper using coal as fuel and saves the event of smelting 3 raw copper.
}


================================================
FILE: skill_library/trial3/skill/description/waitAndEatCookedMutton.txt
================================================
async function waitAndEatCookedMutton(bot) {
    // The function waits until the bot's hunger is less than 20, equips a cooked mutton in the bot's hand, consumes it, and then sends a chat message indicating that 1 cooked mutton has been eaten.
}


================================================
FILE: skill_library/trial3/skill/vectordb/chroma-collections.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/vectordb/chroma-embeddings.parquet
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/vectordb/index/id_to_uuid_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/vectordb/index/index_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.bin
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/vectordb/index/index_metadata_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
================================================
[Non-text file]


================================================
FILE: skill_library/trial3/skill/vectordb/index/uuid_to_id_2f8ccde6-89f7-422b-87ec-8e46e8f1292a.pkl
================================================
[Non-text file]


================================================
FILE: voyager/__init__.py
================================================
from .voyager import Voyager



================================================
FILE: voyager/voyager.py
================================================
import copy
import json
import os
import time
from typing import Dict

import voyager.utils as U
from .env import VoyagerEnv

from .agents import ActionAgent
from .agents import CriticAgent
from .agents import CurriculumAgent
from .agents import SkillManager


# TODO: remove event memory
class Voyager:
    def __init__(
        self,
        mc_port: int = None,
        azure_login: Dict[str, str] = None,
        server_port: int = 3000,
        openai_api_key: str = None,
        env_wait_ticks: int = 20,
        env_request_timeout: int = 600,
        max_iterations: int = 160,
        reset_placed_if_failed: bool = False,
        action_agent_model_name: str = "gpt-4",
        action_agent_temperature: float = 0,
        action_agent_task_max_retries: int = 4,
        action_agent_show_chat_log: bool = True,
        action_agent_show_execution_error: bool = True,
        curriculum_agent_model_name: str = "gpt-4",
        curriculum_agent_temperature: float = 0,
        curriculum_agent_qa_model_name: str = "gpt-3.5-turbo",
        curriculum_agent_qa_temperature: float = 0,
        curriculum_agent_warm_up: Dict[str, int] = None,
        curriculum_agent_core_inventory_items: str = r".*_log|.*_planks|stick|crafting_table|furnace"
        r"|cobblestone|dirt|coal|.*_pickaxe|.*_sword|.*_axe",
        curriculum_agent_mode: str = "auto",
        critic_agent_model_name: str = "gpt-4",
        critic_agent_temperature: float = 0,
        critic_agent_mode: str = "auto",
        skill_manager_model_name: str = "gpt-3.5-turbo",
        skill_manager_temperature: float = 0,
        skill_manager_retrieval_top_k: int = 5,
        openai_api_request_timeout: int = 240,
        ckpt_dir: str = "ckpt",
        skill_library_dir: str = None,
        resume: bool = False,
    ):
        """
        The main class for Voyager.
        Action agent is the iterative prompting mechanism in paper.
        Curriculum agent is the automatic curriculum in paper.
        Critic agent is the self-verification in paper.
        Skill manager is the skill library in paper.
        :param mc_port: minecraft in-game port
        :param azure_login: minecraft login config
        :param server_port: mineflayer port
        :param openai_api_key: openai api key
        :param env_wait_ticks: how many ticks at the end each step will wait, if you found some chat log missing,
        you should increase this value
        :param env_request_timeout: how many seconds to wait for each step, if the code execution exceeds this time,
        python side will terminate the connection and need to be resumed
        :param reset_placed_if_failed: whether to reset placed blocks if failed, useful for building task
        :param action_agent_model_name: action agent model name
        :param action_agent_temperature: action agent temperature
        :param action_agent_task_max_retries: how many times to retry if failed
        :param curriculum_agent_model_name: curriculum agent model name
        :param curriculum_agent_temperature: curriculum agent temperature
        :param curriculum_agent_qa_model_name: curriculum agent qa model name
        :param curriculum_agent_qa_temperature: curriculum agent qa temperature
        :param curriculum_agent_warm_up: info will show in curriculum human message
        if completed task larger than the value in dict, available keys are:
        {
            "context": int,
            "biome": int,
            "time": int,
            "other_blocks": int,
            "nearby_entities": int,
            "health": int,
            "hunger": int,
            "position": int,
            "equipment": int,
            "chests": int,
            "optional_inventory_items": int,
        }
        :param curriculum_agent_core_inventory_items: only show these items in inventory before optional_inventory_items
        reached in warm up
        :param curriculum_agent_mode: "auto" for automatic curriculum, "manual" for human curriculum
        :param critic_agent_model_name: critic agent model name
        :param critic_agent_temperature: critic agent temperature
        :param critic_agent_mode: "auto" for automatic critic ,"manual" for human critic
        :param skill_manager_model_name: skill manager model name
        :param skill_manager_temperature: skill manager temperature
        :param skill_manager_retrieval_top_k: how many skills to retrieve for each task
        :param openai_api_request_timeout: how many seconds to wait for openai api
        :param ckpt_dir: checkpoint dir
        :param skill_library_dir: skill library dir
        :param resume: whether to resume from checkpoint
        """
        # init env
        self.env = VoyagerEnv(
            mc_port=mc_port,
            azure_login=azure_login,
            server_port=server_port,
            request_timeout=env_request_timeout,
        )
        self.env_wait_ticks = env_wait_ticks
        self.reset_placed_if_failed = reset_placed_if_failed
        self.max_iterations = max_iterations

        # set openai api key
        os.environ["OPENAI_API_KEY"] = openai_api_key

        # init agents
        self.action_agent = ActionAgent(
            model_name=action_agent_model_name,
            temperature=action_agent_temperature,
            request_timout=openai_api_request_timeout,
            ckpt_dir=ckpt_dir,
            resume=resume,
            chat_log=action_agent_show_chat_log,
            execution_error=action_agent_show_execution_error,
        )
        self.action_agent_task_max_retries = action_agent_task_max_retries
        self.curriculum_agent = CurriculumAgent(
            model_name=curriculum_agent_model_name,
            temperature=curriculum_agent_temperature,
            qa_model_name=curriculum_agent_qa_model_name,
            qa_temperature=curriculum_agent_qa_temperature,
            request_timout=openai_api_request_timeout,
            ckpt_dir=ckpt_dir,
            resume=resume,
            mode=curriculum_agent_mode,
            warm_up=curriculum_agent_warm_up,
            core_inventory_items=curriculum_agent_core_inventory_items,
        )
        self.critic_agent = CriticAgent(
            model_name=critic_agent_model_name,
            temperature=critic_agent_temperature,
            request_timout=openai_api_request_timeout,
            mode=critic_agent_mode,
        )
        self.skill_manager = SkillManager(
            model_name=skill_manager_model_name,
            temperature=skill_manager_temperature,
            retrieval_top_k=skill_manager_retrieval_top_k,
            request_timout=openai_api_request_timeout,
            ckpt_dir=skill_library_dir if skill_library_dir else ckpt_dir,
            resume=True if resume or skill_library_dir else False,
        )
        self.recorder = U.EventRecorder(ckpt_dir=ckpt_dir, resume=resume)
        self.resume = resume

        # init variables for rollout
        self.action_agent_rollout_num_iter = -1
        self.task = None
        self.context = ""
        self.messages = None
        self.conversations = []
        self.last_events = None

    def reset(self, task, context="", reset_env=True):
        self.action_agent_rollout_num_iter = 0
        self.task = task
        self.context = context
        if reset_env:
            self.env.reset(
                options={
                    "mode": "soft",
                    "wait_ticks": self.env_wait_ticks,
                }
            )
        difficulty = (
            "easy" if len(self.curriculum_agent.completed_tasks) > 15 else "peaceful"
        )
        # step to peek an observation
        events = self.env.step(
            "bot.chat(`/time set ${getNextTime()}`);\n"
            + f"bot.chat('/difficulty {difficulty}');"
        )
        skills = self.skill_manager.retrieve_skills(query=self.context)
        print(
            f"\033[33mRender Action Agent system message with {len(skills)} skills\033[0m"
        )
        system_message = self.action_agent.render_system_message(skills=skills)
        human_message = self.action_agent.render_human_message(
            events=events, code="", task=self.task, context=context, critique=""
        )
        self.messages = [system_message, human_message]
        print(
            f"\033[32m****Action Agent human message****\n{human_message.content}\033[0m"
        )
        assert len(self.messages) == 2
        self.conversations = []
        return self.messages

    def close(self):
        self.env.close()

    def step(self):
        if self.action_agent_rollout_num_iter < 0:
            raise ValueError("Agent must be reset before stepping")
        ai_message = self.action_agent.llm(self.messages)
        print(f"\033[34m****Action Agent ai message****\n{ai_message.content}\033[0m")
        self.conversations.append(
            (self.messages[0].content, self.messages[1].content, ai_message.content)
        )
        parsed_result = self.action_agent.process_ai_message(message=ai_message)
        success = False
        if isinstance(parsed_result, dict):
            code = parsed_result["program_code"] + "\n" + parsed_result["exec_code"]
            events = self.env.step(
                code,
                programs=self.skill_manager.programs,
            )
            self.recorder.record(events, self.task)
            self.action_agent.update_chest_memory(events[-1][1]["nearbyChests"])
            success, critique = self.critic_agent.check_task_success(
                events=events,
                task=self.task,
                context=self.context,
                chest_observation=self.action_agent.render_chest_observation(),
                max_retries=5,
            )

            if self.reset_placed_if_failed and not success:
                # revert all the placing event in the last step
                blocks = []
                positions = []
                for event_type, event in events:
                    if event_type == "onSave" and event["onSave"].endswith("_placed"):
                        block = event["onSave"].split("_placed")[0]
                        position = event["status"]["position"]
                        blocks.append(block)
                        positions.append(position)
                new_events = self.env.step(
                    f"await givePlacedItemBack(bot, {U.json_dumps(blocks)}, {U.json_dumps(positions)})",
                    programs=self.skill_manager.programs,
                )
                events[-1][1]["inventory"] = new_events[-1][1]["inventory"]
                events[-1][1]["voxels"] = new_events[-1][1]["voxels"]
            new_skills = self.skill_manager.retrieve_skills(
                query=self.context
                + "\n\n"
                + self.action_agent.summarize_chatlog(events)
            )
            system_message = self.action_agent.render_system_message(skills=new_skills)
            human_message = self.action_agent.render_human_message(
                events=events,
                code=parsed_result["program_code"],
                task=self.task,
                context=self.context,
                critique=critique,
            )
            self.last_events = copy.deepcopy(events)
            self.messages = [system_message, human_message]
        else:
            assert isinstance(parsed_result, str)
            self.recorder.record([], self.task)
            print(f"\033[34m{parsed_result} Trying again!\033[0m")
        assert len(self.messages) == 2
        self.action_agent_rollout_num_iter += 1
        done = (
            self.action_agent_rollout_num_iter >= self.action_agent_task_max_retries
            or success
        )
        info = {
            "task": self.task,
            "success": success,
            "conversations": self.conversations,
        }
        if success:
            assert (
                "program_code" in parsed_result and "program_name" in parsed_result
            ), "program and program_name must be returned when success"
            info["program_code"] = parsed_result["program_code"]
            info["program_name"] = parsed_result["program_name"]
        else:
            print(
                f"\033[32m****Action Agent human message****\n{self.messages[-1].content}\033[0m"
            )
        return self.messages, 0, done, info

    def rollout(self, *, task, context, reset_env=True):
        self.reset(task=task, context=context, reset_env=reset_env)
        while True:
            messages, reward, done, info = self.step()
            if done:
                break
        return messages, reward, done, info

    def learn(self, reset_env=True):
        if self.resume:
            # keep the inventory
            self.env.reset(
                options={
                    "mode": "soft",
                    "wait_ticks": self.env_wait_ticks,
                }
            )
        else:
            # clear the inventory
            self.env.reset(
                options={
                    "mode": "hard",
                    "wait_ticks": self.env_wait_ticks,
                }
            )
            self.resume = True
        self.last_events = self.env.step("")

        while True:
            if self.recorder.iteration > self.max_iterations:
                print("Iteration limit reached")
                break
            task, context = self.curriculum_agent.propose_next_task(
                events=self.last_events,
                chest_observation=self.action_agent.render_chest_observation(),
                max_retries=5,
            )
            print(
                f"\033[35mStarting task {task} for at most {self.action_agent_task_max_retries} times\033[0m"
            )
            try:
                messages, reward, done, info = self.rollout(
                    task=task,
                    context=context,
                    reset_env=reset_env,
                )
            except Exception as e:
                time.sleep(3)  # wait for mineflayer to exit
                info = {
                    "task": task,
                    "success": False,
                }
                # reset bot status here
                self.last_events = self.env.reset(
                    options={
                        "mode": "hard",
                        "wait_ticks": self.env_wait_ticks,
                        "inventory": self.last_events[-1][1]["inventory"],
                        "equipment": self.last_events[-1][1]["status"]["equipment"],
                        "position": self.last_events[-1][1]["status"]["position"],
                    }
                )
                # use red color background to print the error
                print("Your last round rollout terminated due to error:")
                print(f"\033[41m{e}\033[0m")

            if info["success"]:
                self.skill_manager.add_new_skill(info)

            self.curriculum_agent.update_exploration_progress(info)
            print(
                f"\033[35mCompleted tasks: {', '.join(self.curriculum_agent.completed_tasks)}\033[0m"
            )
            print(
                f"\033[35mFailed tasks: {', '.join(self.curriculum_agent.failed_tasks)}\033[0m"
            )

        return {
            "completed_tasks": self.curriculum_agent.completed_tasks,
            "failed_tasks": self.curriculum_agent.failed_tasks,
            "skills": self.skill_manager.skills,
        }

    def decompose_task(self, task):
        if not self.last_events:
            self.last_events = self.env.reset(
                options={
                    "mode": "hard",
                    "wait_ticks": self.env_wait_ticks,
                }
            )
        return self.curriculum_agent.decompose_task(task, self.last_events)

    def inference(self, task=None, sub_goals=[], reset_mode="hard", reset_env=True):
        if not task and not sub_goals:
            raise ValueError("Either task or sub_goals must be provided")
        if not sub_goals:
            sub_goals = self.decompose_task(task)
        self.env.reset(
            options={
                "mode": reset_mode,
                "wait_ticks": self.env_wait_ticks,
            }
        )
        self.curriculum_agent.completed_tasks = []
        self.curriculum_agent.failed_tasks = []
        self.last_events = self.env.step("")
        while self.curriculum_agent.progress < len(sub_goals):
            next_task = sub_goals[self.curriculum_agent.progress]
            context = self.curriculum_agent.get_task_context(next_task)
            print(
                f"\033[35mStarting task {next_task} for at most {self.action_agent_task_max_retries} times\033[0m"
            )
            messages, reward, done, info = self.rollout(
                task=next_task,
                context=context,
                reset_env=reset_env,
            )
            self.curriculum_agent.update_exploration_progress(info)
            print(
                f"\033[35mCompleted tasks: {', '.join(self.curriculum_agent.completed_tasks)}\033[0m"
            )
            print(
                f"\033[35mFailed tasks: {', '.join(self.curriculum_agent.failed_tasks)}\033[0m"
            )



================================================
FILE: voyager/agents/__init__.py
================================================
from .action import ActionAgent
from .critic import CriticAgent
from .curriculum import CurriculumAgent
from .skill import SkillManager



================================================
FILE: voyager/agents/action.py
================================================
import re
import time

import voyager.utils as U
from javascript import require
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from voyager.prompts import load_prompt
from voyager.control_primitives_context import load_control_primitives_context


class ActionAgent:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        temperature=0,
        request_timout=120,
        ckpt_dir="ckpt",
        resume=False,
        chat_log=True,
        execution_error=True,
    ):
        self.ckpt_dir = ckpt_dir
        self.chat_log = chat_log
        self.execution_error = execution_error
        U.f_mkdir(f"{ckpt_dir}/action")
        if resume:
            print(f"\033[32mLoading Action Agent from {ckpt_dir}/action\033[0m")
            self.chest_memory = U.load_json(f"{ckpt_dir}/action/chest_memory.json")
        else:
            self.chest_memory = {}
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        )

    def update_chest_memory(self, chests):
        for position, chest in chests.items():
            if position in self.chest_memory:
                if isinstance(chest, dict):
                    self.chest_memory[position] = chest
                if chest == "Invalid":
                    print(
                        f"\033[32mAction Agent removing chest {position}: {chest}\033[0m"
                    )
                    self.chest_memory.pop(position)
            else:
                if chest != "Invalid":
                    print(f"\033[32mAction Agent saving chest {position}: {chest}\033[0m")
                    self.chest_memory[position] = chest
        U.dump_json(self.chest_memory, f"{self.ckpt_dir}/action/chest_memory.json")

    def render_chest_observation(self):
        chests = []
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, dict) and len(chest) > 0:
                chests.append(f"{chest_position}: {chest}")
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, dict) and len(chest) == 0:
                chests.append(f"{chest_position}: Empty")
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, str):
                assert chest == "Unknown"
                chests.append(f"{chest_position}: Unknown items inside")
        assert len(chests) == len(self.chest_memory)
        if chests:
            chests = "\n".join(chests)
            return f"Chests:\n{chests}\n\n"
        else:
            return f"Chests: None\n\n"

    def render_system_message(self, skills=[]):
        system_template = load_prompt("action_template")
        # FIXME: Hardcoded control_primitives
        base_skills = [
            "exploreUntil",
            "mineBlock",
            "craftItem",
            "placeItem",
            "smeltItem",
            "killMob",
        ]
        if not self.llm.model_name == "gpt-3.5-turbo":
            base_skills += [
                "useChest",
                "mineflayer",
            ]
        programs = "\n\n".join(load_control_primitives_context(base_skills) + skills)
        response_format = load_prompt("action_response_format")
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            system_template
        )
        system_message = system_message_prompt.format(
            programs=programs, response_format=response_format
        )
        assert isinstance(system_message, SystemMessage)
        return system_message

    def render_human_message(
        self, *, events, code="", task="", context="", critique=""
    ):
        chat_messages = []
        error_messages = []
        # FIXME: damage_messages is not used
        damage_messages = []
        assert events[-1][0] == "observe", "Last event must be observe"
        for i, (event_type, event) in enumerate(events):
            if event_type == "onChat":
                chat_messages.append(event["onChat"])
            elif event_type == "onError":
                error_messages.append(event["onError"])
            elif event_type == "onDamage":
                damage_messages.append(event["onDamage"])
            elif event_type == "observe":
                biome = event["status"]["biome"]
                time_of_day = event["status"]["timeOfDay"]
                voxels = event["voxels"]
                entities = event["status"]["entities"]
                health = event["status"]["health"]
                hunger = event["status"]["food"]
                position = event["status"]["position"]
                equipment = event["status"]["equipment"]
                inventory_used = event["status"]["inventoryUsed"]
                inventory = event["inventory"]
                assert i == len(events) - 1, "observe must be the last event"

        observation = ""

        if code:
            observation += f"Code from the last round:\n{code}\n\n"
        else:
            observation += f"Code from the last round: No code in the first round\n\n"

        if self.execution_error:
            if error_messages:
                error = "\n".join(error_messages)
                observation += f"Execution error:\n{error}\n\n"
            else:
                observation += f"Execution error: No error\n\n"

        if self.chat_log:
            if chat_messages:
                chat_log = "\n".join(chat_messages)
                observation += f"Chat log: {chat_log}\n\n"
            else:
                observation += f"Chat log: None\n\n"

        observation += f"Biome: {biome}\n\n"

        observation += f"Time: {time_of_day}\n\n"

        if voxels:
            observation += f"Nearby blocks: {', '.join(voxels)}\n\n"
        else:
            observation += f"Nearby blocks: None\n\n"

        if entities:
            nearby_entities = [
                k for k, v in sorted(entities.items(), key=lambda x: x[1])
            ]
            observation += f"Nearby entities (nearest to farthest): {', '.join(nearby_entities)}\n\n"
        else:
            observation += f"Nearby entities (nearest to farthest): None\n\n"

        observation += f"Health: {health:.1f}/20\n\n"

        observation += f"Hunger: {hunger:.1f}/20\n\n"

        observation += f"Position: x={position['x']:.1f}, y={position['y']:.1f}, z={position['z']:.1f}\n\n"

        observation += f"Equipment: {equipment}\n\n"

        if inventory:
            observation += f"Inventory ({inventory_used}/36): {inventory}\n\n"
        else:
            observation += f"Inventory ({inventory_used}/36): Empty\n\n"

        if not (
            task == "Place and deposit useless items into a chest"
            or task.startswith("Deposit useless items into the chest at")
        ):
            observation += self.render_chest_observation()

        observation += f"Task: {task}\n\n"

        if context:
            observation += f"Context: {context}\n\n"
        else:
            observation += f"Context: None\n\n"

        if critique:
            observation += f"Critique: {critique}\n\n"
        else:
            observation += f"Critique: None\n\n"

        return HumanMessage(content=observation)

    def process_ai_message(self, message):
        assert isinstance(message, AIMessage)

        retry = 3
        error = None
        while retry > 0:
            try:
                babel = require("@babel/core")
                babel_generator = require("@babel/generator").default

                code_pattern = re.compile(r"```(?:javascript|js)(.*?)```", re.DOTALL)
                code = "\n".join(code_pattern.findall(message.content))
                parsed = babel.parse(code)
                functions = []
                assert len(list(parsed.program.body)) > 0, "No functions found"
                for i, node in enumerate(parsed.program.body):
                    if node.type != "FunctionDeclaration":
                        continue
                    node_type = (
                        "AsyncFunctionDeclaration"
                        if node["async"]
                        else "FunctionDeclaration"
                    )
                    functions.append(
                        {
                            "name": node.id.name,
                            "type": node_type,
                            "body": babel_generator(node).code,
                            "params": list(node["params"]),
                        }
                    )
                # find the last async function
                main_function = None
                for function in reversed(functions):
                    if function["type"] == "AsyncFunctionDeclaration":
                        main_function = function
                        break
                assert (
                    main_function is not None
                ), "No async function found. Your main function must be async."
                assert (
                    len(main_function["params"]) == 1
                    and main_function["params"][0].name == "bot"
                ), f"Main function {main_function['name']} must take a single argument named 'bot'"
                program_code = "\n\n".join(function["body"] for function in functions)
                exec_code = f"await {main_function['name']}(bot);"
                return {
                    "program_code": program_code,
                    "program_name": main_function["name"],
                    "exec_code": exec_code,
                }
            except Exception as e:
                retry -= 1
                error = e
                time.sleep(1)
        return f"Error parsing action response (before program execution): {error}"

    def summarize_chatlog(self, events):
        def filter_item(message: str):
            craft_pattern = r"I cannot make \w+ because I need: (.*)"
            craft_pattern2 = (
                r"I cannot make \w+ because there is no crafting table nearby"
            )
            mine_pattern = r"I need at least a (.*) to mine \w+!"
            if re.match(craft_pattern, message):
                return re.match(craft_pattern, message).groups()[0]
            elif re.match(craft_pattern2, message):
                return "a nearby crafting table"
            elif re.match(mine_pattern, message):
                return re.match(mine_pattern, message).groups()[0]
            else:
                return ""

        chatlog = set()
        for event_type, event in events:
            if event_type == "onChat":
                item = filter_item(event["onChat"])
                if item:
                    chatlog.add(item)
        return "I also need " + ", ".join(chatlog) + "." if chatlog else ""



================================================
FILE: voyager/agents/critic.py
================================================
from voyager.prompts import load_prompt
from voyager.utils.json_utils import fix_and_parse_json
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


class CriticAgent:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        temperature=0,
        request_timout=120,
        mode="auto",
    ):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        )
        assert mode in ["auto", "manual"]
        self.mode = mode

    def render_system_message(self):
        system_message = SystemMessage(content=load_prompt("critic"))
        return system_message

    def render_human_message(self, *, events, task, context, chest_observation):
        assert events[-1][0] == "observe", "Last event must be observe"
        biome = events[-1][1]["status"]["biome"]
        time_of_day = events[-1][1]["status"]["timeOfDay"]
        voxels = events[-1][1]["voxels"]
        health = events[-1][1]["status"]["health"]
        hunger = events[-1][1]["status"]["food"]
        position = events[-1][1]["status"]["position"]
        equipment = events[-1][1]["status"]["equipment"]
        inventory_used = events[-1][1]["status"]["inventoryUsed"]
        inventory = events[-1][1]["inventory"]

        for i, (event_type, event) in enumerate(events):
            if event_type == "onError":
                print(f"\033[31mCritic Agent: Error occurs {event['onError']}\033[0m")
                return None

        observation = ""

        observation += f"Biome: {biome}\n\n"

        observation += f"Time: {time_of_day}\n\n"

        if voxels:
            observation += f"Nearby blocks: {', '.join(voxels)}\n\n"
        else:
            observation += f"Nearby blocks: None\n\n"

        observation += f"Health: {health:.1f}/20\n\n"
        observation += f"Hunger: {hunger:.1f}/20\n\n"

        observation += f"Position: x={position['x']:.1f}, y={position['y']:.1f}, z={position['z']:.1f}\n\n"

        observation += f"Equipment: {equipment}\n\n"

        if inventory:
            observation += f"Inventory ({inventory_used}/36): {inventory}\n\n"
        else:
            observation += f"Inventory ({inventory_used}/36): Empty\n\n"

        observation += chest_observation

        observation += f"Task: {task}\n\n"

        if context:
            observation += f"Context: {context}\n\n"
        else:
            observation += f"Context: None\n\n"

        print(f"\033[31m****Critic Agent human message****\n{observation}\033[0m")
        return HumanMessage(content=observation)

    def human_check_task_success(self):
        confirmed = False
        success = False
        critique = ""
        while not confirmed:
            success = input("Success? (y/n)")
            success = success.lower() == "y"
            critique = input("Enter your critique:")
            print(f"Success: {success}\nCritique: {critique}")
            confirmed = input("Confirm? (y/n)") in ["y", ""]
        return success, critique

    def ai_check_task_success(self, messages, max_retries=5):
        if max_retries == 0:
            print(
                "\033[31mFailed to parse Critic Agent response. Consider updating your prompt.\033[0m"
            )
            return False, ""

        if messages[1] is None:
            return False, ""

        critic = self.llm(messages).content
        print(f"\033[31m****Critic Agent ai message****\n{critic}\033[0m")
        try:
            response = fix_and_parse_json(critic)
            assert response["success"] in [True, False]
            if "critique" not in response:
                response["critique"] = ""
            return response["success"], response["critique"]
        except Exception as e:
            print(f"\033[31mError parsing critic response: {e} Trying again!\033[0m")
            return self.ai_check_task_success(
                messages=messages,
                max_retries=max_retries - 1,
            )

    def check_task_success(
        self, *, events, task, context, chest_observation, max_retries=5
    ):
        human_message = self.render_human_message(
            events=events,
            task=task,
            context=context,
            chest_observation=chest_observation,
        )

        messages = [
            self.render_system_message(),
            human_message,
        ]

        if self.mode == "manual":
            return self.human_check_task_success()
        elif self.mode == "auto":
            return self.ai_check_task_success(
                messages=messages, max_retries=max_retries
            )
        else:
            raise ValueError(f"Invalid critic agent mode: {self.mode}")



================================================
FILE: voyager/agents/curriculum.py
================================================
from __future__ import annotations

import random
import re

import voyager.utils as U
from voyager.prompts import load_prompt
from voyager.utils.json_utils import fix_and_parse_json
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import HumanMessage, SystemMessage
from langchain.vectorstores import Chroma


class CurriculumAgent:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        temperature=0,
        qa_model_name="gpt-3.5-turbo",
        qa_temperature=0,
        request_timout=120,
        ckpt_dir="ckpt",
        resume=False,
        mode="auto",
        warm_up=None,
        core_inventory_items: str | None = None,
    ):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        )
        self.qa_llm = ChatOpenAI(
            model_name=qa_model_name,
            temperature=qa_temperature,
            request_timeout=request_timout,
        )
        assert mode in [
            "auto",
            "manual",
        ], f"mode {mode} not supported"
        self.mode = mode
        self.ckpt_dir = ckpt_dir
        U.f_mkdir(f"{ckpt_dir}/curriculum/vectordb")
        if resume:
            print(f"\033[35mLoading Curriculum Agent from {ckpt_dir}/curriculum\033[0m")
            self.completed_tasks = U.load_json(
                f"{ckpt_dir}/curriculum/completed_tasks.json"
            )
            self.failed_tasks = U.load_json(f"{ckpt_dir}/curriculum/failed_tasks.json")
            self.qa_cache = U.load_json(f"{ckpt_dir}/curriculum/qa_cache.json")
        else:
            self.completed_tasks = []
            self.failed_tasks = []
            self.qa_cache = {}
        # vectordb for qa cache
        self.qa_cache_questions_vectordb = Chroma(
            collection_name="qa_cache_questions_vectordb",
            embedding_function=OpenAIEmbeddings(),
            persist_directory=f"{ckpt_dir}/curriculum/vectordb",
        )
        assert self.qa_cache_questions_vectordb._collection.count() == len(
            self.qa_cache
        ), (
            f"Curriculum Agent's qa cache question vectordb is not synced with qa_cache.json.\n"
            f"There are {self.qa_cache_questions_vectordb._collection.count()} questions in vectordb "
            f"but {len(self.qa_cache)} questions in qa_cache.json.\n"
            f"Did you set resume=False when initializing the agent?\n"
            f"You may need to manually delete the qa cache question vectordb directory for running from scratch.\n"
        )
        # if warm up not defined, initialize it as a dict, else, initialize all the missing value as a default value
        if not warm_up:
            warm_up = self.default_warmup
        self.warm_up = {}
        if "optional_inventory_items" in warm_up:
            assert core_inventory_items is not None
            self._core_inv_items_regex = re.compile(core_inventory_items)
            self.warm_up["optional_inventory_items"] = warm_up[
                "optional_inventory_items"
            ]
        else:
            self.warm_up["optional_inventory_items"] = 0
        for key in self.curriculum_observations:
            self.warm_up[key] = warm_up.get(key, self.default_warmup[key])
        self.warm_up["nearby_blocks"] = 0
        self.warm_up["inventory"] = 0
        self.warm_up["completed_tasks"] = 0
        self.warm_up["failed_tasks"] = 0

    @property
    def default_warmup(self):
        return {
            "context": 15,
            "biome": 10,
            "time": 15,
            "nearby_blocks": 0,
            "other_blocks": 10,
            "nearby_entities": 5,
            "health": 15,
            "hunger": 15,
            "position": 0,
            "equipment": 0,
            "inventory": 0,
            "optional_inventory_items": 7,
            "chests": 0,
            "completed_tasks": 0,
            "failed_tasks": 0,
        }

    @property
    def curriculum_observations(self):
        return [
            "context",
            "biome",
            "time",
            "nearby_blocks",
            "other_blocks",
            "nearby_entities",
            "health",
            "hunger",
            "position",
            "equipment",
            "inventory",
            "chests",
            "completed_tasks",
            "failed_tasks",
        ]

    @property
    def progress(self):
        return len(self.completed_tasks)

    def render_system_message(self):
        system_message = SystemMessage(content=load_prompt("curriculum"))
        assert isinstance(system_message, SystemMessage)
        return system_message

    def render_observation(self, *, events, chest_observation):
        assert events[-1][0] == "observe", "Last event must be observe"
        event = events[-1][1]
        biome = event["status"]["biome"]
        time_of_day = event["status"]["timeOfDay"]
        voxels = event["voxels"]
        block_records = event["blockRecords"]
        entities = event["status"]["entities"]
        health = event["status"]["health"]
        hunger = event["status"]["food"]
        position = event["status"]["position"]
        equipment = event["status"]["equipment"]
        inventory_used = event["status"]["inventoryUsed"]
        inventory = event["inventory"]

        if not any(
            "dirt" in block
            or "log" in block
            or "grass" in block
            or "sand" in block
            or "snow" in block
            for block in voxels
        ):
            biome = "underground"

        other_blocks = ", ".join(
            list(
                set(block_records).difference(set(voxels).union(set(inventory.keys())))
            )
        )

        other_blocks = other_blocks if other_blocks else "None"

        nearby_entities = (
            ", ".join([k for k, v in sorted(entities.items(), key=lambda x: x[1])])
            if entities
            else "None"
        )

        completed_tasks = (
            ", ".join(self.completed_tasks) if self.completed_tasks else "None"
        )
        failed_tasks = ", ".join(self.failed_tasks) if self.failed_tasks else "None"

        # filter out optional inventory items if required
        if self.progress < self.warm_up["optional_inventory_items"]:
            inventory = {
                k: v
                for k, v in inventory.items()
                if self._core_inv_items_regex.search(k) is not None
            }

        observation = {
            "context": "",
            "biome": f"Biome: {biome}\n\n",
            "time": f"Time: {time_of_day}\n\n",
            "nearby_blocks": f"Nearby blocks: {', '.join(voxels) if voxels else 'None'}\n\n",
            "other_blocks": f"Other blocks that are recently seen: {other_blocks}\n\n",
            "nearby_entities": f"Nearby entities: {nearby_entities}\n\n",
            "health": f"Health: {health:.1f}/20\n\n",
            "hunger": f"Hunger: {hunger:.1f}/20\n\n",
            "position": f"Position: x={position['x']:.1f}, y={position['y']:.1f}, z={position['z']:.1f}\n\n",
            "equipment": f"Equipment: {equipment}\n\n",
            "inventory": f"Inventory ({inventory_used}/36): {inventory if inventory else 'Empty'}\n\n",
            "chests": chest_observation,
            "completed_tasks": f"Completed tasks so far: {completed_tasks}\n\n",
            "failed_tasks": f"Failed tasks that are too hard: {failed_tasks}\n\n",
        }
        return observation

    def render_human_message(self, *, events, chest_observation):
        content = ""
        observation = self.render_observation(
            events=events, chest_observation=chest_observation
        )
        if self.progress >= self.warm_up["context"]:
            questions, answers = self.run_qa(
                events=events, chest_observation=chest_observation
            )
            i = 1
            for question, answer in zip(questions, answers):
                if "Answer: Unknown" in answer or "language model" in answer:
                    continue
                observation["context"] += f"Question {i}: {question}\n"
                observation["context"] += f"{answer}\n\n"
                i += 1
                if i > 5:
                    break

        for key in self.curriculum_observations:
            if self.progress >= self.warm_up[key]:
                if self.warm_up[key] != 0:
                    should_include = random.random() < 0.8
                else:
                    should_include = True
                if should_include:
                    content += observation[key]

        print(f"\033[35m****Curriculum Agent human message****\n{content}\033[0m")
        return HumanMessage(content=content)

    def propose_next_task(self, *, events, chest_observation, max_retries=5):
        if self.progress == 0 and self.mode == "auto":
            task = "Mine 1 wood log"
            context = "You can mine one of oak, birch, spruce, jungle, acacia, dark oak, or mangrove logs."
            return task, context

        # hard code task when inventory is almost full
        inventoryUsed = events[-1][1]["status"]["inventoryUsed"]
        if inventoryUsed >= 33:
            if chest_observation != "Chests: None\n\n":
                chests = chest_observation[8:-2].split("\n")
                for chest in chests:
                    content = chest.split(":")[1]
                    if content == " Unknown items inside" or content == " Empty":
                        position = chest.split(":")[0]
                        task = f"Deposit useless items into the chest at {position}"
                        context = (
                            f"Your inventory have {inventoryUsed} occupied slots before depositing. "
                            "After depositing, your inventory should only have 20 occupied slots. "
                            "You should deposit useless items such as andesite, dirt, cobblestone, etc. "
                            "Also, you can deposit low-level tools, "
                            "For example, if you have a stone pickaxe, you can deposit a wooden pickaxe. "
                            "Make sure the list of useless items are in your inventory "
                            "(do not list items already in the chest), "
                            "You can use bot.inventoryUsed() to check how many inventory slots are used."
                        )
                        return task, context
            if "chest" in events[-1][1]["inventory"]:
                task = "Place a chest"
                context = (
                    f"You have a chest in inventory, place it around you. "
                    f"If chests is not None, or nearby blocks contains chest, this task is success."
                )
            else:
                task = "Craft 1 chest"
                context = "Craft 1 chest with 8 planks of any kind of wood."
            return task, context

        messages = [
            self.render_system_message(),
            self.render_human_message(
                events=events, chest_observation=chest_observation
            ),
        ]

        if self.mode == "auto":
            return self.propose_next_ai_task(messages=messages, max_retries=max_retries)
        elif self.mode == "manual":
            return self.propose_next_manual_task()
        else:
            raise ValueError(f"Invalid curriculum agent mode: {self.mode}")

    def propose_next_ai_task(self, *, messages, max_retries=5):
        if max_retries == 0:
            raise RuntimeError("Max retries reached, failed to propose ai task.")
        curriculum = self.llm(messages).content
        print(f"\033[31m****Curriculum Agent ai message****\n{curriculum}\033[0m")
        try:
            response = self.parse_ai_message(curriculum)
            assert "next_task" in response
            context = self.get_task_context(response["next_task"])
            return response["next_task"], context
        except Exception as e:
            print(
                f"\033[35mError parsing curriculum response: {e}. Trying again!\033[0m"
            )
            return self.propose_next_ai_task(
                messages=messages,
                max_retries=max_retries - 1,
            )

    def parse_ai_message(self, message):
        task = ""
        for line in message.split("\n"):
            if line.startswith("Task:"):
                task = line[5:].replace(".", "").strip()
        assert task, "Task not found in Curriculum Agent response"
        return {"next_task": task}

    def propose_next_manual_task(self):
        confirmed = False
        task, context = "", ""
        while not confirmed:
            task = input("Enter task: ")
            context = input("Enter context: ")
            print(f"Task: {task}\nContext: {context}")
            confirmed = input("Confirm? (y/n)").lower() in ["y", ""]
        return task, context

    def update_exploration_progress(self, info):
        task = info["task"]
        if task.startswith("Deposit useless items into the chest at"):
            # No need to record the deposit task
            return
        if info["success"]:
            print(f"\033[35mCompleted task {task}.\033[0m")
            self.completed_tasks.append(task)
        else:
            print(
                f"\033[35mFailed to complete task {task}. Skipping to next task.\033[0m"
            )
            self.failed_tasks.append(task)

        # clean up tasks and dump to disk
        self.clean_up_tasks()

    def clean_up_tasks(self):
        updated_completed_tasks = []
        # record repeated failed tasks
        updated_failed_tasks = self.failed_tasks
        # dedup but keep order
        for task in self.completed_tasks:
            if task not in updated_completed_tasks:
                updated_completed_tasks.append(task)

        # remove completed tasks from failed tasks
        for task in updated_completed_tasks:
            while task in updated_failed_tasks:
                updated_failed_tasks.remove(task)

        self.completed_tasks = updated_completed_tasks
        self.failed_tasks = updated_failed_tasks

        # dump to json
        U.dump_json(
            self.completed_tasks, f"{self.ckpt_dir}/curriculum/completed_tasks.json"
        )
        U.dump_json(self.failed_tasks, f"{self.ckpt_dir}/curriculum/failed_tasks.json")

    def decompose_task(self, task, events):
        messages = [
            SystemMessage(
                content=load_prompt("curriculum_task_decomposition"),
            ),
            self.render_human_message(events=events, chest_observation=""),
            HumanMessage(content=f"Final task: {task}"),
        ]
        print(
            f"\033[31m****Curriculum Agent task decomposition****\nFinal task: {task}\033[0m"
        )
        response = self.llm(messages).content
        print(f"\033[31m****Curriculum Agent task decomposition****\n{response}\033[0m")
        return fix_and_parse_json(response)

    def run_qa(self, *, events, chest_observation):
        questions_new, _ = self.run_qa_step1_ask_questions(
            events=events, chest_observation=chest_observation
        )
        questions = []
        answers = []
        for question in questions_new:
            if self.qa_cache_questions_vectordb._collection.count() > 0:
                docs_and_scores = (
                    self.qa_cache_questions_vectordb.similarity_search_with_score(
                        question, k=1
                    )
                )
                if docs_and_scores and docs_and_scores[0][1] < 0.05:
                    question_cached = docs_and_scores[0][0].page_content
                    assert question_cached in self.qa_cache
                    answer_cached = self.qa_cache[question_cached]
                    questions.append(question_cached)
                    answers.append(answer_cached)
                    continue
            answer = self.run_qa_step2_answer_questions(question=question)
            assert question not in self.qa_cache
            self.qa_cache[question] = answer
            self.qa_cache_questions_vectordb.add_texts(
                texts=[question],
            )
            U.dump_json(self.qa_cache, f"{self.ckpt_dir}/curriculum/qa_cache.json")
            self.qa_cache_questions_vectordb.persist()
            questions.append(question)
            answers.append(answer)
        assert len(questions_new) == len(questions) == len(answers)
        return questions, answers

    def get_task_context(self, task):
        # if include ore in question, gpt will try to use tool with skill touch enhancement to mine
        question = (
            f"How to {task.replace('_', ' ').replace(' ore', '').replace(' ores', '').replace('.', '').strip().lower()}"
            f" in Minecraft?"
        )
        if question in self.qa_cache:
            answer = self.qa_cache[question]
        else:
            answer = self.run_qa_step2_answer_questions(question=question)
            self.qa_cache[question] = answer
            self.qa_cache_questions_vectordb.add_texts(
                texts=[question],
            )
            U.dump_json(self.qa_cache, f"{self.ckpt_dir}/curriculum/qa_cache.json")
            self.qa_cache_questions_vectordb.persist()
        context = f"Question: {question}\n{answer}"
        return context

    def render_system_message_qa_step1_ask_questions(self):
        return SystemMessage(content=load_prompt("curriculum_qa_step1_ask_questions"))

    def render_human_message_qa_step1_ask_questions(self, *, events, chest_observation):
        observation = self.render_observation(
            events=events, chest_observation=chest_observation
        )
        content = ""
        for key in self.curriculum_observations:
            content += observation[key]
        return HumanMessage(content=content)

    def run_qa_step1_ask_questions(self, *, events, chest_observation):
        biome = events[-1][1]["status"]["biome"].replace("_", " ")
        questions = [
            f"What are the blocks that I can find in the {biome} in Minecraft?",
            f"What are the items that I can find in the {biome} in Minecraft?",
            f"What are the mobs that I can find in the {biome} in Minecraft?",
        ]
        concepts = [biome, biome, biome]
        messages = [
            self.render_system_message_qa_step1_ask_questions(),
            self.render_human_message_qa_step1_ask_questions(
                events=events, chest_observation=chest_observation
            ),
        ]
        qa_response = self.qa_llm(messages).content
        try:
            # Regex pattern to extract question and concept pairs
            pattern = r"Question \d+: (.+)\nConcept \d+: (.+)"
            # Extracting all question and concept pairs from the text
            pairs = re.findall(pattern, qa_response)
            # Storing each question and concept in separate lists
            questions_new = [pair[0] for pair in pairs]
            concepts_new = [pair[1] for pair in pairs]
            assert len(questions_new) == len(concepts_new)
            questions.extend(questions_new)
            concepts.extend(concepts_new)
        except Exception as e:
            print(
                f"\033[35mError parsing curriculum response for "
                f"QA step 1 ask questions: {e}.\033[0m"
            )
        return questions, concepts

    def render_system_message_qa_step2_answer_questions(self):
        return SystemMessage(
            content=load_prompt("curriculum_qa_step2_answer_questions")
        )

    def render_human_message_qa_step2_answer_questions(self, question):
        content = f"Question: {question}"
        return HumanMessage(content=content)

    def run_qa_step2_answer_questions(self, question):
        messages = [
            self.render_system_message_qa_step2_answer_questions(),
            self.render_human_message_qa_step2_answer_questions(question=question),
        ]
        print(f"\033[35mCurriculum Agent Question: {question}\033[0m")
        qa_answer = self.qa_llm(messages).content
        print(f"\033[31mCurriculum Agent {qa_answer}\033[0m")
        return qa_answer



================================================
FILE: voyager/agents/skill.py
================================================
import os

import voyager.utils as U
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import HumanMessage, SystemMessage
from langchain.vectorstores import Chroma

from voyager.prompts import load_prompt
from voyager.control_primitives import load_control_primitives


class SkillManager:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        temperature=0,
        retrieval_top_k=5,
        request_timout=120,
        ckpt_dir="ckpt",
        resume=False,
    ):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        )
        U.f_mkdir(f"{ckpt_dir}/skill/code")
        U.f_mkdir(f"{ckpt_dir}/skill/description")
        U.f_mkdir(f"{ckpt_dir}/skill/vectordb")
        # programs for env execution
        self.control_primitives = load_control_primitives()
        if resume:
            print(f"\033[33mLoading Skill Manager from {ckpt_dir}/skill\033[0m")
            self.skills = U.load_json(f"{ckpt_dir}/skill/skills.json")
        else:
            self.skills = {}
        self.retrieval_top_k = retrieval_top_k
        self.ckpt_dir = ckpt_dir
        self.vectordb = Chroma(
            collection_name="skill_vectordb",
            embedding_function=OpenAIEmbeddings(),
            persist_directory=f"{ckpt_dir}/skill/vectordb",
        )
        assert self.vectordb._collection.count() == len(self.skills), (
            f"Skill Manager's vectordb is not synced with skills.json.\n"
            f"There are {self.vectordb._collection.count()} skills in vectordb but {len(self.skills)} skills in skills.json.\n"
            f"Did you set resume=False when initializing the manager?\n"
            f"You may need to manually delete the vectordb directory for running from scratch."
        )

    @property
    def programs(self):
        programs = ""
        for skill_name, entry in self.skills.items():
            programs += f"{entry['code']}\n\n"
        for primitives in self.control_primitives:
            programs += f"{primitives}\n\n"
        return programs

    def add_new_skill(self, info):
        if info["task"].startswith("Deposit useless items into the chest at"):
            # No need to reuse the deposit skill
            return
        program_name = info["program_name"]
        program_code = info["program_code"]
        skill_description = self.generate_skill_description(program_name, program_code)
        print(
            f"\033[33mSkill Manager generated description for {program_name}:\n{skill_description}\033[0m"
        )
        if program_name in self.skills:
            print(f"\033[33mSkill {program_name} already exists. Rewriting!\033[0m")
            self.vectordb._collection.delete(ids=[program_name])
            i = 2
            while f"{program_name}V{i}.js" in os.listdir(f"{self.ckpt_dir}/skill/code"):
                i += 1
            dumped_program_name = f"{program_name}V{i}"
        else:
            dumped_program_name = program_name
        self.vectordb.add_texts(
            texts=[skill_description],
            ids=[program_name],
            metadatas=[{"name": program_name}],
        )
        self.skills[program_name] = {
            "code": program_code,
            "description": skill_description,
        }
        assert self.vectordb._collection.count() == len(
            self.skills
        ), "vectordb is not synced with skills.json"
        U.dump_text(
            program_code, f"{self.ckpt_dir}/skill/code/{dumped_program_name}.js"
        )
        U.dump_text(
            skill_description,
            f"{self.ckpt_dir}/skill/description/{dumped_program_name}.txt",
        )
        U.dump_json(self.skills, f"{self.ckpt_dir}/skill/skills.json")
        self.vectordb.persist()

    def generate_skill_description(self, program_name, program_code):
        messages = [
            SystemMessage(content=load_prompt("skill")),
            HumanMessage(
                content=program_code
                + "\n\n"
                + f"The main function is `{program_name}`."
            ),
        ]
        skill_description = f"    // { self.llm(messages).content}"
        return f"async function {program_name}(bot) {{\n{skill_description}\n}}"

    def retrieve_skills(self, query):
        k = min(self.vectordb._collection.count(), self.retrieval_top_k)
        if k == 0:
            return []
        print(f"\033[33mSkill Manager retrieving for {k} skills\033[0m")
        docs_and_scores = self.vectordb.similarity_search_with_score(query, k=k)
        print(
            f"\033[33mSkill Manager retrieved skills: "
            f"{', '.join([doc.metadata['name'] for doc, _ in docs_and_scores])}\033[0m"
        )
        skills = []
        for doc, _ in docs_and_scores:
            skills.append(self.skills[doc.metadata["name"]]["code"])
        return skills



================================================
FILE: voyager/control_primitives/__init__.py
================================================
import pkg_resources
import os
import voyager.utils as U


def load_control_primitives(primitive_names=None):
    package_path = pkg_resources.resource_filename("voyager", "")
    if primitive_names is None:
        primitive_names = [
            primitives[:-3]
            for primitives in os.listdir(f"{package_path}/control_primitives")
            if primitives.endswith(".js")
        ]
    primitives = [
        U.load_text(f"{package_path}/control_primitives/{primitive_name}.js")
        for primitive_name in primitive_names
    ]
    return primitives



================================================
FILE: voyager/control_primitives/craftHelper.js
================================================
function failedCraftFeedback(bot, name, item, craftingTable) {
    const recipes = bot.recipesAll(item.id, null, craftingTable);
    if (!recipes.length) {
        throw new Error(`No crafting table nearby`);
    } else {
        const recipes = bot.recipesAll(
            item.id,
            null,
            mcData.blocksByName.crafting_table.id
        );
        // find the recipe with the fewest missing ingredients
        var min = 999;
        var min_recipe = null;
        for (const recipe of recipes) {
            const delta = recipe.delta;
            var missing = 0;
            for (const delta_item of delta) {
                if (delta_item.count < 0) {
                    const inventory_item = bot.inventory.findInventoryItem(
                        mcData.items[delta_item.id].name,
                        null
                    );
                    if (!inventory_item) {
                        missing += -delta_item.count;
                    } else {
                        missing += Math.max(
                            -delta_item.count - inventory_item.count,
                            0
                        );
                    }
                }
            }
            if (missing < min) {
                min = missing;
                min_recipe = recipe;
            }
        }
        const delta = min_recipe.delta;
        let message = "";
        for (const delta_item of delta) {
            if (delta_item.count < 0) {
                const inventory_item = bot.inventory.findInventoryItem(
                    mcData.items[delta_item.id].name,
                    null
                );
                if (!inventory_item) {
                    message += ` ${-delta_item.count} more ${
                        mcData.items[delta_item.id].name
                    }, `;
                } else {
                    if (inventory_item.count < -delta_item.count) {
                        message += `${
                            -delta_item.count - inventory_item.count
                        } more ${mcData.items[delta_item.id].name}`;
                    }
                }
            }
        }
        bot.chat(`I cannot make ${name} because I need: ${message}`);
    }
}



================================================
FILE: voyager/control_primitives/craftItem.js
================================================
async function craftItem(bot, name, count = 1) {
    // return if name is not string
    if (typeof name !== "string") {
        throw new Error("name for craftItem must be a string");
    }
    // return if count is not number
    if (typeof count !== "number") {
        throw new Error("count for craftItem must be a number");
    }
    const itemByName = mcData.itemsByName[name];
    if (!itemByName) {
        throw new Error(`No item named ${name}`);
    }
    const craftingTable = bot.findBlock({
        matching: mcData.blocksByName.crafting_table.id,
        maxDistance: 32,
    });
    if (!craftingTable) {
        bot.chat("Craft without a crafting table");
    } else {
        await bot.pathfinder.goto(
            new GoalLookAtBlock(craftingTable.position, bot.world)
        );
    }
    const recipe = bot.recipesFor(itemByName.id, null, 1, craftingTable)[0];
    if (recipe) {
        bot.chat(`I can make ${name}`);
        try {
            await bot.craft(recipe, count, craftingTable);
            bot.chat(`I did the recipe for ${name} ${count} times`);
        } catch (err) {
            bot.chat(`I cannot do the recipe for ${name} ${count} times`);
        }
    } else {
        failedCraftFeedback(bot, name, itemByName, craftingTable);
        _craftItemFailCount++;
        if (_craftItemFailCount > 10) {
            throw new Error(
                "craftItem failed too many times, check chat log to see what happened"
            );
        }
    }
}



================================================
FILE: voyager/control_primitives/exploreUntil.js
================================================
// Explore downward for 60 seconds: exploreUntil(bot, new Vec3(0, -1, 0), 60);
async function exploreUntil(
    bot,
    direction,
    maxTime = 60,
    callback = () => {
        return false;
    }
) {
    if (typeof maxTime !== "number") {
        throw new Error("maxTime must be a number");
    }
    if (typeof callback !== "function") {
        throw new Error("callback must be a function");
    }
    const test = callback();
    if (test) {
        bot.chat("Explore success.");
        return Promise.resolve(test);
    }
    if (direction.x === 0 && direction.y === 0 && direction.z === 0) {
        throw new Error("direction cannot be 0, 0, 0");
    }
    if (
        !(
            (direction.x === 0 || direction.x === 1 || direction.x === -1) &&
            (direction.y === 0 || direction.y === 1 || direction.y === -1) &&
            (direction.z === 0 || direction.z === 1 || direction.z === -1)
        )
    ) {
        throw new Error(
            "direction must be a Vec3 only with value of -1, 0 or 1"
        );
    }
    maxTime = Math.min(maxTime, 1200);
    return new Promise((resolve, reject) => {
        const dx = direction.x;
        const dy = direction.y;
        const dz = direction.z;

        let explorationInterval;
        let maxTimeTimeout;

        const cleanUp = () => {
            clearInterval(explorationInterval);
            clearTimeout(maxTimeTimeout);
            bot.pathfinder.setGoal(null);
        };

        const explore = () => {
            const x =
                bot.entity.position.x +
                Math.floor(Math.random() * 20 + 10) * dx;
            const y =
                bot.entity.position.y +
                Math.floor(Math.random() * 20 + 10) * dy;
            const z =
                bot.entity.position.z +
                Math.floor(Math.random() * 20 + 10) * dz;
            let goal = new GoalNear(x, y, z);
            if (dy === 0) {
                goal = new GoalNearXZ(x, z);
            }
            bot.pathfinder.setGoal(goal);

            try {
                const result = callback();
                if (result) {
                    cleanUp();
                    bot.chat("Explore success.");
                    resolve(result);
                }
            } catch (err) {
                cleanUp();
                reject(err);
            }
        };

        explorationInterval = setInterval(explore, 2000);

        maxTimeTimeout = setTimeout(() => {
            cleanUp();
            bot.chat("Max exploration time reached");
            resolve(null);
        }, maxTime * 1000);
    });
}



================================================
FILE: voyager/control_primitives/givePlacedItemBack.js
================================================
async function givePlacedItemBack(bot, name, position) {
    await bot.chat("/gamerule doTileDrops false");
    // iterate name and position
    const history = [];
    for (let i = 0; i < name.length; i++) {
        await givePlacedItemBackSingle(bot, name[i], position[i]);
    }
    await bot.chat("/gamerule doTileDrops true");

    async function givePlacedItemBackSingle(bot, name, position) {
        bot.chat(`/give bot ${name} 1`);
        const x = Math.floor(position.x);
        const y = Math.floor(position.y);
        const z = Math.floor(position.z);
        // loop through 125 blocks around the block
        const size = 3;
        for (let dx = -size; dx <= size; dx++) {
            for (let dy = -size; dy <= size; dy++) {
                for (let dz = -size; dz <= size; dz++) {
                    const block = bot.blockAt(new Vec3(x + dx, y + dy, z + dz));
                    if (
                        block?.name === name &&
                        !history.includes(block.position)
                    ) {
                        await bot.chat(
                            `/setblock ${x + dx} ${y + dy} ${
                                z + dz
                            } air destroy`
                        );
                        history.push(block.position);
                        await bot.waitForTicks(20);
                        return;
                    }
                }
            }
        }
    }
}



================================================
FILE: voyager/control_primitives/killMob.js
================================================
async function killMob(bot, mobName, timeout = 300) {
    // return if mobName is not string
    if (typeof mobName !== "string") {
        throw new Error(`mobName for killMob must be a string`);
    }
    // return if timeout is not number
    if (typeof timeout !== "number") {
        throw new Error(`timeout for killMob must be a number`);
    }

    const weaponsForShooting = [
        "bow",
        "crossbow",
        "snowball",
        "ender_pearl",
        "egg",
        "splash_potion",
        "trident",
    ];
    const mainHandItem = bot.inventory.slots[bot.getEquipmentDestSlot("hand")];

    const entity = bot.nearestEntity(
        (entity) =>
            entity.name === mobName &&
            // kill mob distance should be slightly bigger than explore distance
            entity.position.distanceTo(bot.entity.position) < 48
    );
    if (!entity) {
        bot.chat(`No ${mobName} nearby, please explore first`);
        _killMobFailCount++;
        if (_killMobFailCount > 10) {
            throw new Error(
                `killMob failed too many times, make sure you explore before calling killMob`
            );
        }
        return;
    }

    let droppedItem;
    if (mainHandItem && weaponsForShooting.includes(mainHandItem.name)) {
        bot.hawkEye.autoAttack(entity, mainHandItem.name);
        droppedItem = await waitForMobShot(bot, entity, timeout);
    } else {
        await bot.pvp.attack(entity);
        droppedItem = await waitForMobRemoved(bot, entity, timeout);
    }
    if (droppedItem) {
        await bot.collectBlock.collect(droppedItem, { ignoreNoPath: true });
    }
    bot.save(`${mobName}_killed`);
}



================================================
FILE: voyager/control_primitives/mineBlock.js
================================================
async function mineBlock(bot, name, count = 1) {
    // return if name is not string
    if (typeof name !== "string") {
        throw new Error(`name for mineBlock must be a string`);
    }
    if (typeof count !== "number") {
        throw new Error(`count for mineBlock must be a number`);
    }
    const blockByName = mcData.blocksByName[name];
    if (!blockByName) {
        throw new Error(`No block named ${name}`);
    }
    const blocks = bot.findBlocks({
        matching: [blockByName.id],
        maxDistance: 32,
        count: 1024,
    });
    if (blocks.length === 0) {
        bot.chat(`No ${name} nearby, please explore first`);
        _mineBlockFailCount++;
        if (_mineBlockFailCount > 10) {
            throw new Error(
                "mineBlock failed too many times, make sure you explore before calling mineBlock"
            );
        }
        return;
    }
    const targets = [];
    for (let i = 0; i < blocks.length; i++) {
        targets.push(bot.blockAt(blocks[i]));
    }
    await bot.collectBlock.collect(targets, {
        ignoreNoPath: true,
        count: count,
    });
    bot.save(`${name}_mined`);
}



================================================
FILE: voyager/control_primitives/placeItem.js
================================================
async function placeItem(bot, name, position) {
    // return if name is not string
    if (typeof name !== "string") {
        throw new Error(`name for placeItem must be a string`);
    }
    // return if position is not Vec3
    if (!(position instanceof Vec3)) {
        throw new Error(`position for placeItem must be a Vec3`);
    }
    const itemByName = mcData.itemsByName[name];
    if (!itemByName) {
        throw new Error(`No item named ${name}`);
    }
    const item = bot.inventory.findInventoryItem(itemByName.id);
    if (!item) {
        bot.chat(`No ${name} in inventory`);
        return;
    }
    const item_count = item.count;
    // find a reference block
    const faceVectors = [
        new Vec3(0, 1, 0),
        new Vec3(0, -1, 0),
        new Vec3(1, 0, 0),
        new Vec3(-1, 0, 0),
        new Vec3(0, 0, 1),
        new Vec3(0, 0, -1),
    ];
    let referenceBlock = null;
    let faceVector = null;
    for (const vector of faceVectors) {
        const block = bot.blockAt(position.minus(vector));
        if (block?.name !== "air") {
            referenceBlock = block;
            faceVector = vector;
            bot.chat(`Placing ${name} on ${block.name} at ${block.position}`);
            break;
        }
    }
    if (!referenceBlock) {
        bot.chat(
            `No block to place ${name} on. You cannot place a floating block.`
        );
        _placeItemFailCount++;
        if (_placeItemFailCount > 10) {
            throw new Error(
                `placeItem failed too many times. You cannot place a floating block.`
            );
        }
        return;
    }

    // You must use try catch to placeBlock
    try {
        // You must first go to the block position you want to place
        await bot.pathfinder.goto(new GoalPlaceBlock(position, bot.world, {}));
        // You must equip the item right before calling placeBlock
        await bot.equip(item, "hand");
        await bot.placeBlock(referenceBlock, faceVector);
        bot.chat(`Placed ${name}`);
        bot.save(`${name}_placed`);
    } catch (err) {
        const item = bot.inventory.findInventoryItem(itemByName.id);
        if (item?.count === item_count) {
            bot.chat(
                `Error placing ${name}: ${err.message}, please find another position to place`
            );
            _placeItemFailCount++;
            if (_placeItemFailCount > 10) {
                throw new Error(
                    `placeItem failed too many times, please find another position to place.`
                );
            }
        } else {
            bot.chat(`Placed ${name}`);
            bot.save(`${name}_placed`);
        }
    }
}



================================================
FILE: voyager/control_primitives/shoot.js
================================================
// shoot 1 pig with a bow: shoot(bot, "bow", "pig");
async function shoot(bot, weapon, target) {
    const validWeapons = [
        "bow",
        "crossbow",
        "snowball",
        "ender_pearl",
        "egg",
        "splash_potion",
        "trident",
    ];
    if (!validWeapons.includes(weapon)) {
        bot.chat(`${weapon} is not a valid weapon for shooting`);
        return;
    }

    const weaponItem = mcData.itemsByName[weapon];
    if (!bot.inventory.findInventoryItem(weaponItem.id, null)) {
        bot.chat(`No ${weapon} in inventory for shooting`);
        return;
    }

    const targetEntity = bot.nearestEntity(
        (entity) =>
            entity.name === target
    );
    if (!targetEntity) {
        bot.chat(`No ${target} nearby`);
        return;
    }
    bot.hawkEye.autoAttack(targetEntity, "bow");
    bot.on('auto_shot_stopped', (target) => {
    })
}



================================================
FILE: voyager/control_primitives/smeltItem.js
================================================
async function smeltItem(bot, itemName, fuelName, count = 1) {
    // return if itemName or fuelName is not string
    if (typeof itemName !== "string" || typeof fuelName !== "string") {
        throw new Error("itemName or fuelName for smeltItem must be a string");
    }
    // return if count is not a number
    if (typeof count !== "number") {
        throw new Error("count for smeltItem must be a number");
    }
    const item = mcData.itemsByName[itemName];
    const fuel = mcData.itemsByName[fuelName];
    if (!item) {
        throw new Error(`No item named ${itemName}`);
    }
    if (!fuel) {
        throw new Error(`No item named ${fuelName}`);
    }
    const furnaceBlock = bot.findBlock({
        matching: mcData.blocksByName.furnace.id,
        maxDistance: 32,
    });
    if (!furnaceBlock) {
        throw new Error("No furnace nearby");
    } else {
        await bot.pathfinder.goto(
            new GoalLookAtBlock(furnaceBlock.position, bot.world)
        );
    }
    const furnace = await bot.openFurnace(furnaceBlock);
    let success_count = 0;
    for (let i = 0; i < count; i++) {
        if (!bot.inventory.findInventoryItem(item.id, null)) {
            bot.chat(`No ${itemName} to smelt in inventory`);
            break;
        }
        if (furnace.fuelSeconds < 15 && furnace.fuelItem()?.name !== fuelName) {
            if (!bot.inventory.findInventoryItem(fuel.id, null)) {
                bot.chat(`No ${fuelName} as fuel in inventory`);
                break;
            }
            await furnace.putFuel(fuel.id, null, 1);
            await bot.waitForTicks(20);
            if (!furnace.fuel && furnace.fuelItem()?.name !== fuelName) {
                throw new Error(`${fuelName} is not a valid fuel`);
            }
        }
        await furnace.putInput(item.id, null, 1);
        await bot.waitForTicks(12 * 20);
        if (!furnace.outputItem()) {
            throw new Error(`${itemName} is not a valid input`);
        }
        await furnace.takeOutput();
        success_count++;
    }
    furnace.close();
    if (success_count > 0) bot.chat(`Smelted ${success_count} ${itemName}.`);
    else {
        bot.chat(
            `Failed to smelt ${itemName}, please check the fuel and input.`
        );
        _smeltItemFailCount++;
        if (_smeltItemFailCount > 10) {
            throw new Error(
                `smeltItem failed too many times, please check the fuel and input.`
            );
        }
    }
}



================================================
FILE: voyager/control_primitives/useChest.js
================================================
async function getItemFromChest(bot, chestPosition, itemsToGet) {
    // return if chestPosition is not Vec3
    if (!(chestPosition instanceof Vec3)) {
        bot.chat("chestPosition for getItemFromChest must be a Vec3");
        return;
    }
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    const chest = await bot.openContainer(chestBlock);
    for (const name in itemsToGet) {
        const itemByName = mcData.itemsByName[name];
        if (!itemByName) {
            bot.chat(`No item named ${name}`);
            continue;
        }

        const item = chest.findContainerItem(itemByName.id);
        if (!item) {
            bot.chat(`I don't see ${name} in this chest`);
            continue;
        }
        try {
            await chest.withdraw(item.type, null, itemsToGet[name]);
        } catch (err) {
            bot.chat(`Not enough ${name} in chest.`);
        }
    }
    await closeChest(bot, chestBlock);
}

async function depositItemIntoChest(bot, chestPosition, itemsToDeposit) {
    // return if chestPosition is not Vec3
    if (!(chestPosition instanceof Vec3)) {
        throw new Error(
            "chestPosition for depositItemIntoChest must be a Vec3"
        );
    }
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    const chest = await bot.openContainer(chestBlock);
    for (const name in itemsToDeposit) {
        const itemByName = mcData.itemsByName[name];
        if (!itemByName) {
            bot.chat(`No item named ${name}`);
            continue;
        }
        const item = bot.inventory.findInventoryItem(itemByName.id);
        if (!item) {
            bot.chat(`No ${name} in inventory`);
            continue;
        }
        try {
            await chest.deposit(item.type, null, itemsToDeposit[name]);
        } catch (err) {
            bot.chat(`Not enough ${name} in inventory.`);
        }
    }
    await closeChest(bot, chestBlock);
}

async function checkItemInsideChest(bot, chestPosition) {
    // return if chestPosition is not Vec3
    if (!(chestPosition instanceof Vec3)) {
        throw new Error(
            "chestPosition for depositItemIntoChest must be a Vec3"
        );
    }
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    await bot.openContainer(chestBlock);
    await closeChest(bot, chestBlock);
}

async function moveToChest(bot, chestPosition) {
    if (!(chestPosition instanceof Vec3)) {
        throw new Error(
            "chestPosition for depositItemIntoChest must be a Vec3"
        );
    }
    if (chestPosition.distanceTo(bot.entity.position) > 32) {
        bot.chat(
            `/tp ${chestPosition.x} ${chestPosition.y} ${chestPosition.z}`
        );
        await bot.waitForTicks(20);
    }
    const chestBlock = bot.blockAt(chestPosition);
    if (chestBlock.name !== "chest") {
        bot.emit("removeChest", chestPosition);
        throw new Error(
            `No chest at ${chestPosition}, it is ${chestBlock.name}`
        );
    }
    await bot.pathfinder.goto(
        new GoalLookAtBlock(chestBlock.position, bot.world, {})
    );
    return chestBlock;
}

async function listItemsInChest(bot, chestBlock) {
    const chest = await bot.openContainer(chestBlock);
    const items = chest.containerItems();
    if (items.length > 0) {
        const itemNames = items.reduce((acc, obj) => {
            if (acc[obj.name]) {
                acc[obj.name] += obj.count;
            } else {
                acc[obj.name] = obj.count;
            }
            return acc;
        }, {});
        bot.emit("closeChest", itemNames, chestBlock.position);
    } else {
        bot.emit("closeChest", {}, chestBlock.position);
    }
    return chest;
}

async function closeChest(bot, chestBlock) {
    try {
        const chest = await listItemsInChest(bot, chestBlock);
        await chest.close();
    } catch (err) {
        await bot.closeWindow(chestBlock);
    }
}

function itemByName(items, name) {
    for (let i = 0; i < items.length; ++i) {
        const item = items[i];
        if (item && item.name === name) return item;
    }
    return null;
}



================================================
FILE: voyager/control_primitives/waitForMobRemoved.js
================================================
function waitForMobRemoved(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.pvp.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Killed ${entity.name}!`);
                bot.pvp.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onStoppedAttacking() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("stoppedAttacking", onStoppedAttacking);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to kill ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("stoppedAttacking", onStoppedAttacking);
        bot.on("itemDrop", onItemDrop);
    });
}


function waitForMobShot(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.hawkEye.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Shot ${entity.name}!`);
                bot.hawkEye.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onAutoShotStopped() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("auto_shot_stopped", onAutoShotStopped);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to shoot ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("auto_shot_stopped", onAutoShotStopped);
        bot.on("itemDrop", onItemDrop);
    });
}



================================================
FILE: voyager/control_primitives/.prettierrc.json
================================================
{
    "tabWidth": 4
}



================================================
FILE: voyager/control_primitives_context/__init__.py
================================================
import pkg_resources
import os
import voyager.utils as U


def load_control_primitives_context(primitive_names=None):
    package_path = pkg_resources.resource_filename("voyager", "")
    if primitive_names is None:
        primitive_names = [
            primitive[:-3]
            for primitive in os.listdir(f"{package_path}/control_primitives_context")
            if primitive.endswith(".js")
        ]
    primitives = [
        U.load_text(f"{package_path}/control_primitives_context/{primitive_name}.js")
        for primitive_name in primitive_names
    ]
    return primitives



================================================
FILE: voyager/control_primitives_context/craftItem.js
================================================
// Craft 8 oak_planks from 2 oak_log (do the recipe 2 times): craftItem(bot, "oak_planks", 2);
// You must place a crafting table before calling this function
async function craftItem(bot, name, count = 1) {
    const item = mcData.itemsByName[name];
    const craftingTable = bot.findBlock({
        matching: mcData.blocksByName.crafting_table.id,
        maxDistance: 32,
    });
    await bot.pathfinder.goto(
        new GoalLookAtBlock(craftingTable.position, bot.world)
    );
    const recipe = bot.recipesFor(item.id, null, 1, craftingTable)[0];
    await bot.craft(recipe, count, craftingTable);
}



================================================
FILE: voyager/control_primitives_context/exploreUntil.js
================================================
/*
Explore until find an iron_ore, use Vec3(0, -1, 0) because iron ores are usually underground
await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
    const iron_ore = bot.findBlock({
        matching: mcData.blocksByName["iron_ore"].id,
        maxDistance: 32,
    });
    return iron_ore;
});

Explore until find a pig, use Vec3(1, 0, 1) because pigs are usually on the surface
let pig = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const pig = bot.nearestEntity((entity) => {
        return (
            entity.name === "pig" &&
            entity.position.distanceTo(bot.entity.position) < 32
        );
    });
    return pig;
});
*/
async function exploreUntil(bot, direction, maxTime = 60, callback) {
    /*
    Implementation of this function is omitted.
    direction: Vec3, can only contain value of -1, 0 or 1
    maxTime: number, the max time for exploration
    callback: function, early stop condition, will be called each second, exploration will stop if return value is not null

    Return: null if explore timeout, otherwise return the return value of callback
    */
}



================================================
FILE: voyager/control_primitives_context/killMob.js
================================================
// Kill a pig and collect the dropped item: killMob(bot, "pig", 300);
async function killMob(bot, mobName, timeout = 300) {
    const entity = bot.nearestEntity(
        (entity) =>
            entity.name === mobName &&
            entity.position.distanceTo(bot.entity.position) < 32
    );
    await bot.pvp.attack(entity);
    await bot.pathfinder.goto(
        new GoalBlock(entity.position.x, entity.position.y, entity.position.z)
    );
}



================================================
FILE: voyager/control_primitives_context/mineBlock.js
================================================
// Mine 3 cobblestone: mineBlock(bot, "stone", 3);
async function mineBlock(bot, name, count = 1) {
    const blocks = bot.findBlocks({
        matching: (block) => {
            return block.name === name;
        },
        maxDistance: 32,
        count: count,
    });
    const targets = [];
    for (let i = 0; i < Math.min(blocks.length, count); i++) {
        targets.push(bot.blockAt(blocks[i]));
    }
    await bot.collectBlock.collect(targets, { ignoreNoPath: true });
}



================================================
FILE: voyager/control_primitives_context/mineflayer.js
================================================
await bot.pathfinder.goto(goal); // A very useful function. This function may change your main-hand equipment.
// Following are some Goals you can use:
new GoalNear(x, y, z, range); // Move the bot to a block within the specified range of the specified block. `x`, `y`, `z`, and `range` are `number`
new GoalXZ(x, z); // Useful for long-range goals that don't have a specific Y level. `x` and `z` are `number`
new GoalGetToBlock(x, y, z); // Not get into the block, but get directly adjacent to it. Useful for fishing, farming, filling bucket, and beds. `x`, `y`, and `z` are `number`
new GoalFollow(entity, range); // Follow the specified entity within the specified range. `entity` is `Entity`, `range` is `number`
new GoalPlaceBlock(position, bot.world, {}); // Position the bot in order to place a block. `position` is `Vec3`
new GoalLookAtBlock(position, bot.world, {}); // Path into a position where a blockface of the block at position is visible. `position` is `Vec3`

// These are other Mineflayer functions you can use:
bot.isABed(bedBlock); // Return true if `bedBlock` is a bed
bot.blockAt(position); // Return the block at `position`. `position` is `Vec3`

// These are other Mineflayer async functions you can use:
await bot.equip(item, destination); // Equip the item in the specified destination. `item` is `Item`, `destination` can only be "hand", "head", "torso", "legs", "feet", "off-hand"
await bot.consume(); // Consume the item in the bot's hand. You must equip the item to consume first. Useful for eating food, drinking potions, etc.
await bot.fish(); // Let bot fish. Before calling this function, you must first get to a water block and then equip a fishing rod. The bot will automatically stop fishing when it catches a fish
await bot.sleep(bedBlock); // Sleep until sunrise. You must get to a bed block first
await bot.activateBlock(block); // This is the same as right-clicking a block in the game. Useful for buttons, doors, etc. You must get to the block first
await bot.lookAt(position); // Look at the specified position. You must go near the position before you look at it. To fill bucket with water, you must lookAt first. `position` is `Vec3`
await bot.activateItem(); // This is the same as right-clicking to use the item in the bot's hand. Useful for using buckets, etc. You must equip the item to activate first
await bot.useOn(entity); // This is the same as right-clicking an entity in the game. Useful for shearing sheep, equipping harnesses, etc. You must get to the entity first



================================================
FILE: voyager/control_primitives_context/placeItem.js
================================================
// Place a crafting_table near the player, Vec3(1, 0, 0) is just an example, you shouldn't always use that: placeItem(bot, "crafting_table", bot.entity.position.offset(1, 0, 0));
async function placeItem(bot, name, position) {
    const item = bot.inventory.findInventoryItem(mcData.itemsByName[name].id);
    // find a reference block
    const faceVectors = [
        new Vec3(0, 1, 0),
        new Vec3(0, -1, 0),
        new Vec3(1, 0, 0),
        new Vec3(-1, 0, 0),
        new Vec3(0, 0, 1),
        new Vec3(0, 0, -1),
    ];
    let referenceBlock = null;
    let faceVector = null;
    for (const vector of faceVectors) {
        const block = bot.blockAt(position.minus(vector));
        if (block?.name !== "air") {
            referenceBlock = block;
            faceVector = vector;
            break;
        }
    }
    // You must first go to the block position you want to place
    await bot.pathfinder.goto(new GoalPlaceBlock(position, bot.world, {}));
    // You must equip the item right before calling placeBlock
    await bot.equip(item, "hand");
    await bot.placeBlock(referenceBlock, faceVector);
}



================================================
FILE: voyager/control_primitives_context/smeltItem.js
================================================
// Smelt 1 raw_iron into 1 iron_ingot using 1 oak_planks as fuel: smeltItem(bot, "raw_iron", "oak_planks");
// You must place a furnace before calling this function
async function smeltItem(bot, itemName, fuelName, count = 1) {
    const item = mcData.itemsByName[itemName];
    const fuel = mcData.itemsByName[fuelName];
    const furnaceBlock = bot.findBlock({
        matching: mcData.blocksByName.furnace.id,
        maxDistance: 32,
    });
    await bot.pathfinder.goto(
        new GoalLookAtBlock(furnaceBlock.position, bot.world)
    );
    const furnace = await bot.openFurnace(furnaceBlock);
    for (let i = 0; i < count; i++) {
        await furnace.putFuel(fuel.id, null, 1);
        await furnace.putInput(item.id, null, 1);
        // Wait 12 seconds for the furnace to smelt the item
        await bot.waitForTicks(12 * 20);
        await furnace.takeOutput();
    }
    await furnace.close();
}



================================================
FILE: voyager/control_primitives_context/useChest.js
================================================
// Get a torch from chest at (30, 65, 100): getItemFromChest(bot, new Vec3(30, 65, 100), {"torch": 1});
// This function will work no matter how far the bot is from the chest.
async function getItemFromChest(bot, chestPosition, itemsToGet) {
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    const chest = await bot.openContainer(chestBlock);
    for (const name in itemsToGet) {
        const itemByName = mcData.itemsByName[name];
        const item = chest.findContainerItem(itemByName.id);
        await chest.withdraw(item.type, null, itemsToGet[name]);
    }
    await closeChest(bot, chestBlock);
}
// Deposit a torch into chest at (30, 65, 100): depositItemIntoChest(bot, new Vec3(30, 65, 100), {"torch": 1});
// This function will work no matter how far the bot is from the chest.
async function depositItemIntoChest(bot, chestPosition, itemsToDeposit) {
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    const chest = await bot.openContainer(chestBlock);
    for (const name in itemsToDeposit) {
        const itemByName = mcData.itemsByName[name];
        const item = bot.inventory.findInventoryItem(itemByName.id);
        await chest.deposit(item.type, null, itemsToDeposit[name]);
    }
    await closeChest(bot, chestBlock);
}
// Check the items inside the chest at (30, 65, 100): checkItemInsideChest(bot, new Vec3(30, 65, 100));
// You only need to call this function once without any action to finish task of checking items inside the chest.
async function checkItemInsideChest(bot, chestPosition) {
    await moveToChest(bot, chestPosition);
    const chestBlock = bot.blockAt(chestPosition);
    await bot.openContainer(chestBlock);
    // You must close the chest after opening it if you are asked to open a chest
    await closeChest(bot, chestBlock);
}



================================================
FILE: voyager/control_primitives_context/.prettierrc.json
================================================
{
    "tabWidth": 4
}



================================================
FILE: voyager/env/__init__.py
================================================
from .bridge import VoyagerEnv



================================================
FILE: voyager/env/bridge.py
================================================
import os.path
import time
import warnings
from typing import SupportsFloat, Any, Tuple, Dict

import requests
import json

import gymnasium as gym
from gymnasium.core import ObsType

import voyager.utils as U

from .minecraft_launcher import MinecraftInstance
from .process_monitor import SubprocessMonitor


class VoyagerEnv(gym.Env):
    def __init__(
        self,
        mc_port=None,
        azure_login=None,
        server_host="http://127.0.0.1",
        server_port=3000,
        request_timeout=600,
        log_path="./logs",
    ):
        if not mc_port and not azure_login:
            raise ValueError("Either mc_port or azure_login must be specified")
        if mc_port and azure_login:
            warnings.warn(
                "Both mc_port and mc_login are specified, mc_port will be ignored"
            )
        self.mc_port = mc_port
        self.azure_login = azure_login
        self.server = f"{server_host}:{server_port}"
        self.server_port = server_port
        self.request_timeout = request_timeout
        self.log_path = log_path
        self.mineflayer = self.get_mineflayer_process(server_port)
        if azure_login:
            self.mc_instance = self.get_mc_instance()
        else:
            self.mc_instance = None
        self.has_reset = False
        self.reset_options = None
        self.connected = False
        self.server_paused = False

    def get_mineflayer_process(self, server_port):
        U.f_mkdir(self.log_path, "mineflayer")
        file_path = os.path.abspath(os.path.dirname(__file__))
        return SubprocessMonitor(
            commands=[
                "node",
                U.f_join(file_path, "mineflayer/index.js"),
                str(server_port),
            ],
            name="mineflayer",
            ready_match=r"Server started on port (\d+)",
            log_path=U.f_join(self.log_path, "mineflayer"),
        )

    def get_mc_instance(self):
        print("Creating Minecraft server")
        U.f_mkdir(self.log_path, "minecraft")
        return MinecraftInstance(
            **self.azure_login,
            mineflayer=self.mineflayer,
            log_path=U.f_join(self.log_path, "minecraft"),
        )

    def check_process(self):
        if self.mc_instance and not self.mc_instance.is_running:
            # if self.mc_instance:
            #     self.mc_instance.check_process()
            #     if not self.mc_instance.is_running:
            print("Starting Minecraft server")
            self.mc_instance.run()
            self.mc_port = self.mc_instance.port
            self.reset_options["port"] = self.mc_instance.port
            print(f"Server started on port {self.reset_options['port']}")
        retry = 0
        while not self.mineflayer.is_running:
            print("Mineflayer process has exited, restarting")
            self.mineflayer.run()
            if not self.mineflayer.is_running:
                if retry > 3:
                    raise RuntimeError("Mineflayer process failed to start")
                else:
                    continue
            print(self.mineflayer.ready_line)
            res = requests.post(
                f"{self.server}/start",
                json=self.reset_options,
                timeout=self.request_timeout,
            )
            if res.status_code != 200:
                self.mineflayer.stop()
                raise RuntimeError(
                    f"Minecraft server reply with code {res.status_code}"
                )
            return res.json()

    def step(
        self,
        code: str,
        programs: str = "",
    ) -> Tuple[ObsType, SupportsFloat, bool, bool, Dict[str, Any]]:
        if not self.has_reset:
            raise RuntimeError("Environment has not been reset yet")
        self.check_process()
        self.unpause()
        data = {
            "code": code,
            "programs": programs,
        }
        res = requests.post(
            f"{self.server}/step", json=data, timeout=self.request_timeout
        )
        if res.status_code != 200:
            raise RuntimeError("Failed to step Minecraft server")
        returned_data = res.json()
        self.pause()
        return json.loads(returned_data)

    def render(self):
        raise NotImplementedError("render is not implemented")

    def reset(
        self,
        *,
        seed=None,
        options=None,
    ) -> Tuple[ObsType, Dict[str, Any]]:
        if options is None:
            options = {}

        if options.get("inventory", {}) and options.get("mode", "hard") != "hard":
            raise RuntimeError("inventory can only be set when options is hard")

        self.reset_options = {
            "port": self.mc_port,
            "reset": options.get("mode", "hard"),
            "inventory": options.get("inventory", {}),
            "equipment": options.get("equipment", []),
            "spread": options.get("spread", False),
            "waitTicks": options.get("wait_ticks", 5),
            "position": options.get("position", None),
        }

        self.unpause()
        self.mineflayer.stop()
        time.sleep(1)  # wait for mineflayer to exit

        returned_data = self.check_process()
        self.has_reset = True
        self.connected = True
        # All the reset in step will be soft
        self.reset_options["reset"] = "soft"
        self.pause()
        return json.loads(returned_data)

    def close(self):
        self.unpause()
        if self.connected:
            res = requests.post(f"{self.server}/stop")
            if res.status_code == 200:
                self.connected = False
        if self.mc_instance:
            self.mc_instance.stop()
        self.mineflayer.stop()
        return not self.connected

    def pause(self):
        if self.mineflayer.is_running and not self.server_paused:
            res = requests.post(f"{self.server}/pause")
            if res.status_code == 200:
                self.server_paused = True
        return self.server_paused

    def unpause(self):
        if self.mineflayer.is_running and self.server_paused:
            res = requests.post(f"{self.server}/pause")
            if res.status_code == 200:
                self.server_paused = False
            else:
                print(res.json())
        return self.server_paused



================================================
FILE: voyager/env/minecraft_launcher.py
================================================
import os
import re

import minecraft_launcher_lib
import sys
import voyager.utils as U

from .process_monitor import SubprocessMonitor


class MinecraftInstance:
    def __init__(
        self,
        client_id,
        redirect_url,
        secret_value,
        version,
        mineflayer,
        log_path="logs",
    ):
        self.client_id = client_id
        self.redirect_url = redirect_url
        self.secret_value = secret_value
        self.version = version
        self.log_path = log_path
        self.mc_dir = minecraft_launcher_lib.utils.get_minecraft_directory()
        self.port = None

        def stop_mineflayer():
            print("Stopping mineflayer")
            try:
                mineflayer.stop()
            except Exception as e:
                print(e)

        self.mc_command = self.get_mc_command()
        self.mc_process = SubprocessMonitor(
            commands=self.mc_command,
            name="minecraft",
            ready_match=r"Started serving on (\d+)",
            log_path=self.log_path,
            callback=stop_mineflayer,
            callback_match=r"\[Server thread/INFO\]: bot left the game",
            finished_callback=stop_mineflayer,
        )

    def get_mineflayer_process(self, server_port):
        U.f_mkdir(self.log_path, "../mineflayer")
        file_path = os.path.abspath(os.path.dirname(__file__))
        return SubprocessMonitor(
            commands=[
                "node",
                U.f_join(file_path, "mineflayer/index.js"),
                str(server_port),
            ],
            name="mineflayer",
            ready_match=r"Server started on port (\d+)",
            log_path=U.f_join(self.log_path, "mineflayer"),
        )

    def get_mc_command(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        if not U.f_exists(file_path, "config.json"):
            (
                login_url,
                state,
                code_verifier,
            ) = minecraft_launcher_lib.microsoft_account.get_secure_login_data(
                self.client_id, self.redirect_url
            )
            print(
                f"Please open {login_url} in your browser and copy the url you are redirected into the prompt below."
            )
            code_url = input()

            try:
                auth_code = (
                    minecraft_launcher_lib.microsoft_account.parse_auth_code_url(
                        code_url, state
                    )
                )
            except AssertionError:
                print("States do not match!")
                sys.exit(1)
            except KeyError:
                print("Url not valid")
                sys.exit(1)

            login_data = minecraft_launcher_lib.microsoft_account.complete_login(
                self.client_id,
                self.secret_value,
                self.redirect_url,
                auth_code,
                code_verifier,
            )

            options = {
                "username": login_data["name"],
                "uuid": login_data["id"],
                "token": login_data["access_token"],
            }
            U.json_dump(options, file_path, "config.json")
            print(f"Login success, save to {U.f_join(file_path, 'config.json')}")

        options = U.json_load(file_path, "config.json")
        mc_command = minecraft_launcher_lib.command.get_minecraft_command(
            self.version, self.mc_dir, options
        )

        return mc_command

    def run(self):
        self.mc_process.run()
        pattern = r"Started serving on (\d+)"
        match = re.search(pattern, self.mc_process.ready_line)
        if match:
            self.port = int(match.group(1))
            print("The mc server is listening on port", self.port)
        else:
            raise RuntimeError("Port not found")

    def stop(self):
        self.mc_process.stop()

    @property
    def is_running(self):
        return self.mc_process.is_running



================================================
FILE: voyager/env/process_monitor.py
================================================
import time
import re
import warnings
from typing import List

import psutil
import subprocess
import logging
import threading

import voyager.utils as U


class SubprocessMonitor:
    def __init__(
        self,
        commands: List[str],
        name: str,
        ready_match: str = r".*",
        log_path: str = "logs",
        callback_match: str = r"^(?!x)x$",  # regex that will never match
        callback: callable = None,
        finished_callback: callable = None,
    ):
        self.commands = commands
        start_time = time.strftime("%Y%m%d_%H%M%S")
        self.name = name
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler(U.f_join(log_path, f"{start_time}.log"))
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        self.process = None
        self.ready_match = ready_match
        self.ready_event = None
        self.ready_line = None
        self.callback_match = callback_match
        self.callback = callback
        self.finished_callback = finished_callback
        self.thread = None

    def _start(self):
        self.logger.info(f"Starting subprocess with commands: {self.commands}")

        self.process = psutil.Popen(
            self.commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        print(f"Subprocess {self.name} started with PID {self.process.pid}.")
        for line in iter(self.process.stdout.readline, ""):
            self.logger.info(line.strip())
            if re.search(self.ready_match, line):
                self.ready_line = line
                self.logger.info("Subprocess is ready.")
                self.ready_event.set()
            if re.search(self.callback_match, line):
                self.callback()
        if not self.ready_event.is_set():
            self.ready_event.set()
            warnings.warn(f"Subprocess {self.name} failed to start.")
        if self.finished_callback:
            self.finished_callback()

    def run(self):
        self.ready_event = threading.Event()
        self.ready_line = None
        self.thread = threading.Thread(target=self._start)
        self.thread.start()
        self.ready_event.wait()

    def stop(self):
        self.logger.info("Stopping subprocess.")
        if self.process and self.process.is_running():
            self.process.terminate()
            self.process.wait()

    # def __del__(self):
    #     if self.process.is_running():
    #         self.stop()

    @property
    def is_running(self):
        if self.process is None:
            return False
        return self.process.is_running()



================================================
FILE: voyager/env/.gitignore
================================================
# MCP-Reborn
MCP-Reborn/
run/
*.jar
config.json

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
.idea/

# Logs
logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# Snowpack dependency directory (https://snowpack.dev/)
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional stylelint cache
.stylelintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variable files
.env.development.local
.env.test.local
.env.production.local
.env.local

# parcel-bundler cache (https://parceljs.org/)
.parcel-cache

# Next.js build output
.next
out

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
# Comment in the public line in if your project uses Gatsby and not Next.js
# https://nextjs.org/blog/next-9-1#public-directory-support
# public

# vuepress build output
.vuepress/dist

# vuepress v2.x temp and cache directory
.temp

# Docusaurus cache and generated files
.docusaurus

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*

package-lock.json


================================================
FILE: voyager/env/mineflayer/index.js
================================================
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const mineflayer = require("mineflayer");

const skills = require("./lib/skillLoader");
const { initCounter, getNextTime } = require("./lib/utils");
const obs = require("./lib/observation/base");
const OnChat = require("./lib/observation/onChat");
const OnError = require("./lib/observation/onError");
const { Voxels, BlockRecords } = require("./lib/observation/voxels");
const Status = require("./lib/observation/status");
const Inventory = require("./lib/observation/inventory");
const OnSave = require("./lib/observation/onSave");
const Chests = require("./lib/observation/chests");
const { plugin: tool } = require("mineflayer-tool");

let bot = null;

const app = express();

app.use(bodyParser.json({ limit: "50mb" }));
app.use(bodyParser.urlencoded({ limit: "50mb", extended: false }));

app.post("/start", (req, res) => {
    if (bot) onDisconnect("Restarting bot");
    bot = null;
    console.log(req.body);
    bot = mineflayer.createBot({
        host: "localhost", // minecraft server ip
        port: req.body.port, // minecraft server port
        username: "bot",
        disableChatSigning: true,
        checkTimeoutInterval: 60 * 60 * 1000,
    });
    bot.once("error", onConnectionFailed);

    // Event subscriptions
    bot.waitTicks = req.body.waitTicks;
    bot.globalTickCounter = 0;
    bot.stuckTickCounter = 0;
    bot.stuckPosList = [];
    bot.iron_pickaxe = false;

    bot.on("kicked", onDisconnect);

    // mounting will cause physicsTick to stop
    bot.on("mount", () => {
        bot.dismount();
    });

    bot.once("spawn", async () => {
        bot.removeListener("error", onConnectionFailed);
        let itemTicks = 1;
        if (req.body.reset === "hard") {
            bot.chat("/clear @s");
            bot.chat("/kill @s");
            const inventory = req.body.inventory ? req.body.inventory : {};
            const equipment = req.body.equipment
                ? req.body.equipment
                : [null, null, null, null, null, null];
            for (let key in inventory) {
                bot.chat(`/give @s minecraft:${key} ${inventory[key]}`);
                itemTicks += 1;
            }
            const equipmentNames = [
                "armor.head",
                "armor.chest",
                "armor.legs",
                "armor.feet",
                "weapon.mainhand",
                "weapon.offhand",
            ];
            for (let i = 0; i < 6; i++) {
                if (i === 4) continue;
                if (equipment[i]) {
                    bot.chat(
                        `/item replace entity @s ${equipmentNames[i]} with minecraft:${equipment[i]}`
                    );
                    itemTicks += 1;
                }
            }
        }

        if (req.body.position) {
            bot.chat(
                `/tp @s ${req.body.position.x} ${req.body.position.y} ${req.body.position.z}`
            );
        }

        // if iron_pickaxe is in bot's inventory
        if (
            bot.inventory.items().find((item) => item.name === "iron_pickaxe")
        ) {
            bot.iron_pickaxe = true;
        }

        const { pathfinder } = require("mineflayer-pathfinder");
        const tool = require("mineflayer-tool").plugin;
        const collectBlock = require("mineflayer-collectblock").plugin;
        const pvp = require("mineflayer-pvp").plugin;
        const minecraftHawkEye = require("minecrafthawkeye");
        bot.loadPlugin(pathfinder);
        bot.loadPlugin(tool);
        bot.loadPlugin(collectBlock);
        bot.loadPlugin(pvp);
        bot.loadPlugin(minecraftHawkEye);

        // bot.collectBlock.movements.digCost = 0;
        // bot.collectBlock.movements.placeCost = 0;

        obs.inject(bot, [
            OnChat,
            OnError,
            Voxels,
            Status,
            Inventory,
            OnSave,
            Chests,
            BlockRecords,
        ]);
        skills.inject(bot);

        if (req.body.spread) {
            bot.chat(`/spreadplayers ~ ~ 0 300 under 80 false @s`);
            await bot.waitForTicks(bot.waitTicks);
        }

        await bot.waitForTicks(bot.waitTicks * itemTicks);
        res.json(bot.observe());

        initCounter(bot);
        bot.chat("/gamerule keepInventory true");
        bot.chat("/gamerule doDaylightCycle false");
    });

    function onConnectionFailed(e) {
        console.log(e);
        bot = null;
        res.status(400).json({ error: e });
    }
    function onDisconnect(message) {
        if (bot.viewer) {
            bot.viewer.close();
        }
        bot.end();
        console.log(message);
        bot = null;
    }
});

app.post("/step", async (req, res) => {
    // import useful package
    let response_sent = false;
    function otherError(err) {
        console.log("Uncaught Error");
        bot.emit("error", handleError(err));
        bot.waitForTicks(bot.waitTicks).then(() => {
            if (!response_sent) {
                response_sent = true;
                res.json(bot.observe());
            }
        });
    }

    process.on("uncaughtException", otherError);

    const mcData = require("minecraft-data")(bot.version);
    mcData.itemsByName["leather_cap"] = mcData.itemsByName["leather_helmet"];
    mcData.itemsByName["leather_tunic"] =
        mcData.itemsByName["leather_chestplate"];
    mcData.itemsByName["leather_pants"] =
        mcData.itemsByName["leather_leggings"];
    mcData.itemsByName["leather_boots"] = mcData.itemsByName["leather_boots"];
    mcData.itemsByName["lapis_lazuli_ore"] = mcData.itemsByName["lapis_ore"];
    mcData.blocksByName["lapis_lazuli_ore"] = mcData.blocksByName["lapis_ore"];
    const {
        Movements,
        goals: {
            Goal,
            GoalBlock,
            GoalNear,
            GoalXZ,
            GoalNearXZ,
            GoalY,
            GoalGetToBlock,
            GoalLookAtBlock,
            GoalBreakBlock,
            GoalCompositeAny,
            GoalCompositeAll,
            GoalInvert,
            GoalFollow,
            GoalPlaceBlock,
        },
        pathfinder,
        Move,
        ComputedPath,
        PartiallyComputedPath,
        XZCoordinates,
        XYZCoordinates,
        SafeBlock,
        GoalPlaceBlockOptions,
    } = require("mineflayer-pathfinder");
    const { Vec3 } = require("vec3");

    // Set up pathfinder
    const movements = new Movements(bot, mcData);
    bot.pathfinder.setMovements(movements);

    bot.globalTickCounter = 0;
    bot.stuckTickCounter = 0;
    bot.stuckPosList = [];

    function onTick() {
        bot.globalTickCounter++;
        if (bot.pathfinder.isMoving()) {
            bot.stuckTickCounter++;
            if (bot.stuckTickCounter >= 100) {
                onStuck(1.5);
                bot.stuckTickCounter = 0;
            }
        }
    }

    bot.on("physicTick", onTick);

    // initialize fail count
    let _craftItemFailCount = 0;
    let _killMobFailCount = 0;
    let _mineBlockFailCount = 0;
    let _placeItemFailCount = 0;
    let _smeltItemFailCount = 0;

    // Retrieve array form post bod
    const code = req.body.code;
    const programs = req.body.programs;
    bot.cumulativeObs = [];
    await bot.waitForTicks(bot.waitTicks);
    const r = await evaluateCode(code, programs);
    process.off("uncaughtException", otherError);
    if (r !== "success") {
        bot.emit("error", handleError(r));
    }
    await returnItems();
    // wait for last message
    await bot.waitForTicks(bot.waitTicks);
    if (!response_sent) {
        response_sent = true;
        res.json(bot.observe());
    }
    bot.removeListener("physicTick", onTick);

    async function evaluateCode(code, programs) {
        // Echo the code produced for players to see it. Don't echo when the bot code is already producing dialog or it will double echo
        try {
            await eval("(async () => {" + programs + "\n" + code + "})()");
            return "success";
        } catch (err) {
            return err;
        }
    }

    function onStuck(posThreshold) {
        const currentPos = bot.entity.position;
        bot.stuckPosList.push(currentPos);

        // Check if the list is full
        if (bot.stuckPosList.length === 5) {
            const oldestPos = bot.stuckPosList[0];
            const posDifference = currentPos.distanceTo(oldestPos);

            if (posDifference < posThreshold) {
                teleportBot(); // execute the function
            }

            // Remove the oldest time from the list
            bot.stuckPosList.shift();
        }
    }

    function teleportBot() {
        const blocks = bot.findBlocks({
            matching: (block) => {
                return block.type === 0;
            },
            maxDistance: 1,
            count: 27,
        });

        if (blocks) {
            // console.log(blocks.length);
            const randomIndex = Math.floor(Math.random() * blocks.length);
            const block = blocks[randomIndex];
            bot.chat(`/tp @s ${block.x} ${block.y} ${block.z}`);
        } else {
            bot.chat("/tp @s ~ ~1.25 ~");
        }
    }

    function returnItems() {
        bot.chat("/gamerule doTileDrops false");
        const crafting_table = bot.findBlock({
            matching: mcData.blocksByName.crafting_table.id,
            maxDistance: 128,
        });
        if (crafting_table) {
            bot.chat(
                `/setblock ${crafting_table.position.x} ${crafting_table.position.y} ${crafting_table.position.z} air destroy`
            );
            bot.chat("/give @s crafting_table");
        }
        const furnace = bot.findBlock({
            matching: mcData.blocksByName.furnace.id,
            maxDistance: 128,
        });
        if (furnace) {
            bot.chat(
                `/setblock ${furnace.position.x} ${furnace.position.y} ${furnace.position.z} air destroy`
            );
            bot.chat("/give @s furnace");
        }
        if (bot.inventoryUsed() >= 32) {
            // if chest is not in bot's inventory
            if (!bot.inventory.items().find((item) => item.name === "chest")) {
                bot.chat("/give @s chest");
            }
        }
        // if iron_pickaxe not in bot's inventory and bot.iron_pickaxe
        if (
            bot.iron_pickaxe &&
            !bot.inventory.items().find((item) => item.name === "iron_pickaxe")
        ) {
            bot.chat("/give @s iron_pickaxe");
        }
        bot.chat("/gamerule doTileDrops true");
    }

    function handleError(err) {
        let stack = err.stack;
        if (!stack) {
            return err;
        }
        console.log(stack);
        const final_line = stack.split("\n")[1];
        const regex = /<anonymous>:(\d+):\d+\)/;

        const programs_length = programs.split("\n").length;
        let match_line = null;
        for (const line of stack.split("\n")) {
            const match = regex.exec(line);
            if (match) {
                const line_num = parseInt(match[1]);
                if (line_num >= programs_length) {
                    match_line = line_num - programs_length;
                    break;
                }
            }
        }
        if (!match_line) {
            return err.message;
        }
        let f_line = final_line.match(
            /\((?<file>.*):(?<line>\d+):(?<pos>\d+)\)/
        );
        if (f_line && f_line.groups && fs.existsSync(f_line.groups.file)) {
            const { file, line, pos } = f_line.groups;
            const f = fs.readFileSync(file, "utf8").split("\n");
            // let filename = file.match(/(?<=node_modules\\)(.*)/)[1];
            let source = file + `:${line}\n${f[line - 1].trim()}\n `;

            const code_source =
                "at " +
                code.split("\n")[match_line - 1].trim() +
                " in your code";
            return source + err.message + "\n" + code_source;
        } else if (
            f_line &&
            f_line.groups &&
            f_line.groups.file.includes("<anonymous>")
        ) {
            const { file, line, pos } = f_line.groups;
            let source =
                "Your code" +
                `:${match_line}\n${code.split("\n")[match_line - 1].trim()}\n `;
            let code_source = "";
            if (line < programs_length) {
                source =
                    "In your program code: " +
                    programs.split("\n")[line - 1].trim() +
                    "\n";
                code_source = `at line ${match_line}:${code
                    .split("\n")
                    [match_line - 1].trim()} in your code`;
            }
            return source + err.message + "\n" + code_source;
        }
        return err.message;
    }
});

app.post("/stop", (req, res) => {
    bot.end();
    res.json({
        message: "Bot stopped",
    });
});

app.post("/pause", (req, res) => {
    if (!bot) {
        res.status(400).json({ error: "Bot not spawned" });
        return;
    }
    bot.chat("/pause");
    bot.waitForTicks(bot.waitTicks).then(() => {
        res.json({ message: "Success" });
    });
});

// Server listening to PORT 3000

const DEFAULT_PORT = 3000;
const PORT = process.argv[2] || DEFAULT_PORT;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});



================================================
FILE: voyager/env/mineflayer/package.json
================================================
{
    "name": "voyager",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
        "body-parser": "^1.20.2",
        "express": "^4.18.2",
        "magic-string": "^0.30.0",
        "minecraft-data": "^3.31.0",
        "minecrafthawkeye": "^1.3.6",
        "mineflayer": "^4.8.1",
        "mineflayer-collectblock": "file:mineflayer-collectblock",
        "mineflayer-pathfinder": "^2.4.2",
        "mineflayer-pvp": "^1.3.2",
        "mineflayer-tool": "^1.2.0",
        "mocha": "^10.2.0",
        "prismarine-biome": "^1.3.0",
        "prismarine-block": "=1.16.3",
        "prismarine-entity": "^2.2.0",
        "prismarine-item": "^1.12.1",
        "prismarine-nbt": "^2.2.1",
        "prismarine-recipe": "^1.3.1",
        "prismarine-viewer": "^1.24.0",
        "typescript": "^4.9.5",
        "vec3": "^0.1.8",
        "graceful-fs": "^4.2.11"
    },
    "devDependencies": {
        "prettier": "2.8.5"
    }
}



================================================
FILE: voyager/env/mineflayer/.prettierignore
================================================
# Ignore artifacts:
build
coverage


================================================
FILE: voyager/env/mineflayer/.prettierrc.json
================================================
{
    "tabWidth": 4
}



================================================
FILE: voyager/env/mineflayer/lib/skillLoader.js
================================================
function inject(bot) {
    bot._sleep = bot.sleep;
    bot.sleep = async (bedBlock) => {
        await bot.waitForTicks(20);
        await bot._sleep(bedBlock);
        await bot.waitForTicks(135);
    };

    bot._fish = bot.fish;
    bot.fish = async () => {
        if (bot.heldItem?.name !== "fishing_rod") {
            bot.chat("I'm not holding a fishing rod!");
            return;
        }
        let timeout = null;
        await Promise.race([
            bot._fish(),
            new Promise(
                (resolve, reject) =>
                    (timeout = setTimeout(() => {
                        bot.activateItem();
                        reject(
                            new Error(
                                "Finishing timeout, make sure you get to and look at a water block!"
                            )
                        );
                    }, 60000))
            ),
        ]);
        clearTimeout(timeout);
        await bot.waitForTicks(20);
    };

    bot._consume = bot.consume;
    bot.consume = async () => {
        // action_count.activateItem++;
        await bot._consume();
        await bot.waitForTicks(20);
    };

    bot._useOn = bot.useOn;
    bot.useOn = async (entity) => {
        if (entity.position.distanceTo(bot.entity.position) > 6) {
            bot.chat("Please goto a place near the entity first!");
            return;
        }
        await bot._useOn(entity);
        await bot.waitForTicks(20);
    };

    bot._activateBlock = bot.activateBlock;
    bot.activateBlock = async (block) => {
        if (block.position.distanceTo(bot.entity.position) > 6) {
            bot.chat("Please goto a place near the block first!");
            return;
        }
        // action_count.activateBlock++;
        await bot._activateBlock(block);
    };

    bot._chat = bot.chat;
    bot.chat = (message) => {
        // action_count.chat++;
        bot.emit("chatEvent", "bot", message);
        bot._chat(message);
    };

    bot.inventoryUsed = () => {
        return bot.inventory.slots.slice(9, 45).filter((item) => item !== null)
            .length;
    };

    bot.save = function (eventName) {
        bot.emit("save", eventName);
    };
}

// export all control_primitives
module.exports = { inject };



================================================
FILE: voyager/env/mineflayer/lib/utils.js
================================================
let gameTimeCounter = 0;
let gameTimeList = [];
const initCounter = (bot) => {
    gameTimeList = [];
    for (let i = 0; i < 13000; i += 1000) {
        gameTimeList.push(i);
    }
    for (let i = 13000; i < 24000; i += 2000) {
        gameTimeList.push(i);
    }
    const timeOfDay = bot.time.timeOfDay;
    for (let i = 0; i < gameTimeList.length; i++) {
        if (gameTimeList[i] > timeOfDay) {
            gameTimeCounter = i - 1;
            break;
        }
    }
};

const getNextTime = () => {
    gameTimeCounter++;
    if (gameTimeCounter >= gameTimeList.length) {
        gameTimeCounter = 0;
    }
    return gameTimeList[gameTimeCounter];
};

module.exports = {
    initCounter,
    getNextTime,
};



================================================
FILE: voyager/env/mineflayer/lib/observation/base.js
================================================
class Observation {
    constructor(bot) {
        if (new.target === Observation) {
            throw new TypeError(
                "Cannot instantiate abstract class Observation"
            );
        }

        this.bot = bot;
        this.name = "Observation";
    }

    observe() {
        throw new TypeError("Method 'observe()' must be implemented.");
    }

    reset() {}
}

function inject(bot, obs_list) {
    bot.obsList = [];
    bot.cumulativeObs = [];
    bot.eventMemory = {};
    obs_list.forEach((obs) => {
        bot.obsList.push(new obs(bot));
    });
    bot.event = function (event_name) {
        let result = {};
        bot.obsList.forEach((obs) => {
            if (obs.name.startsWith("on") && obs.name !== event_name) {
                return;
            }
            result[obs.name] = obs.observe();
        });
        bot.cumulativeObs.push([event_name, result]);
    };
    bot.observe = function () {
        bot.event("observe");
        const result = bot.cumulativeObs;
        bot.cumulativeObs = [];
        return JSON.stringify(result);
    };
}

module.exports = { Observation, inject };



================================================
FILE: voyager/env/mineflayer/lib/observation/chests.js
================================================
const { Observation } = require("./base");

class Chests extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "nearbyChests";
        this.chestsItems = {};
        bot.on("closeChest", (chestItems, position) => {
            this.chestsItems[position] = chestItems;
        });
        bot.on("removeChest", (chestPosition) => {
            this.chestsItems[chestPosition] = "Invalid";
        });
    }

    observe() {
        const chests = this.bot.findBlocks({
            matching: this.bot.registry.blocksByName.chest.id,
            maxDistance: 16,
            count: 999,
        });
        chests.forEach((chest) => {
            if (!this.chestsItems.hasOwnProperty(chest)) {
                this.chestsItems[chest] = "Unknown";
            }
        });
        return this.chestsItems;
    }
}

module.exports = Chests;



================================================
FILE: voyager/env/mineflayer/lib/observation/inventory.js
================================================
const { Observation } = require("./base");

class Inventory extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "inventory";
    }

    observe() {
        return listItems(this.bot);
    }
}

function listItems(bot) {
    const items = getInventoryItems(bot);
    return items.reduce(itemToDict, {});
}

function getInventoryItems(bot) {
    const inventory = bot.currentWindow || bot.inventory;
    return inventory.items();
}

function itemToDict(acc, cur) {
    if (cur.name && cur.count) {
        //if both name and count property are defined
        if (acc[cur.name]) {
            //if the item is already in the dict
            acc[cur.name] += cur.count;
        } else {
            //if the item is not in the dict
            acc[cur.name] = cur.count;
        }
    }
    return acc;
}

//export modules
module.exports = Inventory;



================================================
FILE: voyager/env/mineflayer/lib/observation/onChat.js
================================================
const Observation = require("./base.js").Observation;

class onChat extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "onChat";
        this.obs = "";
        bot.on("chatEvent", (username, message) => {
            // Save entity status to local variable
            if (message.startsWith("/")) {
                return;
            }

            this.obs += message;
            this.bot.event(this.name);
        });
    }

    observe() {
        const result = this.obs;
        this.obs = "";
        return result;
    }
}

module.exports = onChat;



================================================
FILE: voyager/env/mineflayer/lib/observation/onError.js
================================================
const Observation = require("./base.js").Observation;

class onError extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "onError";
        this.obs = null;
        bot.on("error", (err) => {
            // Save entity status to local variable
            this.obs = err;
            this.bot.event(this.name);
        });
    }

    observe() {
        const result = this.obs;
        this.obs = null;
        return result;
    }
}

module.exports = onError;



================================================
FILE: voyager/env/mineflayer/lib/observation/onSave.js
================================================
const Observation = require("./base.js").Observation;

class onSave extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "onSave";
        this.obs = null;
        bot.on("save", (eventName) => {
            // Save entity status to local variable
            this.obs = eventName;
            this.bot.event(this.name);
        });
    }

    observe() {
        const result = this.obs;
        this.obs = null;
        return result;
    }
}

module.exports = onSave;



================================================
FILE: voyager/env/mineflayer/lib/observation/status.js
================================================
const Observation = require("./base.js").Observation;

class Status extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "status";
    }

    observe() {
        return {
            health: this.bot.health,
            food: this.bot.food,
            saturation: this.bot.foodSaturation,
            oxygen: this.bot.oxygenLevel,
            position: this.bot.entity.position,
            velocity: this.bot.entity.velocity,
            yaw: this.bot.entity.yaw,
            pitch: this.bot.entity.pitch,
            onGround: this.bot.entity.onGround,
            equipment: this.getEquipment(),
            name: this.bot.entity.username,
            timeSinceOnGround: this.bot.entity.timeSinceOnGround,
            isInWater: this.bot.entity.isInWater,
            isInLava: this.bot.entity.isInLava,
            isInWeb: this.bot.entity.isInWeb,
            isCollidedHorizontally: this.bot.entity.isCollidedHorizontally,
            isCollidedVertically: this.bot.entity.isCollidedVertically,
            biome: this.bot.blockAt(this.bot.entity.position)
                ? this.bot.blockAt(this.bot.entity.position).biome.name
                : "None",
            entities: this.getEntities(),
            timeOfDay: this.getTime(),
            inventoryUsed: this.bot.inventoryUsed(),
            elapsedTime: this.bot.globalTickCounter,
        };
    }

    itemToObs(item) {
        if (!item) return null;
        return item.name;
    }

    getTime() {
        const timeOfDay = this.bot.time.timeOfDay;
        let time = "";
        if (timeOfDay < 1000) {
            time = "sunrise";
        } else if (timeOfDay < 6000) {
            time = "day";
        } else if (timeOfDay < 12000) {
            time = "noon";
        } else if (timeOfDay < 13000) {
            time = "sunset";
        } else if (timeOfDay < 18000) {
            time = "night";
        } else if (timeOfDay < 22000) {
            time = "midnight";
        } else {
            time = "sunrise";
        }
        return time;
    }

    // For each item in equipment, if it exists, return the name of the item
    // otherwise return null
    getEquipment() {
        const slots = this.bot.inventory.slots;
        const mainHand = this.bot.heldItem;
        return slots
            .slice(5, 9)
            .concat(mainHand, slots[45])
            .map(this.itemToObs);
    }

    getEntities() {
        const entities = this.bot.entities;
        if (!entities) return {};
        // keep all monsters in one list, keep other mobs in another list
        const mobs = {};
        for (const id in entities) {
            const entity = entities[id];
            if (!entity.displayName) continue;
            if (entity.name === "player" || entity.name === "item") continue;
            if (entity.position.distanceTo(this.bot.entity.position) < 32) {
                if (!mobs[entity.name]) {
                    mobs[entity.name] = entity.position.distanceTo(
                        this.bot.entity.position
                    );
                } else if (
                    mobs[entity.name] >
                    entity.position.distanceTo(this.bot.entity.position)
                ) {
                    mobs[entity.name] = entity.position.distanceTo(
                        this.bot.entity.position
                    );
                }
            }
        }
        return mobs;
    }
}

module.exports = Status;



================================================
FILE: voyager/env/mineflayer/lib/observation/voxels.js
================================================
// Blocks = require("./blocks")
const { Observation } = require("./base");

class Voxels extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "voxels";
    }

    observe() {
        return Array.from(getSurroundingBlocks(this.bot, 8, 2, 8));
    }
}

class BlockRecords extends Observation {
    constructor(bot) {
        super(bot);
        this.name = "blockRecords";
        this.records = new Set();
        this.tick = 0;
        bot.on("physicsTick", () => {
            this.tick++;
            if (this.tick >= 100) {
                const items = getInventoryItems(this.bot);
                getSurroundingBlocks(this.bot, 8, 2, 8).forEach((block) => {
                    if (!items.has(block)) this.records.add(block);
                });
                this.tick = 0;
            }
        });
    }

    observe() {
        return Array.from(this.records);
    }

    reset() {
        this.records = new Set();
    }
}

function getSurroundingBlocks(bot, x_distance, y_distance, z_distance) {
    const surroundingBlocks = new Set();

    for (let x = -x_distance; x <= x_distance; x++) {
        for (let y = -y_distance; y <= y_distance; y++) {
            for (let z = -z_distance; z <= z_distance; z++) {
                const block = bot.blockAt(bot.entity.position.offset(x, y, z));
                if (block && block.type !== 0) {
                    surroundingBlocks.add(block.name);
                }
            }
        }
    }
    // console.log(surroundingBlocks);
    return surroundingBlocks;
}

function getInventoryItems(bot) {
    const items = new Set();
    bot.inventory.items().forEach((item) => {
        if (item) items.add(item.name);
    });
    return items;
}

module.exports = { Voxels, BlockRecords };



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/README.md
================================================
<h1 align="center">mineflayer-collectblock</h1>
<p align="center"><i>A small utility plugin for allowing users to collect blocks using a higher level API.</i></p>

<p align="center">
  <img src="https://github.com/TheDudeFromCI/mineflayer-collectblock/workflows/Build/badge.svg" />
  <a href="https://www.npmjs.com/package/mineflayer-collectblock"><img src="https://img.shields.io/npm/v/mineflayer-collectblock" /></a>
  <img src="https://img.shields.io/github/repo-size/TheDudeFromCI/mineflayer-collectblock" />
  <img src="https://img.shields.io/npm/dm/mineflayer-collectblock" />
  <img src="https://img.shields.io/github/contributors/TheDudeFromCI/mineflayer-collectblock" />
  <img src="https://img.shields.io/github/license/TheDudeFromCI/mineflayer-collectblock" />
</p>

---
## This is a modified version to better support Voyager

## Showcase

You can see a video of the plugin in action, [here.](https://youtu.be/5T_rcCnNnf4)
The source code of the bot in the video can be seen in the examples folder, [here.](https://github.com/TheDudeFromCI/mineflayer-collectblock/blob/master/examples/collector.js)

### Description

This plugin is a wrapper for mineflayer that allows for easier API usage when collecting blocks or item drops. This plugin is designed to reduce some of the boilerplate code based around the act of pathfinding to a block _(handled by_ ***mineflayer-pathfinder***_)_, selecting the best tool to mine that block _(handled by_ ***mineflayer-tool***_)_, actually mining it, then moving to collect the item drops from that block. This plugin allows for all of that basic concept to be wrapped up into a single API function.

In addition to the usage above, some additional quality of life features are available in this plugin. These include the ability to automatically deposit items into a chest when the bot's inventory is full, collecting new tools from a chest if the bot doesn't currently have a required tool _(also handled by_ ***mineflayer-tool***_)_, and allowing for queueing of multiple blocks or item drops to the collection task, so they can be processed later.

### Getting Started

This plugin is built using Node and can be installed using:
```bash
npm install --save mineflayer-collectblock
```

### Simple Bot

The brief description goes here.

```js
// Create your bot
const mineflayer = require("mineflayer")
const bot = mineflayer.createBot({
  host: 'localhost',
  username: 'Player',
})
let mcData

// Load collect block
bot.loadPlugin(require('mineflayer-collectblock').plugin)

async function collectGrass() {
  // Find a nearby grass block
  const grass = bot.findBlock({
    matching: mcData.blocksByName.grass_block.id,
    maxDistance: 64
  })

  if (grass) {
    // If we found one, collect it.
    try {
      await bot.collectBlock.collect(grass)
      collectGrass() // Collect another grass block
    } catch (err) {
      console.log(err) // Handle errors, if any
    }
  }
}

// On spawn, start collecting all nearby grass
bot.once('spawn', () => {
  mcData = require('minecraft-data')(bot.version)
  collectGrass()
})
```

### Documentation

[API](https://github.com/TheDudeFromCI/mineflayer-collectblock/blob/master/docs/api.md)

[Examples](https://github.com/TheDudeFromCI/mineflayer-collectblock/tree/master/examples)

### License

This project uses the [MIT](https://github.com/TheDudeFromCI/mineflayer-collectblock/blob/master/LICENSE) license.

### Contributions

This project is accepting PRs and Issues. See something you think can be improved? Go for it! Any and all help is highly appreciated!

For larger changes, it is recommended to discuss these changes in the issues tab before writing any code. It's also preferred to make many smaller PRs than one large one, where applicable.



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/_config.yml
================================================
theme: jekyll-theme-cayman


================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/LICENSE
================================================
MIT License

Copyright (c) 2020 TheDudeFromCI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/package.json
================================================
{
  "name": "mineflayer-collectblock",
  "version": "1.4.1",
  "description": "A simple utility plugin for Mineflayer that add a higher level API for collecting blocks.",
  "main": "lib/index.js",
  "types": "lib/index.d.ts",
  "scripts": {
    "build": "ts-standard && tsc && require-self",
    "clean": "rm -rf lib",
    "test": "test"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/TheDudeFromCI/mineflayer-collectblock.git"
  },
  "keywords": [
    "mineflayer",
    "plugin",
    "api",
    "utility",
    "helper",
    "collect"
  ],
  "author": "TheDudeFromCI",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/TheDudeFromCI/mineflayer-collectblock/issues"
  },
  "homepage": "https://github.com/TheDudeFromCI/mineflayer-collectblock#readme",
  "dependencies": {
    "mineflayer": "^4.0.0",
    "mineflayer-pathfinder": "^2.1.1",
    "mineflayer-tool": "^1.1.0"
  },
  "devDependencies": {
    "@types/node": "^18.6.4",
    "require-self": "^0.2.3",
    "ts-standard": "^11.0.0",
    "typescript": "^4.1.3"
  },
  "files": [
    "lib/**/*"
  ]
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/tsconfig.json
================================================
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */
    /* Basic Options */
    // "incremental": true,                   /* Enable incremental compilation */
    "target": "ES2015", /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', or 'ESNEXT'. */
    "module": "commonjs", /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', or 'ESNext'. */
    // "lib": [],                             /* Specify library files to be included in the compilation. */
    "allowJs": true, /* Allow javascript files to be compiled. */
    "checkJs": true, /* Report errors in .js files. */
    // "jsx": "preserve",                     /* Specify JSX code generation: 'preserve', 'react-native', or 'react'. */
    "declaration": true,
    // "declarationMap": true,                /* Generates a sourcemap for each corresponding '.d.ts' file. */
    // "sourceMap": true,                     /* Generates corresponding '.map' file. */
    // "outFile": "./",                       /* Concatenate and emit output to single file. */
    "outDir": "./lib",
    // "rootDir": "./",                       /* Specify the root directory of input files. Use to control the output directory structure with --outDir. */
    // "composite": true,                     /* Enable project compilation */
    // "tsBuildInfoFile": "./",               /* Specify file to store incremental compilation information */
    // "removeComments": true,                /* Do not emit comments to output. */
    // "noEmit": true,                        /* Do not emit outputs. */
    // "importHelpers": true,                 /* Import emit helpers from 'tslib'. */
    // "downlevelIteration": true,            /* Provide full support for iterables in 'for-of', spread, and destructuring when targeting 'ES5' or 'ES3'. */
    // "isolatedModules": true,               /* Transpile each file as a separate module (similar to 'ts.transpileModule'). */
    /* Strict Type-Checking Options */
    "strict": true, /* Enable all strict type-checking options. */
    // "noImplicitAny": true,                 /* Raise error on expressions and declarations with an implied 'any' type. */
    "strictNullChecks": true, /* Enable strict null checks. */
    // "strictFunctionTypes": true,           /* Enable strict checking of function types. */
    // "strictBindCallApply": true,           /* Enable strict 'bind', 'call', and 'apply' methods on functions. */
    // "strictPropertyInitialization": true,  /* Enable strict checking of property initialization in classes. */
    // "noImplicitThis": true,                /* Raise error on 'this' expressions with an implied 'any' type. */
    "alwaysStrict": true, /* Parse in strict mode and emit "use strict" for each source file. */
    /* Additional Checks */
    "noUnusedLocals": true, /* Report errors on unused locals. */
    // "noUnusedParameters": true,            /* Report errors on unused parameters. */
    "noImplicitReturns": true, /* Report error when not all code paths in function return a value. */
    // "noFallthroughCasesInSwitch": true,    /* Report errors for fallthrough cases in switch statement. */
    /* Module Resolution Options */
    // "moduleResolution": "node",            /* Specify module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6). */
    // "baseUrl": "./",                       /* Base directory to resolve non-absolute module names. */
    // "paths": {},                           /* A series of entries which re-map imports to lookup locations relative to the 'baseUrl'. */
    // "rootDirs": [],                        /* List of root folders whose combined content represents the structure of the project at runtime. */
    // "typeRoots": [],                       /* List of folders to include type definitions from. */
    // "types": [],                           /* Type declaration files to be included in compilation. */
    // "allowSyntheticDefaultImports": true,  /* Allow default imports from modules with no default export. This does not affect code emit, just typechecking. */
    "esModuleInterop": true, /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */
    // "preserveSymlinks": true,              /* Do not resolve the real path of symlinks. */
    // "allowUmdGlobalAccess": true,          /* Allow accessing UMD globals from modules. */
    /* Source Map Options */
    // "sourceRoot": "",                      /* Specify the location where debugger should locate TypeScript files instead of source locations. */
    // "mapRoot": "",                         /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSourceMap": true,               /* Emit a single file with source maps instead of having a separate file. */
    // "inlineSources": true,                 /* Emit the source alongside the sourcemaps within a single file; requires '--inlineSourceMap' or '--sourceMap' to be set. */
    /* Experimental Options */
    // "experimentalDecorators": true,        /* Enables experimental support for ES7 decorators. */
    // "emitDecoratorMetadata": true,         /* Enables experimental support for emitting type metadata for decorators. */
    /* Advanced Options */
    "skipLibCheck": true, /* Skip type checking of declaration files. */
    "forceConsistentCasingInFileNames": true /* Disallow inconsistently-cased references to the same file. */
  },
  "include": [
    "src"
  ],
  "exclude": [
    "node_modules",
    "**/__tests__/*"
  ]
}


================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/.gitignore
================================================
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# TypeScript v1 declaration files
typings/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env
.env.test

# parcel-bundler cache (https://parceljs.org/)
.cache

# Next.js build output
.next

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
# Comment in the public line in if your project uses Gatsby and *not* Next.js
# https://nextjs.org/blog/next-9-1#public-directory-support
# public

# vuepress build output
.vuepress/dist

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

lib/
package-lock.json



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/docs/api.md
================================================
# API <!-- omit in toc -->

Welcome to the *mineflayer-collectblock* API documentation page.

## Table of Contents <!-- omit in toc -->

- [1. Summary](#1-summary)
- [Properties](#properties)
  - [`bot.collectblock.movements: Movements`](#botcollectblockmovements-movements)
- [Functions](#functions)
  - [collect](#collect)
    - [Options:](#options)

## 1. Summary

The collect block plugin is a utility plugin that can be used to help make collecting blocks and item drops very easy, using only a single API call. No need to worry about pathfinding to the block, selecting the right tool, or moving to pick up the item drop after mining.

## Properties

### `bot.collectblock.movements: Movements`

The movements object used by the pathfinder plugin to define the movement configuration. This object is passed to the pathfinder plugin when any API from this plugin is called in order to control how pathfinding should work when collecting the given blocks or item.

If set to null, the pathfinder plugin movements is not updated.

Defaults to a new movements object instance.

## Functions

### collect

Usage: `bot.collectblock.collect(target: Collectable | Collectable[], options?: CollectOptions, cb: (err?: Error) => void): void`

Causes the bot to collect the given block, item drop, or list of those. If the target is a block, the bot will move to the block, mine it, and pick up the item drop. If the target is an item drop, the bot will move to the item drop and pick it up. If the target is a list of collectables, the bot will move from target to target in order of closest to furthest and collect each target in turn.

#### Options:

  * `append: boolean`

    If true, the target(s) will be appended to the existing target list instead of starting a new task. Defaults to false.

  * `ignoreNoPath: boolean`

    If true, errors will not be thrown when a path to the target block cannot be found. The bot will attempt to choose the best available position it can find, instead. Errors are still thrown if the bot cannot interact with the block from it's final location. Defaults to false.

  * `chestLocations: Vec3[]`

    Gets the list of chest locations to use when storing items after the bot's inventory becomes full. If undefined, it defaults to the chest location list on the bot.collectBlock plugin.

  * `itemFilter: ItemFilter`

    When transferring items to a chest, this filter is used to determine what items are allowed to be moved, and what items aren't allowed to be moved. Defaults to the item filter specified on the bot.collectBlock plugin.


================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/examples/collector.js
================================================
/**
 * This bot example show how to direct a bot to collect a specific block type
 * or a group of nearby blocks of that type.
 */

const mineflayer = require('mineflayer')
const collectBlock = require('mineflayer-collectblock').plugin

if (process.argv.length < 4 || process.argv.length > 6) {
  console.log('Usage : node collector.js <host> <port> [<name>] [<password>]')
  process.exit(1)
}

const bot = mineflayer.createBot({
  host: process.argv[2],
  port: process.argv[3],
  username: process.argv[4] || 'collector',
  password: process.argv[5]
})

bot.loadPlugin(collectBlock)

let mcData
bot.once('spawn', () => {
  mcData = require('minecraft-data')(bot.version)
})

bot.on('chat', async (username, message) => {
  const args = message.split(' ')
  if (args[0] !== 'collect') return

  let count = 1
  if (args.length === 3) count = parseInt(args[1])

  let type = args[1]
  if (args.length === 3) type = args[2]

  const blockType = mcData.blocksByName[type]
  if (!blockType) {
    return
  }

  const blocks = bot.findBlocks({
    matching: blockType.id,
    maxDistance: 64,
    count: count
  })

  if (blocks.length === 0) {
    bot.chat("I don't see that block nearby.")
    return
  }

  const targets = []
  for (let i = 0; i < Math.min(blocks.length, count); i++) {
    targets.push(bot.blockAt(blocks[i]))
  }

  bot.chat(`Found ${targets.length} ${type}(s)`)

  try {
    await bot.collectBlock.collect(targets)
    // All blocks have been collected.
    bot.chat('Done')
  } catch (err) {
    // An error occurred, report it.
    bot.chat(err.message)
    console.log(err)
  }
})



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/examples/oreMiner.js
================================================
/**
 * This bot example shows how to collect a vein of ores quickly after only finding a single block.
 * This makes it easy to collect a vein of ores or mine a tree without looking for every block in the
 * area.
 */

const mineflayer = require('mineflayer')
const collectBlock = require('mineflayer-collectblock').plugin

if (process.argv.length < 4 || process.argv.length > 6) {
  console.log('Usage : node oreMiner.js <host> <port> [<name>] [<password>]')
  process.exit(1)
}

const bot = mineflayer.createBot({
  host: process.argv[2],
  port: process.argv[3],
  username: process.argv[4] || 'oreMiner',
  password: process.argv[5]
})

bot.loadPlugin(collectBlock)

let mcData
bot.once('spawn', () => {
  mcData = require('minecraft-data')(bot.version)
})

bot.on('chat', async (username, message) => {
  const args = message.split(' ')
  if (args[0] !== 'collect') return

  const blockType = mcData.blocksByName[args[1]]
  if (!blockType) {
    bot.chat(`I don't know any blocks named ${args[1]}.`)
    return
  }

  const block = bot.findBlock({
    matching: blockType.id,
    maxDistance: 64
  })

  if (!block) {
    bot.chat("I don't see that block nearby.")
    return
  }

  const targets = bot.collectBlock.findFromVein(block)
  try {
    await bot.collectBlock.collect(targets)
    // All blocks have been collected.
    bot.chat('Done')
  } catch (err) {
    // An error occurred, report it.
    bot.chat(err.message)
    console.log(err)
  }
})



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/examples/storageBot.js
================================================
/**
 * This bot example shows how to use the chest filling mechanic of the plugin.
 * Simply provide a given storage chest, and the bot will automatically try and
 * store it's inventory in that chest when the bot's inventory becomes full.
 */

if (process.argv.length < 4 || process.argv.length > 6) {
  console.log('Usage : node storageBot.js <host> <port> [<name>] [<password>]')
  process.exit(1)
}

// Load your libraries
const mineflayer = require('mineflayer')
const collectBlock = require('mineflayer-collectblock').plugin

// Create your bot
const bot = mineflayer.createBot({
  host: process.argv[2],
  port: parseInt(process.argv[3]),
  username: process.argv[4] ? process.argv[4] : 'storageBot',
  password: process.argv[5]
})

// Load the collect block plugin
bot.loadPlugin(collectBlock)

// Load mcData on login
let mcData
bot.once('login', () => {
  mcData = require('minecraft-data')(bot.version)
})

// On spawn, try to find any nearby chests and save those as storage locations.
// When the bot's inventory becomes too full, it will empty it's inventory into
// these chests before collecting more resources. If a chest gets full, it moves
// to the next one in order until it's inventory is empty or it runs out of chests.
bot.once('spawn', () => {
  bot.collectBlock.chestLocations = bot.findBlocks({
    matching: mcData.blocksByName.chest.id,
    maxDistance: 16,
    count: 999999 // Get as many chests as we can
  })

  if (bot.collectBlock.chestLocations.length === 0) {
    bot.chat("I don't see any chests nearby.")
  } else {
    for (const chestPos of bot.collectBlock.chestLocations) {
      bot.chat(`I found a chest at ${chestPos}`)
    }
  }
})

// Wait for someone to say something
bot.on('chat', async (username, message) => {
  // If the player says something start starts with "collect"
  // Otherwise, do nothing
  const args = message.split(' ')
  if (args[0] !== 'collect') return

  // If the player specifies a number, collect that many. Otherwise, default to 1.
  let count = 1
  if (args.length === 3) count = parseInt(args[1])

  // If a number was given the item number is the 3rd arg, not the 2nd.
  let type = args[1]
  if (args.length === 3) type = args[2]

  // Get the id of that block type for this version of Minecraft.
  const blockType = mcData.blocksByName[type]
  if (!blockType) {
    bot.chat(`I don't know any blocks named ${type}.`)
    return
  }

  // Find all nearby blocks of that type, up to the given count, within 64 blocks.
  const blocks = bot.findBlocks({
    matching: blockType.id,
    maxDistance: 64,
    count: count
  })

  // Complain if we can't find any nearby blocks of that type.
  if (blocks.length === 0) {
    bot.chat("I don't see that block nearby.")
    return
  }

  // Convert the block position array into a block array to pass to collect block.
  const targets = []
  for (let i = 0; i < Math.min(blocks.length, count); i++) {
    targets.push(bot.blockAt(blocks[i]))
  }

  // Announce what we found.
  bot.chat(`Found ${targets.length} ${type}(s)`)

  // Tell the bot to collect all of the given blocks in the block list.
  try {
    await bot.collectBlock.collect(targets)
    // All blocks have been collected.
    bot.chat('Done')
  } catch (err) {
    // An error occurred, report it.
    bot.chat(err.message)
    console.log(err)
  }
})



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/BlockVeins.ts
================================================
import { Bot } from 'mineflayer'
import { Block } from 'prismarine-block'

export function findFromVein (bot: Bot, block: Block, maxBlocks: number, maxDistance: number, floodRadius: number): Block[] {
  const targets: Block[] = []
  const open: Block[] = [block]
  const type = block.type
  const center = block.position

  for (let i = 0; i < maxBlocks; i++) {
    const next = open.pop()
    if (next == null) break

    targets.push(next)

    for (let x = -floodRadius; x <= floodRadius; x++) {
      for (let y = -floodRadius; y <= floodRadius; y++) {
        for (let z = -floodRadius; z <= floodRadius; z++) {
          const neighborPos = next.position.offset(x, y, z)
          if (neighborPos.manhattanDistanceTo(center) > maxDistance) continue

          const neighbor = bot.blockAt(neighborPos)
          if (neighbor == null || neighbor.type !== type) continue

          if (targets.includes(neighbor)) continue
          if (open.includes(neighbor)) continue

          open.push(neighbor)
        }
      }
    }
  }

  return targets
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/CollectBlock.ts
================================================
import { Bot } from "mineflayer";
import { Block } from "prismarine-block";
import { Movements, goals } from "mineflayer-pathfinder";
import { TemporarySubscriber } from "./TemporarySubscriber";
import { Entity } from "prismarine-entity";
import { error } from "./Util";
import { Vec3 } from "vec3";
import { emptyInventoryIfFull, ItemFilter } from "./Inventory";
import { findFromVein } from "./BlockVeins";
import { Collectable, Targets } from "./Targets";
import { Item } from "prismarine-item";
import mcDataLoader from "minecraft-data";
import { once } from "events";
import { callbackify } from "util";

export type Callback = (err?: Error) => void;

async function collectAll(
    bot: Bot,
    options: CollectOptionsFull
): Promise<void> {
    let success_count = 0;
    while (!options.targets.empty) {
        await emptyInventoryIfFull(
            bot,
            options.chestLocations,
            options.itemFilter
        );
        const closest = options.targets.getClosest();
        if (closest == null) break;
        switch (closest.constructor.name) {
            case "Block": {
                try {
                    if (success_count >= options.count) {
                        break;
                    }
                    await bot.tool.equipForBlock(
                        closest as Block,
                        equipToolOptions
                    );
                    const goal = new goals.GoalLookAtBlock(
                        closest.position,
                        bot.world
                    );
                    await bot.pathfinder.goto(goal);
                    await mineBlock(bot, closest as Block, options);
                    success_count++;
                    // TODO: options.ignoreNoPath
                } catch (err) {
                    // @ts-ignore
                    // console.log(err.stack)
                    // bot.pathfinder.stop()
                    // bot.waitForTicks(10)
                    try {
                        bot.pathfinder.setGoal(null);
                    } catch (err) {}
                    if (options.ignoreNoPath) {
                        // @ts-ignore
                        if (err.name === "Invalid block") {
                            console.log(
                                `Block ${closest.name} at ${closest.position} is not valid! Skip it!`
                            );
                        } // @ts-ignore
                        else if (err.name === "Unsafe block") {
                            console.log(
                                `${closest.name} at ${closest.position} is not safe to break! Skip it!`
                            );
                            // @ts-ignore
                        } else if (err.name === "NoItem") {
                            const properties =
                                bot.registry.blocksByName[closest.name];
                            const leastTool = Object.keys(
                                properties.harvestTools
                            )[0];
                            const item = bot.registry.items[leastTool];
                            bot.chat(
                                `I need at least a ${item.name} to mine ${closest.name}!  Skip it!`
                            );
                            return;
                        } else if (
                            // @ts-ignore
                            err.name === "NoPath" ||
                            // @ts-ignore
                            err.name === "Timeout"
                        ) {
                            if (
                                bot.entity.position.distanceTo(
                                    closest.position
                                ) < 0.5
                            ) {
                                await mineBlock(bot, closest as Block, options);
                                break;
                            }
                            console.log(
                                `No path to ${closest.name} at ${closest.position}! Skip it!`
                            );
                            // @ts-ignore
                        } else if (err.message === "Digging aborted") {
                            console.log(`Digging aborted! Skip it!`);
                        } else {
                            // @ts-ignore
                            bot.chat(`Error: ${err.message}`);
                        }
                        break;
                    }
                    throw err;
                }
                break;
            }
            case "Entity": {
                // Don't collect any entities that are marked as 'invalid'
                if (!(closest as Entity).isValid) break;
                try {
                    const tempEvents = new TemporarySubscriber(bot);
                    const waitForPickup = new Promise<void>(
                        (resolve, reject) => {
                            const timeout = setTimeout(() => {
                                // After 10 seconds, reject the promise
                                clearTimeout(timeout);
                                tempEvents.cleanup();
                                reject(new Error("Failed to pickup item"));
                            }, 10000);
                            tempEvents.subscribeTo(
                                "entityGone",
                                (entity: Entity) => {
                                    if (entity === closest) {
                                        clearTimeout(timeout);
                                        tempEvents.cleanup();
                                        resolve();
                                    }
                                }
                            );
                        }
                    );
                    bot.pathfinder.setGoal(
                        new goals.GoalFollow(closest as Entity, 0)
                    );
                    // await bot.pathfinder.goto(new goals.GoalBlock(closest.position.x, closest.position.y, closest.position.z))
                    await waitForPickup;
                } catch (err) {
                    // @ts-ignore
                    console.log(err.stack);
                    try {
                        bot.pathfinder.setGoal(null);
                    } catch (err) {}
                    if (options.ignoreNoPath) {
                        // @ts-ignore
                        if (err.message === "Failed to pickup item") {
                            bot.chat(`Failed to pickup item! Skip it!`);
                        }
                        break;
                    }
                    throw err;
                }
                break;
            }
            default: {
                throw error(
                    "UnknownType",
                    `Target ${closest.constructor.name} is not a Block or Entity!`
                );
            }
        }
        options.targets.removeTarget(closest);
    }
    bot.chat(`Collect finish!`);
}

const equipToolOptions = {
    requireHarvest: true,
    getFromChest: false,
    maxTools: 2,
};

async function mineBlock(
    bot: Bot,
    block: Block,
    options: CollectOptionsFull
): Promise<void> {
    if (
        bot.blockAt(block.position)?.type !== block.type ||
        bot.blockAt(block.position)?.type === 0
    ) {
        options.targets.removeTarget(block);
        throw error("Invalid block", "Block is not valid!");
        // @ts-expect-error
    } else if (!bot.pathfinder.movements.safeToBreak(block)) {
        options.targets.removeTarget(block);
        throw error("Unsafe block", "Block is not safe to break!");
    }

    await bot.tool.equipForBlock(block, equipToolOptions);

    if (!block.canHarvest(bot.heldItem ? bot.heldItem.type : bot.heldItem)) {
        options.targets.removeTarget(block);
        throw error("NoItem", "Bot does not have a harvestable tool!");
    }

    const tempEvents = new TemporarySubscriber(bot);
    tempEvents.subscribeTo("itemDrop", (entity: Entity) => {
        if (
            entity.position.distanceTo(block.position.offset(0.5, 0.5, 0.5)) <=
            0.5
        ) {
            options.targets.appendTarget(entity);
        }
    });
    try {
        await bot.dig(block);
        // Waiting for items to drop
        await new Promise<void>((resolve) => {
            let remainingTicks = 10;
            tempEvents.subscribeTo("physicTick", () => {
                remainingTicks--;
                if (remainingTicks <= 0) {
                    tempEvents.cleanup();
                    resolve();
                }
            });
        });
    } finally {
        tempEvents.cleanup();
    }
}

/**
 * A set of options to apply when collecting the given targets.
 */
export interface CollectOptions {
    /**
     * If true, the target(s) will be appended to the existing target list instead of
     * starting a new task. Defaults to false.
     */
    append?: boolean;

    /**
     * If true, errors will not be thrown when a path to the target block cannot
     * be found. The bot will attempt to choose the best available position it
     * can find, instead. Errors are still thrown if the bot cannot interact with
     * the block from it's final location. Defaults to false.
     */
    ignoreNoPath?: boolean;

    /**
     * Gets the list of chest locations to use when storing items after the bot's
     * inventory becomes full. If undefined, it defaults to the chest location
     * list on the bot.collectBlock plugin.
     */
    chestLocations?: Vec3[];

    /**
     * When transferring items to a chest, this filter is used to determine what
     * items are allowed to be moved, and what items aren't allowed to be moved.
     * Defaults to the item filter specified on the bot.collectBlock plugin.
     */
    itemFilter?: ItemFilter;

    /**
     * The total number of items to collect
     */
    count?: number;
}

/**
 * A version of collect options where all values are assigned.
 */
interface CollectOptionsFull {
    append: boolean;
    ignoreNoPath: boolean;
    chestLocations: Vec3[];
    itemFilter: ItemFilter;
    targets: Targets;
    count: number;
}

/**
 * The collect block plugin.
 */
export class CollectBlock {
    /**
     * The bot.
     */
    private readonly bot: Bot;

    /**
     * The list of active targets being collected.
     */
    private readonly targets: Targets;

    /**
     * The movements configuration to be sent to the pathfinder plugin.
     */
    movements?: Movements;

    /**
     * A list of chest locations which the bot is allowed to empty their inventory into
     * if it becomes full while the bot is collecting resources.
     */
    chestLocations: Vec3[] = [];

    /**
     * When collecting items, this filter is used to determine what items should be placed
     * into a chest if the bot's inventory becomes full. By default, returns true for all
     * items except for tools, weapons, and armor.
     *
     * @param item - The item stack in the bot's inventory to check.
     *
     * @returns True if the item should be moved into the chest. False otherwise.
     */
    itemFilter: ItemFilter = (item: Item) => {
        if (item.name.includes("helmet")) return false;
        if (item.name.includes("chestplate")) return false;
        if (item.name.includes("leggings")) return false;
        if (item.name.includes("boots")) return false;
        if (item.name.includes("shield")) return false;
        if (item.name.includes("sword")) return false;
        if (item.name.includes("pickaxe")) return false;
        if (item.name.includes("axe")) return false;
        if (item.name.includes("shovel")) return false;
        if (item.name.includes("hoe")) return false;
        return true;
    };

    /**
     * Creates a new instance of the create block plugin.
     *
     * @param bot - The bot this plugin is acting on.
     */
    constructor(bot: Bot) {
        this.bot = bot;
        this.targets = new Targets(bot);
        // @ts-ignore
        this.movements = new Movements(bot, mcDataLoader(bot.version));
    }

    /**
     * If target is a block:
     * Causes the bot to break and collect the target block.
     *
     * If target is an item drop:
     * Causes the bot to collect the item drop.
     *
     * If target is an array containing items or blocks, preforms the correct action for
     * all targets in that array sorting dynamically by distance.
     *
     * @param target - The block(s) or item(s) to collect.
     * @param options - The set of options to use when handling these targets
     * @param cb - The callback that is called finished.
     */
    async collect(
        target: Collectable | Collectable[],
        options: CollectOptions | Callback = {},
        cb?: Callback
    ): Promise<void> {
        if (typeof options === "function") {
            cb = options;
            options = {};
        }
        // @ts-expect-error
        if (cb != null) return callbackify(this.collect)(target, options, cb);

        const optionsFull: CollectOptionsFull = {
            append: options.append ?? false,
            ignoreNoPath: options.ignoreNoPath ?? false,
            chestLocations: options.chestLocations ?? this.chestLocations,
            itemFilter: options.itemFilter ?? this.itemFilter,
            targets: this.targets,
            count: options.count ?? Infinity,
        };

        if (this.bot.pathfinder == null) {
            throw error(
                "UnresolvedDependency",
                "The mineflayer-collectblock plugin relies on the mineflayer-pathfinder plugin to run!"
            );
        }

        if (this.bot.tool == null) {
            throw error(
                "UnresolvedDependency",
                "The mineflayer-collectblock plugin relies on the mineflayer-tool plugin to run!"
            );
        }

        if (this.movements != null) {
            this.bot.pathfinder.setMovements(this.movements);
        }

        if (!optionsFull.append) await this.cancelTask();
        if (Array.isArray(target)) {
            this.targets.appendTargets(target);
        } else {
            this.targets.appendTarget(target);
        }

        try {
            await collectAll(this.bot, optionsFull);
            this.targets.clear();
        } catch (err) {
            this.targets.clear();
            // Ignore path stopped error for cancelTask to work properly (imo we shouldn't throw any pathing errors)
            // @ts-expect-error
            if (err.name !== "PathStopped") throw err;
        } finally {
            // @ts-expect-error
            this.bot.emit("collectBlock_finished");
        }
    }

    /**
     * Loads all touching blocks of the same type to the given block and returns them as an array.
     * This effectively acts as a flood fill algorithm to retrieve blocks in the same ore vein and similar.
     *
     * @param block - The starting block.
     * @param maxBlocks - The maximum number of blocks to look for before stopping.
     * @param maxDistance - The max distance from the starting block to look.
     * @param floodRadius - The max distance distance from block A to block B to be considered "touching"
     */
    findFromVein(
        block: Block,
        maxBlocks = 100,
        maxDistance = 16,
        floodRadius = 1
    ): Block[] {
        return findFromVein(
            this.bot,
            block,
            maxBlocks,
            maxDistance,
            floodRadius
        );
    }

    /**
     * Cancels the current collection task, if still active.
     *
     * @param cb - The callback to use when the task is stopped.
     */
    async cancelTask(cb?: Callback): Promise<void> {
        if (this.targets.empty) {
            if (cb != null) cb();
            return await Promise.resolve();
        }
        this.bot.pathfinder.stop();
        if (cb != null) {
            // @ts-expect-error
            this.bot.once("collectBlock_finished", cb);
        }
        await once(this.bot, "collectBlock_finished");
    }
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/index.ts
================================================
import { Bot } from 'mineflayer'
import { CollectBlock } from './CollectBlock'
import { pathfinder as pathfinderPlugin } from 'mineflayer-pathfinder'
import { plugin as toolPlugin } from 'mineflayer-tool'

export function plugin (bot: Bot): void {
  // @ts-expect-error
  bot.collectBlock = new CollectBlock(bot)

  // Load plugins if not loaded manually.
  setTimeout(() => loadPathfinderPlugin(bot), 0)
  setTimeout(() => loadToolPlugin(bot), 0)
}

function loadPathfinderPlugin (bot: Bot): void {
  if (bot.pathfinder != null) return
  bot.loadPlugin(pathfinderPlugin)
}

function loadToolPlugin (bot: Bot): void {
  if (bot.tool != null) return
  bot.loadPlugin(toolPlugin)
}

export { CollectBlock, Callback, CollectOptions } from './CollectBlock'



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/Inventory.ts
================================================
import { Bot } from 'mineflayer'
import { Callback } from './CollectBlock'
import { Vec3 } from 'vec3'
import { error } from './Util'
import { Item } from 'prismarine-item'
import { goals } from 'mineflayer-pathfinder'
import { callbackify } from 'util'

export type ItemFilter = (item: Item) => boolean

function getClosestChest (bot: Bot, chestLocations: Vec3[]): Vec3 | null {
  let chest = null
  let distance = 0

  for (const c of chestLocations) {
    const dist = c.distanceTo(bot.entity.position)
    if (chest == null || dist < distance) {
      chest = c
      distance = dist
    }
  }

  if (chest != null) {
    chestLocations.splice(chestLocations.indexOf(chest), 1)
  }

  return chest
}

export async function emptyInventoryIfFull (bot: Bot, chestLocations: Vec3[], itemFilter: ItemFilter, cb?: Callback): Promise<void> {
  // @ts-expect-error
  if (cb != null) return callbackify(emptyInventoryIfFull)(bot, chestLocations, cb)
  if (bot.inventory.emptySlotCount() > 0) return
  return await emptyInventory(bot, chestLocations, itemFilter)
}

export async function emptyInventory (bot: Bot, chestLocations: Vec3[], itemFilter: ItemFilter, cb?: Callback): Promise<void> {
  // @ts-expect-error
  if (cb != null) return callbackify(emptyInventory)(bot, chestLocations, cb)
  if (chestLocations.length === 0) {
    throw error('NoChests', 'There are no defined chest locations!')
  }

  // Shallow clone so we can safely remove chests from the list that are full.
  chestLocations = [...chestLocations]

  while (true) {
    const chest = getClosestChest(bot, chestLocations)
    if (chest == null) {
      throw error('NoChests', 'All chests are full.')
    }
    const hasRemaining = await tryEmptyInventory(bot, chest, itemFilter)
    if (!hasRemaining) return
  }
}

async function tryEmptyInventory (bot: Bot, chestLocation: Vec3, itemFilter: ItemFilter, cb?: (err: Error | undefined, hasRemaining: boolean) => void): Promise<boolean> {
  // @ts-expect-error
  if (cb != null) return callbackify(tryEmptyInventory)(bot, chestLocation, itemFilter, cb)
  await gotoChest(bot, chestLocation)
  return await placeItems(bot, chestLocation, itemFilter)
}

async function gotoChest (bot: Bot, location: Vec3, cb?: Callback): Promise<void> {
  // @ts-expect-error
  if (cb != null) return callbackify(gotoChest)(bot, location)
  await bot.pathfinder.goto(new goals.GoalGetToBlock(location.x, location.y, location.z))
}

async function placeItems (bot: Bot, chestPos: Vec3, itemFilter: ItemFilter, cb?: (err: Error | undefined, hasRemaining: boolean) => void): Promise<boolean> {
  // @ts-expect-error
  if (cb != null) return callbackify(placeItems)(bot, chestPos, itemFilter, cb)
  const chestBlock = bot.blockAt(chestPos)
  if (chestBlock == null) {
    throw error('UnloadedChunk', 'Chest is in an unloaded chunk!')
  }
  const chest = await bot.openChest(chestBlock)
  for (const item of bot.inventory.items()) {
    if (!itemFilter(item)) continue
    if (chest.firstEmptyContainerSlot() === null) {
      // We have items that didn't fit.
      return true
    }
    await chest.deposit(item.type, item.metadata, item.count)
  }
  return false
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/Targets.ts
================================================
import { Bot } from 'mineflayer'
import { Block } from 'prismarine-block'
import { Entity } from 'prismarine-entity'

export type Collectable = Block | Entity

export class Targets {
  private readonly bot: Bot
  private targets: Collectable[] = []

  constructor (bot: Bot) {
    this.bot = bot
  }

  appendTargets (targets: Collectable[]): void {
    for (const target of targets) {
      this.appendTarget(target)
    }
  }

  appendTarget (target: Collectable): void {
    if (this.targets.includes(target)) return
    this.targets.push(target)
  }

  /**
   * Gets the closest target to the bot in this list.
   *
   * @returns The closest target, or null if there are no targets.
   */
  getClosest (): Collectable | null {
    let closest: Collectable | null = null
    let distance: number = 0

    for (const target of this.targets) {
      const dist = target.position.distanceTo(this.bot.entity.position)

      if (closest == null || dist < distance) {
        closest = target
        distance = dist
      }
    }

    return closest
  }

  get empty (): boolean {
    return this.targets.length === 0
  }

  clear (): void {
    this.targets.length = 0
  }

  removeTarget (target: Collectable): void {
    const index = this.targets.indexOf(target)
    if (index < 0) return
    this.targets.splice(index, 1)
  }
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/TaskQueue.ts
================================================
import type { Callback } from './index'
export type Task = (cb: Callback) => void
export type SyncTask = () => void

/**
 * A simple utility class for queuing up a series of async tasks to execute.
 */
export class TaskQueue {
  private tasks: Task[] = []

  /**
   * If true, the task list will stop executing if one of the tasks throws an error.
   */
  readonly stopOnError: boolean = true

  /**
   * Adds a new async task to this queue. The provided callback should be executed when
   * the async task is complete.
   *
   * @param task - The async task to add.
   */
  add (task: Task): void {
    this.tasks.push(task)
  }

  /**
   * Adds a synchronous task toi this queue.
   *
   * @param task - The sync task to add.
   */
  addSync (task: SyncTask): void {
    this.add((cb) => {
      try {
        task()
        cb()
      } catch (err: any) {
        cb(err)
      }
    })
  }

  /**
   * Runs all tasks currently in this queue and empties the queue.
   *
   * @param cb - The optional callback to be executed when all tasks in this queue have
   * finished executing.
   */
  runAll (cb?: Callback): void {
    const taskList = this.tasks
    this.tasks = []

    let index = -1
    const runNext: () => void = () => {
      index++
      if (index >= taskList.length) {
        if (cb !== undefined) cb()
        return
      }

      try {
        taskList[index]((err) => {
          if (err !== undefined) {
            if (cb !== undefined) cb(err)

            if (this.stopOnError) return
          }

          runNext()
        })
      } catch (err: any) {
        if (cb !== undefined) cb(err)
      }
    }

    runNext()
  }
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/TemporarySubscriber.ts
================================================
import { Bot } from 'mineflayer'

class Subscription {
  constructor (readonly eventName: string, readonly callback: Function) {}
}

export class TemporarySubscriber {
  private readonly subscriptions: Subscription[] = []

  constructor (readonly bot: Bot) {}

  /**
   * Adds a new temporary event listener to the bot.
   *
   * @param event - The event to subscribe to.
   * @param callback - The function to execute.
   */
  subscribeTo (event: string, callback: Function): void {
    this.subscriptions.push(new Subscription(event, callback))

    // @ts-expect-error
    this.bot.on(event, callback)
  }

  /**
   * Removes all attached event listeners from the bot.
   */
  cleanup (): void {
    for (const sub of this.subscriptions) {
      // @ts-expect-error
      this.bot.removeListener(sub.eventName, sub.callback)
    }
  }
}



================================================
FILE: voyager/env/mineflayer/mineflayer-collectblock/src/Util.ts
================================================
/**
 * Creates a new error object with the given type and message.
 *
 * @param type - The error type.
 * @param message - The error message.
 *
 * @returns The error object.
 */
export function error (type: string, message: string): Error {
  const e = new Error(message)
  e.name = type
  return e
}



================================================
FILE: voyager/prompts/__init__.py
================================================
import pkg_resources
import voyager.utils as U


def load_prompt(prompt):
    package_path = pkg_resources.resource_filename("voyager", "")
    return U.load_text(f"{package_path}/prompts/{prompt}.txt")



================================================
FILE: voyager/prompts/action_response_format.txt
================================================
Explain: ...
Plan:
1) ...
2) ...
3) ...
...
Code:
```javascript
// helper functions (only if needed, try to avoid them)
...
// main function after the helper functions
async function yourMainFunctionName(bot) {
  // ...
}
```


================================================
FILE: voyager/prompts/action_template.txt
================================================
You are a helpful assistant that writes Mineflayer javascript code to complete any Minecraft task specified by me.

Here are some useful programs written with Mineflayer APIs.

{programs}


At each round of conversation, I will give you
Code from the last round: ...
Execution error: ...
Chat log: ...
Biome: ...
Time: ...
Nearby blocks: ...
Nearby entities (nearest to farthest):
Health: ...
Hunger: ...
Position: ...
Equipment: ...
Inventory (xx/36): ...
Chests: ...
Task: ...
Context: ...
Critique: ...

You should then respond to me with
Explain (if applicable): Are there any steps missing in your plan? Why does the code not complete the task? What does the chat log and execution error imply?
Plan: How to complete the task step by step. You should pay attention to Inventory since it tells what you have. The task completeness check is also based on your final inventory.
Code:
    1) Write an async function taking the bot as the only argument.
    2) Reuse the above useful programs as much as possible.
        - Use `mineBlock(bot, name, count)` to collect blocks. Do not use `bot.dig` directly.
        - Use `craftItem(bot, name, count)` to craft items. Do not use `bot.craft` or `bot.recipesFor` directly.
        - Use `smeltItem(bot, name count)` to smelt items. Do not use `bot.openFurnace` directly.
        - Use `placeItem(bot, name, position)` to place blocks. Do not use `bot.placeBlock` directly.
        - Use `killMob(bot, name, timeout)` to kill mobs. Do not use `bot.attack` directly.
    3) Your function will be reused for building more complex functions. Therefore, you should make it generic and reusable. You should not make strong assumption about the inventory (as it may be changed at a later time), and therefore you should always check whether you have the required items before using them. If not, you should first collect the required items and reuse the above useful programs.
    4) Functions in the "Code from the last round" section will not be saved or executed. Do not reuse functions listed there.
    5) Anything defined outside a function will be ignored, define all your variables inside your functions.
    6) Call `bot.chat` to show the intermediate progress.
    7) Use `exploreUntil(bot, direction, maxDistance, callback)` when you cannot find something. You should frequently call this before mining blocks or killing mobs. You should select a direction at random every time instead of constantly using (1, 0, 1).
    8) `maxDistance` should always be 32 for `bot.findBlocks` and `bot.findBlock`. Do not cheat.
    9) Do not write infinite loops or recursive functions.
    10) Do not use `bot.on` or `bot.once` to register event listeners. You definitely do not need them.
    11) Name your function in a meaningful way (can infer the task from the name).

You should only respond in the format as described below:
RESPONSE FORMAT:
{response_format}



================================================
FILE: voyager/prompts/critic.txt
================================================
You are an assistant that assesses my progress of playing Minecraft and provides useful guidance.

You are required to evaluate if I have met the task requirements. Exceeding the task requirements is also considered a success while failing to meet them requires you to provide critique to help me improve.

I will give you the following information:

Biome: The biome after the task execution.
Time: The current time.
Nearby blocks: The surrounding blocks. These blocks are not collected yet. However, this is useful for some placing or planting tasks.
Health: My current health.
Hunger: My current hunger level. For eating task, if my hunger level is 20.0, then I successfully ate the food.
Position: My current position.
Equipment: My final equipment. For crafting tasks, I sometimes equip the crafted item.
Inventory (xx/36): My final inventory. For mining and smelting tasks, you only need to check inventory.
Chests: If the task requires me to place items in a chest, you can find chest information here.
Task: The objective I need to accomplish.
Context: The context of the task.

You should only respond in JSON format as described below:
{
    "reasoning": "reasoning",
    "success": boolean,
    "critique": "critique",
}
Ensure the response can be parsed by Python `json.loads`, e.g.: no trailing commas, no single quotes, etc.

Here are some examples:
INPUT:
Inventory (2/36): {'oak_log':2, 'spruce_log':2}

Task: Mine 3 wood logs

RESPONSE:
{
    "reasoning": "You need to mine 3 wood logs. You have 2 oak logs and 2 spruce logs, which add up to 4 wood logs.",
    "success": true,
    "critique": ""
}

INPUT:
Inventory (3/36): {'crafting_table': 1, 'spruce_planks': 6, 'stick': 4}

Task: Craft a wooden pickaxe

RESPONSE:
{
    "reasoning": "You have enough materials to craft a wooden pickaxe, but you didn't craft it.",
    "success": false,
    "critique": "Craft a wooden pickaxe with a crafting table using 3 spruce planks and 2 sticks."
}

INPUT:
Inventory (2/36): {'raw_iron': 5, 'stone_pickaxe': 1}

Task: Mine 5 iron_ore

RESPONSE:
{
    "reasoning": "Mining iron_ore in Minecraft will get raw_iron. You have 5 raw_iron in your inventory.",
    "success": true,
    "critique": ""
}

INPUT:
Biome: plains

Nearby blocks: stone, dirt, grass_block, grass, farmland, wheat

Inventory (26/36): ...

Task:  Plant 1 wheat seed.

RESPONSE:
{
    "reasoning": "For planting tasks, inventory information is useless. In nearby blocks, there is farmland and wheat, which means you succeed to plant the wheat seed.",
    "success": true,
    "critique": ""
}

INPUT:
Inventory (11/36): {... ,'rotten_flesh': 1}

Task: Kill 1 zombie

Context: ...

RESPONSE
{
    "reasoning": "You have rotten flesh in your inventory, which means you successfully killed one zombie.",
    "success": true,
    "critique": ""
}

INPUT:
Hunger: 20.0/20.0

Inventory (11/36): ...

Task: Eat 1 ...

Context: ...

RESPONSE
{
    "reasoning": "For all eating task, if the player's hunger is 20.0, then the player successfully ate the food.",
    "success": true,
    "critique": ""
}

INPUT:
Nearby blocks: chest

Inventory (28/36): {'rail': 1, 'coal': 2, 'oak_planks': 13, 'copper_block': 1, 'diorite': 7, 'cooked_beef': 4, 'granite': 22, 'cobbled_deepslate': 23, 'feather': 4, 'leather': 2, 'cooked_chicken': 3, 'white_wool': 2, 'stick': 3, 'black_wool': 1, 'stone_sword': 2, 'stone_hoe': 1, 'stone_axe': 2, 'stone_shovel': 2, 'cooked_mutton': 4, 'cobblestone_wall': 18, 'crafting_table': 1, 'furnace': 1, 'iron_pickaxe': 1, 'stone_pickaxe': 1, 'raw_copper': 12}

Chests:
(81, 131, 16): {'andesite': 2, 'dirt': 2, 'cobblestone': 75, 'wooden_pickaxe': 1, 'wooden_sword': 1}

Task: Deposit useless items into the chest at (81, 131, 16)

Context: ...

RESPONSE
{
    "reasoning": "You have 28 items in your inventory after depositing, which is more than 20. You need to deposit more items from your inventory to the chest.",
    "success": false,
    "critique": "Deposit more useless items such as copper_block, diorite, granite, cobbled_deepslate, feather, and leather to meet the requirement of having only 20 occupied slots in your inventory."
}


================================================
FILE: voyager/prompts/curriculum.txt
================================================
You are a helpful assistant that tells me the next immediate task to do in Minecraft. My ultimate goal is to discover as many diverse things as possible, accomplish as many diverse tasks as possible and become the best Minecraft player in the world.

I will give you the following information:
Question 1: ...
Answer: ...
Question 2: ...
Answer: ...
Question 3: ...
Answer: ...
...
Biome: ...
Time: ...
Nearby blocks: ...
Other blocks that are recently seen: ...
Nearby entities (nearest to farthest): ...
Health: Higher than 15 means I'm healthy.
Hunger: Higher than 15 means I'm not hungry.
Position: ...
Equipment: If I have better armor in my inventory, you should ask me to equip it.
Inventory (xx/36): ...
Chests: You can ask me to deposit or take items from these chests. There also might be some unknown chest, you should ask me to open and check items inside the unknown chest.
Completed tasks so far: ...
Failed tasks that are too hard: ...

You must follow the following criteria:
1) You should act as a mentor and guide me to the next task based on my current learning progress.
2) Please be very specific about what resources I need to collect, what I need to craft, or what mobs I need to kill.
3) The next task should follow a concise format, such as "Mine [quantity] [block]", "Craft [quantity] [item]", "Smelt [quantity] [item]", "Kill [quantity] [mob]", "Cook [quantity] [food]", "Equip [item]" etc. It should be a single phrase. Do not propose multiple tasks at the same time. Do not mention anything else.
4) The next task should not be too hard since I may not have the necessary resources or have learned enough skills to complete it yet.
5) The next task should be novel and interesting. I should look for rare resources, upgrade my equipment and tools using better materials, and discover new things. I should not be doing the same thing over and over again.
6) I may sometimes need to repeat some tasks if I need to collect more resources to complete more difficult tasks. Only repeat tasks if necessary.
7) Do not ask me to build or dig shelter even if it's at night. I want to explore the world and discover new things. I don't want to stay in one place.
8) Tasks that require information beyond the player's status to verify should be avoided. For instance, "Placing 4 torches" and "Dig a 2x1x2 hole" are not ideal since they require visual confirmation from the screen. All the placing, building, planting, and trading tasks should be avoided. Do not propose task starting with these keywords.

You should only respond in the format as described below:
RESPONSE FORMAT:
Reasoning: Based on the information I listed above, do reasoning about what the next task should be.
Task: The next task.

Here's an example response:
Reasoning: The inventory is empty now, chop down a tree to get some wood.
Task: Obtain a wood log.


================================================
FILE: voyager/prompts/curriculum_qa_step1_ask_questions.txt
================================================
You are a helpful assistant that asks questions to help me decide the next immediate task to do in Minecraft. My ultimate goal is to discover as many things as possible, accomplish as many tasks as possible and become the best Minecraft player in the world.

I will give you the following information:
Biome: ...
Time: ...
Nearby blocks: ...
Other blocks that are recently seen: ...
Nearby entities (nearest to farthest): ...
Health: ...
Hunger: ...
Position: ...
Equipment: ...
Inventory (xx/36): ...
Chests: ...
Completed tasks so far: ...
Failed tasks that are too hard: ...

You must follow the following criteria:
1) You should ask at least 5 questions (but no more than 10 questions) to help me decide the next immediate task to do. Each question should be followed by the concept that the question is about.
2) Your question should be specific to a concept in Minecraft.
  Bad example (the question is too general):
    Question: What is the best way to play Minecraft?
    Concept: unknown
  Bad example (axe is still general, you should specify the type of axe such as wooden axe):
    What are the benefits of using an axe to gather resources?
    Concept: axe
  Good example:
    Question: How to make a wooden pickaxe?
    Concept: wooden pickaxe
3) Your questions should be self-contained and not require any context.
  Bad example (the question requires the context of my current biome):
    Question: What are the blocks that I can find in my current biome?
    Concept: unknown
  Bad example (the question requires the context of my current inventory):
    Question: What are the resources you need the most currently?
    Concept: unknown
  Bad example (the question requires the context of my current inventory):
    Question: Do you have any gold or emerald resources?
    Concept: gold
  Bad example (the question requires the context of my nearby entities):
    Question: Can you see any animals nearby that you can kill for food?
    Concept: food
  Bad example (the question requires the context of my nearby blocks):
    Question: Is there any water source nearby?
    Concept: water
  Good example:
    Question: What are the blocks that I can find in the sparse jungle?
    Concept: sparse jungle
4) Do not ask questions about building tasks (such as building a shelter) since they are too hard for me to do.

Let's say your current biome is sparse jungle. You can ask questions like:
Question: What are the items that I can find in the sparse jungle?
Concept: sparse jungle
Question: What are the mobs that I can find in the sparse jungle?
Concept: sparse jungle

Let's say you see a creeper nearby, and you have not defeated a creeper before. You can ask a question like:
Question: How to defeat the creeper?
Concept: creeper

Let's say your last completed task is "Craft a wooden pickaxe". You can ask a question like:
Question: What are the suggested tasks that I can do after crafting a wooden pickaxe?
Concept: wooden pickaxe

Here are some more question and concept examples:
Question: What are the ores that I can find in the sparse jungle?
Concept: sparse jungle
(the above concept should not be "ore" because I need to look up the page of "sparse jungle" to find out what ores I can find in the sparse jungle)
Question: How can you obtain food in the sparse jungle?
Concept: sparse jungle
(the above concept should not be "food" because I need to look up the page of "sparse jungle" to find out what food I can obtain in the sparse jungle)
Question: How can you use the furnace to upgrade your equipment and make useful items?
Concept: furnace
Question: How to obtain a diamond ore?
Concept: diamond ore
Question: What are the benefits of using a stone pickaxe over a wooden pickaxe?
Concept: stone pickaxe
Question: What are the tools that you can craft using wood planks and sticks?
Concept: wood planks

You should only respond in the format as described below:
RESPONSE FORMAT:
Reasoning: ...
Question 1: ...
Concept 1: ...
Question 2: ...
Concept 2: ...
Question 3: ...
Concept 3: ...
Question 4: ...
Concept 4: ...
Question 5: ...
Concept 5: ...
...



================================================
FILE: voyager/prompts/curriculum_qa_step2_answer_questions.txt
================================================
You are a helpful assistant that answer my question about Minecraft.

I will give you the following information:
Question: ...

You will answer the question based on the context (only if available and helpful) and your own knowledge of Minecraft.
1) Start your answer with "Answer: ".
2) Answer "Answer: Unknown" if you don't know the answer.


================================================
FILE: voyager/prompts/curriculum_task_decomposition.txt
================================================
You are a helpful assistant that generates a curriculum of subgoals to complete any Minecraft task specified by me.

I'll give you a final task and my current inventory, you need to decompose the task into a list of subgoals based on my inventory.

You must follow the following criteria:
1) Return a Python list of subgoals that can be completed in order to complete the specified task.
2) Each subgoal should follow a concise format, such as "Mine [quantity] [block]", "Craft [quantity] [item]", "Smelt [quantity] [item]", "Kill [quantity] [mob]", "Cook [quantity] [food]", "Equip [item]".
3) Include each level of necessary tools as a subgoal, such as wooden, stone, iron, diamond, etc.

You should only respond in JSON format as described below:
["subgoal1", "subgoal2", "subgoal3", ...]
Ensure the response can be parsed by Python `json.loads`, e.g.: no trailing commas, no single quotes, etc.


================================================
FILE: voyager/prompts/skill.txt
================================================
You are a helpful assistant that writes a description of the given function written in Mineflayer javascript code.

1) Do not mention the function name.
2) Do not mention anything about `bot.chat` or helper functions.
3) There might be some helper functions before the main function, but you only need to describe the main function.
4) Try to summarize the function in no more than 6 sentences.
5) Your response should be a single line of text.

For example, if the function is:

async function mineCobblestone(bot) {
  // Check if the wooden pickaxe is in the inventory, if not, craft one
  let woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["wooden_pickaxe"].id);
  if (!woodenPickaxe) {
    bot.chat("Crafting a wooden pickaxe.");
    await craftWoodenPickaxe(bot);
    woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName["wooden_pickaxe"].id);
  }

  // Equip the wooden pickaxe if it exists
  if (woodenPickaxe) {
    await bot.equip(woodenPickaxe, "hand");

    // Explore until we find a stone block
    await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {
      const stone = bot.findBlock({
        matching: mcData.blocksByName["stone"].id,
        maxDistance: 32
      });
      if (stone) {
        return true;
      }
    });

    // Mine 8 cobblestone blocks using the wooden pickaxe
    bot.chat("Found a stone block. Mining 8 cobblestone blocks.");
    await mineBlock(bot, "stone", 8);
    bot.chat("Successfully mined 8 cobblestone blocks.");

    // Save the event of mining 8 cobblestone
    bot.save("cobblestone_mined");
  } else {
    bot.chat("Failed to craft a wooden pickaxe. Cannot mine cobblestone.");
  }
}

The main function is `mineCobblestone`.

Then you would write:

The function is about mining 8 cobblestones using a wooden pickaxe. First check if a wooden pickaxe is in the inventory. If not, craft one. If the wooden pickaxe is available, equip the wooden pickaxe in the hand. Next, explore the environment until finding a stone block. Once a stone block is found, mine a total of 8 cobblestone blocks using the wooden pickaxe.


================================================
FILE: voyager/utils/__init__.py
================================================
from .file_utils import *
from .json_utils import *
from .record_utils import EventRecorder



================================================
FILE: voyager/utils/file_utils.py
================================================
"""
File system utils.
"""
import collections
import os
import pickle
import sys
import errno
import shutil
import glob

# import pwd
import codecs
import hashlib
import tarfile
import fnmatch
import tempfile
from datetime import datetime
from socket import gethostname
import logging


f_ext = os.path.splitext

f_size = os.path.getsize

is_file = os.path.isfile

is_dir = os.path.isdir

get_dir = os.path.dirname


def host_name():
    "Get host name, alias with ``socket.gethostname()``"
    return gethostname()


def host_id():
    """
    Returns: first part of hostname up to '.'
    """
    return host_name().split(".")[0]


def utf_open(fname, mode):
    """
    Wrapper for codecs.open
    """
    return codecs.open(fname, mode=mode, encoding="utf-8")


def is_sequence(obj):
    """
    Returns:
      True if the sequence is a collections.Sequence and not a string.
    """
    return isinstance(obj, collections.abc.Sequence) and not isinstance(obj, str)


def pack_varargs(args):
    """
    Pack *args or a single list arg as list

    def f(*args):
        arg_list = pack_varargs(args)
        # arg_list is now packed as a list
    """
    assert isinstance(args, tuple), "please input the tuple `args` as in *args"
    if len(args) == 1 and is_sequence(args[0]):
        return args[0]
    else:
        return args


def f_not_empty(*fpaths):
    """
    Returns:
        True if and only if the file exists and file size > 0
          if fpath is a dir, if and only if dir exists and has at least 1 file
    """
    fpath = f_join(*fpaths)
    if not os.path.exists(fpath):
        return False

    if os.path.isdir(fpath):
        return len(os.listdir(fpath)) > 0
    else:
        return os.path.getsize(fpath) > 0


def f_expand(fpath):
    return os.path.expandvars(os.path.expanduser(fpath))


def f_exists(*fpaths):
    return os.path.exists(f_join(*fpaths))


def f_join(*fpaths):
    """
    join file paths and expand special symbols like `~` for home dir
    """
    fpaths = pack_varargs(fpaths)
    fpath = f_expand(os.path.join(*fpaths))
    if isinstance(fpath, str):
        fpath = fpath.strip()
    return fpath


def f_listdir(
    *fpaths,
    filter_ext=None,
    filter=None,
    sort=True,
    full_path=False,
    nonexist_ok=True,
    recursive=False,
):
    """
    Args:
        full_path: True to return full paths to the dir contents
        filter: function that takes in file name and returns True to include
        nonexist_ok: True to return [] if the dir is non-existent, False to raise
        sort: sort the file names by alphabetical
        recursive: True to use os.walk to recursively list files. Note that `filter`
            will be applied to the relative path string to the root dir.
            e.g. filter will take "a/data1.txt" and "a/b/data3.txt" as input, instead of
            just the base file names "data1.txt" and "data3.txt".
            if False, will simply call os.listdir()
    """
    assert not (filter_ext and filter), "filter_ext and filter are mutually exclusive"
    dir_path = f_join(*fpaths)
    if not os.path.exists(dir_path) and nonexist_ok:
        return []
    if recursive:
        files = [
            os.path.join(os.path.relpath(root, dir_path), file)
            for root, _, files in os.walk(dir_path)
            for file in files
        ]
    else:
        files = os.listdir(dir_path)
    if filter is not None:
        files = [f for f in files if filter(f)]
    elif filter_ext is not None:
        files = [f for f in files if f.endswith(filter_ext)]
    if sort:
        files.sort()
    if full_path:
        return [os.path.join(dir_path, f) for f in files]
    else:
        return files


def f_mkdir(*fpaths):
    """
    Recursively creates all the subdirs
    If exist, do nothing.
    """
    fpath = f_join(*fpaths)
    os.makedirs(fpath, exist_ok=True)
    return fpath


def f_mkdir_in_path(*fpaths):
    """
    fpath is a file,
    recursively creates all the parent dirs that lead to the file
    If exist, do nothing.
    """
    os.makedirs(get_dir(f_join(*fpaths)), exist_ok=True)


def last_part_in_path(fpath):
    """
    https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python
    """
    return os.path.basename(os.path.normpath(f_expand(fpath)))


def is_abs_path(*fpath):
    return os.path.isabs(f_join(*fpath))


def is_relative_path(*fpath):
    return not is_abs_path(f_join(*fpath))


def f_time(*fpath):
    "File modification time"
    return str(os.path.getctime(f_join(*fpath)))


def f_append_before_ext(fpath, suffix):
    """
    Append a suffix to file name and retain its extension
    """
    name, ext = f_ext(fpath)
    return name + suffix + ext


def f_add_ext(fpath, ext):
    """
    Append an extension if not already there
    Args:
      ext: will add a preceding `.` if doesn't exist
    """
    if not ext.startswith("."):
        ext = "." + ext
    if fpath.endswith(ext):
        return fpath
    else:
        return fpath + ext


def f_has_ext(fpath, ext):
    "Test if file path is a text file"
    _, actual_ext = f_ext(fpath)
    return actual_ext == "." + ext.lstrip(".")


def f_glob(*fpath):
    return glob.glob(f_join(*fpath), recursive=True)


def f_remove(*fpath, verbose=False, dry_run=False):
    """
    If exist, remove. Supports both dir and file. Supports glob wildcard.
    """
    assert isinstance(verbose, bool)
    fpath = f_join(fpath)
    if dry_run:
        print("Dry run, delete:", fpath)
        return
    for f in glob.glob(fpath):
        try:
            shutil.rmtree(f)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                try:
                    os.remove(f)
                except:  # final resort safeguard
                    pass
    if verbose:
        print(f'Deleted "{fpath}"')


def f_copy(fsrc, fdst, ignore=None, include=None, exists_ok=True, verbose=False):
    """
    Supports both dir and file. Supports glob wildcard.
    """
    fsrc, fdst = f_expand(fsrc), f_expand(fdst)
    for f in glob.glob(fsrc):
        try:
            f_copytree(f, fdst, ignore=ignore, include=include, exist_ok=exists_ok)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copy(f, fdst)
            else:
                raise
    if verbose:
        print(f'Copied "{fsrc}" to "{fdst}"')


def _f_copytree(
    src,
    dst,
    symlinks=False,
    ignore=None,
    exist_ok=True,
    copy_function=shutil.copy2,
    ignore_dangling_symlinks=False,
):
    """Copied from python standard lib shutil.copytree
    except that we allow exist_ok
    Use f_copytree as entry
    """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    os.makedirs(dst, exist_ok=exist_ok)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        _f_copytree(
                            srcname, dstname, symlinks, ignore, exist_ok, copy_function
                        )
                    else:
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                _f_copytree(srcname, dstname, symlinks, ignore, exist_ok, copy_function)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy_function(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr(why, "winerror", None) is None:
            errors.append((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors)
    return dst


def _include_patterns(*patterns):
    """Factory function that can be used with copytree() ignore parameter.

    Arguments define a sequence of glob-style patterns
    that are used to specify what files to NOT ignore.
    Creates and returns a function that determines this for each directory
    in the file hierarchy rooted at the source directory when used with
    shutil.copytree().
    """

    def _ignore_patterns(path, names):
        keep = set(
            name for pattern in patterns for name in fnmatch.filter(names, pattern)
        )
        ignore = set(
            name
            for name in names
            if name not in keep and not os.path.isdir(os.path.join(path, name))
        )
        return ignore

    return _ignore_patterns


def f_copytree(fsrc, fdst, symlinks=False, ignore=None, include=None, exist_ok=True):
    fsrc, fdst = f_expand(fsrc), f_expand(fdst)
    assert (ignore is None) or (
        include is None
    ), "ignore= and include= are mutually exclusive"
    if ignore:
        ignore = shutil.ignore_patterns(*ignore)
    elif include:
        ignore = _include_patterns(*include)
    _f_copytree(fsrc, fdst, ignore=ignore, symlinks=symlinks, exist_ok=exist_ok)


def f_move(fsrc, fdst):
    fsrc, fdst = f_expand(fsrc), f_expand(fdst)
    for f in glob.glob(fsrc):
        shutil.move(f, fdst)


def f_split_path(fpath, normpath=True):
    """
    Splits path into a list of its component folders

    Args:
        normpath: call os.path.normpath to remove redundant '/' and
            up-level references like ".."
    """
    if normpath:
        fpath = os.path.normpath(fpath)
    allparts = []
    while 1:
        parts = os.path.split(fpath)
        if parts[0] == fpath:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == fpath:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            fpath = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def get_script_dir():
    """
    Returns: the dir of current script
    """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def get_script_file_name():
    """
    Returns: the dir of current script
    """
    return os.path.basename(sys.argv[0])


def get_script_self_path():
    """
    Returns: the dir of current script
    """
    return os.path.realpath(sys.argv[0])


def get_parent_dir(location, abspath=False):
    """
    Args:
      location: current directory or file

    Returns:
        parent directory absolute or relative path
    """
    _path = os.path.abspath if abspath else os.path.relpath
    return _path(f_join(location, os.pardir))


def md5_checksum(*fpath):
    """
    File md5 signature
    """
    hash_md5 = hashlib.md5()
    with open(f_join(*fpath), "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def create_tar(fsrc, output_tarball, include=None, ignore=None, compress_mode="gz"):
    """
    Args:
        fsrc: source file or folder
        output_tarball: output tar file name
        compress_mode: "gz", "bz2", "xz" or "" (empty for uncompressed write)
        include: include pattern, will trigger copy to temp directory
        ignore: ignore pattern, will trigger copy to temp directory
    """
    fsrc, output_tarball = f_expand(fsrc), f_expand(output_tarball)
    assert compress_mode in ["gz", "bz2", "xz", ""]
    src_base = os.path.basename(fsrc)

    tempdir = None
    if include or ignore:
        tempdir = tempfile.mkdtemp()
        tempdest = f_join(tempdir, src_base)
        f_copy(fsrc, tempdest, include=include, ignore=ignore)
        fsrc = tempdest

    with tarfile.open(output_tarball, "w:" + compress_mode) as tar:
        tar.add(fsrc, arcname=src_base)

    if tempdir:
        f_remove(tempdir)


def extract_tar(source_tarball, output_dir=".", members=None):
    """
    Args:
        source_tarball: extract members from archive
        output_dir: default to current working dir
        members: must be a subset of the list returned by getmembers()
    """
    source_tarball, output_dir = f_expand(source_tarball), f_expand(output_dir)
    with tarfile.open(source_tarball, "r:*") as tar:
        tar.extractall(output_dir, members=members)


def move_with_backup(*fpath, suffix=".bak"):
    """
    Ensures that a path is not occupied. If there is a file, rename it by
    adding @suffix. Resursively backs up everything.

    Args:
        fpath: file path to clear
        suffix: Add to backed up files (default: {'.bak'})
    """
    fpath = str(f_join(*fpath))
    if os.path.exists(fpath):
        move_with_backup(fpath + suffix)
        shutil.move(fpath, fpath + suffix)


def insert_before_ext(name, insert):
    """
    log.txt -> log.ep50.txt
    """
    name, ext = os.path.splitext(name)
    return name + insert + ext


def timestamp_file_name(fname):
    timestr = datetime.now().strftime("_%H-%M-%S_%m-%d-%y")
    return insert_before_ext(fname, timestr)


def get_file_lock(*fpath, timeout: int = 15, logging_level="critical"):
    """
    NFS-safe filesystem-backed lock. `pip install flufl.lock`
    https://flufllock.readthedocs.io/en/stable/apiref.html

    Args:
        fpath: should be a path on NFS so that every process can see it
        timeout: seconds
    """
    from flufl.lock import Lock

    logging.getLogger("flufl.lock").setLevel(logging_level.upper())
    return Lock(f_join(*fpath), lifetime=timeout)


def load_pickle(*fpaths):
    with open(f_join(*fpaths), "rb") as fp:
        return pickle.load(fp)


def dump_pickle(data, *fpaths):
    with open(f_join(*fpaths), "wb") as fp:
        pickle.dump(data, fp)


def load_text(*fpaths, by_lines=False):
    with open(f_join(*fpaths), "r") as fp:
        if by_lines:
            return fp.readlines()
        else:
            return fp.read()


def load_text_lines(*fpaths):
    return load_text(*fpaths, by_lines=True)


def dump_text(s, *fpaths):
    with open(f_join(*fpaths), "w") as fp:
        fp.write(s)


def dump_text_lines(lines: list[str], *fpaths, add_newline=True):
    with open(f_join(*fpaths), "w") as fp:
        for line in lines:
            print(line, file=fp, end="\n" if add_newline else "")


# aliases to be consistent with other load_* and dump_*
pickle_load = load_pickle
pickle_dump = dump_pickle
text_load = load_text
read_text = load_text
read_text_lines = load_text_lines
write_text = dump_text
write_text_lines = dump_text_lines
text_dump = dump_text



================================================
FILE: voyager/utils/json_utils.py
================================================
import json
import re
from typing import Any, Dict, Union
from .file_utils import f_join


def json_load(*file_path, **kwargs):
    file_path = f_join(file_path)
    with open(file_path, "r") as fp:
        return json.load(fp, **kwargs)


def json_loads(string, **kwargs):
    return json.loads(string, **kwargs)


def json_dump(data, *file_path, **kwargs):
    file_path = f_join(file_path)
    with open(file_path, "w") as fp:
        json.dump(data, fp, **kwargs)


def json_dumps(data, **kwargs):
    """
    Returns: string
    """
    return json.dumps(data, **kwargs)


# ---------------- Aliases -----------------
# add aliases where verb goes first, json_load -> load_json
load_json = json_load
loads_json = json_loads
dump_json = json_dump
dumps_json = json_dumps


def extract_char_position(error_message: str) -> int:
    """Extract the character position from the JSONDecodeError message.
    Args:
        error_message (str): The error message from the JSONDecodeError
          exception.
    Returns:
        int: The character position.
    """
    import re

    char_pattern = re.compile(r"\(char (\d+)\)")
    if match := char_pattern.search(error_message):
        return int(match[1])
    else:
        raise ValueError("Character position not found in the error message.")


def add_quotes_to_property_names(json_string: str) -> str:
    """
    Add quotes to property names in a JSON string.
    Args:
        json_string (str): The JSON string.
    Returns:
        str: The JSON string with quotes added to property names.
    """

    def replace_func(match):
        return f'"{match.group(1)}":'

    property_name_pattern = re.compile(r"(\w+):")
    corrected_json_string = property_name_pattern.sub(replace_func, json_string)

    try:
        json.loads(corrected_json_string)
        return corrected_json_string
    except json.JSONDecodeError as e:
        raise e


def balance_braces(json_string: str) -> str:
    """
    Balance the braces in a JSON string.
    Args:
        json_string (str): The JSON string.
    Returns:
        str: The JSON string with braces balanced.
    """

    open_braces_count = json_string.count("{")
    close_braces_count = json_string.count("}")

    while open_braces_count > close_braces_count:
        json_string += "}"
        close_braces_count += 1

    while close_braces_count > open_braces_count:
        json_string = json_string.rstrip("}")
        close_braces_count -= 1

    try:
        json.loads(json_string)
        return json_string
    except json.JSONDecodeError as e:
        raise e


def fix_invalid_escape(json_str: str, error_message: str) -> str:
    while error_message.startswith("Invalid \\escape"):
        bad_escape_location = extract_char_position(error_message)
        json_str = json_str[:bad_escape_location] + json_str[bad_escape_location + 1 :]
        try:
            json.loads(json_str)
            return json_str
        except json.JSONDecodeError as e:
            error_message = str(e)
    return json_str


def correct_json(json_str: str) -> str:
    """
    Correct common JSON errors.
    Args:
        json_str (str): The JSON string.
    """

    try:
        json.loads(json_str)
        return json_str
    except json.JSONDecodeError as e:
        error_message = str(e)
        if error_message.startswith("Invalid \\escape"):
            json_str = fix_invalid_escape(json_str, error_message)
        if error_message.startswith(
            "Expecting property name enclosed in double quotes"
        ):
            json_str = add_quotes_to_property_names(json_str)
            try:
                json.loads(json_str)
                return json_str
            except json.JSONDecodeError as e:
                error_message = str(e)
        if balanced_str := balance_braces(json_str):
            return balanced_str
    return json_str


def fix_and_parse_json(
    json_str: str, try_to_fix_with_gpt: bool = True
) -> Union[str, Dict[Any, Any]]:
    """Fix and parse JSON string"""
    try:
        json_str = json_str.replace("\t", "")
        return json.loads(json_str)
    except json.JSONDecodeError as _:  # noqa: F841
        json_str = correct_json(json_str)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as _:  # noqa: F841
            pass
    # Let's do something manually:
    # sometimes GPT responds with something BEFORE the braces:
    # "I'm sorry, I don't understand. Please try again."
    # {"text": "I'm sorry, I don't understand. Please try again.",
    #  "confidence": 0.0}
    # So let's try to find the first brace and then parse the rest
    #  of the string
    try:
        brace_index = json_str.index("{")
        json_str = json_str[brace_index:]
        last_brace_index = json_str.rindex("}")
        json_str = json_str[: last_brace_index + 1]
        return json.loads(json_str)
    except json.JSONDecodeError as e:  # noqa: F841
        # if try_to_fix_with_gpt:
        #     print(
        #         "Warning: Failed to parse AI output, attempting to fix."
        #         "\n If you see this warning frequently, it's likely that"
        #         " your prompt is confusing the AI. Try changing it up"
        #         " slightly."
        #     )
        #     # Now try to fix this up using the ai_functions
        #     ai_fixed_json = fix_json(json_str, JSON_SCHEMA)
        #
        #     if ai_fixed_json != "failed":
        #         return json.loads(ai_fixed_json)
        #     else:
        #         # This allows the AI to react to the error message,
        #         #   which usually results in it correcting its ways.
        #         print("Failed to fix ai output, telling the AI.")
        #         return json_str
        # else:
        raise e


# def fix_json(json_str: str, schema: str) -> str:
#     """Fix the given JSON string to make it parseable and fully complient with the provided schema."""
#
#     # Try to fix the JSON using gpt:
#     function_string = "def fix_json(json_str: str, schema:str=None) -> str:"
#     args = [f"'''{json_str}'''", f"'''{schema}'''"]
#     description_string = (
#         "Fixes the provided JSON string to make it parseable"
#         " and fully complient with the provided schema.\n If an object or"
#         " field specified in the schema isn't contained within the correct"
#         " JSON, it is ommited.\n This function is brilliant at guessing"
#         " when the format is incorrect."
#     )
#
#     # If it doesn't already start with a "`", add one:
#     if not json_str.startswith("`"):
#         json_str = "```json\n" + json_str + "\n```"
#     result_string = call_ai_function(
#         function_string, args, description_string, model=cfg.fast_llm_model
#     )
#     if cfg.debug:
#         print("------------ JSON FIX ATTEMPT ---------------")
#         print(f"Original JSON: {json_str}")
#         print("-----------")
#         print(f"Fixed JSON: {result_string}")
#         print("----------- END OF FIX ATTEMPT ----------------")
#
#     try:
#         json.loads(result_string)  # just check the validity
#         return result_string
#     except:  # noqa: E722
#         # Get the call stack:
#         # import traceback
#         # call_stack = traceback.format_exc()
#         # print(f"Failed to fix JSON: '{json_str}' "+call_stack)
#         return "failed"



================================================
FILE: voyager/utils/record_utils.py
================================================
import time

from .file_utils import *
from .json_utils import *


class EventRecorder:
    def __init__(
        self,
        ckpt_dir="ckpt",
        resume=False,
        init_position=None,
    ):
        self.ckpt_dir = ckpt_dir
        self.item_history = set()
        self.item_vs_time = {}
        self.item_vs_iter = {}
        self.biome_history = set()
        self.init_position = init_position
        self.position_history = [[0, 0]]
        self.elapsed_time = 0
        self.iteration = 0
        f_mkdir(self.ckpt_dir, "events")
        if resume:
            self.resume()

    def record(self, events, task):
        task = re.sub(r'[\\/:"*?<>| ]', "_", task)
        task = task.replace(" ", "_") + time.strftime(
            "_%Y%m%d_%H%M%S", time.localtime()
        )
        self.iteration += 1
        if not self.init_position:
            self.init_position = [
                events[0][1]["status"]["position"]["x"],
                events[0][1]["status"]["position"]["z"],
            ]
        for event_type, event in events:
            self.update_items(event)
            if event_type == "observe":
                self.update_elapsed_time(event)
        print(
            f"\033[96m****Recorder message: {self.elapsed_time} ticks have elapsed****\033[0m\n"
            f"\033[96m****Recorder message: {self.iteration} iteration passed****\033[0m"
        )
        dump_json(events, f_join(self.ckpt_dir, "events", task))

    def resume(self, cutoff=None):
        self.item_history = set()
        self.item_vs_time = {}
        self.item_vs_iter = {}
        self.elapsed_time = 0
        self.position_history = [[0, 0]]

        def get_timestamp(string):
            timestamp = "_".join(string.split("_")[-2:])
            return time.mktime(time.strptime(timestamp, "%Y%m%d_%H%M%S"))

        records = f_listdir(self.ckpt_dir, "events")
        sorted_records = sorted(records, key=get_timestamp)
        for record in sorted_records:
            self.iteration += 1
            if cutoff and self.iteration > cutoff:
                break
            events = load_json(f_join(self.ckpt_dir, "events", record))
            if not self.init_position:
                self.init_position = (
                    events[0][1]["status"]["position"]["x"],
                    events[0][1]["status"]["position"]["z"],
                )
            for event_type, event in events:
                self.update_items(event)
                self.update_position(event)
                if event_type == "observe":
                    self.update_elapsed_time(event)

    def update_items(self, event):
        inventory = event["inventory"]
        elapsed_time = event["status"]["elapsedTime"]
        biome = event["status"]["biome"]
        items = set(inventory.keys())
        new_items = items - self.item_history
        self.item_history.update(items)
        self.biome_history.add(biome)
        if new_items:
            if self.elapsed_time + elapsed_time not in self.item_vs_time:
                self.item_vs_time[self.elapsed_time + elapsed_time] = []
            self.item_vs_time[self.elapsed_time + elapsed_time].extend(new_items)
            if self.iteration not in self.item_vs_iter:
                self.item_vs_iter[self.iteration] = []
            self.item_vs_iter[self.iteration].extend(new_items)

    def update_elapsed_time(self, event):
        self.elapsed_time += event["status"]["elapsedTime"]

    def update_position(self, event):
        position = [
            event["status"]["position"]["x"] - self.init_position[0],
            event["status"]["position"]["z"] - self.init_position[1],
        ]
        if self.position_history[-1] != position:
            self.position_history.append(position)



================================================
FILE: .github/ISSUE_TEMPLATE/voyager-issue-template.md
================================================
---
name: Voyager Issue Template
about: Create an issue to Voyager
title: ''
labels: ''
assignees: ''

---

### Before submitting an issue, make sure you read the [FAQ.md](FAQ.md)

### Briefly describe your issue
...
### Please provide your python, nodejs, Minecraft, and Fabric versions here
...
### [If applicable] Please provide the Minefalyer and Minecraft logs, you can find the log under `logs` folder
...
### [If applicable] Please provide the GPT conversations that are printed each round.
...



================================================
FILE: .github/workflows/close_issue.yml
================================================
name: Close inactive issues
on:
  schedule:
    - cron: "30 1 * * *"

jobs:
  close-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
      - uses: actions/stale@v5
        with:
          days-before-issue-stale: 30
          days-before-issue-close: 14
          stale-issue-label: "stale"
          stale-issue-message: "This issue is stale because it has been open for 30 days with no activity."
          close-issue-message: "This issue was closed because it has been inactive for 14 days since being marked as stale."
          days-before-pr-stale: -1
          days-before-pr-close: -1
          repo-token: ${{ secrets.GITHUB_TOKEN }}


