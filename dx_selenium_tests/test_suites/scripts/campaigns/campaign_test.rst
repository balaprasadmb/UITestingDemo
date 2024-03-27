================= ==============================
Settings           Value
================= ==============================
Library            campaign_test.CampaignTest
Force Tags         campaigns
================= ==============================


======================================================================================= =========================================== ==========================
Test Case                                                                                       Action                                   Argument
======================================================================================= =========================================== ==========================
DXUITC-1514:To verify Campaign Name can not be blank                                      Login As Campaign Manager
\                                                                                         Fill Fields With Blank Data
\                                                                                         Blank Campaign Name
DXUITC-1543:To verify Campaign Start Date can not be blank                                Blank Start Date
DXUITC-1564:To verify Campaign End Date can not be blank                                  Blank End Date
DXUITC-995:To verify is select in tactics cannot be blank                                 Blank Tactics
DXUITC-1389:To verify name as blank for 'Add On Costs' section                            Blank Add On Costs
DXUITC-890:To verify that CPA should not be blank                                         Blank Cpa
DXUITC-893:To verify that IO Budget should not be blank                                   Blank Io Budget
DXUITC-896:To verify that COGS should not be blank                                        Blank Cogs
DXUITC-899:To verify that Margin should not be blank                                      Blank Io Margin
DXUITC-1810:To check 'Value' field as blank                                               Blank Activity Type
#DXUITC-1772:To check 3rd party tag id as blank                                           Blank Third Party Tag Id
DXUITC-1410:To verify 'CPM' field as blank                                                Blank Cpm
DXUITC-894:To verify that CPM should not be blank                                         Blank Cpm
DXUITC-1528:To verify Campaign Start Date accepts numbers in mm/dd/yyyy                   Complete Flow With Distribution
\                                                                                         Go To Campaign Show Page
\                                                                                         Assert Start Date
DXUITC-1560:To verify Campaign End Date accepts numbers in mm/dd/yyyy                     Assert End Date
DXUITC-879:Maximize Distribution                                                          Assert Objective
DXUITC-987:To verify that the new text box appear when custom is select in tactics        Assert Tactics
DXUITC-1057:To verify that Custom tactic is present with default                          Assert Tactics
DXUITC-1068:The new custom text box appeared in tactics accepts characters                Assert Tactics
DXUITC-1075:To verify that the budget in tactic section accepts numbers                   Assert Tactics Budget
DXUITC-1078:To verify that the impression in tactic section accepts numbers               Assert Tactics Impression Cap
DXUITC-1006:Add RMX External IDs                                                          Assert External Id Source
DXUITC-1376:To verify that the campaign is created with Brand Safety level 4              Assert Brand Safety
DXUITC-1381:The Whitelist section is observed for Brand Safety level 4                    Assert Brand Safety
DXUITC-1391:To verify that the manualy entered whiltelist is present                      Assert Whitelist
DXUITC-1416:To verify that the manualy entered blacklist is present                       Assert Blacklist
DXUITC-1382:To enter valid name for 'Add On Costs' section                                Go To Campaign Edit
\                                                                                         Assert Aoc Name
DXUITC-1400:To enter valid value for CPM field under 'Add On Costs' section               Assert Aoc Cpm Value
DXUITC-341:Allow fractional percentages in margin field                                   Assert Margin
DXUITC-1535:To verify Campaign Start Date accepts date as past date                       Complete Flow With Ctr
\                                                                                         Assert Start Date
\                                                                                         Go To Campaign Show Page
DXUITC-1562:To verify Campaign End Date accepts date as past date                         Assert End Date
DXUITC-1855:To check valid values for Campaign Objective i.e. Maximize CTR                Assert Objective
DXUITC-875:Maximize CTR                                                                   Assert Objective
DXUITC-1071:The new custom text box appeared in tactics accepts numbers                   Assert Tactics
DXUITC-1018:Add AtlasExternal IDs                                                         Assert External Id Source
DXUITC-1384:To verify that the exported blacklist is present for the campaign             Assert Uploaded Blacklist
DXUITC-1418:To verify that the exported whitelist is present for the campaign             Assert Uploaded Whitelist
DXUITC-1533:To verify Campaign Start Date accepts date in future                          Complete Flow With Future Dates
\                                                                                         Go To Campaign Show Page
\                                                                                         Assert Start Date
DXUITC-1561:To verify Campaign End Date accepts date in future                            Assert End Date
DXUITC-1073:The new custom text box appeared in tactics accepts spcl char                 Assert Tactics
DXUITC-1020:Add WURFL External IDs                                                        Assert External Id Source
DXUITC-1452:To verify that the .txt exported whitelist is present for the campaign        Assert Uploaded Whitelist
DXUITC-1429:To verify that the .txt exported blacklist is present for the campaign        Assert Uploaded Blacklist
DXUITC-1052:To verify that retargeting tactic is present with default                     Complete Flow With Retargeting Xls
\                                                                                         Go To Campaign Show Page
DXUITC-1023:Add Bluekai External IDs                                                      Assert External Id Source
DXUITC-1431:To verify that the .xls exported blacklist is present for the campaign        Assert Uploaded Blacklist
DXUITC-1454:To verify that the .xls exported whitelist is present for the campaign        Assert Uploaded Whitelist
DXUITC-1054:To verify that Optimized tactic is present with default                       Complete Flow With Optimized Xlsx
\                                                                                         Go To Campaign Show Page
DXUITC-1024:Add MediaMind External IDs                                                    Assert External Id Source
DXUITC-1432:To verify that the .xlxs exported blacklist is present for the campaign       Assert Uploaded Blacklist
DXUITC-1455:To verify that the .xlxs exported whitelist is present for the campaign       Assert Uploaded Whitelist
DXUITC-1056:To verify that Channel tactic is present with default                         Complete Flow With Channel Xlsx
\                                                                                         Go To Campaign Show Page
DXUITC-1025:Add Facebook External IDs                                                     Assert External Id Source
DXUITC-1474:To verify that the blacklist and whitelist are present for campaign           Assert Uploaded Blacklist
\                                                                                         Assert Uploaded Whitelist
DXUITC-1537:To verify Campaign Start Date value can not exceeds end date value            Date Ahead
\                                                                                         Start Date Exceeds
DXUITC-1563:To verify Campaign End Date value can not be before start date value          End Date Before
DXUITC-4617:To verify that Bulk Assign pixel button is available                          Create Campaign Page
\                                                                                         Verify Bulk Assign Pixels
DXUITC-4618:To verify that Bulk Assign pixel button functionality                         Verify Bulk Assign Pixels Contents
DXUITC-4619:To verify that "Pixel Type" drop down on popup                                Verify Bulk Pixel Type
DXUITC-4620:To verify selecting "Pixel Type" as "Learning Pixles" no text box appear      Verify No New Textbox Appear
DXUITC-4621:To verify selecting "Pixel Type" as "Conversion Pixel" Value text box         Verify New Textbox Appear
DXUITC-4624:To verify Search functionality on Bulk Assign Pixels pop up                   Verify Search Activities
DXUITC-4626:To verify pixels are not saved with invalid data                              Verify Conversion Value Char Data
DXUITC-4627:To verify pixels are not saved with invalid data                              Verify Conversion Value Special Chars
DXUITC-4625:To verify Close( X ) button functionality of "Bulk Assign Pixel" Pop up       Popup Should Close
DXUITC-1134:To verify the content of Geographic Targeting section                         Geo Target Section
DXUITC-1140:To verify that the region list is shown for United states                     Select Region Us
DXUITC-1165:To verify that the region list is shown for Brazil                            Select Region Brazil
DXUITC-1169:To verify that the region list is shown for Canada                            Select Region Canada
DXUITC-1172:To verify that the region list is shown for France                            Select Region France
DXUITC-1173:To verify that the region list is shown for Germany                           Select Region Germany
DXUITC-1174:To verify that the region list is shown for Great Britain                     Select Region Gb
DXUITC-1175:To verify that the region list is shown for Ireland                           Select Region Ireland
DXUITC-1176:To verify that the region list is shown for Italy                             Select Region Italy
DXUITC-1177:To verify that the region list is shown for Poland                            Select Region Poland
DXUITC-1179:To verify that the region list is shown for Spain                             Select Region Spain
DXUITC-1296:To verify the content of Metrocodes in specify regions                        Geo Target Section Metrocodes
#DXUITC-1299:To verify that the Metrocode list is shown for United states                 Metrocodes Shown For Us
DXUITC-1313:To verify that the Metrocode option is not shown for Brazil                   Metrocodes Not Shown For Others              Brazil
DXUITC-1315:To verify that the Metrocode option is not shown for Canada                   Metrocodes Not Shown For Others              Canada
DXUITC-1316:To verify that the Metrocode option is not shown for France                   Metrocodes Not Shown For Others              France
DXUITC-1317:To verify that the Metrocode option is not shown for Germany                  Metrocodes Not Shown For Others              Germany
DXUITC-1318:To verify that the Metrocode option is not shown for Great Britain            Metrocodes Not Shown For Others              Great Britain
DXUITC-1319:To verify that the Metrocode option is not shown for Ireland                  Metrocodes Not Shown For Others              Ireland
DXUITC-1320:To verify that the Metrocode option is not shown for Italy                    Metrocodes Not Shown For Others              Italy
DXUITC-1321:To verify that the Metrocode option is not shown for Poland                   Metrocodes Not Shown For Others              Poland
DXUITC-1322:To verify that the Metrocode option is not shown for Spain                    Metrocodes Not Shown For Others              Spain
DXUITC-1101:To verify that applied country United states is present                       Verify Applied Country
\                                                                                         Verify Applied Country On Edit Page          United States
DXUITC-1105:To verify that applied country Brazil is present                              Verify Applied Country On Edit Page          Brazil
DXUITC-1107:To verify that applied country Canada is present                              Verify Applied Country On Edit Page          Canada
DXUITC-1108:To verify that applied country France is present                              Verify Applied Country On Edit Page          France
DXUITC-1111:To verify that applied country Germany is present                             Verify Applied Country On Edit Page          Germany
DXUITC-1116:To verify that applied country Great Britain is present                       Verify Applied Country On Edit Page          Great Britain
DXUITC-1117:To verify that applied country Ireland is present                             Verify Applied Country On Edit Page          Ireland
DXUITC-1118:To verify that applied country Italy is present                               Verify Applied Country On Edit Page          Italy
DXUITC-1118:To verify that applied country Poland is present                              Verify Applied Country On Edit Page          Poland
DXUITC-1118:To verify that applied country Spain is present                               Verify Applied Country On Edit Page          Spain
DXUITC-1790:To verify 3rd party tag id not accepts negative ID                            Fill Fields With Negative Values
\                                                                                         Negative Value Third Party Tag Id
DXUITC-1814:To verify 'Value' field not accepts negative value                            Negative value Filter Values
DXUITC-1417:To verify 'CPM' field not accepts Negative Value                              Negative Value Cpm
DXUITC-1866:To verify CTR Goal not accepts Negative value                                 Negative Value Ctr Goal
DXUITC-1808:To verify Value field not accepts alphanumeric values                         Fill Fields With Alphanumeric Values
\                                                                                         Alphanumeric Value Third Party Tag Id
DXUITC-1760:To verify 3rd party tag id not accepts alphanumeric values                    Alphanumeric Value Filter Values
\                                                                                         Language Targeting Test Cases
DXUITC-1080:To verify language targeting page content                                     Language Targeting Page Content
DXUITC-1088:To verify select button functionality                                         Select Button Functionality
DXUITC-935:To verify that CPA should not be accept special characters                     Fill Fields With Special Character Data
\                                                                                         Special Char Cpa
DXUITC-1415:To verify 'CPM' field not accepts Special characters                          Special Char Cpm
DXUITC-936:To verify that IO Budget should not accept special characters                  Special Char Io Budget
#DXUITC-1551:To verify Insertion Order accepts Special Characters                         Special Char Insertion Order
DXUITC-938:To verify that COGS should not accept special characters                       Special Char Cog
DXUITC-924:To verify that CPA should not be accept characters                             Fill Fields With String Data
\                                                                                         String Cpa
DXUITC-926:To verify that IO Budget should not accept characters                          String Io Budget
DXUITC-929:To verify that CPM should not accept characters                                String Cpm
DXUITC-930:To verify that COGS should not accept characters                               String Cog
DXUITC-1076:To verify that the budget in tactic section do not accepts chars              String Budget
DXUITC-1079:To verify that the impression in tactic section do not accepts chars          String Impression
DXUITC-1540:To verify calendar appears when clicked on start date text box                Datepicker Should Visible                      start
DXUITC-1559:To verify calendar appears when clicked on end date text box                  Datepicker Should Visible                      end
DXUITC-891:To verify that CPA should accept value between 0.01 to 10000                   Fill Fields With Max Range Data
\                                                                                         Range Cpa
DXUITC-892:To verify that IO Budget should accept value between 0.01 to max limit         Range Io Budget
DXUITC-895:To verify that CPM should accept value between 0.01 to 100                     Range Cpm
#DXUITC-900:To verify that Margin should accept value between 0 to 100                    Range Margin
DXUITC-1869:To check CTR Goal not accepts value more than 100                             Range Goal Ctr
DXUITC-1864:To check CTR Goal not accepts Special Characters                              Special Chars Ctr Goal
DXUITC-1859:To check CTR Goal as blank                                                    Blank Ctr Goal
DXUITC-1779:To check 3rd party tag id value as 4 digit                                    Fill Fields With Limit Data
DXUITC-1395:To verify name fields accepts 255 characters                                  Fill Activity With Max Limit
DXUITC-1397:To verify name fields not accepts more than 255 characters                    Aoc Name Exceeding Limit
DXUITC-1414:To verify 'CPM' field not accepts Alphanumeruc value                          Fill Cpm Alphanumeric Value
DXUITC-1067:To verify that the tactics not accepts not more than 255 characters           Fill Tactics Name With Limit
DXUITC-996:To verify that the tactics accepts 255 characters                              Fill Tactics Name With Limit Data
DXUITC-1026:Add Facebook campaign External IDs                                            Fill Fields With Facebook Campaign
\                                                                                         Go To Campaign Show Page
\                                                                                         Assert External Id Source
DXUITC-1344:To verify that the default level of Brand Safety is level 2                   Assert Brand Safety
DXUITC-1028:Add Facebook Page Post Ad External IDs                                        Fill Fields With Brand Safety One
\                                                                                         Go To Campaign Show Page
\                                                                                         Assert External Id Source
DXUITC-1346:To verify that the campaign is created with Brand Safety level 1              Assert Brand Safety
DXUITC-4622:To verify pixels are assign to campaign with Learning Pixel                   Create Campaign Page
\                                                                                         Assign Learning Pixel Type
DXUITC-4623:To verify pixels are assign to campaign with Conversion Pixels                Create Campaign Page
\                                                                                         Assign Conversion Pixel Type
DXUITC-1029:Add External IDs without value                                                External Id Value Blank
DXUITC-1066:Edit External IDs                                                             Edit External Id Value
DXUITC-1072:External ID button functionality                                              Create Campaign Page
\                                                                                         Verify External Ids Contents
DXUITC-5173:To verify the GeoFenced regions accept only CSV file                          Geofenced Region Valid File
DXUITC-5174:To verify the GeoFenced regions name accept less than 255 characters          Geofenced Invalid Name
DXUITC-5176:To verify the GeoFenced regions does not accept invalid file                  Geofenced Region Invalid File
DXUITC-5175:To verify GeoFenced regions name accept alphanumeric characters               Geofenced Region Alphanumeric Name
DXUITC-1460:To verify the functionality of Info Icon on blacklist section                 Blacklist Info Icon
DXUITC-1461:To verify the functionality of Info Icon on Whitelist section                 Whitelist Info Icon
DXUITC-1424:To verify that the blank .csv exported blacklist is present                   Campaign With Brand Safety Three
\                                                                                         Verify Blank Csv Present
DXUITC-1375:To verify that the campaign is created with Brand Safety level 3              Assert Brand Safety
DXUITC-1476:To verify that the updated blacklist and whitelist are present                Updated Blacklist Whitelist
DXUITC-5013:Blacklist/whitelist should get override with new domains                      Override Blacklist Whitelist
DXUITC-1477:To verify that the deleted blacklist and whitelist are not present            Deleted Blacklist Whitelist
DXUITC-1094:Browser Setting                                                               Lang Target Base Settings                      1
DXUITC-1125:Content Language                                                              Lang Target Base Settings                      2
DXUITC-1128:Either Browse or Content                                                      Lang Target Base Settings                      3
DXUITC-1149:Edit Language targeting                                                       Edit Lang Target Base Settings
DXUITC-1751:To check contents of Maximize Performance and Distribution                    Create Campaign Page
\                                                                                         Verify Max Performance Distribution
DXUITC-1823:To check contents of Campaign Objective i.e. Maximize CTR                     Verify Max Ctr
DXUITC-876:Online Campaign                                                                Verify Campaign Objective
DXUITC-1343:To check contents of Add On Costs section                                     Verify Add On Cost Contents
DXUITC-887:To verify the content of Budget and Spending Setup section                     Verify Budget Spending
DXUITC-888:To verify the CPA is present uder cost model drop down                         Verify Cost Model
DXUITC-966:To verify the content of Tactics                                               Verify Tactics
DXUITC-979:To verify the content of Tactics when expanded                                 Verify Tactics Contents
DXUITC-984:To verify the content of Tactics name drop down                                Verify Tactics Name Contents
DXUITC-978:External IDs                                                                   Verify External Ids Contents
DXUITC-1090:To verify the content of Geographic Targeting section                         Verify Geographic Targeting Section
DXUITC-1095:To verify the functionality of '>', '>>', '<<', '<' buttons                   Verify Buttons In Geographic Targeting
DXUITC-1150:To verify the functionality of serach box in geotargeting sections            Verify Search In Geographic Targeting
DXUITC-1182:To verify the functionality of serach box in geotargeting sections            Verify Search In Geographic Targeting
DXUITC-1258:To verify the content of specify regions within postal code                   Verify Postal Codes In Geo Target
DXUITC-5172:To verify the content of Geographic Targeting section Geofenced regions       Verify Geofenced In Geo Target
DXUITC-1378:To verify the content of Blacklist                                            Verify Blacklist Section
DXUITC-1379:To verify the content of Whiltelist                                           Verify Whitelist Section
DXUITC-1164:Brand Safety contents                                                         Verify Brandsafety Section
DXUITC-880:Maximize Completed Ad Views                                                    Create Campaign With Completed Ad Views
\                                                                                         Go To Campaign Show Page
\                                                                                         Assert Objective
DXUITC-877:Mobile Campaign                                                                Verify Campaign Objective Under Mobile
DXUITC-878:Video Campaign                                                                 Verify Campaign Objective Under Video
======================================================================================= =========================================== ==========================
