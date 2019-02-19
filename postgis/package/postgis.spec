Summary:        Geospatial extensions for Greenplum Database
License:        GPLv2
Name:           postgis
Version:        %{postgis_ver}
Release:        %{postgis_rel}
Group:          Development/Tools
AutoReq:        no
AutoProv:       no
Provides:       postgis = %{postgis_ver}
Requires:       geos = %{geos_ver}, proj = %{proj_ver}, json-c = %{json_ver}, gdal = %{gdal_ver}

%description
The PostGIS module provides geospatial extensions for Greenplum Database.

%install
mkdir -p %{buildroot}%{postgishome}/bin \
         %{buildroot}%{postgishome}/lib/postgresql \
         %{buildroot}%{postgishome}/share/postgresql/extension \
         %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/{install,upgrade,uninstall}/

make -C %{postgis_dir} BLD_TOP=%{bld_top} all install prefix=%{buildroot}%{postgishome}

cp %{postgis_dir}/extensions/postgis/postgis.control                               %{buildroot}%{postgishome}/share/postgresql/extension/postgis.control
cp %{postgis_dir}/extensions/postgis_topology/postgis_topology.control             %{buildroot}%{postgishome}/share/postgresql/extension/postgis_topology.control
cp %{postgis_dir}/extensions/postgis_tiger_geocoder/postgis_tiger_geocoder.control %{buildroot}%{postgishome}/share/postgresql/extension/postgis_tiger_geocoder.control

cp ${GPHOME}/bin/pgsql2shp    %{buildroot}%{postgishome}/bin
cp ${GPHOME}/bin/shp2pgsql    %{buildroot}%{postgishome}/bin
cp ${GPHOME}/bin/raster2pgsql %{buildroot}%{postgishome}/bin

cp ${GPHOME}/lib/postgresql/postgis-2.1.so   %{buildroot}%{postgishome}/lib/postgresql/postgis-2.1.so
cp ${GPHOME}/lib/postgresql/rtpostgis-2.1.so %{buildroot}%{postgishome}/lib/postgresql/rtpostgis-2.1.so


# All the .sql files once installed will be installed in share/contrib/postgis-2.1 folder of your PostgreSQL install

# cp ${GPHOME}/share/postgresql/contrib/postgis-2.1/*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/postgis.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/*comments.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/install/


cp $GPHOME/share/postgresql/contrib/postgis-2.1/*upgrade*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/legacy*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis_legacy.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/uninstall*.sql %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/

# cp %{postgishome}/share/postgresql/contrib/postgis-2.1/postgis.sql  %{buildroot}%{postgishome}/share/postgresql/extension/postgis--2.1.5.sql
# cp %{postgishome}/share/postgresql/contrib/postgis-2.1/topology.sql %{buildroot}%{postgishome}/share/postgresql/extension/postgis_topology--2.1.5.sql

cp %{postgis_dir}/../../package/postgis_manager.sh %{buildroot}%{postgishome}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh

%files

%{postgishome}/bin/pgsql2shp
%{postgishome}/bin/raster2pgsql
%{postgishome}/bin/shp2pgsql
%{postgishome}/include/liblwgeom.h
%{postgishome}/lib/liblwgeom-2.1.5.so
%{postgishome}/lib/liblwgeom.a
%{postgishome}/lib/liblwgeom.la
%{postgishome}/lib/liblwgeom.so
%{postgishome}/lib/postgresql/postgis-2.1.so
%{postgishome}/lib/postgresql/rtpostgis-2.1.so

# %{postgishome}/share/postgresql/contrib/postgis-2.1/*
# %{postgishome}/share/postgresql/extension/postgis--2.1.5.sql
# %{postgishome}/share/postgresql/extension/postgis_topology--2.1.5.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/postgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/postgis_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/raster_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/rtpostgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/spatial_ref_sys.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/install/topology_comments.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_postgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_rtpostgis.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_sfcgal.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_topology.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_gist.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_minimal.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_20_21.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_21_minor.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_legacy.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_20_21.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_21_minor.sql
%{postgishome}/share/postgresql/contrib/postgis-2.1/upgrade/topology_upgrade_21_minor.sql

%{postgishome}/share/postgresql/extension/postgis.control
%{postgishome}/share/postgresql/extension/postgis_topology.control
%{postgishome}/share/postgresql/extension/postgis_tiger_geocoder.control
