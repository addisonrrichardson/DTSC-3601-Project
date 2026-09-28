PREMIER LEAGUE INITIAL DEMO
===========================

What the demo does
------------------
Reads the supplied 2025-26 shooting CSV, saves a smaller table, trains a
simple decision tree, checks it on held-out players, and displays one example.
The answer is OVER (1) if the player's season average is greater than 2.5
shots per 90 minutes, and UNDER (0) otherwise.

Run it on Windows
-----------------
1. Unzip this entire folder and open a terminal in this folder.
   In File Explorer, open the folder, click its address bar, type cmd,
   and press Enter.
2. Install the two packages if you do not have them:
       py -m pip install -r requirements.txt
3. Run:
       py initial_demo.py

If the 'py' command is unavailable, use 'python' in both commands.
The script recreates players_for_demo.csv in this folder on every run.
To try a different player, change PLAYER near the top of initial_demo.py.

What each file is
-----------------
initial_demo.py                 Simple Python ingestion, training, and example
shooting.csv                    Original shooting table used by the code
players_for_demo.csv           Cleaned local table, recreated when code runs
requirements.txt               Python packages to install
5. Initial Demo.docx.pdf       Original assignment instructions
Other original CSV/XLSX files Reference data for later project work

What the result means
---------------------
These rows each summarize a FULL SEASON. The model classifies a player's
season-level shots-per-90 category using age, playing time, position, and
shots on target per 90 from that same season. It does not predict actual
shots in the next match. The script compares model accuracy with a simple
always-UNDER guess because most players are below 2.5 shots per 90.

For the final project, obtain rows for individual player-matches, with
pre-match recent form, opponent, home/away, and expected playing time;
then define the answer from the following match (OVER means 3+ shots).