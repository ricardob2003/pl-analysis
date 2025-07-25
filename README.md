## 1. Project Overview

**Purpose:**
Develop a Business Tool that will visualize and model Chelsea FC’s league progression over the past 3 years. We will aim to compare and analyze on-pitch performance trends over multiple seasons when compared to assess if current recruitment strategy is working. The Business tool will help users understand historical patterns in goals, points, and venue-based performance specifically identify if there has been an improvement and if specific KPIs have been met.

**Rationale:**
A dedicated performance tool will consolidate match data into actionable visualizations for succesful analysis and benchmark .

---

## 2. Business Objectives

1. Compare goals scored, conceded, points difference, matches won, matches lost across the last 5 seasons to identify improvement trends. (e.g., % change).
2. Measure and compare average points per game (PPG) at home vs. away for each season, highlighting statistically significant trends .
3. Identify recurring match periods (e.g., months or game weeks) where Chelsea historically underperforms, using points-per-match and goals scored and conceded as metrics.
4. Rank stadiums where Chelsea has lost points lost and benchmark against league opposition to highlight problematic venues.
5. Analyze and visualize monthly win/draw/loss distribution over 5 seasons to highlight consistent strong/weak months.
6. Compare Chelsea’s season metrics against the top and bottom 4 teams (by points) each season to contextualize performance and see if the Premier League competitiveness keeps expanding.
7. Ensure all visualizations allow filtering by season, team, venue, and match outcome for ad-hoc analysis by stakeholders.
8. Assess whether Chelsea’s recent underperformance stems primarily from the new ownership’s strategic decisions or is part of a longer-term decline that needed revamp

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
