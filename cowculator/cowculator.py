def grazing_pasture_cost(acre_per_month=1.2, months=6, fee_per_acre=30):
    gpc = acre_per_month * fee_per_acre * months
    return round(gpc,2)

def winter_feed_cost(daily_feed_lbs=40, price_per_ton=65, days_on_feed=180):
    TON_PER_POUND = 1.0/2000
    wfc = daily_feed_lbs * price_per_ton * TON_PER_POUND * days_on_feed
    return round(wfc,2)

def yardage(overhead_per_year=69.79, vet_breed_insurance=125.43):
    y = overhead_per_year + vet_breed_insurance
    return round(y,2)

def value(weight_lbs=600, price_per_cwt=158):
    v = weight_lbs/100.0 * price_per_cwt
    return round(v, 2)

def cull_sale(weight_lbs=1300, price_per_cwt=70):
    cs = weight_lbs/100.0 * price_per_cwt
    return round(cs, 2)

def total_income(weight_calf=600, weight_cull=1300, pcwt_calf=158, pcwt_cull=70, calf_crops=4.7, death_rate=0.03):
    val = value(weight_calf, pcwt_calf)
    cul = cull_sale(weight_cull, pcwt_cull)
    net = val * calf_crops + cul * (1-death_rate)
    return round(net, 2)

def total_expenses(years=4.7, gc=216, wc=252, yc=90):
    return years*(gc + wc + yc)

def net_income(ti=5204.63, te=2622.6):
    return ti - te