# Shell script to load multiple rasters.

export PGPORT=5432
export PGHOST=eriboll
#export PGUSER
# defaults to logged in user

export PGDATABASE=atec

raster2pgsql -s 4326 -F -R ./*.tif atec_interim.test_ortho_staging_R | psql

# -s give the SRID
# -C set the standard of constraints
# -F add a column for the filename
# -t chunk the raster into tiles, 1 tile per row 
