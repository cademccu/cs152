def reportData(planets):
    s = dict(sorted(planets.items(), key=lambda k : k[1], reverse=True))
    ps = "{:<8} {:.2f}"
    for planet, mass in s.items():
        print(ps.format(planet, float(mass)))
