def verify(passwd) -> tuple:
    import re

    dg = True if re.search(r"\d+", passwd) else False
    up = True if re.search(r"[A-Z]+", passwd) else False
    lc = True if re.search(r"[a-z]+", passwd) else False
    pt = True if re.search(r"[@#$&*!;]+", passwd) else False
    d = {"digits": dg, "uppercase": up, "lowercase": lc, "symbol": pt}
    error = ", ".join([k for k, v in d.items() if v == False]).split(",")

    match len(error):
        case 1:
            msg = "".join(error)
        case 2:
            msg = " and ".join(error)
        case 3:
            msg = ", ".join(error[:2]) + f" and {error[-1]}"

    if all([dg, up, lc, pt]) and len([dg, up, lc, pt]) == 4 and len(passwd) > 8:
        return True, {"message": "your password is strong."}
    elif len(passwd) < 8:
        return False, {"message": "your password need min 8 char"}
    else:
        return False, {"message": f"your password need {msg}."}
