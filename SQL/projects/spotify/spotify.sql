create database spotify_db;

use spotify_db;
CREATE TABLE IF NOT EXISTS spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)


select * from spotify_tracks;


SELECT track_name, artist, album, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 1;


SELECT AVG(popularity) AS average_popularity
FROM spotify_tracks;


SELECT track_name, artist, duration_minutes
FROM spotify_tracks
WHERE duration_minutes > 4.0;

select
    case
        when popularity >= 65 then "very popular"
        when popularity >= 50 then "popular"
        else "less popular"
    end as popularity_range,
    count(*) as track_count
from spotify_tracks
group by popularity_range;