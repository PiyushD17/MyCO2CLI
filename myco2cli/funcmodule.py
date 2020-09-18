def co2calc(emission_val, distance, unit, output):
    if output=='na' and unit=='km':
        output="kg"
        # distance_in_km*emissions_in_gms/1000
        return round((emission_val*float(distance))/1000,1),output,unit
    elif output=='na' and unit=='m':
        output="g"
        # distance_in_m/1000*emissions_in_gms
        return round(emission_val*float(distance)/1000),output,unit

    elif output=='kg' and unit=='km':
        # distance_in_km*emissions_in_gms/1000
        return round(emission_val*float(distance)/1000,1), output,unit

    elif output=='g' and unit=='km':
        # distance_in_km*emissions_in_gms
        return emission_val*float(distance), output,unit
    elif output=='kg' and unit=='m':
        # distance_in_m/1000*emissions_in_gms/1000
        return round((emission_val*float(distance)/1000)/1000,1), output,unit
            # distance_in_m/1000*emissions_in_gms
    else:
        # output=='g' and unit=='m'
        # distance_in_m/1000*emissions_in_gms
        return round((emission_val*float(distance)/1000),1), output,unit
