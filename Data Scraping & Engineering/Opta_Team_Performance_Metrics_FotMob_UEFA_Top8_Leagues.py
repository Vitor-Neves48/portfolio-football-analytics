# %% Imports
# imports
import locale
import os
import sys
import time

import numpy as np
import pandas as pd
import soccerdata as sd
from scipy.stats import poisson
from tqdm import tqdm  # progress bar  # progress bar

sys.path.append(
    r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Analysis Tools" # Change as needed 
)
import function_town as ft

# %% Check available leagues
sd.FotMob.available_leagues()

# %% Now let's start scraping data from previous seasons
# %% Data Scraping: Eredivisie 2020/2021

Eredivisie_all_teams_dfs_2020_2021 = []

league = "NLD-Eredivisie"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Eredivisie_all_teams_dfs_2020_2021.append(team_df)

# Combine all individual team DataFrames into one
Eredivisie_2020_2021 = pd.concat(Eredivisie_all_teams_dfs_2020_2021, ignore_index=True)

Eredivisie_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Eredivisie 2021/2022
Eredivisie_all_teams_dfs_2021_2022 = []

league = "NLD-Eredivisie"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Eredivisie_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Eredivisie_2021_2022 = pd.concat(Eredivisie_all_teams_dfs_2021_2022, ignore_index=True)

Eredivisie_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Eredivisie 2022/2023
Eredivisie_all_teams_dfs_2022_2023 = []

league = "NLD-Eredivisie"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Eredivisie_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Eredivisie_2022_2023 = pd.concat(Eredivisie_all_teams_dfs_2022_2023, ignore_index=True)

Eredivisie_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Eredivisie 2023/2024
Eredivisie_all_teams_dfs_2023_2024 = []

league = "NLD-Eredivisie"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Eredivisie_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Eredivisie_2023_2024 = pd.concat(Eredivisie_all_teams_dfs_2023_2024, ignore_index=True)

Eredivisie_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed


# %% Data Scraping: Premier League 2020/2021
Premier_League_all_teams_dfs_2020_2021 = []

league = "ENG-Premier League"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Premier_League_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Premier_League_2020_2021 = pd.concat(
    Premier_League_all_teams_dfs_2020_2021, ignore_index=True
)

Premier_League_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Premier League 2021/2022
Premier_League_all_teams_dfs_2021_2022 = []

league = "ENG-Premier League"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Premier_League_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Premier_League_2021_2022 = pd.concat(
    Premier_League_all_teams_dfs_2021_2022, ignore_index=True
)

Premier_League_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Premier League 2022/2023
Premier_League_all_teams_dfs_2022_2023 = []

league = "ENG-Premier League"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Premier_League_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Premier_League_2022_2023 = pd.concat(
    Premier_League_all_teams_dfs_2022_2023, ignore_index=True
)

Premier_League_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Premier League 2023/2024
Premier_League_all_teams_dfs_2023_2024 = []

league = "ENG-Premier League"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Premier_League_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Premier_League_2023_2024 = pd.concat(
    Premier_League_all_teams_dfs_2023_2024, ignore_index=True
)

Premier_League_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: La Liga 2020/2021
La_Liga_all_teams_dfs_2020_2021 = []

league = "ESP-La Liga"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    La_Liga_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
La_Liga_2020_2021 = pd.concat(La_Liga_all_teams_dfs_2020_2021, ignore_index=True)

La_Liga_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: La Liga 2021/2022
La_Liga_all_teams_dfs_2021_2022 = []

league = "ESP-La Liga"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    La_Liga_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
La_Liga_2021_2022 = pd.concat(La_Liga_all_teams_dfs_2021_2022, ignore_index=True)

La_Liga_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: La Liga 2022/2023
La_Liga_all_teams_dfs_2022_2023 = []

league = "ESP-La Liga"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    La_Liga_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
La_Liga_2022_2023 = pd.concat(La_Liga_all_teams_dfs_2022_2023, ignore_index=True)

La_Liga_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: La Liga 2023/2024
La_Liga_all_teams_dfs_2023_2024 = []

league = "ESP-La Liga"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    La_Liga_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
La_Liga_2023_2024 = pd.concat(La_Liga_all_teams_dfs_2023_2024, ignore_index=True)

La_Liga_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Ligue 1 2020/2021
Ligue_1_all_teams_dfs_2020_2021 = []

league = "FRA-Ligue 1"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Ligue_1_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Ligue_1_2020_2021 = pd.concat(Ligue_1_all_teams_dfs_2020_2021, ignore_index=True)

Ligue_1_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Ligue 1 2021/2022
Ligue_1_all_teams_dfs_2021_2022 = []

league = "FRA-Ligue 1"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Ligue_1_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Ligue_1_2021_2022 = pd.concat(Ligue_1_all_teams_dfs_2021_2022, ignore_index=True)

Ligue_1_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Ligue 1 2022/2023
Ligue_1_all_teams_dfs_2022_2023 = []

league = "FRA-Ligue 1"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Ligue_1_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Ligue_1_2022_2023 = pd.concat(Ligue_1_all_teams_dfs_2022_2023, ignore_index=True)

Ligue_1_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Ligue 1 2023/2024
Ligue_1_all_teams_dfs_2023_2024 = []

league = "FRA-Ligue 1"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Ligue_1_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Ligue_1_2023_2024 = pd.concat(Ligue_1_all_teams_dfs_2023_2024, ignore_index=True)

Ligue_1_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Bundesliga 2020/2021
Bundesliga_all_teams_dfs_2020_2021 = []

league = "GER-Bundesliga"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Bundesliga_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Bundesliga_2020_2021 = pd.concat(Bundesliga_all_teams_dfs_2020_2021, ignore_index=True)

Bundesliga_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Bundesliga 2021/2022
Bundesliga_all_teams_dfs_2021_2022 = []

league = "GER-Bundesliga"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Bundesliga_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Bundesliga_2021_2022 = pd.concat(Bundesliga_all_teams_dfs_2021_2022, ignore_index=True)

Bundesliga_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Bundesliga 2022/2023
Bundesliga_all_teams_dfs_2022_2023 = []

league = "GER-Bundesliga"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Bundesliga_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Bundesliga_2022_2023 = pd.concat(Bundesliga_all_teams_dfs_2022_2023, ignore_index=True)

Bundesliga_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Bundesliga 2023/2024
Bundesliga_all_teams_dfs_2023_2024 = []

league = "GER-Bundesliga"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Bundesliga_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Bundesliga_2023_2024 = pd.concat(Bundesliga_all_teams_dfs_2023_2024, ignore_index=True)

Bundesliga_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Serie A 2020/2021
Serie_A_all_teams_dfs_2020_2021 = []

league = "ITA-Serie A"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Serie_A_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Serie_A_2020_2021 = pd.concat(Serie_A_all_teams_dfs_2020_2021, ignore_index=True)

Serie_A_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Serie A 2021/2022
Serie_A_all_teams_dfs_2021_2022 = []

league = "ITA-Serie A"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Serie_A_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Serie_A_2021_2022 = pd.concat(Serie_A_all_teams_dfs_2021_2022, ignore_index=True)

Serie_A_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Serie A 2022/2023
Serie_A_all_teams_dfs_2022_2023 = []

league = "ITA-Serie A"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Serie_A_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Serie_A_2022_2023 = pd.concat(Serie_A_all_teams_dfs_2022_2023, ignore_index=True)

Serie_A_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Serie A 2023/2024
Serie_A_all_teams_dfs_2023_2024 = []

league = "ITA-Serie A"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Serie_A_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Serie_A_2023_2024 = pd.concat(Serie_A_all_teams_dfs_2023_2024, ignore_index=True)

Serie_A_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Liga Portugal 2020/2021
Liga_Portugal_all_teams_dfs_2020_2021 = []

league = "PRT-Liga Portugal"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Liga_Portugal_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Liga_Portugal_2020_2021 = pd.concat(
    Liga_Portugal_all_teams_dfs_2020_2021, ignore_index=True
)

Liga_Portugal_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Liga Portugal 2021/2022
Liga_Portugal_all_teams_dfs_2021_2022 = []

league = "PRT-Liga Portugal"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Liga_Portugal_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Liga_Portugal_2021_2022 = pd.concat(
    Liga_Portugal_all_teams_dfs_2021_2022, ignore_index=True
)

Liga_Portugal_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Liga Portugal 2022/2023
Liga_Portugal_all_teams_dfs_2022_2023 = []

league = "PRT-Liga Portugal"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Liga_Portugal_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Liga_Portugal_2022_2023 = pd.concat(
    Liga_Portugal_all_teams_dfs_2022_2023, ignore_index=True
)

Liga_Portugal_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Liga Portugal 2023/2024
Liga_Portugal_all_teams_dfs_2023_2024 = []

league = "PRT-Liga Portugal"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Liga_Portugal_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Liga_Portugal_2023_2024 = pd.concat(
    Liga_Portugal_all_teams_dfs_2023_2024, ignore_index=True
)

Liga_Portugal_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Jupiler Pro League 2020/2021
Jupiler_Pro_League_all_teams_dfs_2020_2021 = []

league = "BEL-Jupiler Pro League"
season = "2020/2021"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Jupiler_Pro_League_all_teams_dfs_2020_2021.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Jupiler_Pro_League_2020_2021 = pd.concat(
    Jupiler_Pro_League_all_teams_dfs_2020_2021, ignore_index=True
)

Jupiler_Pro_League_2020_2021.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Jupiler Pro League 2021/2022
Jupiler_Pro_League_all_teams_dfs_2021_2022 = []

league = "BEL-Jupiler Pro League"
season = "2021/2022"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Jupiler_Pro_League_all_teams_dfs_2021_2022.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Jupiler_Pro_League_2021_2022 = pd.concat(
    Jupiler_Pro_League_all_teams_dfs_2021_2022, ignore_index=True
)

Jupiler_Pro_League_2021_2022.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Jupiler Pro League 2022/2023
Jupiler_Pro_League_all_teams_dfs_2022_2023 = []

league = "BEL-Jupiler Pro League"
season = "2022/2023"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Jupiler_Pro_League_all_teams_dfs_2022_2023.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Jupiler_Pro_League_2022_2023 = pd.concat(
    Jupiler_Pro_League_all_teams_dfs_2022_2023, ignore_index=True
)

Jupiler_Pro_League_2022_2023.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Data Scraping: Jupiler Pro League 2023/2024
Jupiler_Pro_League_all_teams_dfs_2023_2024 = []

league = "BEL-Jupiler Pro League"
season = "2023/2024"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Jupiler_Pro_League_all_teams_dfs_2023_2024.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Jupiler_Pro_League_2023_2024 = pd.concat(
    Jupiler_Pro_League_all_teams_dfs_2023_2024, ignore_index=True
)

Jupiler_Pro_League_2023_2024.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed

# %% Now let's start scraping data from the current season
# %% Data Scraping: Eredivisie 2024/2025
Eredivisie_all_teams_dfs_2024_2025 = []

league = "NLD-Eredivisie"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Eredivisie_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Eredivisie_2024_2025 = pd.concat(Eredivisie_all_teams_dfs_2024_2025, ignore_index=True)

Eredivisie_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Premier League 2024/2025
Premier_League_all_teams_dfs_2024_2025 = []

league = "ENG-Premier League"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Premier_League_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Premier_League_2024_2025 = pd.concat(
    Premier_League_all_teams_dfs_2024_2025, ignore_index=True
)

Premier_League_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: La Liga 2024/2025
La_Liga_all_teams_dfs_2024_2025 = []

league = "ESP-La Liga"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    La_Liga_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
La_Liga_2024_2025 = pd.concat(La_Liga_all_teams_dfs_2024_2025, ignore_index=True)

La_Liga_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Ligue 1 2024/2025
Ligue_1_all_teams_dfs_2024_2025 = []

league = "FRA-Ligue 1"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Ligue_1_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Ligue_1_2024_2025 = pd.concat(Ligue_1_all_teams_dfs_2024_2025, ignore_index=True)

Ligue_1_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Bundesliga 2024/2025
Bundesliga_all_teams_dfs_2024_2025 = []

league = "GER-Bundesliga"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Bundesliga_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Bundesliga_2024_2025 = pd.concat(Bundesliga_all_teams_dfs_2024_2025, ignore_index=True)

Bundesliga_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Serie A 2024/2025
Serie_A_all_teams_dfs_2024_2025 = []

league = "ITA-Serie A"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Serie_A_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Serie_A_2024_2025 = pd.concat(Serie_A_all_teams_dfs_2024_2025, ignore_index=True)

Serie_A_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Liga Portugal 2024/2025
Liga_Portugal_all_teams_dfs_2024_2025 = []

league = "PRT-Liga Portugal"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Liga_Portugal_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Liga_Portugal_2024_2025 = pd.concat(
    Liga_Portugal_all_teams_dfs_2024_2025, ignore_index=True
)

Liga_Portugal_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed



# %% Data Scraping: Jupiler Pro League 2024/2025
Jupiler_Pro_League_all_teams_dfs_2024_2025 = []

league = "BEL-Jupiler Pro League"
season = "2024/2025"
season_name = season.replace("/", "-")

locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
print(fotmob.__doc__)

league_table = fotmob.read_league_table()
teams = list(league_table["team"].unique())

for team in teams:
    print(f"Fetching stats for {team}...")  # Optional but helpful for progress tracking
    team_df = ft.mod_fotmob_get_all_team_stats_df(team, leagues=league, seasons=season)
    Jupiler_Pro_League_all_teams_dfs_2024_2025.append(team_df)
    time.sleep(10)  # Pause for 3 seconds before next iteration

# Combine all individual team DataFrames into one
Jupiler_Pro_League_2024_2025 = pd.concat(
    Jupiler_Pro_League_all_teams_dfs_2024_2025, ignore_index=True
)

Jupiler_Pro_League_2024_2025.to_parquet(
    rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_{league}_{season_name}.parquet",
    index=False,
) # Change as needed
# %% Join everything into a UEFA Top 8 Leagues dataset
# %% Join everything into a UEFA Top 8 Leagues dataset
UEFA_Top8_Last5_Seasons = [
    Eredivisie_2020_2021,
    Eredivisie_2021_2022,
    Eredivisie_2022_2023,
    Eredivisie_2023_2024,
    Eredivisie_2024_2025,
    Jupiler_Pro_League_2020_2021,
    Jupiler_Pro_League_2021_2022,
    Jupiler_Pro_League_2022_2023,
    Jupiler_Pro_League_2023_2024,
    Jupiler_Pro_League_2024_2025,
    Liga_Portugal_2020_2021,
    Liga_Portugal_2021_2022,
    Liga_Portugal_2022_2023,
    Liga_Portugal_2023_2024,
    Liga_Portugal_2024_2025,
    Serie_A_2020_2021,
    Serie_A_2021_2022,
    Serie_A_2022_2023,
    Serie_A_2023_2024,
    Serie_A_2024_2025,
    Ligue_1_2020_2021,
    Ligue_1_2021_2022,
    Ligue_1_2022_2023,
    Ligue_1_2023_2024,
    Ligue_1_2024_2025,
    Premier_League_2020_2021,
    Premier_League_2021_2022,
    Premier_League_2022_2023,
    Premier_League_2023_2024,
    Premier_League_2024_2025,
    La_Liga_2020_2021,
    La_Liga_2021_2022,
    La_Liga_2022_2023,
    La_Liga_2023_2024,
    La_Liga_2024_2025,
    Bundesliga_2020_2021,
    Bundesliga_2021_2022,
    Bundesliga_2022_2023,
    Bundesliga_2023_2024,
    Bundesliga_2024_2025,
]

UEFA_Top8_Current_Season = [
    Eredivisie_2024_2025,
    Jupiler_Pro_League_2024_2025,
    Liga_Portugal_2024_2025,
    Serie_A_2024_2025,
    Ligue_1_2024_2025,
    Premier_League_2024_2025,
    La_Liga_2024_2025,
    Bundesliga_2024_2025,
]

UEFA_Top8_Last4_Seasons_Without_Current = [
    Eredivisie_2020_2021,
    Eredivisie_2021_2022,
    Eredivisie_2022_2023,
    Eredivisie_2023_2024,
    Jupiler_Pro_League_2020_2021,
    Jupiler_Pro_League_2021_2022,
    Jupiler_Pro_League_2022_2023,
    Jupiler_Pro_League_2023_2024,
    Liga_Portugal_2020_2021,
    Liga_Portugal_2021_2022,
    Liga_Portugal_2022_2023,
    Liga_Portugal_2023_2024,
    Serie_A_2020_2021,
    Serie_A_2021_2022,
    Serie_A_2022_2023,
    Serie_A_2023_2024,
    Ligue_1_2020_2021,
    Ligue_1_2021_2022,
    Ligue_1_2022_2023,
    Ligue_1_2023_2024,
    Premier_League_2020_2021,
    Premier_League_2021_2022,
    Premier_League_2022_2023,
    Premier_League_2023_2024,
    La_Liga_2020_2021,
    La_Liga_2021_2022,
    La_Liga_2022_2023,
    La_Liga_2023_2024,
    Bundesliga_2020_2021,
    Bundesliga_2021_2022,
    Bundesliga_2022_2023,
    Bundesliga_2023_2024
]

UEFA_Top8_Last5_Seasons_df = pd.concat(UEFA_Top8_Last5_Seasons, ignore_index=True)

UEFA_Top8_Last5_Seasons_df.to_parquet(
    r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_UEFA_Top8_Last5_Seasons.parquet",
    index=False,
) # Change as needed
#---
UEFA_Top8_Current_Season_df = pd.concat(UEFA_Top8_Current_Season, ignore_index=True)

UEFA_Top8_Current_Season_df.to_parquet(
    r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_UEFA_Top8_Current_Season.parquet",
    index=False,
) # Change as needed
#---
UEFA_Top8_Last4_Seasons_Without_Current_df = pd.concat(UEFA_Top8_Last4_Seasons_Without_Current, ignore_index=True)

UEFA_Top8_Last4_Seasons_Without_Current_df.to_parquet(
    r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\raw_all_team_stats\FotMob_all_team_stats_UEFA_Top8_Last4_Seasons_Without_Current.parquet",
    index=False,
) # Change as needed
