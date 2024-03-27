================= ===============================
Settings                 Value
================= ===============================
Library            creative_test.CreativeTest
Force Tags         creatives
================= ===============================


=========================================================================================== ====================================================
                  Test Case                                                                                 Action
=========================================================================================== ====================================================
Login                                                                                         Login As Campaign Manager
DXUITC-482:To check name field accepts 255 characters                                         Validation For Limit
\                                                                                             Assert Creative Name
DXUITC-491:To check concept field accepts 200 characters                                      Assert Creative Concept
DXUITC-547:To check Advertiser URL accepts only 255 charracters                               Assert Url With 255 Chars
DXUITC-576:To check additional Advertiser URL accepts only 255 characters                     Assert Additional Url With 255 Chars
DXUITC-598:To check the Language targeting as German                                          Assert Lang Targeting
DXUITC-6361:Creative is created with same External source id and different value              Assert External Ids
DXUITC-6362:Creative is created with different External source id and same value              Creatives With Valid Details
\                                                                                             Assert Different External Ids
DXUITC-604:To check the Language targeting as Italian                                         Assert Lang Targeting
DXUITC-6580:Creative is created with External source id as “SalesForce"                       Assert Salesforce External Id
DXUITC-6340:Creative is created with External source id                                       Creatives With Validation Of External Ids
\                                                                                             Assert Creative Name
DXUITC-6349:External source id value sholud accepts numbers                                   Assert External Ids With Numbers
DXUITC-6351:External source id value sholud accepts characters                                Assert External Ids With Chars
DXUITC-605:To check the Language targeting as Polish                                          Assert Lang Targeting
DXUITC-6357:Creative is created with multiple External source id                              Creatives With Multiple External Ids
\                                                                                             Assert Multiple External Ids
DXUITC-606:To check the Language targeting as Portuguese                                      Assert Lang Targeting
DXUITC-663:To verify the verify the Click Tracking should be enabled                          Assert Click Tracking
DXUITC-654: To verify the valid Ad tag section is saved                                       Valid Tags Entered
DXUITC-4931:To check name field should not be blank                                           Validation While Updating Creatives
\                                                                                             Blank Creative Name
DXUITC-499:To check concept field should not be blank while updating creative                 Blank Concept Name
DXUITC-670:To check the functionality of updated creative button                              Update Details With Limit Values
DXUITC-488:To check name field accepts 255 characters while updating creative                 Assert Updated Name
DXUITC-495:To check concept field accepts 201 characters while updating creative              Assert Updated Concept
DXUITC-504:To check selected size should be appear for creative while updating creative       Assert Updated Size
DXUITC-6343:External ID is updated on creative edit page                                      Assert Updated External Ids
DXUITC-607:To check the Language targeting as Spanish                                         Creatives With Spanish Lang Targeting
\                                                                                             Assert Lang Targeting
DXUITC-662:To verify the Click Tracking should be disabled                                    Assert Click Tracking Disabled
DXUITC-657:To verify the original tag in tag field                                            Valid Tags Entered
DXUITC-489:To check name field should accept special characters while updating creative       Update Creatives With Special Chars
DXUITC-671:To verify that updated name should be present on creative list page                Assert Updated Name
DXUITC-496:To check concept field should accept special characters while updating creative    Assert Updated Concept
DXUITC-6358:Creative with External source id and then added multiple on edit page             Assert Updated Multiple External Ids
=========================================================================================== ====================================================
