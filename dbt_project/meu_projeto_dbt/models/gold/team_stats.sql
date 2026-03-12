with matches as (
    select * from {{ ref('stg_matches') }}
),
home_stats as (
    select
        home_team as team,
        count(*) as home_matches,
        sum(case when winner = 'HOME_TEAM' then 1 else 0 end) as home_wins,
        sum(case when winner = 'AWAY_TEAM' then 1 else 0 end) as home_losses,
        sum(case when winner = 'DRAW' then 1 else 0 end) as home_draws,
        sum(home_score) as home_goals_for,
        sum(away_score) as home_goals_against
    from matches
    group by home_team
),
away_stats as (
    select
        away_team as team,
        count(*) as away_matches,
        sum(case when winner = 'AWAY_TEAM' then 1 else 0 end) as away_wins,
        sum(case when winner = 'HOME_TEAM' then 1 else 0 end) as away_losses,
        sum(case when winner = 'DRAW' then 1 else 0 end) as away_draws,
        sum(away_score) as away_goals_for,
        sum(home_score) as away_goals_against
    from matches
    group by away_team
),
team_aggregated as (
    select
        coalesce(h.team, a.team) as team,
        coalesce(h.home_matches, 0) as home_matches,
        coalesce(a.away_matches, 0) as away_matches,
        coalesce(h.home_matches, 0) + coalesce(a.away_matches, 0) as total_matches,
        coalesce(h.home_wins, 0) as home_wins,
        coalesce(a.away_wins, 0) as away_wins,
        coalesce(h.home_wins, 0) + coalesce(a.away_wins, 0) as total_wins,
        coalesce(h.home_losses, 0) as home_losses,
        coalesce(a.away_losses, 0) as away_losses,
        coalesce(h.home_losses, 0) + coalesce(a.away_losses, 0) as total_losses,
        coalesce(h.home_draws, 0) as home_draws,
        coalesce(a.away_draws, 0) as away_draws,
        coalesce(h.home_draws, 0) + coalesce(a.away_draws, 0) as total_draws,
        coalesce(h.home_goals_for, 0) as home_goals_for,
        coalesce(a.away_goals_for, 0) as away_goals_for,
        coalesce(h.home_goals_for, 0) + coalesce(a.away_goals_for, 0) as total_goals_for,
        coalesce(h.home_goals_against, 0) as home_goals_against,
        coalesce(a.away_goals_against, 0) as away_goals_against,
        coalesce(h.home_goals_against, 0) + coalesce(a.away_goals_against, 0) as total_goals_against
    from home_stats h
    full outer join away_stats a on h.team = a.team
)
select
    team,
    home_matches,
    away_matches,
    total_matches,
    home_wins,
    away_wins,
    total_wins,
    home_losses,
    away_losses,
    total_losses,
    home_draws,
    away_draws,
    total_draws,
    home_goals_for,
    away_goals_for,
    total_goals_for,
    home_goals_against,
    away_goals_against,
    total_goals_against,
    total_goals_for - total_goals_against as goal_difference,
    (total_wins * 3 + total_draws) as points
from team_aggregated
order by points desc, goal_difference desc, total_goals_for desc