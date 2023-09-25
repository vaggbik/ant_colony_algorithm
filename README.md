# Αλγόριθμος της αποικίας των μυρμηγκιών (Ant Colony Algorithm - ACO)

Ο αλγόριθμος αυτός υλοποιήθηκε στα πλαίσια της πτυχιακής μου εργασίας "**Ο Αλγόριθμος της αποικίας μυρμηγκιών και εφαρμογές (The ant colony algorithm and applications)**".
Πρόκειται για έναν μετευρετικό αλγόριθμο βελτιστοποίησης που έχει ως στόχο την εύρεση βέλτιστης διαδρομής σε κάποιο κάποιο πρόβλημα.

Η υλοποίηση έγινε σε γλώσσα προγραμματισμού **python**.
Βιβλιοθήκες που χρησιμοποιήθηκαν για την εκτέλεση του αλγόριθμου:
- math
- numpy

Η συνάρτηση **roulette_wheel_select** που χρησιμοποιείται, είναι μία τεχνική επιλογής διαδρομής με βάση πιθανοτήτων.
Ο αλγόριθμος χωρίζεται στα εξής στάδια:
- Αρχικοποίηση των μεταβλητών,
- Τυχαία επιλογή πίνακα distance,
- Ορισμός πίνακα pheromone με μονάδες,
- Για όσες φορές ορίσαμε,
- Τοποθετούμε το κάθε μυρμήγκι σε τυχαία περιοχή,
- Κάθε μυρμήγκι βρίσκει μία διαδρομή,
- Υπολογίζεται το κόστος της διαδρομής κάθε μυρμηγκιού, και κρατάμε το ελάχιστο σε μία λίστα με την αντίστοιχη διαδρομή,
- Επιλέγουμε το ελάχιστο κόστος της λίστα με τα ελάχιστα κάθε επανάληψης,
- Η καλύτερη διαδρομή που βρέθηκε είναι αυτή.



