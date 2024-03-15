import sqlite3

from ansatt_insertion import insert_ansatte
from arbeidsOppgave_insertion import insert_arbeidsoppgaver
from table_insertion import table_initialization
from teaterStykke_insertion import insert_teaterStykke
from harOppgave_insertion import insert_harOppgave
from rolle_insertion import insert_rolle
from harRolle_insertion import insert_harRolle
from akt_insertion import insert_akt

con = sqlite3.connect("./teater.db")
cursor = con.cursor()

# NECESSARY URLS FOR INFORMATIONS
urlKM = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene"
urlSAAEK = "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten"

# Runs all insertion-files in correct order.
table_initialization()
insert_teaterStykke()
insert_ansatte()
insert_arbeidsoppgaver()
insert_harOppgave()
insert_rolle()
insert_harRolle()
insert_akt()

con.commit()
con.close()
