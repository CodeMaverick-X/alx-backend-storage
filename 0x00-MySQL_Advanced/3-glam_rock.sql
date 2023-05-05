-- an sql script that lists all band with GLAM rock as
-- their main style, ranked by thier longevity
SELECT `band_name`, IFNULL(`split`, 2020) - IFNULL(`formed`, 0) AS `lifespan`
  FROM `metal_bands`
 WHERE LOWER(`style`) LIKE '%Glam rock%'
 ORDER BY `lifespan` DESC;
