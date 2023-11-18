import sqlite3


def arrival(*data, sort):
    query1 = """
        SELECT id, ratio FROM Cities
        WHERE city = ?
    """
    query2 = """
        SELECT name, city_id, reason_id FROM People
        WHERE city_id = ?
    """
    query3 = """
        SELECT id, fee FROM Fees
        WHERE id = ?
    """
    with sqlite3.connect("duties.db") as con:
        cities = []
        names = []
        fees = []
        for i in data:
            cities += con.execute(query1, [(i)]).fetchall()
        for i in cities:
            names += con.execute(query2, [(i[0])]).fetchall()
        for i in names:
            fees += con.execute(query3, [(i[2])]).fetchall()
    res = []
    for name, city, reason in names:
        for i in cities:
            if i[0] == city:
                c = i[1]
        for i in fees:
            if i[0] == reason:
                r = i[1]
        res.append((name, c * r))
    if sort:
        res = sorted(
            res, key=lambda x: (x[1], x[0]), reverse=True
        )
    else:
        res = sorted(res, key=lambda x: (x[1], [-o for o in map(ord, x[0])]))
    return res


data = ["Paris", "Iconion", "Baghdad", "Nowhere", "Qom"]
print(*arrival(*data, sort=True), sep="\n")
print()
data = [
    "Tabriz",
    "Edirne",
    "Venice",
    "Baghdad",
    "Qom",
    "Isfahan",
    "Kashan",
    "Adrianople",
    "Sivas",
]
print(*arrival(*data, sort=False), sep="\n")
