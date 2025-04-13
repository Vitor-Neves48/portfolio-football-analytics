import pandas as pd
import numpy as np
import re
import warnings

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


def standardize_team_names(df, column, new_column=None):
    """
    Standardizes club names in a DataFrame column based on a fixed internal mapping. Finds team names in a certain column and maps those names to those described is the name_mapping dictionary. This dictionary can be expanded upon.

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

