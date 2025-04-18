import pandas as pd
import numpy as np
import re
import warnings
import locale
import soccerdata as sd
import time
import os

optaQualifierCodes = {
    0: "shotSixYardBox",
    1: "shotPenaltyArea",
    2: "shotOboxTotal",
    3: "shotOpenPlay",
    4: "shotCounter",
    5: "shotSetPiece",
    6: "shotDirectCorner",
    7: "shotOffTarget",
    8: "shotOnPost",
    9: "shotOnTarget",
    10: "shotsTotal",
    11: "shotBlocked",
    12: "shotRightFoot",
    13: "shotLeftFoot",
    14: "shotHead",
    15: "shotObp",
    16: "goalSixYardBox",
    17: "goalPenaltyArea",
    18: "goalOBox",
    19: "goalOpenPlay",
    20: "goalCounter",
    21: "goalSetPiece",
    22: "penaltyScored",
    23: "goalOwn",
    24: "goalNormal",
    25: "goalRightFoot",
    26: "goalLeftFoot",
    27: "goalHead",
    28: "goalObp",
    29: "shortPassInaccurate",
    30: "shortPassAccurate",
    31: "passCorner",
    32: "passCornerAccurate",
    33: "passCornerInaccurate",
    34: "passFreekick",
    35: "passBack",
    36: "passForward",
    37: "passLeft",
    38: "passRight",
    39: "keyPassLong",
    40: "keyPassShort",
    41: "keyPassCross",
    42: "keyPassCorner",
    43: "keyPassThroughball",
    44: "keyPassFreekick",
    45: "keyPassThrowin",
    46: "keyPassOther",
    47: "assistCross",
    48: "assistCorner",
    49: "assistThroughball",
    50: "assistFreekick",
    51: "assistThrowin",
    52: "assistOther",
    53: "dribbleLost",
    54: "dribbleWon",
    55: "challengeLost",
    56: "interceptionWon",
    57: "clearanceHead",
    58: "outfielderBlock",
    59: "passCrossBlockedDefensive",
    60: "outfielderBlockedPass",
    61: "offsideGiven",
    62: "offsideProvoked",
    63: "foulGiven",
    64: "foulCommitted",
    65: "yellowCard",
    66: "voidYellowCard",
    67: "secondYellow",
    68: "redCard",
    69: "turnover",
    70: "dispossessed",
    71: "saveLowLeft",
    72: "saveHighLeft",
    73: "saveLowCentre",
    74: "saveHighCentre",
    75: "saveLowRight",
    76: "saveHighRight",
    77: "saveHands",
    78: "saveFeet",
    79: "saveObp",
    80: "saveSixYardBox",
    81: "savePenaltyArea",
    82: "saveObox",
    83: "keeperDivingSave",
    84: "standingSave",
    85: "closeMissHigh",
    86: "closeMissHighLeft",
    87: "closeMissHighRight",
    88: "closeMissLeft",
    89: "closeMissRight",
    90: "shotOffTargetInsideBox",
    91: "touches",
    92: "assist",
    93: "ballRecovery",
    94: "clearanceEffective",
    95: "clearanceTotal",
    96: "clearanceOffTheLine",
    97: "dribbleLastman",
    98: "errorLeadsToGoal",
    99: "errorLeadsToShot",
    100: "intentionalAssist",
    101: "interceptionAll",
    102: "interceptionIntheBox",
    103: "keeperClaimHighLost",
    104: "keeperClaimHighWon",
    105: "keeperClaimLost",
    106: "keeperClaimWon",
    107: "keeperOneToOneWon",
    108: "parriedDanger",
    109: "parriedSafe",
    110: "collected",
    111: "keeperPenaltySaved",
    112: "keeperSaveInTheBox",
    113: "keeperSaveTotal",
    114: "keeperSmother",
    115: "keeperSweeperLost",
    116: "keeperMissed",
    117: "passAccurate",
    118: "passBackZoneInaccurate",
    119: "passForwardZoneAccurate",
    120: "passInaccurate",
    121: "passAccuracy",
    122: "cornerAwarded",
    123: "passKey",
    124: "passChipped",
    125: "passCrossAccurate",
    126: "passCrossInaccurate",
    127: "passLongBallAccurate",
    128: "passLongBallInaccurate",
    129: "passThroughBallAccurate",
    130: "passThroughBallInaccurate",
    131: "passThroughBallInacurate",
    132: "passFreekickAccurate",
    133: "passFreekickInaccurate",
    134: "penaltyConceded",
    135: "penaltyMissed",
    136: "penaltyWon",
    137: "passRightFoot",
    138: "passLeftFoot",
    139: "passHead",
    140: "sixYardBlock",
    141: "tackleLastMan",
    142: "tackleLost",
    143: "tackleWon",
    144: "cleanSheetGK",
    145: "cleanSheetDL",
    146: "cleanSheetDC",
    147: "cleanSheetDR",
    148: "cleanSheetDML",
    149: "cleanSheetDMC",
    150: "cleanSheetDMR",
    151: "cleanSheetML",
    152: "cleanSheetMC",
    153: "cleanSheetMR",
    154: "cleanSheetAML",
    155: "cleanSheetAMC",
    156: "cleanSheetAMR",
    157: "cleanSheetFWL",
    158: "cleanSheetFW",
    159: "cleanSheetFWR",
    160: "cleanSheetSub",
    161: "goalConcededByTeamGK",
    162: "goalConcededByTeamDL",
    163: "goalConcededByTeamDC",
    164: "goalConcededByTeamDR",
    165: "goalConcededByTeamDML",
    166: "goalConcededByTeamDMC",
    167: "goalConcededByTeamDMR",
    168: "goalConcededByTeamML",
    169: "goalConcededByTeamMC",
    170: "goalConcededByTeamMR",
    171: "goalConcededByTeamAML",
    172: "goalConcededByTeamAMC",
    173: "goalConcededByTeamAMR",
    174: "goalConcededByTeamFWL",
    175: "goalConcededByTeamFW",
    176: "goalConcededByTeamFWR",
    177: "goalConcededByTeamSub",
    178: "goalConcededOutsideBoxGoalkeeper",
    179: "goalScoredByTeamGK",
    180: "goalScoredByTeamDL",
    181: "goalScoredByTeamDC",
    182: "goalScoredByTeamDR",
    183: "goalScoredByTeamDML",
    184: "goalScoredByTeamDMC",
    185: "goalScoredByTeamDMR",
    186: "goalScoredByTeamML",
    187: "goalScoredByTeamMC",
    188: "goalScoredByTeamMR",
    189: "goalScoredByTeamAML",
    190: "goalScoredByTeamAMC",
    191: "goalScoredByTeamAMR",
    192: "goalScoredByTeamFWL",
    193: "goalScoredByTeamFW",
    194: "goalScoredByTeamFWR",
    195: "goalScoredByTeamSub",
    196: "aerialSuccess",
    197: "duelAerialWon",
    198: "duelAerialLost",
    199: "offensiveDuel",
    200: "defensiveDuel",
    201: "bigChanceMissed",
    202: "bigChanceScored",
    203: "bigChanceCreated",
    204: "overrun",
    205: "successfulFinalThirdPasses",
    206: "punches",
    207: "penaltyShootoutScored",
    208: "penaltyShootoutMissedOffTarget",
    209: "penaltyShootoutSaved",
    210: "penaltyShootoutSavedGK",
    211: "penaltyShootoutConcededGK",
    212: "throwIn",
    213: "subOn",
    214: "subOff",
    215: "defensiveThird",
    216: "midThird",
    217: "finalThird",
    218: "pos",
}


def smart_title(col_name):
    def preserve_xg(word):
        return "xG" if word.lower() == "xg" else word.title()

    # Function to title only the parts outside of parentheses
    return re.sub(
        r"([^\(\)]+)(?=(?:\([^\)]*\))?|$)",  # match text outside parentheses
        lambda m: " ".join(preserve_xg(word) for word in m.group(1).split()),
        col_name,
    )


def fotmob_get_all_team_stats_df(team_name: str, leagues, seasons):
    """
    Retrieves and merges various match statistics for a given team from FotMob for specified leagues and seasons.

    This function pulls match data across multiple categories (e.g., Shots, Expected Goals, Passes, etc.)
    for a specified team, merges them into a single DataFrame, and processes the data to ensure that the
    resulting DataFrame contains relevant statistics such as 'match date' and 'Opponent'.

    The function also processes the 'game' column to split it into 'match date' and 'matchup', and
    extracts the opponent's team name using a custom function.

    Parameters
    ----------
    team_name : str
        The name of the team for which to retrieve statistics.
    leagues : str
        The leagues for which to fetch the data (in FotMob's league format, e.g., "PRT-Liga Portugal").
    seasons : str
        The seasons for which to fetch the data (e.g., "2024/2025").

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the merged match statistics for the specified team, with columns:
        ['league', 'season', 'team', 'match date', 'Opponent', 'matchup', and various match statistics].

    Notes
    -----
    - The 'game' column is split into two parts: 'match date' (date of the match) and 'matchup' (team vs. opponent).
    - The 'Opponent' column is derived from the 'matchup' column, identifying the opposing team for each match.
    - This function assumes the columns in the match stats DataFrames from FotMob share consistent naming conventions.
    """

    # Set locale for consistent date formatting
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
    fotmob = sd.FotMob(leagues, seasons, no_cache=False, no_store=False)
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

    # Read each stats category for the specified team
    top_stats = fotmob.read_team_match_stats("Top stats", True, team_name).reset_index()
    time.sleep(5)
    shots = fotmob.read_team_match_stats("Shots", True, team_name).reset_index()
    time.sleep(5)
    xg = fotmob.read_team_match_stats(
        "Expected goals (xG)", True, team_name
    ).reset_index()
    time.sleep(5)
    passes = fotmob.read_team_match_stats("Passes", True, team_name).reset_index()
    time.sleep(5)
    defence = fotmob.read_team_match_stats("Defence", True, team_name).reset_index()
    time.sleep(5)
    duels = fotmob.read_team_match_stats("Duels", True, team_name).reset_index()
    time.sleep(5)
    discipline = fotmob.read_team_match_stats(
        "Discipline", True, team_name
    ).reset_index()
    time.sleep(5)

    # Merge all into a single DataFrame
    df_merged = (
        shots.merge(xg, on=["league", "season", "team", "game"], how="outer")
        .merge(passes, on=["league", "season", "team", "game"], how="outer")
        .merge(defence, on=["league", "season", "team", "game"], how="outer")
        .merge(duels, on=["league", "season", "team", "game"], how="outer")
        .merge(discipline, on=["league", "season", "team", "game"], how="outer")
    )

    # Define the columns to keep from Top_stats (including the merge keys)
    merge_keys = ["league", "season", "team", "game"]
    top_stats_cols = merge_keys + [
        "Big chances missed",
        "Corners",
        "Ball possession",
        "Fouls committed",
        "Big chances",
    ]

    # Filter Top_stats to only the necessary columns
    top_stats_filtered = top_stats[
        top_stats_cols
    ]  # this is the merge_keys cols + the columns that are not yet in FC Porto

    # Merge with FCPorto
    df_merged = df_merged.merge(top_stats_filtered, on=merge_keys, how="left")

    df_merged[["match date", "matchup"]] = df_merged["game"].str.split(
        " ", n=1, expand=True
    )

    df_merged["Opponent"] = df_merged.apply(extract_opponent_from_matchup, axis=1)

    df_merged.drop(columns=["game"], inplace=True)
    cols = df_merged.columns.tolist()
    # Remove 'match date' and 'Opponent' from current position
    cols.remove("match date")
    cols.remove("Opponent")
    cols.remove("matchup")
    # Find the index of 'season' and 'team'
    season_idx = cols.index("season")
    team_idx = cols.index("team")
    # Insert 'match date' after 'season' and 'Opponent' after 'team'
    cols.insert(season_idx + 1, "match date")
    cols.insert(
        team_idx + 2, "Opponent"
    )  # +2 because we just inserted one column before
    match_date_idx = cols.index("match date")
    cols.insert(match_date_idx + 1, "matchup")
    # Reorder the DataFrame
    df_merged = df_merged[cols]

    return df_merged


def mod_fotmob_get_all_team_stats_df(team_name: str, leagues, seasons):
    """
    Retrieves and merges various match statistics for a given team from FotMob for specified leagues and seasons.

    This function pulls match data across multiple categories (e.g., Shots, Expected Goals, Passes, etc.)
    for a specified team, merges them into a single DataFrame, and processes the data to ensure that the
    resulting DataFrame contains relevant statistics such as 'match date' and 'Opponent'.

    The function also processes the 'game' column to split it into 'match date' and 'matchup', and
    extracts the opponent's team name using a custom function.

    Parameters
    ----------
    team_name : str
        The name of the team for which to retrieve statistics.
    leagues : str
        The leagues for which to fetch the data (in FotMob's league format, e.g., "PRT-Liga Portugal").
    seasons : str
        The seasons for which to fetch the data (e.g., "2024/2025").

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the merged match statistics for the specified team, with columns:
        ['league', 'season', 'team', 'match date', 'Opponent', 'matchup', and various match statistics].

    Notes
    -----
    - The 'game' column is split into two parts: 'match date' (date of the match) and 'matchup' (team vs. opponent).
    - The 'Opponent' column is derived from the 'matchup' column, identifying the opposing team for each match.
    - This function assumes the columns in the match stats DataFrames from FotMob share consistent naming conventions.
    """

    # Set locale for consistent date formatting
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
    fotmob = sd.FotMob(leagues, seasons, no_cache=False, no_store=False)
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

    # Read each stats category for the specified team
    top_stats = fotmob.mod_read_team_match_stats(
        "Top stats", True, team_name
    ).reset_index()
    time.sleep(5)
    shots = fotmob.mod_read_team_match_stats("Shots", True, team_name).reset_index()
    time.sleep(5)
    xg = fotmob.mod_read_team_match_stats(
        "Expected goals (xG)", True, team_name
    ).reset_index()
    time.sleep(5)
    passes = fotmob.mod_read_team_match_stats("Passes", True, team_name).reset_index()
    time.sleep(5)
    defence = fotmob.mod_read_team_match_stats("Defence", True, team_name).reset_index()
    time.sleep(5)
    duels = fotmob.mod_read_team_match_stats("Duels", True, team_name).reset_index()
    time.sleep(5)
    discipline = fotmob.mod_read_team_match_stats(
        "Discipline", True, team_name
    ).reset_index()
    time.sleep(5)

    # Merge all into a single DataFrame
    df_merged = (
        shots.merge(xg, on=["league", "season", "team", "game"], how="outer")
        .merge(passes, on=["league", "season", "team", "game"], how="outer")
        .merge(defence, on=["league", "season", "team", "game"], how="outer")
        .merge(duels, on=["league", "season", "team", "game"], how="outer")
        .merge(discipline, on=["league", "season", "team", "game"], how="outer")
    )

    # Define the columns to keep from Top_stats (including the merge keys)
    merge_keys = ["league", "season", "team", "game"]
    top_stats_cols = merge_keys + [
        "Big chances missed",
        "Corners",
        "Ball possession",
        "Fouls committed",
        "Big chances",
    ]

    # Filter Top_stats to only the necessary columns
    top_stats_filtered = top_stats[
        top_stats_cols
    ]  # this is the merge_keys cols + the columns that are not yet in FC Porto

    # Merge with FCPorto
    df_merged = df_merged.merge(top_stats_filtered, on=merge_keys, how="left")

    df_merged[["match date", "matchup"]] = df_merged["game"].str.split(
        " ", n=1, expand=True
    )

    df_merged["Opponent"] = df_merged.apply(extract_opponent_from_matchup, axis=1)

    df_merged.drop(columns=["game"], inplace=True)
    cols = df_merged.columns.tolist()
    # Remove 'match date' and 'Opponent' from current position
    cols.remove("match date")
    cols.remove("Opponent")
    cols.remove("matchup")
    # Find the index of 'season' and 'team'
    season_idx = cols.index("season")
    team_idx = cols.index("team")
    # Insert 'match date' after 'season' and 'Opponent' after 'team'
    cols.insert(season_idx + 1, "match date")
    cols.insert(
        team_idx + 2, "Opponent"
    )  # +2 because we just inserted one column before
    match_date_idx = cols.index("match date")
    cols.insert(match_date_idx + 1, "matchup")
    # Reorder the DataFrame
    df_merged = df_merged[cols]

    return df_merged


def extract_opponent_from_matchup(row):
    # Split the matchup string on the '-' character.
    parts = row["matchup"].split("-", 1)

    # There should be 2 parts in a valid matchup.
    if len(parts) != 2:
        return None  # or you can return the original string, or some error value

    # Strip any extra whitespace
    part1 = parts[0].strip()
    part2 = parts[1].strip()

    # Check which part equals the 'team' and return the other as the opponent.
    if part1 == row["team"]:
        return part2
    elif part2 == row["team"]:
        return part1
    else:
        # If neither part exactly matches the team name,
        # you may want to handle this case separately.
        return None


def standardize_team_names(df, column, new_column=None):
    """
    Standardizes club names in a DataFrame column based on a fixed internal mapping.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the column to standardize.
    column : str
        Name of the column with team names to standardize.
    new_column : str, optional
        If provided, the standardized names will be stored in a new column.
        If None, the original column will be overwritten.

    Returns
    -------
    pd.DataFrame
        A copy of the DataFrame with standardized names.
    """

    name_mapping = {
        "Sporting CP": ["Sporting CP", "Sporting Clube de Portugal", "Sporting"],
        "AVS Futebol SAD": ["AVS Futebol SAD", "AVS"],
        "Casa Pia AC": ["Casa Pia AC", "Casa Pia Atlético Clube", "Casa Pia"],
        "FC Porto": ["FC Porto", "F.C. Porto", "Porto"],
        "Braga": ["Braga", "SC Braga"],
        "Estoril": ["Estoril", "GD Estoril", "Estoril Praia"],
        "Famalicao": ["Famalicão", "Famalicao", "F.C. Famalicão", "Famal"],
        "Farense": ["Farense", "S.C. Farense"],
        "Arouca": ["Arouca", "F.C. Arouca"],
        "Manchester United": ["Manchester United", "Man United", "Man Utd", "United"],
        "Arsenal": ["Arsenal", "Arsenal FC"],
        "Everton": ["Everton", "Everton FC"],
        "Ipswich Town": ["Ipswich Town", "Ipswich Town FC", "Ipswich"],
        "Newcastle United": ["Newcastle United", "Newcastle United FC", "Newcastle"],
        "Nottingham Forest": ["Nottingham Forest", "Nottm Forest", "Forest"],
        "West Ham United": ["West Ham United", "West Ham United FC", "West Ham"],
        "Brentford": ["Brentford", "Brentford FC"],
        "Chelsea": ["Chelsea", "Chelsea FC"],
        "Leicester City": ["Leicester City", "Leicester City FC", "Leicester"],
        "Athletic Club": ["Athletic Club", "Athletic Bilbao", "Athletic"],
        "Real Betis": ["Real Betis", "Real Betis Balompié", "Betis"],
        "Celta Vigo": ["Celta Vigo", "RC Celta de Vigo", "Celta"],
        "Las Palmas": ["Las Palmas", "UD Las Palmas", "Las Palmas UD"],
        "Osasuna": ["Osasuna", "CA Osasuna"],
        "Valencia": ["Valencia", "Valencia CF", "Valencia Club de Fútbol"],
        "Mallorca": ["Mallorca", "RCD Mallorca"],
        "Real Sociedad": ["Real Sociedad", "La Real"],
        "Real Valladolid": ["Real Valladolid", "Valladolid"],
        "Villarreal": ["Villarreal", "Villarreal CF"],
        "Le Havre": ["Le Havre", "Le Havre AC"],
        "Brest": ["Brest", "Stade Brestois", "Brestois"],
        "Monaco": ["Monaco", "AS Monaco"],
        "Reims": ["Reims", "Stade de Reims", "Reims FC"],
        "Angers": ["Angers", "Angers SCO"],
        "Auxerre": ["Auxerre", "AJ Auxerre"],
        "Montpellier": ["Montpellier", "Montpellier HSC"],
        "Rennes": ["Rennes", "Stade Rennais", "Stade Rennais FC"],
        "Toulouse": ["Toulouse", "Toulouse FC"],
        "Borussia Mönchengladbach": [
            "Borussia Mönchengladbach",
            "Borussia Monchengladbach",
            "Gladbach",
        ],
        "Augsburg": ["Augsburg", "FC Augsburg"],
        "Borussia Dortmund": ["Borussia Dortmund", "Dortmund", "BVB"],
        "Freiburg": ["Freiburg", "SC Freiburg"],
        "Hoffenheim": ["Hoffenheim", "TSG 1899 Hoffenheim"],
        "Mainz 05": ["Mainz 05", "1. FSV Mainz 05", "Mainz"],
        "RB Leipzig": ["RB Leipzig", "Leipzig"],
        "St. Pauli": ["St. Pauli", "FC St. Pauli", "St Pauli"],
        "Wolfsburg": ["Wolfsburg", "VfL Wolfsburg"],
        "Empoli": ["Empoli", "Empoli FC"],
        "Genoa": ["Genoa", "Genoa CFC", "Genoa Cricket and Football Club"],
        "Milan": ["Milan", "AC Milan"],
        "Parma": ["Parma", "Parma FC"],
        "Bologna": ["Bologna", "Bologna FC 1909"],
        "Cagliari": ["Cagliari", "Cagliari Calcio"],
        "Hellas Verona": ["Hellas Verona", "Verona", "Hellas"],
        "Lazio": ["Lazio", "SS Lazio"],
        "Juventus": ["Juventus", "Juve"],
        "Lecce": ["Lecce", "U.S. Lecce"],
        "FC Groningen": ["FC Groningen", "Groningen"],
        "Almere City FC": ["Almere City FC", "Almere City"],
        "Feyenoord": ["Feyenoord", "Feyenoord Rotterdam"],
        "NEC Nijmegen": ["NEC Nijmegen", "NEC"],
        "PSV Eindhoven": ["PSV Eindhoven", "PSV"],
        "Ajax": ["Ajax", "AFC Ajax"],
        "FC Utrecht": ["FC Utrecht", "Utrecht"],
        "Go Ahead Eagles": ["Go Ahead Eagles", "GA Eagles"],
        "Sparta Rotterdam": ["Sparta Rotterdam", "Sparta"],
        "Rio Ave": ["Rio Ave", "Rio Ave FC"],
        "Nacional": ["Nacional", "CD Nacional"],
        "Boavista": ["Boavista", "Boavista FC"],
        "Gil Vicente": ["Gil Vicente", "Gil Vicente FC"],
        "Estrela da Amadora": [
            "Estrela da Amadora",
            "C.F. Estrela da Amadora",
            "Estrela",
        ],
        "Santa Clara": ["Santa Clara", "C.D. Santa Clara"],
        "Benfica": ["Benfica", "SL Benfica"],
        "Moreirense": ["Moreirense", "Moreirense FC"],
        "Vitoria de Guimaraes": ["Vitória de Guimarães", "Vitoria de Guimaraes"],
        "Fulham": ["Fulham", "Fulham FC"],
        "Wolverhampton Wanderers": [
            "Wolverhampton Wanderers",
            "Wolves",
            "Wolverhampton",
        ],
        "Brighton & Hove Albion": [
            "Brighton & Hove Albion",
            "Brighton & Hove Albion FC",
            "Brighton",
        ],
        "Liverpool": ["Liverpool", "Liverpool FC"],
        "Southampton": ["Southampton", "Southampton FC"],
        "AFC Bournemouth": ["AFC Bournemouth", "Bournemouth"],
        "Aston Villa": ["Aston Villa", "Aston Villa FC"],
        "Crystal Palace": ["Crystal Palace", "Crystal Palace FC"],
        "Manchester City": ["Manchester City", "Man City", "Manchester City FC"],
        "Tottenham Hotspur": [
            "Tottenham Hotspur",
            "Tottenham Hotspur FC",
            "Tottenham",
            "Spurs",
        ],
        "Getafe": ["Getafe", "Getafe CF"],
        "Girona": ["Girona", "Girona FC"],
        "Deportivo Alaves": ["Deportivo Alavés", "Deportivo Alaves"],
        "Sevilla": ["Sevilla", "Sevilla FC"],
        "Leganes": ["Leganés", "Leganes"],
        "Barcelona": ["Barcelona", "FC Barcelona"],
        "Real Madrid": ["Real Madrid", "Real Madrid CF"],
        "Rayo Vallecano": ["Rayo Vallecano", "Rayo"],
        "Espanyol": ["Espanyol", "RCD Espanyol"],
        "Atletico Madrid": ["Atlético Madrid", "Atletico Madrid", "Atleti"],
        "Paris Saint-Germain": ["Paris Saint-Germain", "PSG"],
        "Marseille": ["Marseille", "Olympique de Marseille"],
        "Saint-Etienne": ["Saint-Étienne", "Saint-Etienne", "AS Saint-Étienne"],
        "Lille": ["Lille", "Lille OSC"],
        "Lens": ["Lens", "RC Lens"],
        "Nice": ["Nice", "OGC Nice"],
        "Strasbourg": ["Strasbourg", "RC Strasbourg", "Strasbourg FC"],
        "Lyon": ["Lyon", "Olympique Lyonnais"],
        "Nantes": ["Nantes", "FC Nantes"],
        "Bayer Leverkusen": ["Bayer Leverkusen", "Bayer 04 Leverkusen"],
        "Werder Bremen": ["Werder Bremen", "SV Werder Bremen"],
        "Eintracht Frankfurt": ["Eintracht Frankfurt", "Frankfurt"],
        "VfB Stuttgart": ["VfB Stuttgart", "Stuttgart"],
        "Holstein Kiel": ["Holstein Kiel", "Kiel"],
        "Union Berlin": ["Union Berlin", "UB"],
        "Bochum": ["Bochum", "VfL Bochum"],
        "FC Heidenheim": ["FC Heidenheim", "Heidenheim"],
        "Bayern München": [
            "Bayern München",
            "Bayern Munchen",
            "FC Bayern München",
            "Bayern",
        ],
        "Monza": ["Monza", "AC Monza"],
        "Inter": ["Inter", "Inter Milan", "Internazionale"],
        "Torino": ["Torino", "Torino FC"],
        "Fiorentina": ["Fiorentina", "ACF Fiorentina", "La Viola"],
        "Udinese": ["Udinese", "Udinese Calcio"],
        "Roma": ["Roma", "AS Roma"],
        "Napoli": ["Napoli", "SSC Napoli"],
        "Venezia": ["Venezia", "Venezia FC"],
        "Como": ["Como", "Como 1907", "Calcio Como"],
        "Atalanta": ["Atalanta", "Atalanta BC"],
        "NAC Breda": ["NAC Breda", "NAC"],
        "AZ Alkmaar": ["AZ Alkmaar", "AZ"],
        "Willem II": ["Willem II", "Willem 2"],
        "FC Twente": ["FC Twente", "Twente"],
        "RKC Waalwijk": ["RKC Waalwijk", "RKC"],
        "SC Heerenveen": ["SC Heerenveen", "Heerenveen"],
        "PEC Zwolle": ["PEC Zwolle", "Zwolle"],
        "Fortuna Sittard": ["Fortuna Sittard", "Fortuna"],
        "Heracles": ["Heracles", "Heracles Almelo"],
    }

    # Invert the mapping: each variant → standard name
    variant_to_standard = {
        variant: standard
        for standard, variants in name_mapping.items()
        for variant in variants
    }

    # Choose target column
    target_column = new_column if new_column else column

    # Apply mapping
    df_copy = df.copy()
    df_copy[target_column] = (
        df_copy[column].map(variant_to_standard).fillna(df_copy[column])
    )

    return df_copy


def to_lower_camel_case(text):
    """
    Convert a given string to lowerCamelCase.
    """
    words = text.split()  # Split the string into words based on spaces
    # Convert the first word to lowercase and the rest to title case
    return words[0].lower() + "".join(word.title() for word in words[1:])


def to_pascal_case(s):
    """
    Convert a string (e.g. "Standing Save") into PascalCase (e.g. "StandingSave").
    This removes spaces and capitalizes every word.
    """
    if not isinstance(s, str):
        return s
    return "".join(word.capitalize() for word in s.split())


def transform_qualifiers(quals_list):
    """
    Transform a list (or array) of qualifier dictionaries from the original format:
      { "type": {"displayName": "Length", "value": 212}, "value": "11.5" }
    into a simplified list with keys in PascalCase.

    For example, a row like:
      [{"type": {"displayName": "Standing Save", "value": 999}, "value": ""},
       {"type": {"displayName": "Pass End X", "value": 140}, "value": "30.6"}]
    becomes:
      [{'StandingSave': True}, {'PassEndX': '30.6'}]
    """
    if quals_list is None:
        return []

    if isinstance(quals_list, np.ndarray):
        quals_list = quals_list.tolist()

    if not isinstance(quals_list, list) or len(quals_list) == 0:
        return []

    new_list = []
    for q in quals_list:
        if isinstance(q, dict) and "type" in q:
            # Use to_pascal_case for qualifiers
            display_name = q.get("type", {}).get("displayName", "unknown")
            key = to_pascal_case(display_name)
            val = q.get("value")
            # If val is falsey (e.g., empty string), assume it's a flag and set to True.
            if not val:
                val = True
            new_list.append({key: val})
    return new_list


def transform_event_types(codes_list):
    """
    Given a list (or array) of event type codes, return a list of the corresponding names
    from the dictionary `optaQualifierCodes`.

    If a code isn't found in optaQualifierCodes, returns the code as a string.
    """
    if codes_list is None:
        return []

    if isinstance(codes_list, np.ndarray):
        codes_list = codes_list.tolist()

    if not isinstance(codes_list, list) or len(codes_list) == 0:
        return []

    new_list = []
    for code in codes_list:
        mapping = optaQualifierCodes.get(code, None)
        if mapping is not None:
            new_list.append(mapping)
        else:
            new_list.append(str(code))
    return new_list


def map_qualifier_codes(df, column_name):
    """
    Replace lists of integer codes in a DataFrame column with corresponding string labels
    using the global optaQualifierCodes dictionary. Warns if row is not a list.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column_name (str): Column with lists of integers.

    Returns:
    - pd.DataFrame: Modified copy of the DataFrame.
    """
    df_copy = df.copy()

    def safe_map(row, index):
        if isinstance(row, list):
            return [optaQualifierCodes.get(code, f"unknown_{code}") for code in row]
        else:
            warnings.warn(
                f"Row {index} in column '{column_name}' is not a list (type: {type(row).__name__}). Skipping."
            )
            return row

    df_copy[column_name] = [
        safe_map(row, idx) for idx, row in enumerate(df_copy[column_name])
    ]

    return df_copy


def clean_FotMob_df_1_factor(df):
    df = df.reset_index()
    df[["match date", "matchup"]] = df["game"].str.split(" ", n=1, expand=True)
    df[["home team", "away team"]] = df["matchup"].str.split("-", n=1, expand=True)
    df["team role"] = df.apply(
        lambda row: "home" if row["team"] == row["home team"] else "away", axis=1
    )

    away_df = df[df["team role"] == "away"]
    home_df = df[df["team role"] == "home"]

    away_df = away_df[
        ["league", "season", "match date", "away team"]
        + [
            col
            for col in df.columns
            if col not in ["league", "season", "match date", "away team"]
        ]
    ]
    # Drop unnecessary columns
    away_df.drop(columns=["game", "team", "home team", "team role"], inplace=True)

    # Re-order columns in home df
    home_df = home_df[
        ["league", "season", "match date", "home team"]
        + [
            col
            for col in df.columns
            if col not in ["league", "season", "match date", "home team"]
        ]
    ]
    home_df.drop(columns=["game", "team", "away team", "team role"], inplace=True)

    away_df.columns = away_df.columns.str.title()
    home_df.columns = home_df.columns.str.title()

    columns_to_rename = [
        "Accurate Passes",
        "Ball Possession",
        "Big Chances",
        "Big Chances Missed",
        "Corners",
        "Expected Goals (Xg)",
        "Fouls Committed",
        "Shots On Target",
        "Total Shots",
        "Accurate Passes (%)",
    ]

    rename_dict_away = {col: f"{col} Away Team" for col in columns_to_rename}
    away_df = away_df.rename(columns=rename_dict_away)

    rename_dict_home = {col: f"{col} Home Team" for col in columns_to_rename}
    home_df = home_df.rename(columns=rename_dict_home)

    # Define key columns for merging (all shared identifiers)
    key_columns = ["League", "Season", "Match Date", "Matchup"]

    # Perform the merge without suffixes
    final_df = pd.merge(
        left=home_df,
        right=away_df,
        on=key_columns,
        how="outer",  # Use 'outer' to keep all records from both sides
    )

    season_str = final_df["Season"].astype(str)
    final_df["Season"] = season_str.str[:2] + "/" + season_str.str[2:]
    final_df = final_df.astype(
        {
            "League": "string",
            "Season": "string",
            "Match Date": "datetime64[ns]",
            "Home Team": "string",
            "Accurate Passes Home Team": "float",
            "Ball Possession Home Team": "float",
            "Big Chances Home Team": "float",
            "Big Chances Missed Home Team": "float",
            "Corners Home Team": "float",
            "Expected Goals (Xg) Home Team": "float",
            "Fouls Committed Home Team": "float",
            "Shots On Target Home Team": "float",
            "Total Shots Home Team": "float",
            "Accurate Passes (%) Home Team": "float",
            "Matchup": "string",
            "Away Team": "string",
            "Accurate Passes Away Team": "float",
            "Ball Possession Away Team": "float",
            "Big Chances Away Team": "float",
            "Big Chances Missed Away Team": "float",
            "Corners Away Team": "float",
            "Expected Goals (Xg) Away Team": "float",
            "Fouls Committed Away Team": "float",
            "Shots On Target Away Team": "float",
            "Total Shots Away Team": "float",
            "Accurate Passes (%) Away Team": "float",
        }
    )

    return final_df


def clean_FotMob_df_2_factor(df, df2):
    df = df.reset_index()
    df[["match date", "matchup"]] = df["game"].str.split(" ", n=1, expand=True)
    df[["home team", "away team"]] = df["matchup"].str.split("-", n=1, expand=True)
    df["team role"] = df.apply(
        lambda row: "home" if row["team"] == row["home team"] else "away", axis=1
    )

    away_df = df[df["team role"] == "away"]
    home_df = df[df["team role"] == "home"]

    away_df = away_df[
        ["league", "season", "match date", "away team"]
        + [
            col
            for col in df.columns
            if col not in ["league", "season", "match date", "away team"]
        ]
    ]
    # Drop unnecessary columns
    away_df.drop(columns=["game", "team", "home team", "team role"], inplace=True)

    # Re-order columns in home df
    home_df = home_df[
        ["league", "season", "match date", "home team"]
        + [
            col
            for col in df.columns
            if col not in ["league", "season", "match date", "home team"]
        ]
    ]
    home_df.drop(columns=["game", "team", "away team", "team role"], inplace=True)

    away_df.columns = away_df.columns.str.title()
    home_df.columns = home_df.columns.str.title()

    columns_to_rename = [
        "Accurate Passes",
        "Ball Possession",
        "Big Chances",
        "Big Chances Missed",
        "Corners",
        "Expected Goals (Xg)",
        "Fouls Committed",
        "Shots On Target",
        "Total Shots",
        "Accurate Passes (%)",
    ]

    rename_dict_away = {col: f"{col} Away Team" for col in columns_to_rename}
    away_df = away_df.rename(columns=rename_dict_away)

    rename_dict_home = {col: f"{col} Home Team" for col in columns_to_rename}
    home_df = home_df.rename(columns=rename_dict_home)

    # Define key columns for merging (all shared identifiers)
    key_columns = ["League", "Season", "Match Date", "Matchup"]

    # Perform the merge without suffixes
    final_df = pd.merge(
        left=home_df,
        right=away_df,
        on=key_columns,
        how="outer",  # Use 'outer' to keep all records from both sides
    )

    season_str = final_df["Season"].astype(str)
    final_df["Season"] = season_str.str[:2] + "/" + season_str.str[2:]
    final_df = final_df.astype(
        {
            "League": "string",
            "Season": "string",
            "Match Date": "datetime64[ns]",
            "Home Team": "string",
            "Accurate Passes Home Team": "float",
            "Ball Possession Home Team": "float",
            "Big Chances Home Team": "float",
            "Big Chances Missed Home Team": "float",
            "Corners Home Team": "float",
            "Expected Goals (Xg) Home Team": "float",
            "Fouls Committed Home Team": "float",
            "Shots On Target Home Team": "float",
            "Total Shots Home Team": "float",
            "Accurate Passes (%) Home Team": "float",
            "Matchup": "string",
            "Away Team": "string",
            "Accurate Passes Away Team": "float",
            "Ball Possession Away Team": "float",
            "Big Chances Away Team": "float",
            "Big Chances Missed Away Team": "float",
            "Corners Away Team": "float",
            "Expected Goals (Xg) Away Team": "float",
            "Fouls Committed Away Team": "float",
            "Shots On Target Away Team": "float",
            "Total Shots Away Team": "float",
            "Accurate Passes (%) Away Team": "float",
        }
    )

    df2 = df2.reset_index()
    df2["Matchup"] = df2["home_team"] + "-" + df2["away_team"]
    # Remove rows where home_score OR away_score is NaN
    df2 = df2.dropna(subset=["home_score", "away_score"], how="any")

    final_df = pd.merge(
        final_df,
        df2[["Matchup", "round", "home_score", "away_score", "game_id", "url"]],
        on="Matchup",
        how="outer",  # let's set this as outer and see if the number of rows changes. In theory, both dfs have the same number of rows which should concern the same matches, so the number should stay the same
    )

    new_column_order = [
        "League",
        "Season",
        "Match Date",
        "round",
        "Matchup",
        "game_id",
        "url",
        "Home Team",
        "home_score",
        "away_score",
        "Away Team",
        "Accurate Passes Home Team",
        "Ball Possession Home Team",
        "Big Chances Home Team",
        "Big Chances Missed Home Team",
        "Corners Home Team",
        "Expected Goals (Xg) Home Team",
        "Fouls Committed Home Team",
        "Shots On Target Home Team",
        "Total Shots Home Team",
        "Accurate Passes (%) Home Team",
        "Accurate Passes Away Team",
        "Ball Possession Away Team",
        "Big Chances Away Team",
        "Big Chances Missed Away Team",
        "Corners Away Team",
        "Expected Goals (Xg) Away Team",
        "Fouls Committed Away Team",
        "Shots On Target Away Team",
        "Total Shots Away Team",
        "Accurate Passes (%) Away Team",
    ]

    final_df = final_df[new_column_order]

    columns_to_rename2 = {
        "round": "Matchday",
        "game_id": "Match ID",
        "url": "Match URL",
        "home_score": "Home Team Score",
        "away_score": "Away Team Score",
    }
    final_df = final_df.rename(columns=columns_to_rename2)
    final_df["Matchday"] = final_df["Matchday"].astype(int)
    final_df["Match ID"] = final_df["Match ID"].astype(int)
    final_df["Match URL"] = final_df["Match URL"].astype(str)
    final_df["Home Team Score"] = final_df["Home Team Score"].astype(int)
    final_df["Away Team Score"] = final_df["Away Team Score"].astype(int)

    return final_df


def prep_rolling_plot_df(df, team):
    Team = df[(df["Home Team"] == team) | (df["Away Team"] == team)]
    Team = Team.sort_values(by="Match Date", ascending=True)

    # Prep home_df
    home_df = Team.copy()
    home_df = home_df.melt(
        id_vars=[
            "League",
            "Season",
            "Match Date",
            "Matchday",
            "Matchup",
            "Match ID",
            "Match URL",
            "Home Team",
            "Home Team Score",
            "Away Team Score",
            "Away Team",
        ]
    )
    home_df["venue"] = "H"
    home_df.rename(columns={"Home Team": "Team", "Away Team": "Opponent"}, inplace=True)
    home_df.replace(
        {
            "variable": {
                "Accurate Passes Home Team": "Accurate Passes for",
                "Ball Possession Home Team": "Ball Possession for",
                "Big Chances Home Team": "Big Chances for",
                "Big Chances Missed Home Team": "Big Chances Missed for",
                "Corners Home Team": "Corners for",
                "Expected Goals (Xg) Home Team": "xG for",
                "Fouls Committed Home Team": "Fouls Committed for",
                "Shots On Target Home Team": "Shots On Target for",
                "Total Shots Home Team": "Total Shots for",
                "Accurate Passes (%) Home Team": "Accurate Passes (%) for",
                "Accurate Passes Away Team": "Accurate Passes ag",
                "Ball Possession Away Team": "Ball Possession ag",
                "Big Chances Away Team": "Big Chances ag",
                "Big Chances Missed Away Team": "Big Chances Missed ag",
                "Corners Away Team": "Corners ag",
                "Expected Goals (Xg) Away Team": "xG ag",
                "Fouls Committed Away Team": "Fouls Committed ag",
                "Shots On Target Away Team": "Shots On Target ag",
                "Total Shots Away Team": "Total Shots ag",
                "Accurate Passes (%) Away Team": "Accurate Passes (%) ag",
            }
        },
        inplace=True,
    )

    # Prep away_df
    away_df = Team.copy()
    away_df = away_df.melt(
        id_vars=[
            "League",
            "Season",
            "Match Date",
            "Matchday",
            "Matchup",
            "Match ID",
            "Match URL",
            "Home Team",
            "Home Team Score",
            "Away Team Score",
            "Away Team",
        ]
    )
    away_df["venue"] = "A"
    away_df.rename(columns={"Away Team": "Team", "Home Team": "Opponent"}, inplace=True)
    away_df.replace(
        {
            "variable": {
                "Accurate Passes Away Team": "Accurate Passes for",
                "Ball Possession Away Team": "Ball Possession for",
                "Big Chances Away Team": "Big Chances for",
                "Big Chances Missed Away Team": "Big Chances Missed for",
                "Corners Away Team": "Corners for",
                "Expected Goals (Xg) Away Team": "xG for",
                "Fouls Committed Away Team": "Fouls Committed for",
                "Shots On Target Away Team": "Shots On Target for",
                "Total Shots Away Team": "Total Shots for",
                "Accurate Passes (%) Away Team": "Accurate Passes (%) for",
                "Accurate Passes Home Team": "Accurate Passes ag",
                "Ball Possession Home Team": "Ball Possession ag",
                "Big Chances Home Team": "Big Chances ag",
                "Big Chances Missed Home Team": "Big Chances Missed ag",
                "Corners Home Team": "Corners ag",
                "Expected Goals (Xg) Home Team": "xG ag",
                "Fouls Committed Home Team": "Fouls Committed ag",
                "Shots On Target Home Team": "Shots On Target ag",
                "Total Shots Home Team": "Total Shots ag",
                "Accurate Passes (%) Home Team": "Accurate Passes (%) ag",
            }
        },
        inplace=True,
    )

    columns_to_rename_3 = {"variable": "Variable", "value": "Value", "venue": "Venue"}

    # Prep final_df
    final_df = pd.concat([home_df, away_df]).reset_index(drop=True)
    final_df = final_df.rename(columns=columns_to_rename_3)
    final_df = final_df[final_df["Team"] == team].reset_index(drop=True)
    final_df = final_df.sort_values(by="Match Date")

    return final_df


def clean_FotMob_all_team_stats_df(df, league, season):
    # Clean input df
    df[["Home Team", "Away Team"]] = df["matchup"].str.split("-", expand=True)
    df["Home Team"] = df["Home Team"].str.strip()
    df["Away Team"] = df["Away Team"].str.strip()

    Home_df = df[df["team"] == df["Home Team"]]
    Away_df = df[df["team"] == df["Away Team"]]
    home_rename = {
        "Blocked shots": "Home Blocked shots",
        "Hit woodwork": "Home Hit woodwork",
        "Shots inside box": "Home Shots inside box",
        "Shots off target": "Home Shots off target",
        "Shots on target": "Home Shots on target",
        "Shots outside box": "Home Shots outside box",
        "Total shots": "Home Total shots",
        "Expected goals (xG)": "Home Expected goals (xG)",
        "xG non-penalty": "Home xG non-penalty",
        "xG on target (xGOT)": "Home xG on target (xGOT)",
        "xG open play": "Home xG open play",
        "xG set play": "Home xG set play",
        "Accurate crosses": "Home Accurate crosses",
        "Accurate long balls": "Home Accurate long balls",
        "Accurate passes": "Home Accurate passes",
        "Offsides": "Home Offsides",
        "Opposition half": "Home Opposition half",
        "Own half": "Home Own half",
        "Passes": "Home Passes",
        "Throws": "Home Throws",
        "Touches in opposition box": "Home Touches in opposition box",
        "Accurate crosses (%)": "Home Accurate crosses (%)",
        "Accurate long balls (%)": "Home Accurate long balls (%)",
        "Accurate passes (%)": "Home Accurate passes (%)",
        "Blocks": "Home Blocks",
        "Clearances": "Home Clearances",
        "Interceptions": "Home Interceptions",
        "Keeper saves": "Home Keeper saves",
        "Tackles won": "Home Tackles won",
        "Tackles won (%)": "Home Tackles won (%)",
        "Aerial duels won": "Home Aerial duels won",
        "Duels won": "Home Duels won",
        "Ground duels won": "Home Ground duels won",
        "Successful dribbles": "Home Successful dribbles",
        "Aerial duels won (%)": "Home Aerial duels won (%)",
        "Ground duels won (%)": "Home Ground duels won (%)",
        "Successful dribbles (%)": "Home Successful dribbles (%)",
        "Red cards": "Home Red cards",
        "Yellow cards": "Home Yellow cards",
        "Big chances missed": "Home Big chances missed",
        "Corners": "Home Corners",
        "Ball possession": "Home Ball possession",
        "Fouls committed": "Home Fouls committed",
        "Big chances": "Home Big chances",
    }

    away_rename = {
        "Blocked shots": "Away Blocked shots",
        "Hit woodwork": "Away Hit woodwork",
        "Shots inside box": "Away Shots inside box",
        "Shots off target": "Away Shots off target",
        "Shots on target": "Away Shots on target",
        "Shots outside box": "Away Shots outside box",
        "Total shots": "Away Total shots",
        "Expected goals (xG)": "Away Expected goals (xG)",
        "xG non-penalty": "Away xG non-penalty",
        "xG on target (xGOT)": "Away xG on target (xGOT)",
        "xG open play": "Away xG open play",
        "xG set play": "Away xG set play",
        "Accurate crosses": "Away Accurate crosses",
        "Accurate long balls": "Away Accurate long balls",
        "Accurate passes": "Away Accurate passes",
        "Offsides": "Away Offsides",
        "Opposition half": "Away Opposition half",
        "Own half": "Away Own half",
        "Passes": "Away Passes",
        "Throws": "Away Throws",
        "Touches in opposition box": "Away Touches in opposition box",
        "Accurate crosses (%)": "Away Accurate crosses (%)",
        "Accurate long balls (%)": "Away Accurate long balls (%)",
        "Accurate passes (%)": "Away Accurate passes (%)",
        "Blocks": "Away Blocks",
        "Clearances": "Away Clearances",
        "Interceptions": "Away Interceptions",
        "Keeper saves": "Away Keeper saves",
        "Tackles won": "Away Tackles won",
        "Tackles won (%)": "Away Tackles won (%)",
        "Aerial duels won": "Away Aerial duels won",
        "Duels won": "Away Duels won",
        "Ground duels won": "Away Ground duels won",
        "Successful dribbles": "Away Successful dribbles",
        "Aerial duels won (%)": "Away Aerial duels won (%)",
        "Ground duels won (%)": "Away Ground duels won (%)",
        "Successful dribbles (%)": "Away Successful dribbles (%)",
        "Red cards": "Away Red cards",
        "Yellow cards": "Away Yellow cards",
        "Big chances missed": "Away Big chances missed",
        "Corners": "Away Corners",
        "Ball possession": "Away Ball possession",
        "Fouls committed": "Away Fouls committed",
        "Big chances": "Away Big chances",
    }

    Home_df.rename(columns=home_rename, inplace=True)
    Away_df.rename(columns=away_rename, inplace=True)

    home_cols = Home_df.columns.tolist()
    home_cols.remove("Home Team")
    home_cols.remove("Away Team")
    # Find the index of 'season' and 'team'
    home_matchup_idx = home_cols.index("matchup")
    home_team_idx = home_cols.index("team")
    # Insert 'match date' after 'season' and 'Opponent' after 'team'
    home_cols.insert(home_matchup_idx + 1, "Home Team")
    home_cols.insert(
        home_team_idx + 2, "Away Team"
    )  # +2 because we just inserted one column before
    Home_df = Home_df[home_cols]
    Home_df.drop(columns=["team", "Opponent"], inplace=True)

    away_cols = Away_df.columns.tolist()
    away_cols.remove("Home Team")
    away_cols.remove("Away Team")
    # Find the index of 'season' and 'team'
    away_matchup_idx = away_cols.index("matchup")
    away_team_idx = away_cols.index("team")
    # Insert 'match date' after 'season' and 'Opponent' after 'team'
    away_cols.insert(away_matchup_idx + 1, "Home Team")
    away_cols.insert(
        away_team_idx + 2, "Away Team"
    )  # +2 because we just inserted one column before
    Away_df = Away_df[away_cols]
    Away_df.drop(columns=["team", "Opponent"], inplace=True)

    # Concatenate Home and Away DataFrames
    df = pd.merge(
        Home_df,
        Away_df,
        on=["league", "season", "match date", "matchup", "Home Team", "Away Team"],
        how="left",
    )

    # Get ancilliary df
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
    fotmob = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
    df2 = fotmob.read_schedule()
    df2.reset_index(inplace=True)
    # Clean ancialliary df
    df2[["match date", "matchup"]] = df2["game"].str.split(" ", n=1, expand=True)
    df2[["Home Team", "Away team"]] = df2["matchup"].str.split("-", n=1, expand=True)
    df2["Home Team"] = df2["Home Team"].str.strip()
    df2["Away team"] = df2["Away team"].str.strip()
    df2.rename(columns={"Away team": "Away Team"}, inplace=True)

    final_df = pd.merge(
        df,
        df2[
            [
                "league",
                "season",
                "match date",
                "matchup",
                "home_team",
                "away_team",
                "round",
                "home_score",
                "away_score",
                "game_id",
            ]
        ],
        left_on=["league", "season", "match date", "matchup", "Home Team", "Away Team"],
        right_on=[
            "league",
            "season",
            "match date",
            "matchup",
            "home_team",
            "away_team",
        ],
        how="left",
    )
    # Clean final df
    final_df.drop(columns=["home_team", "away_team"], inplace=True)
    rename2 = {
        "home_score": "Home Score",
        "away_score": "Away Score",
        "round": "Round",
        "game_id": "Game ID",
    }

    final_df.rename(columns=rename2, inplace=True)

    final_cols = final_df.columns.tolist()
    final_cols.remove("Home Score")
    final_cols.remove("Away Score")
    final_cols.remove("Round")
    final_cols.remove("Game ID")
    # Find the index of 'season' and 'team'
    away_matchup_idx = away_cols.index("matchup")
    # Insert 'match date' after 'season' and 'Opponent' after 'team'
    final_cols.insert(away_matchup_idx + 2, "Home Score")
    final_cols.insert(away_matchup_idx + 3, "Away Score")
    final_cols.insert(away_matchup_idx - 1, "Round")
    final_cols.insert(away_matchup_idx - 1, "Game ID")
    final_df = final_df[final_cols]

    final_rename = {
        "league": "League",
        "season": "Season",
        "match date": "Match Date",
        "matchup": "Matchup",
    }

    final_df.rename(columns=final_rename, inplace=True)

    dtypes = {
        "League": str,
        "Season": str,
        "Game ID": int,
        "Round": int,
        "Match Date": "datetime64[ns]",
        "Matchup": str,
        "Home Team": str,
        "Home Score": int,
        "Away Score": int,
        "Away Team": str,
        "Home Blocked shots": float,
        "Home Hit woodwork": float,
        "Home Shots inside box": float,
        "Home Shots off target": float,
        "Home Shots on target": float,
        "Home Shots outside box": float,
        "Home Total shots": float,
        "Home Expected goals (xG)": float,
        "Home xG non-penalty": float,
        "Home xG on target (xGOT)": float,
        "Home xG open play": float,
        "Home xG set play": float,
        "Home Accurate crosses": float,
        "Home Accurate long balls": float,
        "Home Accurate passes": float,
        "Home Offsides": float,
        "Home Opposition half": float,
        "Home Own half": float,
        "Home Passes": float,
        "Home Throws": float,
        "Home Touches in opposition box": float,
        "Home Accurate crosses (%)": float,
        "Home Accurate long balls (%)": float,
        "Home Accurate passes (%)": float,
        "Home Blocks": float,
        "Home Clearances": float,
        "Home Interceptions": float,
        "Home Keeper saves": float,
        "Home Tackles won": float,
        "Home Tackles won (%)": float,
        "Home Aerial duels won": float,
        "Home Duels won": float,
        "Home Ground duels won": float,
        "Home Successful dribbles": float,
        "Home Aerial duels won (%)": float,
        "Home Ground duels won (%)": float,
        "Home Successful dribbles (%)": float,
        "Home Red cards": float,
        "Home Yellow cards": float,
        "Home Big chances missed": float,
        "Home Corners": float,
        "Home Ball possession": float,
        "Home Fouls committed": float,
        "Home Big chances": float,
        "Away Blocked shots": float,
        "Away Hit woodwork": float,
        "Away Shots inside box": float,
        "Away Shots off target": float,
        "Away Shots on target": float,
        "Away Shots outside box": float,
        "Away Total shots": float,
        "Away Expected goals (xG)": float,
        "Away xG non-penalty": float,
        "Away xG on target (xGOT)": float,
        "Away xG open play": float,
        "Away xG set play": float,
        "Away Accurate crosses": float,
        "Away Accurate long balls": float,
        "Away Accurate passes": float,
        "Away Offsides": float,
        "Away Opposition half": float,
        "Away Own half": float,
        "Away Passes": float,
        "Away Throws": float,
        "Away Touches in opposition box": float,
        "Away Accurate crosses (%)": float,
        "Away Accurate long balls (%)": float,
        "Away Accurate passes (%)": float,
        "Away Blocks": float,
        "Away Clearances": float,
        "Away Interceptions": float,
        "Away Keeper saves": float,
        "Away Tackles won": float,
        "Away Tackles won (%)": float,
        "Away Aerial duels won": float,
        "Away Duels won": float,
        "Away Ground duels won": float,
        "Away Successful dribbles": float,
        "Away Aerial duels won (%)": float,
        "Away Ground duels won (%)": float,
        "Away Successful dribbles (%)": float,
        "Away Red cards": float,
        "Away Yellow cards": float,
        "Away Big chances missed": float,
        "Away Corners": float,
        "Away Ball possession": float,
        "Away Fouls committed": float,
        "Away Big chances": float,
    }
    final_df = final_df.astype(dtypes)
    final_df["Season"] = (
        final_df["Season"].astype(str).str[:2]
        + "/"
        + final_df["Season"].astype(str).str[2:]
    )

    final_df = final_df.sort_values(
        by=["Match Date", "Round"], ascending=True, ignore_index=True
    )

    season_name = season.replace("/", "_")
    league_name = league.replace("-", "_")

    final_df.columns = [smart_title(col) for col in final_df.columns]
    folder_league_name = league.split("-")[1]

    # read and insert Club's badges
    final_df["Home Team Badge"] = final_df["Home Team"].apply(
        lambda x: rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\media\team_logos\{folder_league_name}\{x.lower()}.png"
    )
    final_df["Away Team Badge"] = final_df["Away Team"].apply(
        lambda x: rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\media\team_logos\{folder_league_name}\{x.lower()}.png"
    )

    # Create directory to store data
    output_dir = r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\clean_all_team_stats"
    os.makedirs(output_dir, exist_ok=True)

    final_df.to_parquet(
        rf"{output_dir}\FotMob_clean_advanced_team_stats_{league_name}_{season_name}.parquet"
    )
    return final_df


def sum_FotMob_advanced_team_stats_df(df, league, season):
    """
    Aggregates advanced team statistics from FotMob data by summing numeric columns grouped by team.
    The input DataFrame must be the raw output from `mod_fotmob_get_all_team_stats_df`.

    Parameters:
    -----------
    df : pandas.DataFrame
        The input DataFrame containing raw FotMob team stats. Must include columns:
        - "team", "league", "season", "match date", and all numeric stat columns (e.g., "Shots on target").
    league : str
        The league name (e.g., "ENG-Premier-League"). Used for file naming.
    season : str
        The season in format "YY/YY" (e.g., "23/24"). Used for file naming and column formatting.

    Returns:
    --------
    pandas.DataFrame
        A DataFrame with the following properties:
        - Grouped by "team" with summed numeric stats.
        - Columns ordered as: ["league", "season", "match date", "team", ...stats].
        - "season" reformatted to "YY/YY" (e.g., "23/24").
        - Sorted by "match date" (ascending).
        - Saved to a Parquet file in the predefined output directory.

    Example:
    --------
    >>> df_raw = mod_fotmob_get_all_team_stats_df()  # Fetch raw data
    >>> df_summed = sum_FotMob_advanced_team_stats_df(
    ...     df=df_raw,
    ...     league="ENG-Premier-League",
    ...     season="2023/2024"
    ... )
    >>> print(df_summed.head())
    """
    dtypes = {
        "league": str,
        "season": str,
        "match date": "datetime64[ns]",
        "matchup": str,
        "team": str,
        "Opponent": str,
        "Blocked shots": float,
        "Hit woodwork": float,
        "Shots inside box": float,
        "Shots off target": float,
        "Shots on target": float,
        "Shots outside box": float,
        "Total shots": float,
        "Expected goals (xG)": float,
        "xG non-penalty": float,
        "xG on target (xGOT)": float,
        "xG open play": float,
        "xG set play": float,
        "Accurate crosses": float,
        "Accurate long balls": float,
        "Accurate passes": float,
        "Offsides": float,
        "Opposition half": float,
        "Own half": float,
        "Passes": float,
        "Throws": float,
        "Touches in opposition box": float,
        "Accurate crosses (%)": float,
        "Accurate long balls (%)": float,
        "Accurate passes (%)": float,
        "Blocks": float,
        "Clearances": float,
        "Interceptions": float,
        "Keeper saves": float,
        "Tackles won": float,
        "Tackles won (%)": float,
        "Aerial duels won": float,
        "Duels won": float,
        "Ground duels won": float,
        "Successful dribbles": float,
        "Aerial duels won (%)": float,
        "Ground duels won (%)": float,
        "Successful dribbles (%)": float,
        "Red cards": float,
        "Yellow cards": float,
        "Big chances missed": float,
        "Corners": float,
        "Ball possession": float,
        "Fouls committed": float,
        "Big chances": float,
    }

    df = df.astype(dtypes)

    columns_to_sum = [
        "Blocked shots",
        "Hit woodwork",
        "Shots inside box",
        "Shots off target",
        "Shots on target",
        "Shots outside box",
        "Total shots",
        "Expected goals (xG)",
        "xG non-penalty",
        "xG on target (xGOT)",
        "xG open play",
        "xG set play",
        "Accurate crosses",
        "Accurate long balls",
        "Accurate passes",
        "Offsides",
        "Opposition half",
        "Own half",
        "Passes",
        "Throws",
        "Touches in opposition box",
        "Accurate crosses (%)",
        "Accurate long balls (%)",
        "Accurate passes (%)",
        "Blocks",
        "Clearances",
        "Interceptions",
        "Keeper saves",
        "Tackles won",
        "Tackles won (%)",
        "Aerial duels won",
        "Duels won",
        "Ground duels won",
        "Successful dribbles",
        "Aerial duels won (%)",
        "Ground duels won (%)",
        "Successful dribbles (%)",
        "Red cards",
        "Yellow cards",
        "Big chances missed",
        "Corners",
        "Ball possession",
        "Fouls committed",
        "Big chances",
    ]

    df2 = df.groupby("team")[columns_to_sum].sum().reset_index().round(2)
    final_df = pd.merge(
        df2,
        df[["league", "season", "match date", "team"]].drop_duplicates(),
        on="team",
        how="left",
    )

    final_df.drop_duplicates(subset=["team"], inplace=True)

    cols = final_df.columns.tolist()
    cols.remove("match date")
    cols.remove("season")
    cols.remove("league")
    cols.insert(0, "league")
    cols.insert(1, "season")
    cols.insert(2, "match date")
    final_df = final_df[cols]

    final_df["season"] = (
        final_df["season"].astype(str).str[:2]
        + "/"
        + final_df["season"].astype(str).str[2:]
    )

    final_df = final_df.sort_values(
        by=["match date"], ascending=True, ignore_index=True
    )

    final_df.columns = [smart_title(col) for col in final_df.columns]
    folder_league_name = league.split("-")[1]

    # read and insert Club's badges
    final_df["Badge"] = final_df["Team"].apply(
        lambda x: rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\media\team_logos\{folder_league_name}\{x.lower()}.png"
    )

    season_name = season.replace("/", "_")
    league_name = league.replace("-", "_")

    # Create directory to store data
    output_dir = r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\clean_all_team_stats\sum"
    os.makedirs(output_dir, exist_ok=True)

    final_df.to_parquet(
        rf"{output_dir}\sum_FotMob_advanced_team_stats_{league_name}_{season_name}.parquet"
    )

    return final_df


def join_league_table_stats_to_sum_advanced_all_team(df, league, season):
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    ws = sd.FotMob(leagues=league, seasons=season, no_cache=False, no_store=False)
    league_table = ws.read_league_table()
    league_table.reset_index(inplace=True)
    # Filtrar nomes de colunas com mais de 2 caracteres
    cols_to_rename = [col for col in league_table.columns if len(col) > 2]

    # Criar dicionário de renomeação com title case
    rename_dict = {col: col.title() for col in cols_to_rename}

    # Renomear as colunas
    league_table.rename(columns=rename_dict, inplace=True)

    df2 = sum_FotMob_advanced_team_stats_df(df, league, season)
    final_df = pd.merge(
        df2,
        league_table[["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]],
        on=["Team"],
        how="left",
    )
    final_df.columns = [smart_title(col) for col in final_df.columns]

    folder_league_name = league.split("-")[1]

    # read and insert Club's badges
    final_df["Badge"] = final_df["Team"].apply(
        lambda x: rf"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\media\team_logos\{folder_league_name}\{x.lower()}.png"
    )
    cols = final_df.columns.tolist()
    cols.remove("Mp")
    cols.remove("W")
    cols.remove("D")
    cols.remove("L")
    cols.remove("Gf")
    cols.remove("Ga")
    cols.remove("Gd")
    cols.remove("Pts")
    cols.insert(4, "Mp")
    cols.insert(5, "W")
    cols.insert(6, "D")
    cols.insert(7, "L")
    cols.insert(8, "Gf")
    cols.insert(9, "Ga")
    cols.insert(10, "Gd")
    cols.insert(11, "Pts")
    final_df = final_df[cols]

    season_name = season.replace("/", "_")
    league_name = league.replace("-", "_")

    # Create directory to store data
    output_dir = r"C:\Users\Vitor\Desktop\Football Data Analytics\My_Projects\Main level\data\clean_all_team_stats\sum"
    os.makedirs(output_dir, exist_ok=True)

    final_df.to_parquet(
        rf"{output_dir}\FotMob_League_Table_stats_with_sum_advanced_team_stats_{league_name}_{season_name}.parquet"
    )

    return final_df
