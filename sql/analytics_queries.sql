SELECT
home_team,
COUNT(*) as wins
FROM matches
WHERE winner = 'HOME_TEAM'
GROUP BY home_team
ORDER BY wins DESC