import pandas

commentary=[]
dic={"batter":[],"baller":[],"ball_speed":[],"ball_length":[],"ball_swing":[],"wicket":[],"wide":[],"runs":[],"shot":[],"commentary":[]}

with open("match_data\ind-vs-pak.txt","r+") as file:
    commentary=file.readlines()
    for temp in commentary:
        temp=temp.split(".")
        for i in temp:
            i=i.replace("!",",")
            delivery=i.split(",")

            f1=0
            for k in delivery:
                if k.strip()=="THATS OUT":
                    f1=1
                    break
            if f1:
                continue
            if len(delivery[0].split())>3 and len(delivery[0].split())<7 and len(delivery)>2:
                if "to" in delivery[0].split():

                    dic["batter"].append(delivery[0].split("to")[1].strip())
                    dic["baller"].append(delivery[0].split("to")[0].strip())

                    if "out" in delivery[1].lower():
                        dic["wicket"].append(1)
                    else:
                        dic["wicket"].append(0)

                    RUNS={'one':1,"two":2,"three":3,"four":4,"five":5,"six":6,'1':1,"2":2,"3":3,"4":4,"5":5,"6":6}
                    for j in delivery[1].lower().split():
                        if j in RUNS:
                            dic["runs"].append(RUNS[j])
                            dic["wide"].append(0)
                            break
                    else:
                        if delivery[1].lower().strip()=="wide":
                            dic["wide"].append(1)
                            dic["runs"].append(1)
                        else:
                            dic["runs"].append(0)
                            dic["wide"].append(0)

                    for k in delivery:
                        if k.strip()[-3:]=="kph":
                            dic["ball_speed"].append(k.strip()[0:-3])
                            break
                    else:
                        dic["ball_speed"].append(None)

                    ball_length=["full","yorker","short","shorted","middle","length","fuller","mid-off"]
                    ball_swing=["outside","off","leg-side","leg","inswinging"]
                    shot=["square leg"]

                    for t in i.split():
                        if t in ball_length:
                            dic["ball_length"].append(t)
                            break
                    else:
                        dic["ball_length"].append(None)

                    for t in i.split():
                        if t in ball_swing:
                            dic["ball_swing"].append(t)
                            break
                    else:
                        dic["ball_swing"].append(None)

                    for t in i.split():
                        if t in shot:
                            dic["shot"].append(t)
                            break
                    else:
                        dic["shot"].append(None)

                    dic["commentary"].append(i)

df=pandas.DataFrame(dic)
df.to_csv('match_data\ind-vs-pak.csv')