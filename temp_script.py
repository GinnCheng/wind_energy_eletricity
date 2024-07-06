def learing_integration(X,Y):
    area, area_correct = 0., 0.5575
    i_iter = 2.0
    coeff = 0.0

    while abs(area - area_correct) > 1e-9:
        area = 0.0
        i_div = 1.0/i_iter

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

        i_iter = i_iter*2

    return area, coeff

if __name__ == '__main__':
    area, coeff = ROC_learing_integration(X,Y)
    print(area, coeff)
