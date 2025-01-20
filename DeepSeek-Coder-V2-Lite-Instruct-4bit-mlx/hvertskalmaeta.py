def determine_contest_site(municipality):
    distances = {
        "Reykjavik": {"distance_to_reykjavik": 0, "distance_to_akureyri": 388},
        "Kopavogur": {"distance_to_reykjavik": 6, "distance_to_akureyri": 387},
        "Hafnarfjörður": {"distance_to_reykjavik": 12, "distance_to_akureyri": 391},
        "Reykjanesbær": {"distance_to_reykjavik": 48, "distance_to_akureyri": 427},
        "Akureyri": {"distance_to_reykjavik": 388, "distance_to_akureyri": 0},
        "Gardabaer": {"distance_to_reykjavik": 9, "distance_to_akureyri": 389},
        "Mosfellsbær": {"distance_to_reykjavik": 16, "distance_to_akureyri": 371},
        "Arborg": {"distance_to_reykjavik": 64, "distance_to_akureyri": 428},
        "Akranes": {"distance_to_reykjavik": 49, "distance_to_akureyri": 350},
        "Fjarðabyggð": {"distance_to_reykjavik": 659, "distance_to_akureyri": 290},
        "Múlaþing": {"distance_to_reykjavik": 603, "distance_to_akureyri": 216},
        "Seltjarnarnes": {"distance_to_reykjavik": 4, "distance_to_akureyri": 390}
    }
    
    distances_to_reykjavik = distances[municipality]["distance_to_reykjavik"]
    distances_to_akureyri = distances[municipality]["distance_to_akureyri"]
    
    if distances_to_reykjavik <= distances_to_akureyri:
        return "Reykjavik"
    else:
        return "Akureyri"

# Read input from stdin
municipality = input().strip()

# Determine and print the contest site
contest_site = determine_contest_site(municipality)
print(contest_site)