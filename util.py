import datetime

def nextround_timer(times):
    now = datetime.datetime.now()
    nhour = now.hour
    sortlist = sorted(times, reverse=True)
    next_round_list = []
    for i in sortlist:

        if nhour < i:
            n = i-nhour
            next_round_list.append(i)
    try:
        next_round = min(next_round_list)
    except ValueError:
        next_round = min(sortlist) 

    intime = next_round-nhour if nhour <= next_round else (24-nhour)+next_round

    nextround_times = {
        "clock": f"by {next_round}:00",
        "in": f"In {intime} hours"
    }
    return nextround_times
