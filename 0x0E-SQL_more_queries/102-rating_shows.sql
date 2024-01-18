-- Importing the database
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM hbtn_0d_tvshows_rate.tv_shows
JOIN hbtn_0d_tvshows_rate.tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC;

