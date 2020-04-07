import cv2 as cv
import numpy as np
import math
import glob
import time

x_gap = []
y_gap = []
y_R_line = [[0, 169], [1, 165], [2, 163], [3, 179], [4, 175], [5, 175], [6, 174], [7, 172], [8, 168], [9, 170], [10, 164], [11, 163], [12, 153], [13, 165], [14, 156], [15, 162], [16, 160], [17, 168], [18, 163], [19, 166], [20, 165], [21, 162], [22, 163], [23, 163], [24, 161], [25, 165], [26, 168], [27, 173], [28, 171], [29, 172], [30, 174], [31, 171], [32, 172], [33, 175], [34, 170], [35, 177], [36, 169], [37, 170], [38, 164], [39, 162], [40, 160], [41, 159], [42, 159], [43, 160], [44, 156], [45, 163], [46, 156], [47, 167], [48, 167], [49, 168], [50, 164], [51, 168], [52, 162], [53, 169], [54, 165], [55, 166], [56, 164], [57, 158], [58, 158], [59, 153], [60, 158], [61, 155], [62, 159], [63, 160], [64, 165], [65, 165], [66, 168], [67, 165], [68, 169], [69, 161], [70, 165], [71, 158], [72, 154], [73, 157], [74, 160], [75, 166], [76, 160], [77, 161], [78, 156], [79, 157], [80, 156], [81, 159], [82, 157], [83, 158], [84, 158], [85, 162], [86, 161], [87, 158], [88, 148], [89, 149], [90, 145], [91, 144], [92, 147], [93, 147], [94, 147], [95, 149], [96, 151], [97, 147], [98, 154], [99, 162], [100, 155], [101, 161], [102, 154], [103, 156], [104, 148], [105, 153], [106, 143], [107, 150], [108, 147], [109, 152], [110, 154], [111, 146], [112, 154], [113, 151], [114, 158], [115, 157], [116, 164], [117, 158], [118, 164], [119, 156], [120, 159], [121, 153], [122, 159], [123, 157], [124, 160], [125, 160], [126, 160], [127, 159], [128, 157], [129, 154], [130, 154], [131, 154], [132, 152], [133, 158], [134, 149], [135, 152], [136, 156], [137, 153], [138, 153], [139, 154], [140, 150], [141, 155], [142, 155], [143, 154], [144, 155], [145, 148], [146, 156], [147, 146], [148, 145], [149, 144], [150, 149], [151, 144], [152, 151], [153, 143], [154, 143], [155, 142], [156, 149], [157, 152], [158, 145], [159, 148], [160, 148], [161, 149], [162, 140], [163, 137], [164, 131], [165, 124], [166, 133], [167, 131], [168, 135], [169, 135], [170, 136], [171, 136], [172, 129], [173, 127], [174, 125], [175, 124], [176, 124], [177, 130], [178, 124], [179, 131], [180, 124], [181, 119], [182, 108], [183, 112], [184, 103], [185, 114], [186, 110], [187, 118], [188, 112], [189, 119], [190, 114], [191, 115], [192, 127], [193, 109], [194, 113], [195, 99], [196, 96], [197, 99], [198, 91], [199, 101], [200, 99], [201, 103], [202, 106], [203, 103], [204, 102], [205, 100], [206, 100], [207, 99], [208, 97], [209, 96], [210, 95], [211, 94], [212, 92], [213, 93], [214, 92], [215, 92], [216, 92], [217, 87], [218, 89], [219, 95], [220, 100], [221, 104], [222, 104], [223, 100], [224, 100], [225, 93], [226, 99], [227, 96], [228, 100], [229, 102], [230, 110], [231, 109], [232, 105], [233, 105], [234, 100], [235, 96], [236, 96], [237, 92], [238, 91], [239, 93], [240, 86], [241, 89], [242, 82], [243, 87], [244, 83], [245, 82], [246, 82], [247, 84], [248, 90], [249, 98], [250, 106], [251, 113], [252, 115], [253, 115], [254, 114], [255, 114], [256, 111], [257, 115], [258, 113], [259, 115], [260, 113], [261, 116], [262, 109], [263, 115], [264, 108], [265, 103], [266, 107], [267, 102], [268, 108], [269, 104], [270, 108], [271, 108], [272, 107], [273, 108], [274, 104], [275, 101], [276, 100], [277, 97], [278, 101], [279, 107], [280, 116], [281, 110], [282, 113], [283, 110], [284, 109], [285, 109], [286, 111], [287, 106], [288, 105], [289, 110], [290, 111], [291, 108], [292, 110], [293, 108], [294, 104], [295, 105], [296, 98], [297, 107], [298, 105], [299, 115], [300, 124], [301, 119], [302, 111], [303, 112], [304, 99], [305, 104], [306, 106], [307, 103], [308, 119], [309, 109], [310, 119], [311, 113], [312, 110], [313, 102], [314, 104], [315, 103], [316, 108], [317, 116], [318, 120], [319, 122], [320, 122], [321, 113], [322, 110], [323, 102], [324, 102], [325, 100], [326, 104], [327, 102], [328, 106], [329, 111], [330, 104], [331, 109], [332, 103], [333, 103], [334, 106], [335, 108], [336, 108], [337, 116], [338, 114], [339, 116], [340, 111], [341, 105], [342, 105], [343, 101], [344, 100], [345, 102], [346, 98], [347, 99], [348, 101], [349, 100], [350, 100], [351, 90], [352, 93], [353, 91], [354, 91], [355, 89], [356, 99], [357, 89], [358, 109], [359, 111], [360, 112], [361, 119], [362, 116], [363, 115], [364, 113], [365, 112], [366, 109], [367, 111], [368, 105], [369, 104], [370, 100], [371, 100], [372, 101], [373, 122], [374, 120], [375, 123], [376, 122], [377, 115], [378, 111], [379, 113], [380, 109], [381, 116], [382, 116], [383, 116], [384, 118], [385, 108], [386, 110], [387, 107], [388, 107], [389, 115], [390, 113], [391, 120], [392, 117], [393, 117], [394, 112], [395, 108], [396, 102], [397, 90], [398, 90], [399, 89], [400, 91], [401, 93], [402, 102], [403, 109], [404, 109], [405, 119], [406, 100], [407, 97], [408, 83], [409, 85], [410, 93], [411, 106], [412, 93], [413, 98], [414, 88], [415, 86], [416, 93], [417, 96], [418, 109], [419, 114], [420, 118], [421, 119], [422, 111], [423, 107], [424, 101], [425, 103], [426, 98], [427, 106], [428, 104], [429, 106], [430, 108], [431, 104], [432, 102], [433, 108], [434, 101], [435, 111], [436, 104], [437, 109], [438, 105], [439, 106], [440, 108], [441, 107], [442, 109], [443, 108], [444, 103], [445, 103], [446, 101], [447, 99], [448, 99], [449, 103], [450, 96], [451, 102], [452, 90], [453, 92], [454, 91], [455, 95], [456, 119], [457, 118], [458, 136], [459, 141], [460, 137], [461, 139], [462, 130], [463, 127], [464, 122], [465, 121], [466, 115], [467, 118], [468, 108], [469, 104], [470, 98], [471, 88], [472, 86], [473, 83], [474, 80], [475, 81], [476, 81], [477, 78], [478, 80], [479, 79], [480, 78], [481, 83], [482, 89], [483, 87], [484, 82], [485, 85], [486, 81], [487, 93], [488, 94], [489, 104], [490, 99], [491, 99], [492, 90], [493, 98], [494, 98], [495, 97], [496, 96], [497, 97], [498, 90], [499, 95], [500, 89], [501, 96], [502, 94], [503, 100], [504, 97], [505, 93], [506, 91], [507, 88], [508, 85], [509, 85], [510, 81], [511, 88], [512, 80], [513, 89], [514, 82], [515, 81], [516, 82], [517, 82], [518, 78], [519, 82], [520, 78], [521, 89], [522, 87], [523, 92], [524, 92], [525, 92], [526, 89], [527, 94], [528, 92], [529, 93], [530, 95], [531, 106], [532, 94], [533, 104], [534, 94], [535, 96], [536, 95], [537, 100], [538, 96], [539, 111], [540, 99], [541, 107], [542, 96], [543, 93], [544, 93], [545, 92], [546, 95], [547, 95], [548, 108], [549, 104], [550, 125], [551, 122], [552, 120], [553, 113], [554, 96], [555, 95], [556, 93], [557, 83], [558, 96], [559, 90], [560, 96], [561, 101], [562, 96], [563, 97], [564, 98], [565, 99], [566, 97], [567, 97], [568, 95], [569, 95], [570, 98], [571, 97], [572, 97], [573, 101], [574, 90], [575, 97], [576, 92], [577, 95], [578, 91], [579, 94], [580, 89], [581, 98], [582, 96], [583, 97], [584, 98], [585, 94], [586, 93], [587, 102], [588, 107], [589, 108], [590, 110], [591, 100], [592, 93], [593, 89], [594, 85], [595, 95], [596, 93], [597, 105], [598, 96], [599, 95], [600, 93], [601, 90], [602, 96], [603, 105], [604, 100], [605, 104], [606, 97], [607, 91], [608, 93], [609, 85], [610, 95], [611, 91], [612, 96], [613, 94], [614, 92], [615, 90], [616, 93], [617, 90], [618, 93], [619, 95], [620, 89], [621, 93], [622, 83], [623, 80], [624, 78], [625, 76], [626, 76], [627, 79], [628, 77], [629, 84], [630, 85], [631, 91], [632, 91], [633, 91], [634, 87], [635, 89], [636, 89], [637, 102], [638, 90], [639, 89], [640, 87], [641, 84], [642, 87], [643, 90], [644, 92], [645, 92], [646, 93], [647, 91], [648, 80], [649, 78], [650, 83], [651, 97], [652, 88], [653, 95], [654, 77], [655, 82], [656, 73], [657, 84], [658, 91], [659, 85], [660, 101], [661, 97], [662, 95], [663, 104], [664, 90], [665, 96], [666, 91], [667, 88], [668, 93], [669, 90], [670, 90], [671, 96], [672, 86], [673, 98], [674, 101], [675, 111], [676, 96], [677, 102], [678, 82], [679, 85], [680, 77], [681, 81], [682, 80], [683, 82], [684, 85], [685, 86], [686, 102], [687, 101], [688, 108], [689, 100], [690, 94], [691, 89], [692, 81], [693, 85], [694, 84], [695, 84], [696, 79], [697, 78], [698, 76], [699, 84], [700, 82], [701, 87], [702, 97], [703, 95], [704, 101], [705, 104], [706, 93], [707, 95], [708, 94], [709, 93], [710, 93], [711, 92], [712, 91], [713, 88], [714, 82], [715, 82], [716, 76], [717, 83], [718, 84], [719, 95], [720, 95], [721, 94], [722, 88], [723, 80], [724, 78], [725, 78], [726, 76], [727, 82], [728, 80], [729, 82], [730, 84], [731, 84], [732, 81], [733, 89], [734, 83], [735, 88], [736, 96], [737, 95], [738, 105], [739, 102], [740, 105], [741, 101], [742, 102], [743, 100], [744, 96], [745, 91], [746, 90], [747, 95], [748, 93], [749, 92], [750, 89], [751, 92], [752, 88], [753, 97], [754, 99], [755, 96], [756, 99], [757, 101], [758, 106], [759, 108], [760, 95], [761, 97], [762, 84], [763, 83], [764, 91], [765, 88], [766, 104], [767, 108], [768, 115], [769, 117], [770, 118], [771, 123], [772, 128], [773, 127], [774, 130], [775, 126], [776, 124], [777, 120], [778, 120], [779, 112], [780, 106], [781, 96], [782, 79], [783, 64], [784, 59], [785, 57], [786, 51], [787, 64], [788, 62], [789, 76], [790, 89], [791, 104], [792, 107], [793, 110], [794, 105], [795, 102], [796, 95], [797, 95], [798, 89], [799, 88], [800, 89], [801, 83], [802, 89], [803, 87], [804, 85], [805, 90], [806, 71], [807, 59], [808, 44], [809, 36], [810, 88], [811, 133], [812, 228], [813, 247], [814, 248], [815, 198], [816, 116], [817, 61], [818, 51], [819, 44], [820, 78], [821, 105], [822, 121], [823, 141], [824, 124], [825, 114], [826, 83], [827, 74], [828, 85], [829, 81], [830, 99], [831, 98], [832, 106], [833, 99], [834, 91], [835, 85], [836, 70], [837, 76], [838, 75], [839, 89], [840, 93], [841, 89], [842, 84], [843, 91], [844, 78], [845, 92], [846, 76], [847, 82], [848, 75], [849, 72], [850, 75], [851, 76], [852, 76], [853, 84], [854, 74], [855, 72], [856, 73], [857, 62], [858, 84], [859, 89], [860, 103], [861, 113], [862, 78], [863, 56], [864, 31], [865, 53], [866, 220], [867, 251], [868, 247], [869, 250], [870, 252], [871, 249], [872, 249], [873, 243], [874, 52], [875, 31], [876, 27], [877, 36], [878, 65], [879, 74], [880, 83], [881, 90], [882, 101], [883, 107], [884, 108], [885, 109], [886, 98], [887, 105], [888, 83], [889, 77], [890, 76], [891, 74], [892, 82], [893, 89], [894, 99], [895, 100], [896, 104], [897, 95], [898, 88], [899, 79], [900, 87], [901, 90], [902, 88], [903, 97], [904, 81], [905, 86], [906, 72], [907, 77], [908, 71], [909, 78], [910, 78], [911, 78], [912, 81], [913, 80], [914, 83], [915, 82], [916, 85], [917, 82], [918, 85], [919, 80], [920, 81], [921, 73], [922, 76], [923, 65], [924, 79], [925, 84], [926, 86], [927, 86], [928, 87], [929, 85], [930, 86], [931, 86], [932, 86], [933, 87], [934, 85], [935, 86], [936, 76], [937, 70], [938, 65], [939, 77], [940, 79], [941, 83], [942, 93], [943, 85], [944, 91], [945, 90], [946, 86], [947, 91], [948, 87], [949, 93], [950, 92], [951, 93], [952, 99], [953, 93], [954, 97], [955, 91], [956, 89], [957, 89], [958, 88], [959, 91], [960, 88], [961, 90], [962, 83], [963, 83], [964, 84], [965, 84], [966, 85], [967, 92], [968, 83], [969, 93], [970, 83], [971, 83], [972, 71], [973, 70], [974, 69], [975, 69], [976, 81], [977, 77], [978, 85], [979, 80], [980, 79], [981, 78], [982, 78], [983, 82], [984, 80], [985, 85], [986, 77], [987, 76], [988, 73], [989, 68], [990, 72], [991, 67], [992, 72], [993, 68], [994, 70], [995, 71], [996, 73], [997, 83], [998, 83], [999, 87], [1000, 76], [1001, 76], [1002, 65], [1003, 67], [1004, 69], [1005, 71], [1006, 81], [1007, 73], [1008, 74], [1009, 68], [1010, 64], [1011, 63], [1012, 62], [1013, 69], [1014, 63], [1015, 75], [1016, 63], [1017, 69], [1018, 65], [1019, 66], [1020, 75], [1021, 79], [1022, 77], [1023, 82], [1024, 73], [1025, 74], [1026, 71], [1027, 70], [1028, 73], [1029, 74], [1030, 79], [1031, 74], [1032, 79], [1033, 76], [1034, 81], [1035, 90], [1036, 89], [1037, 94], [1038, 96], [1039, 92], [1040, 97], [1041, 95], [1042, 94], [1043, 92], [1044, 93], [1045, 87], [1046, 87], [1047, 80], [1048, 73], [1049, 76], [1050, 65], [1051, 74], [1052, 65], [1053, 68], [1054, 64], [1055, 59], [1056, 65], [1057, 55], [1058, 65], [1059, 62], [1060, 69], [1061, 67], [1062, 66], [1063, 65], [1064, 60], [1065, 60], [1066, 66], [1067, 62], [1068, 71], [1069, 71], [1070, 69], [1071, 72], [1072, 69], [1073, 61], [1074, 67], [1075, 57], [1076, 63], [1077, 64], [1078, 62], [1079, 63]]

for i_Xgap in range(0, len(y_R_line)):
    a_Xgap = y_R_line[i_Xgap][1] - y_R_line[i_Xgap - 1][1]
            
    if a_Xgap >= 15:
        x_gap.append(i_Xgap)
        x_gap.append(a_Xgap)

    
