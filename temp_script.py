X = [0.00,0.2,0.33,0.43,0.63,0.66,1.00]
Y = [0.00,0.25,0.25,0.50,0.50,1.00,1.00]

area, area_correct = 0, 0.5575
i_iter = 1
coeff = 0
while abs(area - area_correct) > 1e-9:
    i_div = 1/(i_iter + 1)
    if area < area_correct:
        coeff += i_div
    else:
        coeff -= i_div

    for i, x in enumerate(X[:-1]):
        # find the best estimation


        tmp_mid_x = (1-coeff)*X[i+1] + coeff*X[i]
        tmp_mid_y = (1-coeff)*Y[i+1] + coeff*Y[i]
        tmp_width = X[i+1] - X[i]

        area += tmp_width*tmp_mid_y
    i_iter += 1
print(area)
