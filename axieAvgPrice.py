PrvyAxie = [0.02, 0.02569, 0.035]
DruhyAxie = [0.00399, 0.004, 0.004, 0.0041, 0.0042, 0.0042, 0.0045, 0.00451, 0.0046, 0.0049, 0.0049, 0.005, 0.005, 0.005, 0.00529, 0.0053, 0.00532, 0.00544, 0.0055, 0.0055, 0.0055, 0.006, 0.006, 0.006, 0.006, 0.00647, 0.0065, 0.0065, 0.007, 0.007, 0.007, 0.007, 0.0074, 0.0074, 0.00744, 0.0075, 0.0075, 0.0075, 0.0075, 0.0079, 0.008, 0.008, 0.008, 0.008, 0.0081, 0.0081, 0.00825, 0.0084, 0.0084, 0.0084, 0.0085, 0.009, 0.009, 0.009, 0.009, 0.009, 0.00901, 0.0094, 0.0094, 0.0094, 0.0094, 0.00943, 0.00949, 0.0095, 0.0095, 0.00972, 0.0099, 0.0099, 0.0099, 0.00998, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.0103, 0.0104, 0.01044, 0.0106, 0.01081, 0.01092, 0.011, 0.011, 0.011, 0.011, 0.012, 0.012, 0.012, 0.012, 0.012, 0.012, 0.012, 0.0124, 0.01249, 0.01255, 0.013, 0.013, 0.01355, 0.01355, 0.01363, 0.01392, 0.014, 0.014, 0.014, 0.014, 0.014, 0.01433, 0.0145, 0.01473, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.01534, 0.0154, 0.0154, 0.0157, 0.016, 0.01612, 0.01622, 0.01647, 0.017, 0.017, 0.017, 0.017, 0.017, 0.01762, 0.018, 0.0188, 0.01884, 0.019, 0.019, 0.019, 0.0194, 0.01944, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.021, 0.02121, 0.022, 0.022, 0.0222, 0.0224, 0.02442, 0.025, 0.025, 0.0262, 0.0265, 0.0265, 0.0265, 0.028, 0.02831, 0.02844, 0.029, 0.02913, 0.02943, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.031, 0.031, 0.0314, 0.032, 0.032, 0.035, 0.035, 0.037, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04191, 0.045, 0.04518, 0.0457, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.053, 0.057, 0.06, 0.06, 0.06, 0.06, 0.06, 0.065, 0.0658, 0.0659, 0.07, 0.08, 0.08, 0.08, 0.08, 0.09, 0.09725, 0.1, 0.1, 0.105, 0.12, 0.12, 0.12, 0.12, 0.12, 0.125, 0.13, 0.13, 0.15, 0.17, 0.2, 0.22, 0.35, 0.5, 0.5, 0.51, 1]
TretiAxie = [0.0093, 0.0119, 0.05]
allAxies = []
allAxies.append(PrvyAxie)
allAxies.append(DruhyAxie)
allAxies.append(TretiAxie)

for axie in allAxies:
    currPrice=float(0)
    for price in axie:
        currPrice += price
    finalPrice = currPrice/len(axie)
    roundedPrice = round(finalPrice, 3)
    print(str(allAxies.index(axie))+": "+str(roundedPrice))