# Crime analysis: USA FBI 2020
Power BI Analytical Project for the Vilnius Coding School
## Project Overview
This Project analyzes 7.9M crime incidents, 8.9M victims, and 2.2M arrests based on FBI 2020 public data.
Data source - official US website https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads
<details>
  <summary>Small glimpse at the original txt master file (4 GB, I'm showing only 40 lines)</summary>

['BH50AK0010100000000000000                ANCHORAGE                     AK1C941Y         3030020A         00028638800  39000000000000000000      000000000000000000      000000000000000000      000000000000000000      000000000  002020NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN020            \n']
['BH50AK0010200000000000000        20210101FAIRBANKS                     AK4 941Y         3030020AA        00003083200 258000000000000000000      000000000000000000      000000000000000000      000000000000000000      00000000006112020NYNNYNNYNNNNNYNNYNNYNNYNNYNNYNNYNNYN090            \n']
['0150AK0010200C60BROS9728N20201231R00010010100    N                                      N\n']
['0250AK0010200C60BROS9728N2020123111ACA  20   N  40       88\n']
['0450AK0010200C60BROS9728N2020123100111A                           I24FINN     M    01OK                                                \n']
['0550AK0010200C60BROS9728N202012310142MBN\n']
['0150AK0010200CE0BAARR728N20200819R00010010200    N                                      N\n']
['0250AK0010200CE0BAARR728N2020081911BCN  20   N  99       88\n']
['0450AK0010200CE0BAARR728N2020081900111B                           I03MBNN     N    01BE02BE                                            \n']
['0550AK0010200CE0BAARR728N202008190112MBN\n']
['0550AK0010200CE0BAARR728N202008190241MBN\n']
['0150AK0010200CE0BIBTR728N20201120R00010010100    N                                      N\n']
['0250AK0010200CE0BIBTR728N2020112013BCN  20   N  40       88\n']
['0450AK0010200CE0BIBTR728N2020112000113B                           I40MWNR     M    01BG                                                \n']
['0550AK0010200CE0BIBTR728N202011200132FWU\n']
['0150AK0010200CN0BABTL728N20201101R00010010100    N                                      N\n']
['0250AK0010200CN0BABTL728N20201101220CN  1901F            88\n']
['0350AK0010200CN0BABTL728N20201101716000005000                                                         \n']
['0450AK0010200CN0BABTL728N20201101001220                           I31FBNR                                                              \n']
['0550AK0010200CN0BABTL728N2020110100     \n']
['0150AK0010200CN0BAETM728N20200804R00010010100    N                                      N\n']
['0250AK0010200CN0BAETM728N2020080423GCN  23               88\n']
['0350AK0010200CN0BAETM728N20200804738000000650                                                         \n']
['0450AK0010200CN0BAETM728N2020080400123G                           I51FANR                                                              \n']
['0550AK0010200CN0BAETM728N2020080400     \n']
['0150AK0010200CN0BAFBV728N20200621R00010010100    N                                      N\n']
['0250AK0010200CN0BAFBV728N2020062123FCN  18               88\n']
['0350AK0010200CN0BAFBV728N20200621725000000070                                                         \n']
['0350AK0010200CN0BAFBV728N20200621765000000000                                                         \n']
['0450AK0010200CN0BAFBV728N2020062100123F                           I38FWNN          01RU                                                \n']
['0550AK0010200CN0BAFBV728N202006210100FUU\n']
['0150AK0010200CN0BAVBV728N20201101R14010010100    N                                      N\n']
['0250AK0010200CN0BAVBV728N20201101220CN  20  N            88\n']
['0350AK0010200CN0BAVBV728N20201101706000001183                                                         \n']
['0450AK0010200CN0BAVBV728N20201101001220                           I22MBNR                                                              \n']
['0550AK0010200CN0BAVBV728N2020110100     \n']
['0150AK0010200CN0BICRC728N20200801R00010010100    N                                      N\n']
['0250AK0010200CN0BICRC728N2020080113ACN  20   N  40       88\n']
['0450AK0010200CN0BICRC728N2020080100113A                           I16FWNR06   I    01BG                                                \n']
</details>

To "decrypt" the data, I've started with reading NIBRS record description pdf file, which consisted of 99 pages (sadly enough, this file was some sort of a scanned copy, so AI couldn't really help with making my work faster, and kept hallucinating).


