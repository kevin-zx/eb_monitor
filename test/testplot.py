# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt



# a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199]
# b = [4.869964996,4.870935589,4.868302974,4.864423656,4.863017483,4.863881558,4.864855585,4.862808842,4.861542378,4.864002834,4.864006495,4.865190768,4.864623816,4.862690897,4.863822713,4.863626228,4.863454015,4.862426399,4.864913341,4.862468682,4.863090703,4.861221769,4.861382946,4.862718062,4.865422955,4.863265196,4.862214833,4.86209046,4.862063311,4.860321482,4.864889171,4.861937761,4.862456987,4.859383733,4.865311095,4.861420011,4.863143475,4.861965247,4.86035127,4.863050779,4.861803782,4.861040818,4.863296847,4.861782857,4.860633614,4.862253672,4.856873308,4.862073089,4.858862137,4.860730827,4.861440486,4.860787709,4.859691778,4.8679434,4.863057381,4.858616575,4.857925743,4.859257606,4.860362983,4.857285695,4.858273888,4.860576703,4.860296018,4.863052902,4.864367145,4.862667042,4.861391109,4.860766413,4.860921024,4.865144634,4.86382667,4.865022295,4.86313246,4.86193459,4.863493265,4.863175348,4.858862453,4.857113484,4.860803391,4.858929797,4.855286672,4.85841774,4.858620082,4.856365222,4.855927131,4.858550773,4.859168692,4.856948706,4.858281174,4.857332691,4.85645668,4.856002305,4.857450746,4.858965621,4.858245899,4.8614752,4.857403382,4.859576216,4.859574315,4.859446224,4.859412133,4.858126209,4.858262681,4.859735964,4.865643609,4.861590473,4.857181531,4.85877069,4.859767981,4.859925474,4.859201188,4.860020241,4.858013811,4.859867603,4.86065854,4.857906432,4.860592112,4.858277829,4.855020193,4.85590632,4.864330491,4.857933619,4.860288137,4.857552912,4.856122564,4.856361697,4.856684011,4.858610502,4.858469382,4.857863209,4.854858419,4.857460351,4.858757676,4.858796334,4.856761055,4.85520559,4.853161948,4.855714916,4.854684302,4.853597195,4.857056182,4.857553955,4.854442778,4.853715427,4.853085951,4.85209202,4.853991589,4.858051467,4.854639228,4.858635105,4.856376537,4.858211047,4.856109125,4.853681541,4.855996116,4.854811067,4.86054884,4.856704223,4.856190547,4.854642583,4.855062683,4.851968487,4.854185905,4.854887965,4.855784613,4.856141778,4.856365603,4.856822294,4.854981041,4.858567392,4.858062166,4.859734509,4.856307539,4.853784504,4.854969762,4.853584007,4.855002862,4.857720443,4.857976563,4.853755707,4.855239357,4.856337326,4.852342276,4.852558279,4.856060041,4.856703078,4.85191716,4.854377561,4.854693774,4.852446896,4.85495638,4.854836739,4.858921598,4.857139025,4.855129513,4.852610272,4.853332365]
# plt.plot(a, b, "b-")
# plt.show()
# plt.figure(1)
# ax = plt.subplot(211)
x = np.linspace(0,47,48)
print x
# # for i in xrange(5):
# plt.figure(1)
# plt.plot(x, 1/(1+(math.e**(0.15*(x-35))))/4)
#
# plt.show()

