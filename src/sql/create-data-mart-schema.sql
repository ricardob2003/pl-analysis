--  Premier League Data Mart – Schema
CREATE TABLE dim_teams (
  team_id SERIAL PRIMARY KEY,
  team_name VARCHAR(100) NOT NULL,
  team_abbreviation VARCHAR(10),
  stadium_name VARCHAR(100)
);
CREATE TABLE dim_seasons (
  season_id SERIAL PRIMARY KEY,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL
);
CREATE TABLE dim_venues (
  venue_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  city VARCHAR(100)
);
-- ========== FACT TABLES ==========
CREATE TABLE fact_fixtures (
  fixture_id SERIAL PRIMARY KEY,
  match_date DATE NOT NULL,
  match_time TIME,
  season_id INT NOT NULL,
  home_team_id INT NOT NULL,
  away_team_id INT NOT NULL,
  home_goals INT,
  away_goals INT,
  venue_id INT,
  matchweek INT,
  result VARCHAR(1),
  -- 'H', 'A', or 'D'
  xG FLOAT,
  xGA FLOAT,
  FOREIGN KEY (season_id) REFERENCES dim_seasons(season_id),
  FOREIGN KEY (home_team_id) REFERENCES dim_teams(team_id),
  FOREIGN KEY (away_team_id) REFERENCES dim_teams(team_id),
  FOREIGN KEY (venue_id) REFERENCES dim_venues(venue_id)
);
CREATE INDEX idx_fixtures_season ON fact_fixtures(season_id);
CREATE INDEX idx_fixtures_date ON fact_fixtures(match_date);
CREATE INDEX idx_fixtures_home_team ON fact_fixtures(home_team_id);
CREATE INDEX idx_fixtures_away_team ON fact_fixtures(away_team_id);
CREATE TABLE fact_team_season_stats (
  team_season_id SERIAL PRIMARY KEY,
  season_id INT NOT NULL,
  team_id INT NOT NULL,
  wins INT,
  draws INT,
  losses INT,
  GF INT,
  GA INT,
  GD INT,
  xG FLOAT,
  xGA FLOAT,
  xGD FLOAT,
  yellow_cards INT,
  red_cards INT,
  FOREIGN KEY (season_id) REFERENCES dim_seasons(season_id),
  FOREIGN KEY (team_id) REFERENCES dim_teams(team_id)
);
CREATE INDEX idx_team_stats_team_season ON fact_team_season_stats(team_id, season_id);
CREATE TABLE fact_rankings (
  ranking_id SERIAL PRIMARY KEY,
  season_id INT NOT NULL,
  team_id INT NOT NULL,
  final_position INT,
  points INT,
  home_rank INT,
  away_rank INT,
  xG_rank INT,
  xGA_rank INT,
  ucl_qualification BOOLEAN,
  FOREIGN KEY (season_id) REFERENCES dim_seasons(season_id),
  FOREIGN KEY (team_id) REFERENCES dim_teams(team_id)
);
CREATE INDEX idx_rankings_team_season ON fact_rankings(team_id, season_id);
