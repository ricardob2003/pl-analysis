## 1. Simulation of a Business Requirement Document

**Purpose:**
Develop a Business Tool that will visualize and model Chelsea FC’s league progression over the past 3 years to analyze on-pitch performance trends over multiple seasons when compared to other teams. The Business tool will help users understand historical patterns in goals, points, and venue-based performance specifically over the last couple of years under the new ownership to identify if there has been an improvement and if specific KPIs have been met.

**Rationale:**
A dedicated performance tool will consolidate match data into actionable visualizations for succesful analysis, benchmark and data based opinions.

---

## 2. Business Objectives

1. Compare total goals scored and conceded across the last 3 seasons to identify improvement trends. Include visual indicators (e.g., % change).
2. Measure and compare average points per game (PPG) at home vs. away for each season, highlighting statistically significant trends.
3. Identify recurring match periods (e.g., months or game weeks) where Chelsea historically underperforms, using points-per-match as metric.
4. Rank stadiums by points lost by Chelsea and benchmark against league average to highlight problem venues.
5. Analyze and visualize monthly win/draw/loss distribution over 3 seasons to highlight consistent strong/weak months.
6. Compare Chelsea’s season metrics against the top and bottom 4 teams (by points) each season to contextualize performance.
7. Attempt to identify macro-trends (e.g., goals conceded in last 15 minutes, poor away form, bad winter form) correlated with season underperformance.
8. Ensure all visualizations allow filtering by season, team, venue, and match outcome for ad-hoc analysis by stakeholders.
9. Assess whether Chelsea’s recent underperformance stems primarily from the new ownership’s strategic decisions or is part of a longer-term decline.

---

## 3. Scope

**In Scope:**

-   Ingestion of match-level data (date, teams, goals).
-   Calculation of aggregate metrics: goals for/against, points per game, win/draw/loss counts.
-   Development of SQL views or CTEs for core analyses.
-   Creation of three dashboard pages: Season Overview, Historical Analysis, Monthly Form.
-   Interactive filters (season, venue) and tooltips.
-   PDF report summarizing key findings and recommendations.

**Out of Scope:**

-   Financial data (transfer spend, revenue, wages).
-   Player-level analytics beyond aggregate goals.
-   Live API integration (data snapshots loaded manually).

---

## 4. Stakeholders

| Role                         | Name / Group                    | Responsibility                            |
| ---------------------------- | ------------------------------- | ----------------------------------------- |
| Project Sponsor              | Chelsea FC Analytics Lead       | Approve budget, prioritize features       |
| BI Developer / Data Engineer | Ricardo Barahona                | Data ingestion, modeling, dashboard build |
| Business Analyst             | Team Analyst / Coaching Staff   | Define KPIs, interpret results            |
| End Users                    | Club Management; Fan Engagement | Consume dashboard; provide feedback       |

---

## 5. Functional Requirements

1. **Data Ingestion Module**: Load CSV or JSON match data into the database; normalize date formats and team names.
2. **SQL Analysis Views**:
    - `season_goals_view` season, goals_for, goals_against.
    - `venue_points_view` season, venue, pts_per_game.
    - `monthly_performance_view` returning month, wins, draws, losses.
3. **Dashboard Pages**:
    - **Season Overview**: Line chart for goals_for vs. goals_against; bar chart for total points per season.
    - **Venue Analysis**: Grouped bar chart or small multiples showing home vs. away pts_per_game by season.
    - **Monthly Form**: Heatmap visualizing count of wins/draws/losses per month.
4. **Interactivity**: Season and venue slicers; hover-tooltips displaying raw metrics.
5. **Export**: Ability to export charts as images or PDF snapshots.

---

## 6. Non-Functional Requirements

-   **Performance**: Dashboard load time under 5 seconds for 10 seasons of data.
-   **Usability**: Intuitive filter placement; clear labels and legends.
-   **Maintainability**: Modular SQL views; parameterized queries.
-   **Portability**: Deployable in Tableau Public or Power BI Desktop.

---

## 7. Data Requirements & Sources

| Data Element      | Source                                            | Frequency     | Format   |
| ----------------- | ------------------------------------------------- | ------------- | -------- |
| Match results     | football-data.org API or Kaggle "European Soccer" | Static import | CSV/JSON |
| Match date        | Same as above                                     | —             | ISO 8601 |
| Teams             | Same as above                                     | —             | String   |
| Goals for/against | Same as above                                     | —             | Integer  |

Optional advanced stats (xG, possession) may be added later.

---

## 8. Assumptions & Constraints

-   Data for at least 5 seasons is available in the chosen source.
-   No real-time updates; dashboard refreshed on-demand.
-   Users have access to Tableau Public or Power BI Desktop.
-   Team name string is consistently "Chelsea FC" in the dataset.

---

## 9. Risks & Mitigations

| Risk                                       | Probability | Impact | Mitigation                                          |
| ------------------------------------------ | ----------- | ------ | --------------------------------------------------- |
| Incomplete or inconsistent match data      | Medium      | Medium | Validate on load; implement data quality checks.    |
| Performance lag with large season datasets | Low         | Medium | Aggregate via SQL views; optimize indices.          |
| Stakeholder changes in KPI definitions     | Low         | High   | Regular review meetings; flexible view definitions. |

---

## 10. Key Performance Indicators (KPIs)

To ensure alignment with business objectives, the following KPIs have been defined. Each KPI is designed to measure a specific aspect of Chelsea FC's performance and support root cause analysis across seasons, venues, and opponent profiles.

### **KPI Definitions**

| KPI Name                             | Description                                                     | Purpose                                              |
| ------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------- |
| **Goals For (GF)**                   | Total goals scored per season, venue, or month                  | Indicates offensive strength                         |
| **Goals Against (GA)**               | Total goals conceded per season, venue, or month                | Indicates defensive stability                        |
| **Goal Difference (GD)**             | GF minus GA                                                     | Measures overall match dominance                     |
| **Points Per Game (PPG)**            | Total points divided by number of matches                       | Provides normalized performance metric               |
| **Performance vs. Top 6 / Bottom 4** | Average PPG against top-tier and bottom-tier teams              | Assesses competitiveness and dominance               |
| **Home vs. Away PPG Split**          | Comparison of PPG at home vs. away                              | Highlights venue-dependent performance gaps          |
| **Points Lost After Leading**        | Total points dropped in matches where Chelsea scored first      | Reveals match control and mentality issues           |
| **Late Goals Conceded**              | Goals conceded after the 75th minute                            | Indicates issues in stamina, focus, or substitutions |
| **Monthly Form Index**               | Aggregated match outcomes by calendar month                     | Captures seasonal performance trends                 |
| **Match Result Conversion Rate**     | % of games converted into wins when leading                     | Measures execution and game management               |
| **Streak Index**                     | Number of win/loss streaks of 3+ matches                        | Reflects momentum and consistency                    |
| **1H vs. 2H Season PPG**             | PPG in first vs. second half of the season                      | Assesses tactical adaptability and squad endurance   |
| **Manager/Ownership Era PPG**        | Comparison of PPG before and after managerial/ownership changes | Measures strategic leadership impact                 |

---
